# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
from osgeo import gdal
ds = gdal.Open('/gdata/lu75c.tif')
gdal.Translate('/tmp/xx_output.tif', ds, format = 'GTiff', outputSRS ='EPSG:3857', xRes=100, yRes=100)
