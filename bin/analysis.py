#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import pandas as pd
import numpy as np
from preprocessor import Preprocessor

class Analyser(Preprocessor):

    def __init__(self,data_folder="data/") -> None:
        self.data_folder = self.get_relative_data_directory()
        self.files = [os.path.join(self.data_folder, file) 
                      for file in os.listdir(self.data_folder)]
        # data = self.by_year(self.product,self.country_list,self.start_time,self.stop_time)
        # print(data.head(5))

    def set_datafile(self,product:str,country_list:list,start_time:str,stop_time:str) -> pd.DataFrame:
        self.product = product
        self.country_list = country_list
        self.start_time = start_time
        self.stop_time = stop_time
    
        self.data = self.by_year(product,country_list,start_time,stop_time)
        print("From set_datafile\n")
        print(self.data.head(5))
        return self.data
    
# def main(args):
    # print(args)
    # analyser = Analyser()
    # parser = argparse.ArgumentParser(description='Command line inputs')
    # parser.add_argument('--product', type=str, help='Product name')
    # parser.add_argument('--countries', nargs='+', help='List of countries')
    # parser.add_argument('--time', type=str, nargs=2, help='Start, Stop')

    # args = parser.parse_args()

    # if not args.product or args.product is None:
    #     print("Missing arguement : --product is required")
    #     print(analyser.list_products())
    # else:
    #     if not args.countries or args.countries is None:
    #         analyser.by_product(args.product)
    #         print("Missing arguement : --countries is required")
    #         print(analyser.list_countries())
    #     else:
            
    #         if not args.time:
    #             analyser.by_country(args.product,args.countries)
    #             print("Missing arguement : --time is required")
    #             print(analyser.list_years())
    #         else:
    #             start,stop = args.time
    #             data = analyser.by_year(args.product,args.countries,start,stop)
    #             analyser.display_head(data)


if __name__ == "__main__":
    analyser = Analyser()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-p', '--product', type=str, help='Product name')
    parser.add_argument('-c', '--countries', nargs='+', help='List of countries')
    parser.add_argument('-t', '--time', type=str, nargs=2, help='Start, Stop')

    args = parser.parse_args()

    if not args.product or args.product is None:
        print("Missing arguement : --product is required")
        print(analyser.list_products())
    else:
        if not args.countries or args.countries is None:
            analyser.by_product(args.product)
            print("Missing arguement : --countries is required")
            print(analyser.list_countries())
        else:
            
            if not args.time:
                analyser.by_country(args.product,args.countries)
                print("Missing arguement : --time is required")
                print(analyser.list_years())
            else:
                start,stop = args.time
                data = analyser.set_datafile(args.product,args.countries,start,stop)
                