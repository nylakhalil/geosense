import logging

import osr
from osgeo import gdal

from model.GeoInfo import GeoInfo
from config.Settings import LOG_FORMAT

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def process_raster(output_file, input_file, display_type):
	options = gdal.DEMProcessingOptions(zeroForFlat=True)
	dataset = gdal.DEMProcessing(output_file, input_file, display_type, options=options)
	logging.info("Dataset Processed: {}".format(dataset.GetDescription()))


def read_raster(filepath):
	dataset = gdal.Open(filepath)
	proj = osr.SpatialReference(wkt=dataset.GetProjection())
	crs = proj.GetAttrValue('AUTHORITY', 1)
	return GeoInfo(dataset.GetDriver().LongName, crs, dataset.ReadAsArray(), dataset.RasterCount, dataset.RasterXSize, dataset.RasterYSize)