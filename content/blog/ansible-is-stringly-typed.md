---
date: 2020-07-05
title: Ansible is Stringly Typed
type: post
---


## Summary
Ansible is weakly typed, but in particular variables set on the command line are [stringly typed](https://wiki.c2.com/?StringlyTyped).
If a string is used in a condition (e.g. `when: skip_build`) it leads to surprising results, because any non-empty string (e.g. `"false"`) evaluate as [truthy](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).
I recommend casting all variables in conditionals, or other calculations.



Prefer

```yaml
- name: Some task
  ...
  when: (foo | bool) or (bar | int) > 0
```

Avoid

```yaml
- name: Some task
  ...
  when: foo or bar > 0
```

## Background

Tasks in a particular playbook used a variable to selectively skip some operations, skip_install was set to `true` for some hosts.

```yaml
- name: Install the test framework
  ...
  when: skip_install is not defined or not skip_install
```

I wanted to run this task on every host. I ran `ansible-playbook ... -e skip_install=false`, but instead of running everywhere the task was always skipped.
Was the boolean logic wrong? No.
Was it operator precendence? No, brackets made no difference.
Was something overriding my value? No, setting a variable on the command line has the highest precendence.

Then I remembed an old tweet

> Ansible WAT: Variables defined on the command line (or a .ini) don't have the type you might expect
> ```
> ansible -i localhost, localhost -mdebug -e 'foo=[1,2,3]' -a 'msg={{ foo | join(",") }}'
> localhost | SUCCESS =>; {
>   "msg": "[,1,,,2,,,3,]"
> }
> ```
> &mdash; Alex Willmer (@moreati) [December 31, 2018](https://twitter.com/moreati/status/1079749469112020992)

When I used `-e skip_install=false` the value I got wasn't `False` (a boolean), it was `"false"` (a string).
In Ansible any non-empty string evaluatesd as [truthy](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) (a behaviour inherited from Python).

## Discussion

Ansible variables can be set by a number of sources - usually in a YAML file such as `roles/<role_name>/vars/main.yml`, `group_vars/<host_group>.yml`, or a playbook. For example

```yaml
- name: Demonstrate Ansible typing
  hosts: localhost
  gather_facts: false
  vars:
    threads_count: 10
  tasks:
    - debug:
        var: threads_count
    - debug:
        msg: "{{ threads_count | type_debug }}"
```

Running this playbook shows our variable `threads_count` has the expected type type `int`

```
$ ansible-playbook -ilocalhost, typing.yaml

PLAY [Demonstrate Ansible typing] **********************************************

TASK [debug] *******************************************************************
ok: [localhost] =>
  threads_count: 10

TASK [debug] *******************************************************************
ok: [localhost] =>
  msg: int
...
```

However, if we override `thread_counts` on the command line, then it morphs into a `str`

```
$ ansible-playbook -ilocalhost, typing.yaml -e threads_count=20

PLAY [Demonstrate Ansible typing] **********************************************

TASK [debug] *******************************************************************
ok: [localhost] =>
  threads_count: '20'

TASK [debug] *******************************************************************
ok: [localhost] =>
  msg: str
...
```

This is because Ansible does not parse command line arguments through the YAML parser.
Instead any variable set using `-e foo=42` or `--extra-vars bar=true` becomes a string.
The same is true of values set in an .ini file, but that's rare in my experience.

# Recommendations

To recap, our original tasks looked like

```yaml
when: skip_install is not defined or not skip_install
```

We can improve this `when:` clause in several ways

1. Explicitly cast `skip_install`, to handle a value provided on the command line

   ```yaml
   when: (skip_install is not defined) or (not skip_install | bool)
   ```

1. Set a local default for `skip_install`, to simplify the expression

   ```yaml
   when: not (skip_install | default(false) | bool)
   ```

1. Set a role default for `skip_install` (in `<role>/defaults/main.yml`) to simplify further

   ```yaml
   when: not (skip_install | bool)
   ```

1. Replace `skip_install` with a variable that doesn't need negating, to simplify even further

   ```yaml
   when: test_framework_install | bool
   ```

1. If you can, use `tags:` instead of a `when:` clause to choose which tasks are executed

   ```yaml
   tags:
     - test-framework-install
   ```

   then to skip those tasks run your playbook as `ansible-playbook ... --skip-tags test-framework-install`.

