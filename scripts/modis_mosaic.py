import os
import sys
from glob import glob

from pymodis import convertmodis
from pymodis.convertmodis_gdal import createMosaicGDAL
from pymodis import optparse_required
from optparse import OptionGroup
try:
    import osgeo.gdal as gdal
except ImportError:
    try:
        import gdal
    except ImportError:
        raise Exception('Python GDAL library not found, please install python-gdal')


def mosaic(data_dir, output_filename, glob_str='*.hdf', selected_layers=None, output_format='GTiff'):
    input_filenames = glob.glob(os.path.join(data_dir, glob_str))

    # sort the filenames into a dict mapping dates => lists of filenames for that date
    tiles = {}
    for hdf_filename in input_filenames:
        date = extract_filename_date(hdf_filename)
        if date not in tiles.keys():
            tiles[date] = []
        tiles[date].append(hdf_filename)

    # create the mosaics for each date
    for date, filenames in tiles.items():
        modisOgg = createMosaicGDAL(filenames, selected_layers, output_format)
        output = f"{date}_{output_filename}"
        modisOgg.run(output)


def extract_filename_date(f):
    return f.stem.split('.')[-1]  # abc/def/MOD13Q1.A2019225.h29v11.006.2019248132853.hdf