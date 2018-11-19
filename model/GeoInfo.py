import logging

import osr

from config.Settings import LOG_FORMAT

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

class GeoInfo():
	def __init__(self, dataset=None, datatype=None):
		if dataset and datatype:
			if datatype.upper() == 'GEOTIFF':
				self.raster(dataset)
			else:
				logging.warn("Unsupported file type")

	def raster(self, dataset):
		self.files = dataset.GetFileList()
		self.count = dataset.RasterCount
		self.height = dataset.RasterXSize
		self.width = dataset.RasterYSize
		self.data = dataset.ReadAsArray()
		self.driver = dataset.GetDriver().LongName
		proj = osr.SpatialReference(wkt=dataset.GetProjection())
		self.epgs = proj.GetAttrValue('AUTHORITY', 1)
		self.datum = proj.GetAttrValue('DATUM', 0)
		return self

	def __str__(self):
		return str(self.__dict__)
