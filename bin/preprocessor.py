#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:42:10 2023

@author: alejandracamelocruz
"""

import os
import pandas as pd


class Preprocessor:
    
    def __init__(self, data_folder='data/'):
        self.data_folder = data_folder
        self.files = self.file_list(data_folder)


    def index_cleaning(self,index_list:list) -> list:
        """
        This function takes the index list of any DataFrame, cleans it and returns it 
        to the calling function to replace the previous data index with the cleaned data index. 
        """
        outlist = []
        for country in index_list:
            if country[0:5] == "China":
                outlist.append(country.split(": ")[-1].replace(" ","_"))
            else:
                outlist.append(country.split(",")[0].replace(" ","_"))
        return outlist

    def data_cleaning(self,file_location:str) -> pd.DataFrame:
        """
        This function reads any particular data set provided and 
        cleans the column headers and indexes and returns the DataFrame.
        """
        data = pd.read_excel(file_location)
        data.index = data["Unnamed: 0"]
        data = data.drop(columns=["Unnamed: 0"])
        data.columns = [c.strip().replace(" ","_") for c in data.columns.values.tolist()]
        data.index = self.index_cleaning(data.index.tolist())
        
        return data
    
    def list_countries(self,intext=""):
        data = self.data_cleaning(self.files[0])
        list_countries = data.index.to_list()
        intext = input("Enter a part of the countries you want: ")
        if intext == "":
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
    
    def by_country(self, country_list:list = []) -> pd.DataFrame:
        data = self.data_cleaning(self.files[0])
    
    def list_years():
        pass
    
    def by_year(year_list=[]):
        pass
    
    def list_products(self) -> list:
        list_products = []
        for file in self.files:
            list_products.append(file.split("_CPI_")[-1].split(".")[0])
        return list_products
        
    def by_product(self,product_list=[]) -> list:
        inprod = input("Enter the Indicator you want to view: ")
        data_files = []

    @staticmethod
    def file_list(directory):
        current_dir = os.path.dirname(__file__)
        data_dir = os.path.abspath(os.path.join(current_dir, os.pardir, 'data'))
        file_list = [os.path.join(data_dir, file) 
                     for file in os.listdir(data_dir)]
        
        return file_list
        
def main():
    preprocessor = Preprocessor()
    print(preprocessor.list_countries())
    
if __name__ == '__main__':
    main()