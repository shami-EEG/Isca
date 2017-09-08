import numpy as np
from netCDF4 import Dataset

def cell_area_all(t_res,base_dir, radius=6376.0e3):
	"""read in grid from approriate file, and return 2D array of grid cell areas in metres**2."""
	resolution_file = Dataset(base_dir+'src/extra/python/scripts/gfdl_grid_files/t'+str(t_res)+'.nc', 'r', format='NETCDF3_CLASSIC')

	lons = resolution_file.variables['lon'][:]
	lats = resolution_file.variables['lat'][:]

	lonb = resolution_file.variables['lonb'][:]
	latb = resolution_file.variables['latb'][:]

	nlon=lons.shape[0]
	nlat=lats.shape[0]

	area_array = np.zeros((nlat,nlon))
	xsize_array = np.zeros((nlat,nlon))
	ysize_array = np.zeros((nlat,nlon))

	for i in np.arange(len(lons)):
	    for j in np.arange(len(lats)):
	    	xsize_array[j,i] = radius*np.absolute(np.radians(lonb[i+1]-lonb[i])*np.cos(np.radians(lats[j])))
	    	ysize_array[j,i] = radius*np.absolute(np.radians(latb[j+1]-latb[j]))
	    	area_array[j,i] = xsize_array[j,i]*ysize_array[j,i]


	return area_array,xsize_array,ysize_array

def cell_area(t_res,base_dir):
	"""wrapper for cell_area_all, such that cell_area only returns area array, and not xsize_array and y_size_array too."""
	area_array,xsize_array,ysize_array = cell_area_all(t_res,base_dir)
	return area_array

if __name__ == "__main__":

	# specify resolution
	t_res = 42
	# specify base dir
	base_dir= '/scratch/sit204/FMS2013/GFDLmoistModel/'
	#return area_array
	area_array=cell_area(t_res,base_dir)

