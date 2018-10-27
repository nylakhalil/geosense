import os

import numpy
import argparse
import rasterio
import numpy as np
from rasterio.plot import plotting_extent

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


script_dir = os.path.dirname(os.path.abspath(__file__))


class GeoInfo():
	def __init__(self, data, meta, shape, extent):
		self.data = data
		self.meta = meta
		self.shape = shape
		self.extent = extent


def hillshade(array, azimuth, angle_altitude):
	# FROM: https://github.com/rveciana/introduccion-python-geoespacial/blob/master/hillshade.py#L23
    azimuth = 360.0 - azimuth 
    
    x, y = np.gradient(array)
    slope = np.pi / 2. - np.arctan(np.sqrt(x*x + y*y))
    aspect = np.arctan2(-x, y)
    azimuthrad = azimuth * np.pi / 180.
    altituderad = angle_altitude * np.pi / 180.
     
 
    shaded = np.sin(altituderad) * np.sin(slope) + np.cos(altituderad) * np.cos(slope) * np.cos((azimuthrad - np.pi/2.) - aspect)
    return 255 * (shaded + 1) / 2


def read_raster(filepath):
	with rasterio.open(filepath) as src:
		print("Metadata: {}".format(src.meta))
		raster = src.read(1, masked=True)
		return GeoInfo(raster, src.meta, raster.shape, rasterio.plot.plotting_extent(src))


def display_raster(raster, display_type):
	if display_type.upper() == "HILLSHADE":
		array = hillshade(raster.data, 30, 30)
	else:
		array = raster.data

	plt.subplots(figsize = (10,10))
	plt.imshow(array, cmap='terrain_r', extent=raster.extent)
	plt.colorbar()
	plt.xlabel('Column')
	plt.ylabel('Row')
	plt.title('Raster Shape - {}'.format(raster.shape))
	plt.show(block=True)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Geosense geospatial library for testing geo libs and data')
	parser.add_argument('--filename', required=True, help='File name')
	parser.add_argument('--display', default='ORIGINAL', help='Display Types: ORIGINAL, HILLSHADE')
	args = parser.parse_args()

	filepath = os.path.join(script_dir, args.filename)
	print('File path: {}'.format(filepath))

	raster = read_raster(filepath)
	display_raster(raster, args.display)

