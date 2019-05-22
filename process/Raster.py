import logging

from osgeo import gdal

from model.GeoInfo import GeoInfo
from config.Settings import LOG_FORMAT

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def process(out_filepath, src_filepath, process_type, color_file=None):
	"""
	Transform src raster file and output to new raster file 
	Args:
		output_file: File path for output file
		src_filepath: File path for source raster file
		process_type: Type of process to apply
	"""
	options = gdal.DEMProcessingOptions(zeroForFlat=True, colorFilename=color_file)
	dataset = gdal.DEMProcessing(out_filepath, src_filepath, process_type, options=options)
	logging.info("Dataset Processed: {}".format(out_filepath))
	dataset = None


def info(filepath):
	"""
	Get Raster metadata as String
	Args:
		filepath: String file path to raster
	Returns:
		String metadata output from GDAL Info 
	"""
	metadata = gdal.Info(filepath)
	logging.info("Dataset Metadata: {}".format(metadata))
	return metadata


def read(filepath):
	"""
	Get Raster metadata and data as GeoInfo object
	Args:
		filepath: String file path to raster
	Returns:
		GeoInfo object with raster metadata and data
	"""
	dataset = gdal.Open(filepath)
	geoinfo = GeoInfo(dataset=dataset, datatype='GEOTIFF')
	logging.info("Dataset Loaded: {}".format(geoinfo))
	dataset = None
	return geoinfo