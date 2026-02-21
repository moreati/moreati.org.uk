---
date: 2008-10-31
title: Barriers to year of linux on the desktop
type: post
---

This post is a tribute to [Linux
Hater](http://linuxhaters.blogspot.com/ "Linux Hater's Blog") who sadly
[has retired](http://linuxhaters.blogspot.com/2008/10/eof.html). He was
insightful and [right about many
things](http://linuxhaters.blogspot.com/2008/06/how-to-be-linux-user.html "How to be a Linux user"),
although sometimes [a bit too
whiny](http://linuxhaters.blogspot.com/2008/09/wine-with-side-of-chrome.html "Wine, with a side of Chrome").
Linux currently holds about [1% market
share](http://marketshare.hitslink.com/report.aspx?qprid=8&qpmr=100&qpdt=1&qpct=3&qptimeframe=Q "2008Q4 OS market share by Net Applications")
on the desktop. It has gained [0.5% in 2
years](http://marketshare.hitslink.com/report.aspx?qprid=9&qpdt=1&qpct=4&qptimeframe=M&qpsp=93&qpnp=25 "OS desktop market share Oct 2006 to Oct 2008"),
whilst Mac OS X has gained 3%, and MS Windows has lost 4%. In the
browser market Firefox is now nudging [20% market
share](http://marketshare.hitslink.com/report.aspx?qprid=1&qpdt=1&qpct=4&qptimeframe=M&qpsp=93&qpnp=25).
Can Linux ever achieve that? A single '[Year of Linux on the
desktop](http://www.google.co.uk/search?q=year+of+linux+on+the+desktop)'
is unlikely, but it's a [popular
meme](http://blogs.gnome.org/uraeus/2008/10/15/what-do-the-free-desktop-need-to-grow-in-market-share/),
so lets to play. It's some number of years in the future. Ubuntu
'Satisfied Squirrel' has built on slow, steady growth. Linux desktop
share now nudges 20%. What might this *future* Linux desktop be like,
compared to *now*?

<!--more-->

### Linux is too difficult to install

**Now**: This goes back to the early days of [Mandrake
Linux](http://en.wikipedia.org/wiki/Mandrake_linux#History), before
Ubuntu. The installers asked about every detail, from the desktop
environment, through to which boot loader. We've progressed since then.
Installing Ubuntu Linux is as easy, if not easier, than installing
Windows Vista. It will even migrate favourites, emails and other
settings from Windows for you.

**Future**: It didn't matter how streamlined the installer was.
Installing any OS is an arduous and risky task, that normal people don't
do. Install-fests, haven't scaled, but automated deployment has proved
very popular in the corporate sphere. Pervasive packaging, hardware
independence, & [LTSP](http://www.ltsp.org/) have streamlined IT
provision. At 20%, almost all consumer linux desktops come
pre-installed, straight from the manufacturer, only geeks install their
own OS.

**Status**: Work in progress

### Linux is too difficult to configure

**Now**: The classic view of Linux is configuration through the command
line and text files. This is still true of many programs targeted at
power users or developers. The major desktop projects, particularly
Gnome, have paid much to making configuration easier. It's still
sometimes necessary to drop to the command line or gconf-editor, these
are becoming rarer. A freshly installed Linux desktop still needs more
configuration than a Windows desktop, for the typical user. **Future**:
Manually configuring a Linux desktop means answering only a few
questions. Everything is automagical that can be made so. It began with
[Zeroconf](http://www.zeroconf.org/) and spread. Now, only an email
address/password are needed to configure email, contacts, calendaring
and document collaboration - *everything* else is inferred or
discovered. Backups are a 2 click or even 0 click affair. The Linux
desktop has truly become a fire and forget appliance. **Status**: Just
beginning

### Linux is too hard to develop for

**Now**: [Independant Software
vendors](http://en.wikipedia.org/wiki/Independent_software_vendor) are
the backbone of the Windows ecosystem, Microsoft makes it easy for them
prosper. Development tools on Linux are prevalent and very easy to
install (although no single tool rivals Visual Studio). However, from
the perspective of an ISV Linux is unattractive, the problem lies with
the instability of the platform. The stack is still rapidly evolving,
especially in the multimedia space, libraries are being replaced on a
yearly basis. Deploying third party software is a chore, outisde the
repositories everyone reinvents the wheel. There are at least 4
partially incompatible distros that must be targeted, each with 2 or
more versions to package and test on. **Future**: Individual installers
have been abandoned, distrusted due to widespread spyware and trojans.
[App Stores](http://www.apple.com/iphone/appstore/) have replaced
package managers, the same interface manages distribution packages and
purchased applications. GTK and Qt have shipped with robust multimedia
widgets for years. **Status**: Just beginning.

### Linux is too unstable

**Now**: Unix has a reputation for rock solid stability, as does Linux
on the server. Desktop Linux is another matter. Gnome, KDE, Firefox and
OpenOffice are young in comparison to GCC, Emacs, Vim & Pine. The
desktop projects are still adding features, faster than fixing bugs.
Linux desktop and Windows are roughly equal in stability. **Future**:
The amount of new code has if anything increased. The core components &
applications have mostly stabilized, effort now goes on umpteen niche
applications targeting at the average user **Status**: Just beginning

### Linux doesn't work with my hardware

**Now**: Brand new hardware is more hit than miss with Linux, typically
one must wait 6-12 months for drivers to trickle through from the newest
kernel release to a distro release. Hardware that is 2 years or older is
well supported, often better than on Windows. There are significant gaps
such as PDA syncing and full iPod support. **Future**: More hardware is
supported by in-tree, open source drivers. Larger vendors release Linux
drivers with their hardware and work with distributions to get them
deployed. There is a stable interface (possibly
[DKMS](http://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support "Dynamic Kernel Module Support"))
for these drivers to integrate with existing releases, so new kernels
break the drivers less. There are still gaps, PDA syncing more or less
works, but others remain. **Status**: Just starting

### Linux can't display the websites I visit

**Now**: Nearly all European & American websites work with Firefox and
Konqueror, Internet Explorer has lost it's strangle hold. A few niche
sites still require ActiveX, or stubbornly stick to bad habits. The
breakdown varies regionally, and corporate Intranets lag behind the
curve. Flash 10 is the multimedia standard and Silverlight 2 have just
been released. **Future**: Internet Explorer still has a majority, just.
Cross browser websites are seen as the norm. Flash is still going
strong. Silverlight continues to struggle on, but hasn't gained the
critical mass it would need to corner the market. **Status**: Nearly
there

### Linux can't play my music or my movies

**Now**: Ogg Vorbis and Theora are still born as audio/video formats.
MP3, AAC, MPEG 2/4, H.264 and FLV are the victors. Linux can play these
with minimal tweaking, but DVDs or Blu Rays require manual intervention
or just don't work. BBC iPlayer support has been promised for over 12
months now. **Future**: The [MP3
patents](http://en.wikipedia.org/wiki/MP3#Licensing_and_patent_issues)
have expired, there is much rejoicing. Old timers still manually install
libdvdcss and libbdaacs, but many people simply pay \$20 at the App
Store for Fluendo Player or CyberLink PowerDVD. There are rumours that
Apple may announce iTunes for Linux in the next 12 months. **Status**:
Just starting

### Linux can't chat online with my friends

**Now:**Dependant on the territory, either [Windows Live
Messenger](http://get.live.com/messenger), [AOL Instant
Messenger](http://www.aim.com), [Yahoo
Messenger](http://messenger.yahoo.com/) or some other closed network
rules the roost. A few brave souls manage to configure a cross-network
client for text only chat. With one exception, Skype, no official
clients exist for Linux, and third-party clients support only the bare
minimum. **Future**:
[Jingle](http://en.wikipedia.org/wiki/Jingle_(protocol)) has finally
been adopted outside [Google Talk](http://www.google.com/talk/).
[Pidgin](http://pidgin.im/) has been replaced by another, more
multimedia, instant messenger. Cross network messaging is still an arms
race, but it's easier to configure and
[XMPP](http://en.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol)
is slowly becoming the standard. **Status**: Work in progress

### Linux can't connect me to the Internet

**Now**:****Linux is a network OS, but connecting a Linux Desktop
through anything but an ethernet cable is hit and miss. 3G, VPN, ISDN &
ADSL modems require fiddling and manual configuration in all but the
[very latest version of Network
Manager](http://blogs.gnome.org/dcbw/2008/07/20/the-road-to-networkmanager-07/).
[ISPs will not support
Linux](http://joeb454.co.uk/2008/10/15/isps-require-msappleapparently/)
- their software and step by step guides cater only to Windows or
perhaps Mac. At best, setting up a connection requires discovering the
proper parameters and figuring out where to enter them **Future**: A few
brave mainstream ISPs support Linux, the machine can even autoconfigure
given an [Internet Settings
File](http://technet.microsoft.com/en-us/library/bb496381.aspx).
**Status**: In progress

### Linux can't play my games

**Now**: Wine has recently released 1.0 and it's irrelevant to most
games players. **Future**: Wine has recently released 2.0 and it's
irrelevant to most games players. **Status**: Lost

### Linux can't run Photoshop

**Now**: [Photoshop](http://www.adobe.com/products/photoshop/),
[AutoCAD](http://www.autodesk.co.uk/autocad) and
[ArcGIS](http://www.esri.com/software/arcgis/index.html) users make a
small but vocal proportion of the overall user base. They're exacting
and their work is valuable. There seems little prospect of their
products running on the Linux desktop. The vendors apparently don't
consider the potential market worth the expense. **Future**: Market
share has tipped the scales. AutoCAD was the first to be ported,
engineers wanted to run their workstations on the same platforms that
ran their [aerodynamic
simulations](http://en.wikipedia.org/wiki/Computational_fluid_dynamics).
The GIMP has scrubbed up and begun attracting more professional
designers. Adobe is keeping tight lipped, rumours are spreading, the
demand is too great for them to ignore much longer. Others such as
ArcGIS Desktop have Windows technologies too deeply ingrained. Wine
offers some measure of stopgap. **Status**: Not yet started

### Conclusion

There's a lot of work still to do. It certainly won't happen this way,
there's a good chance it won't happen at all. There are other issues,
such as usability and MS Office compatibility, that I've not touched on.
Firefox has shown it's possible, we should be aiming at 20% desktop
market share within the next few years.
