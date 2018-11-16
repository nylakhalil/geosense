import os
import logging

import argparse

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import process.Raster as raster
from config.Settings import LOG_FORMAT

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
script_dir = os.path.dirname(os.path.abspath(__file__))


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
	logging.info('Source File: {}, Out File: {}'.format(src_file, out_file))

	raster.process_raster(out_file, src_file, args.process)
	geoinfo = raster.read_raster(out_file)
	#display_raster(geoinfo)