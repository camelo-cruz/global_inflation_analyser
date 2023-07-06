#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import pandas as pd
import numpy as np
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

class Analyser:
    def __init__(self) -> None:
        pass
    
if __name__ == '__main__':
    
    product, product_country, product_country_year = test_preprocessor()