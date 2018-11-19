### GEOSENSE
_Making sense of worldly libs and data_

---

##### Sample data
- Search for samples via [USGS Earth Explorer](https://earthexplorer.usgs.gov/)
- Starting point, download [SRTM](https://lta.cr.usgs.gov/SRTM1Arc) or [GMTED2010](https://lta.cr.usgs.gov/GMTED2010) GeoTiff files

##### Install
```
pip install -r requirements.txt
```

##### Run
```
python geosense.py --srcfile data/geofile.tif  --outfile output/output.tif --process hillshade
```

##### Process Types
- GDAL Dem Processing: hillshade, slope, aspect, color-relief, TRI, TPI, Roughness

##### Web Server
- Optional - Testing JavaScript libs ...
- Download and copy geotiff.bundle.min.js and plotty.min.js into web/lib
- Open index.html in browser
- Run webserver

```
python web/server.py
```