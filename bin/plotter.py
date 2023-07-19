#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:32:03 2023

@author: alejandracamelocruz
"""

import argparse
from analysis import Analyser
from matplotlib import pyplot as plt


class Plotter:
    
    def __init__(self, data):
        self.data = data
        
    def plot_bar(self):
        pass
    
    def plot_line(self):
        pass

def main(args):
    
    analyser = Analyser()
    
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
                inflation_data = analyser.inflation_calculator(data)
                plotter = Plotter(inflation_data)
    
    # bar = (args.graphic == 'bar')
    # line = (args.graphic == 'line')
    
    # if bar:
    #     plotter.plot_bar()
    
    # if line:
    #     plotter.plot_line()
    
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument('-p', '--product', type=str, help='Product name')
    parser.add_argument('-c', '--countries', nargs='+', help='List of countries')
    parser.add_argument('-t', '--time', type=str, nargs=2, help='Start, Stop')
    parser.add_argument('-g', '--graphic', type=str, help='type of plot')
    
    args = parser.parse_args()
    
    main(args)

    
    