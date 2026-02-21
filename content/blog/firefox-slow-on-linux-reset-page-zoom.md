---
date: 2008-11-23
title: 'Firefox rendering/scrolling slow on Linux? Try reseting page zoom'
type: post
---

For months now, I've found Firefox on my Linux laptop to sometimes be
sluggish and a CPU hogging, particularly when scrolling. T-Mobile UK and
Engadget were the worst affected. Visiting t-mobile.co.uk saturated the
CPU for several seconds whilst rendering. The result looked horrible -
grainy, and badly pixelated. I'd attributed this to X, Nvidia, browser
sniffing, Flash and Javascript/CSS. Of course it was me all along.
Firefox 3 has a feature called [Full Page
Zoom](http://www.mozilla.com/en-US/firefox/features/#full-zoom), it
doesn't just resize text, it scales everything on the page. I had zoomed
these pages, then forgotten. If any of this sounds familiar, try
reseting your zoom level:

1.  Visit the page that scrolls slowly or looks pixelated.
2.  Either press Ctrl + 0, or click Edit -> Zoom -> Reset.
3.  If text is now too small to read, enable Edit -> Zoom -> Zoom Text
    Only, then zoom in with Ctrl + +.

Firefox should now scroll the site smoothly and quickly. The zoom level
is remembered on a per site basis, so repeat this for any other pages
affected. If you would like to control zoom from the toolbar, try the
[PageZoom](https://addons.mozilla.org/en-US/firefox/addon/1499)
extension. If you would like to set the zoom globally, try [No
Squint](https://addons.mozilla.org/en-US/firefox/addon/2592) (courtesy
of [AncientPC on Al-Osaimi
Techlog](http://alosaimi.blogspot.com/2008/01/firefox-3-full-page-zoom-good-idea-bad.html)).
The question remains why Full Page Zoom can be so sluggish, and under
what circumstances. Also, why does [Try Firefox 3 full page
zoom](http://mozillalinks.org/wp/2007/07/try-firefox-3-full-page-zoom-with-full-page-zoom/)
on Mozillalinks performs so poorly for me, regardless of page zoom.
