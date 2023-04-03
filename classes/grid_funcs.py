import numpy as np

class map_grid():
    '''
    Map_grid creates a grid object of coordinates to simply selection of geographical areas.

    '''
    def __init__(self,grid_size,source):
        self.source = source
        self.grid_size  = grid_size

        if source.lower() == 'airs':
 

            self.nh_lat = np.genfromtxt(f'coordinates_{grid_size}km_grid/Airs_nh_lat_{grid_size}_grid.csv', delimiter=',')
            self.nh_lon = np.genfromtxt(f'coordinates_{grid_size}km_grid/Airs_nh_lon_{grid_size}_grid.csv', delimiter=',')
            self.sh_lat = np.genfromtxt(f'coordinates_{grid_size}km_grid/Airs_sh_lat_{grid_size}_grid.csv', delimiter=',')
            self.sh_lon = np.genfromtxt(f'coordinates_{grid_size}km_grid/Airs_sh_lon_{grid_size}_grid.csv', delimiter=',')

            self.nh_stacked = np.stack((self.nh_lat, self.nh_lon), axis=2)
            self.sh_stacked = np.stack((self.sh_lat, self.sh_lon), axis=2)

        elif source.lower() == 'era5':
            self.lat = np.genfromtxt(f'coordinates_era/COORDINATES_ERA5_LAT.csv', delimiter=',')
            self.lon = np.genfromtxt(f'coordinates_era/COORDINATES_ERA5_LON.csv', delimiter=',')
            self.grid_ = np.meshgrid(self.lon,self.lat)
            self.stacked = np.transpose(self.grid_,(1,2,0))

        elif source.lower() == 'era5_online':
            self.lat = np.genfromtxt(f'coordinates_era5_online/COORDINATES_ERA5_ONLINE_LAT.csv', delimiter=',')
            self.lon = np.genfromtxt(f'coordinates_era5_online/COORDINATES_ERA5_ONLINE_LON.csv', delimiter=',')
            self.grid_ = np.meshgrid(self.lon,self.lat)
            self.stacked = np.transpose(self.grid_,(1,2,0))
        else:
            raise Exception('Please specify source')



    def select_area_indexer(self,min_lat,max_lat,min_lon,max_lon):
        '''
        Selects coordinates for a range of longitudes and latitudes.
        Output is an array of indeces of shape (n,n) used to filter the output from  mamatlab_reader.select()
        '''
        if self.source.lower() == 'airs':
            if max_lat < 0:
                a = self.sh_stacked
            else:
                a = self.nh_stacked
            
            a = np.where((a[...,0] > min_lat) & (a[...,0] < max_lat) & (a[...,1] > min_lon) & (a[...,1] < max_lon) )

        else :
            a = self.stacked
            a = np.where((a[...,1] > min_lat) & (a[...,1] < max_lat) )# & (a[...,0] > min_lon) & (a[...,0] < max_lon) )
        return np.transpose(a)

class dataset():
    def __init__(self,data):
        ''' Data class : holds an array of data of shape nxn'''
        self.data = data
        self.mean = np.nanmean(data)
        self.max = np.nanmax(data)
        self.min = np.nanmin(data)
    

class data_wizard():
    '''Colletion of functions to simplify filtering and agreggating geospatial matlab data'''
    def data_filtering(self,select_area_indexer,data):
        temp_data_select = data[select_area_indexer[:,0], select_area_indexer[:,1]]
        mask = np.full(np.shape(data), np.nan)
        mask[select_area_indexer[:,0], select_area_indexer[:,1]] = temp_data_select
        return mask