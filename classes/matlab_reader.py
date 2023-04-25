from scipy import io
import numpy as np
import pandas as pd

class matlab_reader():
    '''
    # Example 

    matlab = matlab_reader('AIRS_40KM_2022/20220125_AIRS_3DST-1_40km_grid.mat')

    temp_data = matlab.select(
        hemisphere= 'nh',
        data_field='tp',
        daytime='night',
        altitude=24)      
    '''
    def __init__(self,file):
        self.file_path = file
        self.data = io.loadmat(file)
        self.data_info = io.whosmat(file)
        self.data_airs = self.data['Airs']

    def select(self,
        hemisphere = 'NH',
        daytime = 'Night',
        data_field = 'mfx',
        altitude = 1):
        ''' 
        Returns a selection on the dataset filtered based on the input values
        hemisphere : selects what hemisphere to select data, North or South
        daytime : selects what time of day to collect values, Night or Day
        data_field : selects data field from tp (temperature) , bg , a , ha , k, l , m , mfx and mfy.
        '''
        data_ = self.data_airs[hemisphere.upper()][0][0][0][0][daytime][0][0][data_field][:, :, altitude]

        return data_
