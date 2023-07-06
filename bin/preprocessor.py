#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class ...

Copyright (C) 2023 Kshitij Kar Alejandra Camelo Cruz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

contact email: camelocruz@uni-potsdam.de

"""

#import sys
import os
import argparse
import pandas as pd
import numpy as np


class Preprocessor:
    '''Preprocessor as first stage for data cleaning and filtering'''
    
    def __init__(self):
        self.data_folder = self.get_relative_data_directory()
        self.files = [os.path.join(self.data_folder, file) 
                      for file in os.listdir(self.data_folder)]


    def index_cleaning(self,index_list:list) -> list:
        '''
        This function takes the index list of any DataFrame, cleans it 
        and returns it to the calling function to replace the previous 
        data index with the cleaned data index. 

        Parameters
        ----------
        index_list : list
            DESCRIPTION.

        Returns
        -------
        list
            DESCRIPTION.

        '''
        outlist = []
        for country in index_list:
            if country[0:5] == "China":
                outlist.append(country.split(": ")[-1].replace(" ","_"))
            else:
                outlist.append(country.split(",")[0].replace(" ","_"))
        return outlist


    def data_cleaning(self,file_location:str) -> pd.DataFrame:
        '''
        This function reads any particular data set provided and 
        cleans the column headers and indexes and returns the DataFrame.

        Parameters
        ----------
        file_location : str
            DESCRIPTION.

        Returns
        -------
        data : TYPE
            DESCRIPTION.

        '''
        data = pd.read_excel(file_location)
        data.index = data["Unnamed: 0"]
        data = data.drop(columns=["Unnamed: 0"])
        data.columns = [c.strip().replace(" ","_") for c in data.columns.values.tolist()]
        data.index = self.index_cleaning(data.index.tolist())
        
        return data
    
    
    def list_countries(self,intext=""):
        '''
        List all the countries available in a data file
        
        Parameters
        ----------
        intext : TYPE, optional
            DESCRIPTION. The default is "".

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        data = self.data_cleaning(self.files[0])
        list_countries = data.index.to_list()
        intext = input("Enter a part of the countries you want. "
                       "Don't write anything or write \"all\" if you want to see "
                       "a list with all available countries: ")
        intext = intext.capitalize()
        all_countries = (intext == "" or intext == 'All')
        if all_countries:
            return list_countries
        else:
            if intext.endswith("*"):
                list_countries_specific = []
                for country in list_countries:
                    if country.startswith(intext[:-1]):
                        list_countries_specific.append(country)
                
                return list_countries_specific
            else:
                list_countries_specific = []
                for country in list_countries:
                    if intext in country:
                        list_countries_specific.append(country)
                return list_countries_specific
    
    
    def by_country(self,product:str,country_list:list) -> pd.DataFrame:
        '''
        Returns data with only selected countries.

        Parameters
        ----------
        product : str
            DESCRIPTION.
        country_list : list
            DESCRIPTION.

        Returns
        -------
        data_countries : TYPE
            DESCRIPTION.

        '''

        print(f"You have chosen the following countries : {country_list}")
        self.country_list = country_list
        self.product = product
        data = self.by_product(product)
        data_countries = data.loc[country_list]
    
        return data_countries
    
    
    def list_years(self):
        '''
        

        Returns
        -------
        available_time : TYPE
            DESCRIPTION.

        '''
        
        data = self.by_country(self.product,self.country_list)
        available_time = data.columns.values

        return available_time
    
    
    def by_year(self,product:str,country_list:list,start,stop):
        '''
        

        Parameters
        ----------
        product : str
            DESCRIPTION.
        country_list : list
            DESCRIPTION.
        start : TYPE
            DESCRIPTION.
        stop : TYPE
            DESCRIPTION.

        Returns
        -------
        data_years : TYPE
            DESCRIPTION.

        '''
        data = self.by_country(product,country_list)
        wanted_columns = data.columns.values[np.where(data.columns.
                                                      values == start)[0][0]:
                                             np.where(data.columns.
                                                      values == stop)[0][0]]
        data_years = data[wanted_columns]
        print(f"You have chosen the time data from {wanted_columns[0]} to {wanted_columns[-1]}")
        # print(np.where(data.columns.values == start)[0][0])
        # print(np.where(data.columns.values == stop)[0][0])

        return data_years
    
    def list_products(self) -> list:
        '''
        

        Returns
        -------
        list
            DESCRIPTION.

        '''
        list_products = []
        for file in self.files:
            list_products.append(file.split("_CPI_")[-1].split(".")[0])
        return list_products
        
    def by_product(self,product) -> pd.DataFrame:
        '''
        This function asks the user to input the product they wish to analyse 
        and returns the data set with only that product.

        Parameters
        ----------
        product : TYPE
            DESCRIPTION.

        Returns
        -------
        data : TYPE
            DESCRIPTION.

        '''

        self.product = product
        print(f"You have chosen {self.product}")
        self.data_file = os.path.abspath(
            os.path.join(self.data_folder, f"Consumer_Price_Index_CPI_{self.product}.xlsx"))
        data = self.data_cleaning(self.data_file)
    
        return data

    def display_head(self, data: pd.DataFrame) -> None:
        '''
        

        Parameters
        ----------
        data : pd.DataFrame
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        '''
        print(data.head())

    
    @staticmethod
    def get_relative_data_directory():
        current_dir = os.path.dirname(__file__)
        data_dir = os.path.abspath(os.path.join(current_dir, os.pardir, 'data'))
        
        return data_dir
        
    
def main(args):
    prpr = Preprocessor()
    no_product = (not args.product or args.product is None)
    no_countries = (not args.countries or args.countries is None) 
    no_time = not args.time
    
    if no_product:
        print("Missing argument : -p, --products is required.")
        print(prpr.list_products())
    else:
        if no_countries:
            prpr.by_product(args.product)
            print("Missing argument : -c, --countries is required.")
            print(prpr.list_countries())
        else:
            if no_time:
                prpr.by_country(args.product,args.countries)
                print("Missing argument : -t, --time is required.")
                print(prpr.list_years())
            else:
                start,stop = args.time
                data = prpr.by_year(args.product,args.countries,start,stop)
                prpr.display_head(data)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command line inputs')
    parser.add_argument('-p', '--product', type=str, help='Product name')
    parser.add_argument('-c', '--countries', nargs='+', help='List of countries')
    parser.add_argument('-t', '--time', type=str, nargs=2, help='Start, Stop')

    args = parser.parse_args()

    main(args)
