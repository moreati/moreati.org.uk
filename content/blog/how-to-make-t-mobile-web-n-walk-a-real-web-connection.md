---
date: 2008-02-28
title: 'How to make T-Mobile Web n Walk a real web connection'
type: post
---

Thanks to a comment on the blog post [Hacking
T-Mobile](http://www.lewiz.org/archive/2007/01/03/hacking-t-mobile-web-proxy/),
I've discovered that the T-Mobile Web n Walk transparent proxy can be
~~bypassed~~ neutered. Assuming you use Firefox, here are the steps:

1.  Install the [Modify Headers](https://addons.mozilla.org/firefox/967)
    addon.
2.  In Tools -\> Modify Headers, open the Modify Headers dialog.
3.  Along the top row set the operation as Add, the name as
    'Cache-Control', the value as 'no-transform'. Click Add, the header
    modification should appear in the list, with a green circle to show
    it's enabled.
4.  Click Configuration, tick the Always On check box. Close the dialog.

Explanation: Normally T-Mobile recompresses all images in websites
viewed through web n walk. The effect varies from slightly grainy to
jarringly blocky. The recompression can be overridden, by performing a
forced refresh. T-Mobile add tooltips in the HTML, to mention this. A
forced refresh causes the header 'Cache-Control: no-cache' to be sent,
which overrides the transparent proxy and forces the request to go
straight to the original web server. This means the original image is
delivered, but more traffic than necessary is generated. The header
'Cache-Control: no-transform' allows T-Mobile to cache the content, but
forbids them from recompressing images or otherwise modifying the web
page. Alex
