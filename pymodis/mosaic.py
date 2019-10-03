from pathlib import Path

from pymodis.convert.gdal import createMosaicGDAL
try:
    import osgeo.gdal as gdal
except ImportError:
    try:
        import gdal
    except ImportError:
        raise Exception('Python GDAL library not found, please install python-gdal')


def mosaic(data_dir, glob_str='*.hdf', selected_layers=None):
    data_dir = Path(data_dir)
    input_filenames = list(data_dir.glob(glob_str))
    print(f'Found: {input_filenames}')

    # save the first product name to check each filename against
    product = extract_filename_product(input_filenames[0])

    # sort the filenames into a dict mapping dates => lists of filenames for that date
    tiles = {}
    for hdf_filename in input_filenames:
        f_date = extract_filename_date(hdf_filename)
        f_prod = extract_filename_product(hdf_filename)
        assert f_prod == product, f'Inconsistent products! {f_prod} {product}'
        if f_date not in tiles.keys():
            tiles[f_date] = []
        tiles[f_date].append(str(hdf_filename))

    # create the mosaics for each date
    output_format = 'GTiff'
    for date, filenames in tiles.items():
        modisOgg = createMosaicGDAL(filenames, selected_layers, output_format)
        save_as = data_dir / f'{product}.{date}.tif'
        print(f'Writing "{save_as}"')
        modisOgg.run(str(save_as))


def extract_filename_product(f):
    return f.stem.split('.')[0]  # abc/def/MOD13Q1.A2019225.h29v11.006.2019248132853.hdf


def extract_filename_date(f):
    return f.stem.split('.')[1]  # abc/def/MOD13Q1.A2019225.h29v11.006.2019248132853.hdf
