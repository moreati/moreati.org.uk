---
date: 2008-10-06
title: 'Honey I hid the dot-files'
type: post
---

Backing up my home folder this weekend, in readiness for the Ubuntu
Intrepid beta I spotted some unusual path names scroll by:

    ~/.local/share/applications
    ~/.local/share/desktop-directories
    ~/.local/share/gnome-do
    ~/.local/share/mime
    ~/.local/share/Mono Paint
    ~/.local/share/Trash
    ~/.local/share/tracker`

It turns out that the hidden folders `$HOME/.local/`, `$HOME/.config`,
and `$HOME/.cache` are default values, specified by the [Freedesktop.org
Basedir
specification](http://www.freedesktop.org/wiki/Specifications/basedir-spec).
To override these values one may set some environment varibles:

-   `$XDG_DATA_HOME` for user specific application data.
-   `$XDG_CONFIG_HOME` for user specific configuration data.
-   `$XDG_CACHE_HOME` for user specfic 'non-essential' data.

The BaseDir specification has shades of the Windows user profile file
structure, but in a good way. Agreeing on such cross-desktop conventions
will solidify Linux as a desktop platform for ISVs, but there's still a
way to go. Other [Freedesktop.org
specifications](http://www.freedesktop.org/wiki/Specifications) build on
BaseDir, for instance the [Trash
specification](http://www.freedesktop.org/wiki/Specifications/trash-spec).
So now Gnome's trash applet knows where a deleted item should be
restored to.
