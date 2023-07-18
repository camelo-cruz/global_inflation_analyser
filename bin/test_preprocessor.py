#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:26:49 2023

@author: alejandracamelocruz
"""

import pandas as pd
from preprocessor import Preprocessor
import os

prpr = Preprocessor()

cwd = os.getcwd()
data_dir = os.path.abspath(os.path.join(cwd, os.pardir, 'data'))


def get_correct_country_list():
    num_countries_list = []
    for file in os.listdir(data_dir):
         filename = os.fsdecode(file)
         if filename.endswith('.xlsx'):
             filename = os.path.join('..', 'data', filename)
             file = pd.read_excel(filename)
             num_countries = len(file.iloc[:, 0])
             if num_countries_list != []:
                 if num_countries >= num_countries_list[-1]:
                      file_to_test = file
             num_countries_list.append(num_countries)

    
    
    correct_country_list = prpr.index_cleaning(list(file_to_test.iloc[:, 0]))

    
    return correct_country_list


def test_product():
    
    correct_product_list = set(['Alcoholic_Beverages', 'Clothing', 'Communication',
                               'Education', 'Food', 'Health', 'Housing_Energy', 'Misc_Goods_Services',
                               'Recreation_Culture', 'Restaurants_Hotels', 'Transport'])
    
    test_product_list = set(prpr.list_products())
    
    assert correct_product_list == test_product_list
    
def test_country():
    correct_country_list = get_correct_country_list()
    test_country_list = prpr.list_countries('all')
    
    assert correct_country_list == test_country_list