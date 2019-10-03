=======
PyMODIS
=======

This is a fork of the original `pyModis <https://github.com/lucadelu/pyModis>`_ package.

License
-------

pyModis is licensed under the terms of **GNU GPL 2**. Read COPYING for more info

Install
-------

For how to compile or install pyModis see INSTALL file.

Executables
-----------

Some executables are distributed with the library:

  * **modis_download** downloads MODIS data
  * **modis_download_from_list** downloads MODIS data from NASA servers, the names of files to download have to be contained into a text file.
  * **modis_parse** parses the XML file of MODIS data and return some variables
  * **modis_multiparse** parses the XML file of multiple MODIS data and returns the bounding box or writes the XML file with the information of all
    selected tiles
  * **modis_mosaic** creates the mosaic of multiple MODIS tiles
  * **modis_convert** converts MODIS data from HDF format and Sinusoidal projection to other formats and projections
  * **modis_quality** checks the quality of MODIS data using the QA layer
