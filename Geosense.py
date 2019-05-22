import os
import logging

import argparse

import process.Raster as raster
from config.Settings import LOG_FORMAT, DATA_PATH

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
script_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Geosense: Geospatial library for testing geo libs and data')
	parser.add_argument('--srcfile', required=True, help='Source file name')
	parser.add_argument('--outfile', required=False, help='Ouput file name')
	parser.add_argument('--colorfile', help='Color file name. Used in color-relief process')
	parser.add_argument('--process', default='hillshade', help='Process Types: hillshade, slope, aspect, color-relief, TRI, TPI, Roughness')
	args = parser.parse_args()

	color_file = None
	if args.process == 'color-relief':
		color_file = os.path.join(DATA_PATH, args.colorfile)

	src_file = os.path.join(script_dir, args.srcfile)
	if args.outfile:
		out_file = os.path.join(script_dir, args.outfile)
		logging.info('Source File: {}, Out File: {}'.format(src_file, out_file))
		raster.process(out_file, src_file, args.process, color_file)
	else:
		raster.read(src_file)