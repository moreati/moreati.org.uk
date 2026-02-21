---
date: 2008-03-27
title: Notes on using sdelayer to mosaic data into ArcSDE
type: post
---

For those who aren't familiar, ArcSDE is server software that sits atop
a database to spatially enable it. The resulting geodatabase is able to
store geographic features (e.g. roads, buildings, endangered habitats)
along with more common SQL data types. ArcSDE can also store
georeferenced rasters such as scanned plans/maps or satellite/aerial
imagery. To load raster data as a continuous layer one typically mosaics
many images, using ArcGIS Desktop or the sderaster command. ArcGIS
Desktop is more flexible, it accepts many image formats and can resample
images that don't perfectly align, but it's slow and struggles with
large jobs. The sderaster command is faster and scriptable, but it
accepts only tiffs and it's *very fussy* about them.

<!--more-->

What
follows are some notes that will remind me the next time and possibly
help others.

1.  If the real world pixel size (i.e. units m/px or ft/px) on lines 1 &
    4 of the world file are not exactly equalt to the value you
    calculate then correct the world files. If present also correct the
    geotiff headers. Ordnance Survey 10K tiles may need this correction.
2.  Pyramidding is only visually effective if it can create pixels with
    averaged colour values. Monochrome or colour mapped images do not
    satisfy this requirement.
3.  The documentation states that ArcSDE cannot mosaic images with a
    colour map. This also applies in some cases where no colourmap is
    present, such as 4 bit greyscale. Use the -N switch to be safe and
    then reapply the colour map with sderaster -o colormap, once all
    images are mosaiced.
4.  Geotiff headers are tricky to remove in place, en masse. When
    preprocessing images be sure that either the world file and/or
    geotiff tags are correct, or generate your tiffs without getiff
    tags.
5.  GDAL is much faster than ImageMagick for altering bit depth. The
    libtiff utilities are faster yet.
6.  Until ArcSDE 8.3 SP, sderaster required that the top left image be
    loaded into a raster first, or it wouldn't mosaic anything.

Those wishing to save the effort of loading images into ArcSDE, might
wish to look into ArcGIS ImageServer or a WMS server. To update world
files in a batch try the following python script:

    import os
    import sys
    import fileinput
    import re
    import glob

    def replace_in_files(filenames, pattern, rterm):
        '''Replace all occurances of regex pattern with rterm in sequence of filenames'''
        regex = re.compile(pattern)
        for line in fileinput.input(filenames, inplace=True):
            sys.stdout.write(re.sub(rterm, line))

    if __name__ == '__main__':
        pattern = sys.argv[1]
        rterm = sys.argv[2]
        filenames = glob.glob(sys.argv[3])

        replace_in_files(filenames, pattern, rterm)
