# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from osgeo import ogr
import shapely
################################################################################
print(shapely.__version__)
################################################################################
import shapely.geos
shapely.geos.geos_version
shapely.geos.geos_capi_version
shapely.geos.geos_version_string
################################################################################
################################################################################
################################################################################
from shapely import speedups
speedups.available
################################################################################
speedups.enable()
