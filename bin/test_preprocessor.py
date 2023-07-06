#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:26:49 2023

@author: alejandracamelocruz
"""

from preprocessor import Preprocessor

def test_preprocessor():
    prpr = Preprocessor()
    product = prpr.by_product('health')
    print(product.head())
    product_country = prpr.by_country(product='transport', 
                                      country_list = ['italy', 'spain', 'germany'])
    print(product_country.head())
    product_country_year = prpr.by_year(product='education', 
                                   country_list = ['colombia', 'germany'], 
                                   start = 'jan_2002', stop = 'dec_2003')
    print(product_country_year.head())
    
    return product, product_country, product_country_year
