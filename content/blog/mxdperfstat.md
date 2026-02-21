---
date: 2009-02-14
title: MXDPERFSTAT
type: post
---

Investigating the performance of an intranet mapping website this week,
I was introduced
[MXDPERFSTAT](http://arcscripts.esri.com/details.asp?dbid=15570). It's a
fantastic tool for investigating map display performance. Given an
ArcMap document (a .mxd file) it runs ArcMap and loops over the map
layers, displaying each at a list of scales (e.g. 1:100000, 1:10000,
1:2500, 1:500) automatically. Scale cut-offs are followed, in the same
way ArcMap would. Once done, MXDPERFSTAT writes an html report, of the
time taken and features retrieved to display each layer at each scale.
Since it runs in situ, network delays and other real world bottlenecks
are accounted for. It even highlights layers that are abnormally slow,
or that fetch an excessive number of features. Perfect for diagnosing a
slow map, or guiding a tune up of the infrastructure. Supporting ArcGIS
installations, I'm a regular searcher on
[ArcScripts](http://arcscripts.esri.com). How did I miss this for the
last 4 years, and what other gems are there? What GIS utilities do you
find indispensable?
