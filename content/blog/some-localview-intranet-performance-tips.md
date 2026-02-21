---
date: 2009-08-04
title: Some LocalView Intranet performance tips
type: post
---

[LocalView
Intranet](http://www.esriuk.com/products/product.asp?prodid=138&) is a
web mapping product developed and sold by ESRI UK, predominantly to
local councils. The current version (as of August 2009) is 2.1 SP2,
supported on ArcGIS Server 9.2 SP5. The following are some straight
forward tips for improving it's performance:

1.  The ArcMap document (mxd) defining each map service is critical to
    every aspect of LocalView performance. Simplify, simplify, simplify.
    Start with a *few, simple* layers and test the responsiveness of the
    site, particularly with *simultaneous users*.
2.  You're only as fast as your slowest layer. Test your mxd separately
    with [MXDPERFSTAT]({{< relref "mxdperfstat.md" >}}). For an overall quick
    map response, with many concurrent users then you should aim for a
    worst case 0.5-1.0 second draw time per layer.
3.  File Geodatabases are very fast. Hold as many layers as you can (all
    if possible) locally in a File Geodatabase. Small latencies in the
    data access add up, and you may be surprised at the performance
    gain, perhaps 50% or higher.
4.  Minimize the number of tasks you assign to each role, don't assign
    every task to every user. Each task added increases the cost of
    starting a new session.
5.  Don't enable the navigation overlay, if you can avoid it.
6.  LocalView is written in ASP.NET, using the Web ADF. To maintain your
    session these use
    [ViewState](http://msdn.microsoft.com/en-us/library/ms972976.aspx)
    extensively. With each request the ViewState is sent from the
    browser to the server and back. This has a performance impact,
    particularly on high latency network links. To keep the ViewState
    manageable keep the number of layers and tasks to a minimum. To
    monitor the ViewState use Firefox with the [ViewState size
    addon](https://addons.mozilla.org/en-US/firefox/addon/5956). For
    LocalView I consider a 2 kB ViewState small, a 20 kB ViewState on
    the large size, and a 200 kB ViewState very large.
7.  Within the MXD hide any attributes that are unnecessary. Each
    visible attribute contributes to the size of ViewState. However, do
    not hide the spatial column - it is necessary for the correct
    function of LocalView.
8.  Read and understand the articles listed in [Top Ten Most Helpful
    ArcGIS Server Help Topics
    Countdown](http://blogs.esri.com/Support/blogs/supportcenter/archive/2008/12/30/getting-the-most-out-of-server-web-help.aspx).
    But don't spend too long reading about the map cache, LocalView
    won't use it.

Once you've taken care of the above, there are some more esoteric

1.  Enable [HTTP
    Keep-Alive](http://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/d7e13ea5-4350-497e-ba34-b25c0e9efd68.mspx?mfr=true)
    in IIS. LocalView makes a lot of GETs and POSTs, and establishing a
    new connection for each one is unnecessary.
2.  Enable [persistent Kerberos Integrated
    Authentication](http://support.microsoft.com/kb/917557). If you're
    in an Active Directory domain and using Integrated Authentication,
    then the default configuration of IIS and Internet Explore may
    double the number of requests made by the browser. NB: You must
    still set EnableKerbAuthPersist whether you
    have the hotfix or SP2, the Microsoft Knowledge-base article doesn't
    make this clear.
3.  If your server has CPU cycles to spare,
    enable HTTP compression for both *static and dynamic content*. This
    should reduce your network traffic significantly. Follow the
    instructions at [Coding
    Horror](http://www.codinghorror.com/blog/archives/000059.html). The
    bulk of LocalView traffic is from dynamic content,
    unfortunately.
4.  Choose the image format of your map
    carefully. On a large monitor, each map zoom could result in a 1 MB
    image being generated. If your data is mostly vector and
    pre-rendered rasters (e.g. OS 1:50000), then 8-bit PNG should
    suffice. If you are using scanned maps, or aerial imagery in your
    map, then JPEG may be better.
5.  Check what requests and responses are
    happening, with
    [Firebug](https://addons.mozilla.org/en-US/firefox/addon/1843) for
    Firefox and[Fiddler](http://www.fiddlertool.com/fiddler/) for
    Internet Explorer. Bare in mind that they may behave differently,
    depending on your proxy and authentication settings.
6.  If you can choose the browser, then I've
    found that Firefox 3 is most responsive, then Internet Explorer 7,
    and Internet Explorer 6 is the least responsive. Particularly, IE 6
    can freeze for many seconds at a time.

To enable integrated authentication within
Firefox, the following 2 items should be configured within
about:config:

-   network.automatic-ntlm-auth.trusted-uris
-   network.negotiate-auth.trusted-uris
