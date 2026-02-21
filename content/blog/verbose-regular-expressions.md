---
date: 2020-06-30
title: Verbose regular expressions, now you have one and a bit problems
type: post
---

Regular expressions (regexes) are famously hard to read or write. There are
some techniques you can use to improve this. Like any other code you write,
your regular expression patterns should

- include comments
- break apart large blocks into smaller related sections
- use named variables and identifiers

Verbose regular expressions, and named caputure groups make this possible.
With these you can

- put explanatory comments anywhere in a pattern
- seperate parts over multiple lines
- refer to matches by name rather than number

Let's demonstrate, with a typical regex horror in Python 3.x. This pattern
extracts fields from the logs of a web server

```python
# e.g. '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
NCSA_COMMON_LOG_PATTERN = re.compile(
    r'([^ ]+) ([^ ]+) ([^ ]+) \[([0-9]{2}/[a-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2} [+-][0-9]{4})\] "([a-z]+) ([^ ]+) HTTP/([0-9.]+)" ([0-9]{3}) ([0-9]+|-)',
    re.IGNORECASE,
)

```

My mind just bounces right off that ... bag of symbols. Running it gives the
desired output

```python
>>> line = '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
>>> match = NCSA_COMMON_LOG_PATTERN.match(line)
>>> match.groups()
('127.0.0.1', '-', 'james', '09/May/2018:16:00:39 +0000', 'GET', '/report', '1.0', '200', '123')
```

but it's unreadable, barely usable, and unmaintainable.

## Step 1: break it up

Our first improvement is to break the pattern into logical parts, using just
string concatenation

```python
# e.g. '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
NCSA_COMMON_LOG_PATTERN = re.compile(
    r'([^ ]+) ' +
    r'([^ ]+) ' +
    r'([^ ]+) ' +
    r'\[([0-9]{2}/[a-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2} [+-][0-9]{4})\] ' +
    r'"([a-z]+) ' +
    r'([^ ]+) ' +
    r'HTTP/([0-9.]+)" ' +
    r'([0-9]{3}) ' +
    r'([0-9]+|-)',
    re.IGNORECASE,
)
```

That's better, at least we can see the capture groups, but the extra quoting
adds visual noise.

## Step 2: Verbose syntax

Instead lets write the pattern using verbose syntax.

```python
# e.g. '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
NCSA_COMMON_LOG_PATTERN = re.compile(r'''
    ([^ ]+)[ ]
    ([^ ]+)[ ]
    ([^ ]+)[ ]
    \[([0-9]{2}/[a-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}[ ][+-][0-9]{4})\][ ]
    "([a-z]+)[ ]
    ([^ ]+)[ ]
    HTTP/([0-9.]+)"[ ]
    ([0-9]{3})[ ]
    ([0-9]+|-)
    ''',
    re.IGNORECASE | re.VERBOSE,
)
```

Adding `re.VERBOSE` tells Python to ignore most whitespace in the pattern.
As a result we can have our expression broken up over several lines, & indent
those lines. We use `'[ ]'` instead of just `' '` for the few spaces we care
about.

## Step 3: Add comments

With this new freedom we can break apart the expression more, & comment it

```python
# e.g. '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
NCSA_COMMON_LOG_PATTERN = re.compile(r'''
    ([^ ]+)  # Remote host, e.g. "127.0.0.1"
    [ ]
    ([^ ]+)  # Remote ident, almost invariably "-"
    [ ]
    ([^ ]+)  # Remote user, e.g. -, juan, DOMAIN\aniyah
    [ ]
    \[
        (  # Date & time the request was made
            [0-9]{2}/[a-z]{3}/[0-9]{4}  # Date, e.g. 01/jan/1970
            :
            [0-9]{2}:[0-9]{2}:[0-9]{2}  # Time, e.g. 23:59:59
            [ ]
            [+-][0-9]{4}  # Time offset, e.g. +0530
        )
    \]
    [ ]
    "
        ([a-z]+)  # HTTP method, e.g. GET, HEAD, Head
        [ ]
        ([^ ]+)  # Path, e.g. /, /report, /imgs/cat.jpg
        [ ]
        HTTP/([0-9.]+)  # HTTP version, e.g. 1.0, 2
    "
    [ ]
    ([0-9]{3})  # HTTP Response code, e.g. 200, 404, 503
    [ ]
    ([0-9]+|-)  # Size of HTTP response body, e.g. -, 10, 0, 123456

    # Intentionally don't terminate the pattern with a $.
    # This allows it to accept lines with extra fields.
    # For now, they're just ignored.
    ''',
    re.IGNORECASE | re.VERBOSE,
)
```

That's already much better than what we started with.

## Step 4: Name the capture groups

we can go one better by naming the capture groups

```python
NCSA_COMMON_LOG_PATTERN = re.compile(r'''
    (?P<remote_host>[^ ]+)  # e.g. "127.0.0.1"
    [ ]
    (?P<remote_ident>[^ ]+)  # Almost invariably "-"
    [ ]
    (?P<remote_user>[^ ]+)  # e.g. -, juan, DOMAIN\aniyah
    [ ]
    \[
        (?P<request_datetime>  # e.g. 01/jan/1970:23:59:59 +0530
            [0-9]{2}/[a-z]{3}/[0-9]{4}  # Date, e.g. 01/jan/1970
            :
            [0-9]{2}:[0-9]{2}:[0-9]{2}  # Time, e.g. 23:59:59
            [ ]
            [+-][0-9]{4}  # Time offset, e.g. +0530
        )
    \]
    [ ]
    "
        (?P<http_method>[a-z]+)  # e.g. GET, HEAD, Head
        [ ]
        (?P<path>[^ ]+)  # e.g. /, /report, /imgs/cat.jpg
        [ ]
        HTTP/(?P<http_version>[0-9.]+)  # e.g. 1.0, 2
    "
    [ ]
    (?P<http_response_code>[0-9]{3})  # e.g. 200, 404, 503
    [ ]
    (?P<http_response_body_size>[0-9]+|-)  # e.g. -, 10, 0, 123456

    # Intentionally don't terminate the pattern with a $.
    # This allows it to accept lines with extra fields.
    # For now, they're just ignored.
    ''',
    re.IGNORECASE | re.VERBOSE,
)
```

Now our pattern is readble, maintainble, & it returns results by name

```python
>>> line = '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123'
>>> match = NCSA_COMMON_LOG_PATTERN.match(line)
>>> match.groupdict()
{'remote_host': '127.0.0.1',
 'remote_ident': '-',
 'remote_user': 'james',
 'request_datetime': '09/May/2018:16:00:39 +0000',
 'http_method': 'GET',
 'path': '/report',
 'http_version': '1.0',
 'http_response_code': '200',
 'http_response_body_size': '123'}
```
