import os

import argparse
import osr
from osgeo import gdal

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


script_dir = os.path.dirname(os.path.abspath(__file__))

class GeoInfo():
	def __init__(self, driver,crs, data, count, height, width):
		self.driver = driver
		self.crs = 'epsg:' + crs
		self.data = data
		self.count = count
		self.height = height
		self.width = width


def process_raster(output_file, input_file, display_type):
	options = gdal.DEMProcessingOptions(zeroForFlat=True)
	dataset = gdal.DEMProcessing(output_file, input_file, display_type, options=options)
	print("Dataset Processed: {}".format(dataset.GetDescription()))


def read_raster(filepath):
	dataset = gdal.Open(filepath)
	proj = osr.SpatialReference(wkt=dataset.GetProjection())
	crs = proj.GetAttrValue('AUTHORITY', 1)
	return GeoInfo(dataset.GetDriver().LongName, crs, dataset.ReadAsArray(), dataset.RasterCount, dataset.RasterXSize, dataset.RasterYSize)


def display_raster(geoinfo):
	plt.subplots(figsize = (10,10))
	plt.imshow(geoinfo.data, cmap='Greys')
	plt.colorbar()
	plt.xlabel('Column')
	plt.ylabel('Row')
	plt.title('Raster Shape - {}, {}'.format(geoinfo.height, geoinfo.width))
	plt.show(block=True)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Geosense: Geospatial library for testing geo libs and data')
	parser.add_argument('--srcfile', required=True, help='Source File name')
	parser.add_argument('--outfile', required=True, help='Ouput File name')
	parser.add_argument('--process', default='hillshade', help='Display Types: hillshade, slope, aspect, color-relief, TRI, TPI, Roughness')
	args = parser.parse_args()

	src_file = os.path.join(script_dir, args.srcfile)
	out_file = os.path.join(script_dir, args.outfile)
	print('Source File: {}, Out File: {}'.format(src_file, out_file))

	process_raster(out_file, src_file, args.process)
	geoinfo = read_raster(out_file)
	#display_raster(geoinfo)