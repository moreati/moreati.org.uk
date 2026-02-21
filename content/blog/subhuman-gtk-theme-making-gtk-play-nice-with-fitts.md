---
date: 2008-09-20
title: 'SubHuman GTK theme: making GTK play nice with Fitts'
type: post
---

In [Fitts Law and Minimalism vs GTK+ and
Qt](/blog/2008/09/18/fitts-law-and-minimalism-vs-gtk-and-qt/)
I complained about the excessive use of borders and padding in GTK+ and
Qt. Here's what I've got so far (click for unscaled versions):

[![Pidgin
chat before
slimming](/uploads/2008/09/pidgin-chat-before.png "pidgin-chat-before")](/uploads/2008/09/pidgin-chat-before.png)[![Pidgin
chat after slimming
down](/uploads/2008/09/pidgin-chat-after.png "pidgin-chat-after")](/uploads/2008/09/pidgin-chat-after.png)

Although work in progress still, I think the window looks cleaner
already. Most importantly the chat history scrollbar now lies flush with
the window edge. To achieve this, I've created a customized gtkrc and
made a small patch for pidgin.

<!--more-->

### GTK+ theming

[GTK can be
themed](http://live.gnome.org/GnomeArt/Tutorials/GtkThemes%20) on a per
system, per user, per application or even per widget basis. Each visible
widget has a style attached. The style is specified in gtkrc files, in a
manner similar to CSS. A GTK+ theme is a gtkrc file, perhaps bundled
with some images. The default GTK+ theme is functional but ugly, so
Linux distributions usually create their own. On Ubuntu the default
theme is Human. To override Human, one can:

-   Install a new GTK theme, such as
    [ClearLooks](http://www.gnome-look.org/content/show.php?content=19527)
    or [Human
    Compact](http://www.gnome-look.org/content/show.php?content=80980).
-   Override the default theme by creating a `~/.gtkrc-2.0` file.

The gtkrc that I' currently using is
[subhuman-gtkrc-20](/uploads/2008/09/subhuman-gtkrc-20).
To use this, download it and save it as `.gtkrc-2.0` in your home
folder. Any GTK+ programs started from then on will have padding
removed. Gedit, Anjuta and Gnome Terminal respond well. Seahorse and
undoubtedly others aren't as good.

### Application patching

Theming, still leaves the problem of the border and the users list in
Pidgin. The border is taken care of by
[pidgin-chat-border.patch](http://developer.pidgin.im/attachment/ticket/6987/pidgin-chat-border.patch)
(attached to [Pidgin bug 6987](http://developer.pidgin.im/ticket/6987)).
Swapping the user list I'm working on, so no patch yet.

### Next steps

The customized gtkrc file is still raw, it's causing visual glitches
such as lack of an outline around the Pidgin chat history and the Gnome
Terminal VT. So my first priority is fixing those, without shifting the
boundary. Apple OS X appears to draw no window decorations along the
vertical edge of a window, I'd like to experiment with this. If there's
interest I'll refine the gtkrc and release it as a GTK theme. For now,
I aim to get the border removal merged into a future Pidgin release and
submit a patch to swap the user list and chat history.
