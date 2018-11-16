class GeoInfo():
	def __init__(self, driver, crs, data, count, height, width):
		self.driver = driver
		self.crs = 'epsg:' + crs
		self.data = data
		self.count = count
		self.height = height
		self.width = width