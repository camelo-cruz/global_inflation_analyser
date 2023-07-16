#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inflation Analyzer class.

Created on Sat Jul 08 21:15:48 2023

@author: Bruk Asrat
"""

import sys
import os
import argparse
import pandas as pd
import numpy as np
from preprocessor import Preprocessor


class Analyser(Preprocessor):

    def set_datafile(self,product:str,country_list:list,start_time:str,stop_time:str) -> pd.DataFrame:
        self.product = product
        self.country_list = country_list
        self.start_time = start_time
        self.stop_time = stop_time
    
        self.data = self.by_year(product,country_list,start_time,stop_time)
        # print("From set_datafile\n")
        # print(self.data.head(5))

        return self.data

    def inflation_calculator(self,input_df:pd.DataFrame) -> pd.DataFrame:
        """
        This function calculates inflation rate of a given dataframe.

        Parameters
        ----------
        input_df : pandas DataFrame
            well formulated dataframe result of other functions ready to be analysed. 

        Returns
        -------
        inflation_result : dataframe
            returns calculated inflation rate

        """
        
        prev_cpi = 100
        time_span = input_df.columns.values.tolist()
        for time in time_span:
            infl = time + '_INF'
            #Inflation = ((New CPI - Previous Month CPI)/ Previous Month CPI) X 100
            val = round(((input_df[time]-prev_cpi) / prev_cpi)* 100 , 1)
            prev_cpi = input_df[str(time)]
            input_df[infl] = val
        
        inflation_result = input_df.loc[:, ~input_df.columns.isin(time_span)]
        #print(inflation_result)

        return inflation_result
    
    def all_products_inflation(self,nation:str,start:str,stop:str) -> pd.DataFrame:
        """
        This function merge all products inflation rate of a given country for 
        specific period of time, provided by the user.

        Parameters
        ----------
        nation : string
            The name of the country
        start : string
            The initial month or the reference month.
        stop : string
            The last month of the time.

        Returns
        -------
        resultframe : dataframe
        Returns a dataframe of all products for a given period of time and country.

        """
        product_list = self.list_products()
        l_nation = [nation]

        resultframe = pd.DataFrame()
        
        for product in product_list:             
            result = self.set_datafile(product,l_nation,start,stop)
            #result2 = pd.append(result,ignore_index=True,sort=False)
            
            resultframe = resultframe.append(result,ignore_index=True,sort=False)
        
        for i,product in enumerate(product_list):                
            resultframe = resultframe.rename(index={i: product_list[i]})
            
        print (resultframe.index.values)
        
        return resultframe

    
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
    parser = argparse.ArgumentParser(description='Command line inputs')
    parser.add_argument('--product', type=str, help='Product name')
    parser.add_argument('--countries', nargs='+', help='List of countries')
    parser.add_argument('--time', type=str, nargs=2, help='Start, Stop')

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
                