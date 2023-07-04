#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:42:10 2023

@author: alejandracamelocruz
"""

import os
import pandas as pd

def file_list(rootdir='data/'):
    for subdir, dirs, files in os.walk(rootdir):
        file_list =  [os.path.join(subdir, file) for file in files]
    
    return file_list

class Preprocessor():
    
    def __init__(self, data_folder='data/'):
        self.data_folder = data_folder
        self.files = file_list(self.data_folder)
    
    def list_countries(self):
        data = pd.read_excel(self.files[0])
        list_countries = [country for country in data.iloc[:, 0]]
        
        return list_countries
    
    def by_country(country_list=[]):
        pass
    
    def list_years():
        pass
    
    def by_year(year_list=[]):
        pass
    
    def list_products():
        pass
    
    def by_product(product_list=[]):
        pass

preprocessor = Preprocessor()
print(preprocessor.list_countries())