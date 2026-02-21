---
date: 2008-11-26
title: Deep Zoom and others for displaying large images on the web
type: post
---

Slashgeo have noted the release of [Deep Zoom in
Javascript](http://technology.slashgeo.org/technology/08/11/26/1717243.shtml)
aka [Seadragon](http://livelabs.com/seadragon/), by Microsoft. [Deep
Zoom](http://msdn.microsoft.com/en-us/library/cc645050(VS.95).aspx)
allows one to deliver a very high resolution image over the web, with
pan and zoom. Only the portions viewed are download, so bandwidth usage
is minimised. Until now Deep Zoom was Silverlight only. It works
similarly to OpenStreetMap, Google Maps or Live Search Maps. A large
image is transformed into a 'pyramid', by generating lower resolution
versions (e.g. full, ½, ¼, …) and stacking them until a peak is
reached. Each level is cut into square tiles, which are stored
individually in a known hierarchy. The pyramid generation is similar to
[mip-mapping](http://en.wikipedia.org/wiki/Mip_map). The image might be
satellite or aerial photography, a scanned map, a legal document,
medical imagery (e.g. a smear test or x-ray) or any highly detailed
photograph. Deep Zoom joins a collection of platforms and technologies
that perform a similar role, which I'll briefly summarise.

<!--more-->

IIPImage
--------

[IIPImage](http://iipimage.sourceforge.net/)[](http://iipimage.sourceforge.net/documentation/protocol/)
is an Open Source package that has a similar design to Deep Zoom, it's
named after the [Internet Image
Protocol](http://iipimage.sourceforge.net/documentation/protocol/). The
tiles are extracted as needed from a specially constructed tiff file. On
the server a FastCGI module extracts the tiles as needed.
[Clients](http://iipimage.sourceforge.net/documentation/clients/)
written in Java
([demo](http://merovingio.c2rmf.cnrs.fr/iipimage/IIPJavaDemo-Galaxy.html)),
Flash
([demo](http://merovingio.c2rmf.cnrs.fr/iipimage/IIPFlashDemo.html)) and
AJAX
([demo](http://merovingio.c2rmf.cnrs.fr/iipimage/iipmooviewer-1.1/nebula.html))
clients are available.

Lizardtech GeoExpress/MrSID
---------------------------

[Lizardtech
ExpressView](http://www.lizardtech.com/download/dl_download.php?detail=geo_expressview_plugin&platform=win)
is a browser plugin to view files in the proprietary
[MrSID](http://en.wikipedia.org/wiki/MrSID) image format. MrSID files
can achieve higher compression ratios than JPEG for a given image
quality, particularly for aerial imagery. ExpressView is Windows only,
but is also able to render a MrSID file from a local disk or an email
attachment. Encoding can be done with GeoExpress, or GDAL or other
applications that embed the SDK.

OpenLayers
----------

[OpenLayers](http://openlayers.org/) is a JavaScript library used for
embedding a map (e.g. [OpenStreetMap](http://openstreetmap.org/)) within
the browser. OpenLayers is not restricted to maps, it can be used with
[TileCache](http://tilecache.org/), to [view any
bitmap](http://tilecache.org/demos/mario.html).

Zoomify
-------

[Zoomify](http://www.zoomify.com) is a long term player in this field,
offering Zoomify EZ, Zoomify Flash and Zoomify Enterprise. The Flash
client is free to use in it's most basic form, or additional features
are available for a fee.

Other image formats
-------------------

[JPEG 2000](http://www.jpeg.org/jpeg2000/) is a open format similar in
design to MrSID, but it has gained little traction on the desktop. [HD
Photo](http://en.wikipedia.org/wiki/HD_Photo) (aka JPEG XR, fka Windows
Media Photo) is a fledgling format with similar capabilities to JPEG
2000 or MrSID, but cheaper encoding routines that make it faster to
compress. [ER Mapper](http://www.ermapper.com/) ECW is again similar to
MrSID and JPEG 2000, a Windows only [ER
Viewer](http://www.ermapper.com/ProductView.aspx?t=160) is available. If
you know of other formats, technologies or techniques, or if you'd like
to know more, please leave a comment.
