---
date: 2009-01-27
title: 'from ESRI.ArcGIS import Geodatabase'
type: post
---

A couple of years ago [I tried to use ArcObjects, through
IronPython](http://lists.ironpython.com/pipermail/users-ironpython.com/2007-February/004588.html).
It didn't quite work. Last week I tried again, using the newly released
IronPython 2.0. This time it worked better.
[create\_sde\_conn\_file.py](/uploads/2009/01/create_sde_conn_filepy.txt)
is based on CreateSDEConnFile.java, from [Creating ArcSDE connection
files on the fly using Python and
ArcObjects](http://blogs.esri.com/Dev/blogs/geoprocessing/archive/2008/09/24/Tips-and-Tricks-_2D00_-Creating-ArcSDE-connection-files-on-the-fly-using-Python-and-ArcObjects.aspx)
on ESRI's Geoprocessing blog. For those not already familiar,
[ArcGIS](http://en.wikipedia.org/wiki/ArcGIS) is by accounts the market
leader for Geographic Information System (GIS) software. The core of the
suite comprises ArcGIS Desktop, and ArcGIS Server. On the desktop ArcMap
is used to create map documents (.mxd file), whilst ArcCatalog is used
to manage data sources. ArcGIS Server can (amongst other things) serve a
map document, as a service for web client, Google Earth or remote ArcMap
users. ArcGIS may be automated to an extent, through an interface known
as ArcGIS Geoprocessing. But this covers only some cases, delving deeper
provides much greater opportunities. ArcGIS is built on a COM object
library named
[ArcObjects](http://resources.esri.com/arcgisdesktop/index.cfm?fa=forDevelopers).
Native ArcGIS files, such as an ArcSDE connection (.sde file) are the in
memory COM object, serialised to disk as binary. It is difficult to edit
or create such files in an automated fashion, without calling
ArcObjects. So, like the Java code CreateSDEConnFile.py calls ArcObjects
directly. It can produce an ArcSDE connection file, suitable for
ArcCatalog. It works by calling the .NET bindings, through Interop
assemblies. Anything that can be done through VBA, or C\# should be
possible through IronPython. There are a couple of rough edges.
ArcObjects is verbose, and IronPython requires some boilerplate to deal
with interfaces. Instead of writing `conn_props['SERVER'] = sys.argv[2]`
or even `conn_props.SetProperty('SERVER', sys.argv[2])` one needs to
write:
`esriSystem.IPropertySet.SetProperty(conn_props, 'SERVER', sys.argv[2])`
This is explained properly in IronPython bug
[1506](http://www.codeplex.com/IronPython/WorkItem/View.aspx?WorkItemId=1506)
and
[4538](http://www.codeplex.com/IronPython/WorkItem/View.aspx?WorkItemId=4538).
To run the script call it as:
`"c:Program FilesIronPythonipy.exe" create_sde_conn_file.py  filename.sde hostname 5151 username password SDE.DEFAULT ""`
My intention is to take this proof of concept further. To do the same
with layer files and map documents. Ultimately to create a build system,
able to automatically generate a complete ArcMap document, from textual
source files (e.g. json2mxd.py, mxd2xml.py). This would allow proper
version control of the source material, and automatic deployment of
ArcGIS Server map services. In the wider scheme, it should be possible
to create custom GIS applications with Python, using the full
capabilities ArcObjects and ArcGIS. Updated 29 Jan 2009: Added some
context, for those coming to this post from a Python background.
Expanded goals.
