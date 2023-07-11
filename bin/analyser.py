#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inflation Analyzer class.

Created on Sat Jul 08 21:15:48 2023

@author: Bruk Asrat
"""
import argparse
import logging
import pandas as pd
import awoc
from preprocessor import Preprocessor

PRODUCTS = ['Alcoholic_Beverages','Clothing','Communication','Education','Food',
            'Health','Housing_Energy', 'Misc_Goods_Services','Recreation_Culture',
            'Restaurants_Hotels','Transport']

class Analyser:
    def __init__(self) -> None:
        pass
    
    def query_formatter(self,product,product_nation:list,start,end):
        """
        

        Parameters
        ----------
        product : TYPE
            DESCRIPTION.
        product_nation : list
            DESCRIPTION.
        start : TYPE
            DESCRIPTION.
        end : TYPE
            DESCRIPTION.

        Returns
        -------
        data : TYPE
            DESCRIPTION.

        """
        pre_proc = Preprocessor()
        self.product = pre_proc.by_product(product)
        self.product_nation = pre_proc.by_country(product,product_nation)
        #data = pre_proc.by_year(product,product_nation,'Dec_2021', 'Jan_2022')
        data = pre_proc.by_year(product,product_nation,start, end)
        return data
            
    
    def inflation_calculator(self,result):
        """
        This function calculates inflation rate of a given dataframe.

        Parameters
        ----------
        result : dataframe
            well formulated dataframe result of other functions ready to be analysed. 

        Returns
        -------
        inflation_result : dataframe
            returns calculated inflation rate

        """
        prev_cpi = 100
        time_span = result.columns.values.tolist()     
        for time in time_span:
            infl = time + '_INF'
            #Inflation = ((New CPI - Old Year CPI)/ Old Year CPI) X 100
            val = round(((result[time]-prev_cpi) / prev_cpi)* 100 , 1)
            prev_cpi = result[str(time)]
            result[infl] = val
        
        inflation_result = result.loc[:, ~result.columns.isin(time_span)]
        #print(inflation_result)
        return inflation_result
    
    def all_products_inflation(self,nation,start,stop):
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
        #pre_proc = Preprocessor()
        #products1 = pre_proc.list_products()
        #print(products1)
        #products = products1.values.tolist()
        resultframe = pd.DataFrame()
        for product in PRODUCTS:            
            result = self.query_formatter(product,nation,start,stop)
            #result2 = pd.append(result,ignore_index=True,sort=False)
            resultframe = resultframe._append(result,ignore_index=True,sort=False)
        return resultframe


def main(param):
    """
    

    Parameters
    ----------
    param : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    inf_analyser= Analyser()
    #print(inf_analyser)
    no_task = (not param.do or param.do is None)
    no_countries = (not param.nation or param.nation is None) 
    no_continent = (not param.continent or param.continent is None)
    no_product = (not param.product or param.product is None)
    no_time = (not param.year or param.year is None)
    
    
    if no_task:
        logging.error("Missing argument : -d, --do :analysis task is required.")
    else:
        if no_product:
            logging.error("Missing argument : -p, --product :product name is required.")
        else:
            if no_countries and no_continent:
                logging.error("Missing argument : -n, --nation or -c --continent:\
                              Country name or Continent name is required.")
            else:
                if no_time:
                    logging.error("Missing argument : -y, --year :Year is required.")
                else: 
                    start = 'Dec_'+ str((int(param.year)-1))
                    stop = 'Jan_'+ str((int(param.year)+1))
                    if param.do == 'EPIF':
                        result = inf_analyser.all_products_inflation(param.nation,start,stop)
                    elif param.do == 'AIF':
                        """if no_continent:
                            result = inf_analyser.query_formatter(param.product,param.nation,start,stop)
                        elif no_countries:
                            my_world = awoc.AWOC()
                            countries_list = my_world.get_countries_list_of(param.continent)
                            print (countries_list)
                            result = inf_analyser.query_formatter(param.product,countries_list,start,stop)
                        """
                        result = inf_analyser.query_formatter(param.product,param.nation,start,stop)
    
    print(inf_analyser.inflation_calculator(result))

    
    #countries_of_europe = my_world.get_countries_list_of('Europe')
    #countries_of_africa = my_world.get_countries_list_of('Africa')
    #print (countries_of_europe)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    """ parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input the dataset file')"""
    parser.add_argument('-d','--do',
                        type=str, default='AIF',
                        help="Select the desired function: \
                             AIF for Annual_inflation \
                             EPIF for all_prodocts_inflation \
                             HIY for Highest Inflation Year")
    parser.add_argument('-n','--nation',
                         nargs='+', default= None,
                        help="Input the name of the countries'")
    parser.add_argument('-c','--continent',
                        type=str, default=None,
                        help="Input specific the name of the continent")
    parser.add_argument('-y','--year',
                        type=str, default=2019,
                        help="Input the desired year:")
    parser.add_argument('-p','--product',
                        type=str, default='Education',
                        help="Input specific product name eg: Education")
    args = parser.parse_args()
    main(args)
