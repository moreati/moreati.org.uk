---
layout: post
title: 'The Shapefile 2.0 manifesto'
---

Geographic Information Systems (GIS) are by their nature data driven.
The data comes in a wide variety of raster and vector formats. Rasters
hold raw, continuous data recorded striaght from the real world. An
example is Satellite/aerial imagery, this is a commonly held in an open
format with broad support, such as
[GeoTIFF](http://en.wikipedia.org/wiki/GeoTIFF) or
[GeoJPEG](http://en.wikipedia.org/wiki/JPEG). [Vector
formats](http://en.wikipedia.org/wiki/GIS_file_formats#Vector_formats)
hold refined, discrete data, which has been manually traced or otherwise
derived other data sources. Examples include building outlines,
contours, road routes, pipe networks land land parcels and locations.
Vector data is usually traced or derived, at great expense from raster
data, to encode business information - as a result it's usually highly
valuable. Unfortunately, there are many GIS vector file formats, and
most are proprietary. They can only be used to their full in their
native software. Three of the biggest are AutoCAD
[DXF](http://en.wikipedia.org/wiki/AutoCAD_DXF), MapInfo
[TAB](http://en.wikipedia.org/wiki/MapInfo_TAB_format) and ArcGIS
[Personal
Geodatabase](http://en.wikipedia.org/w/index.php?title=Personal_Geodatabase).
One vector format is unique - both an open standard, and in wide use:
Shapefile [Shapefile](http://en.wikipedia.org/wiki/Shapefile) is
publicly documented in [ESRI Shapefile Technical
Description](http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf)
by [ESRI Inc.](http://www.esri.com), it's creator. Any GIS software
worth it's salt can read and write to the format, so it's become the
least common denominator. It is *the* format for storing and exchanging
vector data between teams, departments, businesses and government. In my
opinion this makes Shapefile the best thing ever to happen to GIS,
without it the GIS market would be a fraction of it's current
size.

<!--more-->

Despite it's popularity, Shapefile does have some
serious limitations, mainly due to it's DBF heritage:

-   A shapefile is limited to <del>2</del> 4 GB or <del>65535</del> 4
    billion/len(record) records. Where len(record) is greater of either
    the average feature length in bytes, or the length of a DBF record.
-   Records are limited to <del>1000</del> 65536 bytes or
    <del>32</del> between 257 &
    2038 fields.
-   Field names are limited to <del>8</del> 10 characters,
    character fields can hold up to 254 bytes.
-   Unicode is <del>not supported</del> not widely supported.

Currently the only real alternative, for data exchange, is [Geography
Markup Language
(GML)](http://en.wikipedia.org/wiki/Geography_Markup_Language) as
defined by the [Open Geospatial Consortium
(OGC)](http://www.opengeospatial.org/). An XML dialect, GML has none of
the limitations of Shapefile this is why Ordnance Survey use GML to
supply
[MasterMap](http://www.ordnancesurvey.co.uk/oswebsite/products/osmastermap/),
a highly detailed vector map of Great Britain. Support for GML in
software is growing, but it's unsuitable as a storage format. Viewing
and editing vector data requires support for random access by attribute
and by spatial extent. As an XML dialect GML cannot do this, to find one
record, the entire file must be parsed from beginning to end. GML is
almost always converted to another format, or loaded into a spatial
database before it is used. A spatial database is a database with data
types and functions able to handle geospatial data. For the major
databases there is [Oracle
Spatial](http://www.oracle.com/technology/products/spatial/index.html),
[PostgreSQL PostGIS](http://postgis.refractions.net/), [SQL Server
Spatial](http://www.microsoft.com/sqlserver/2008/en/us/spatial-data.aspx),
[MySQL
Spatial](http://dev.mysql.com/doc/refman/5.1/en/spatial-extensions.html)
and [DB2 Spatial
Extender](http://www-01.ibm.com/software/data/spatial/). All are based
on [Simple Features for
SQL](http://en.wikipedia.org/wiki/Simple_Features) an open standard,
meaning spatial data can be queried and updated with SQL like any other
data type. I believe that a portable, standalone spatial database, would
make a very good successor to Shapefile. Such a format would drive the
GIS market forward, increasing usage of GIS by making it easier to share
edit, publish and share GIS data. A portable spatial database would
negate the need for the import, view, edit, export cycle that GML
imposes. At the moment I see 3 contenders for the crown:

1.  [File
    Geodatabase](http://www.esri.com/software/arcgis/geodatabase/about/file-gdbs.html)
    is a format from ESRI, it is natively supported by ArcGIS. ESRI
    proclaim it "Allow[s] users to easily exchange geodatabases." That
    is true only if both users are running ESRI's ArcGIS software. File
    Geodatabase is a proprietary format, despite promises by ESRI when
    it was launched.
2.  [Spatial Data Format](http://fdo.osgeo.org/fdosdf/index.html) (SDF)
    is a format from Autodesk, it is native support . Support is
    included as part of their Feature Data Objects library, released as
    Open Source. SDF is based on the popular SQLite embedded database
    engine.
3.  [Spatialite](http://www.gaia-gis.it/spatialite/) is another format
    based on SQLite, by an Alessandro Furieri. Spatialite is in it's
    infancy still, it's first release was 11 months ago.

Unfortunately none of these looks like it will become a clear winner any
time soon. Each is supported by only one application currently. If ESRI
releases the specification for File Geodatabase, I expect it will
quickly gain widespread support due to their position as market leader.
As open source applications such as [QGIS gain Spatialite
support](http://lists.osgeo.org/pipermail/qgis-developer/2009-January/005791.html),
it could slowly achieve dominance in a grass roots fashion. SDF seems to
be going nowhere. So ESRI, please publish the details of File
Geodatabase. At it's launch, during the 2006 ESRI User Conference, you
promised that File Geodatabase would be an interoperable format. You
promised to release a software library, so we could read and write
them without ArcGIS. Neither has happened. So File Geodatabase is just
another closed format, another pretender to the throne that's achieved
only 1% of it's true potential. Publish File Geodatabase, or we'll take
the Shapefile crown by force. Update 27 Mar 2009: Corrected Shapefile
limits, based on [Xbase file
structure](http://www.clicketyclick.dk/databases/xbase/format/dbf.html)
rather than [dBASE software
specifications](http://www.clicketyclick.dk/databases/xbase/format/dbase_spec.html).
