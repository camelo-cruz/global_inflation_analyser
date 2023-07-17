# Software Architecture and Design

## Overview

This project is named as Global Inflation Analyzer (GIA). It is a python library, and written to give a comprehensive analysis of inflation rate. The library can be used to perform analysis based on a given dataset with the classification standard of classification of individual consumption by purpose (COICOP 2-5-digit hierarchy). 

## Architecture

<div>
<img src="class_uml.png">
</div>

$\hspace{10cm}$

The preprocessor class contains internal functions ```_index_cleaning(), _data_cleaning() and _get_relative_data_directory()``` that are used by the external functions ```list_products(), list_countries() and list_year()``` which inform the user about the available options for the software. The function ```by_product()``` provides a Pandas DataFrame as an output containing all countries and all time periods available. Similarly, ```by_country()``` return a Pandas DataFrame with chosen countries for a specific product and ```by_year()``` returns a Pandas DataFrame for chosen time period, countries and product.

These functions can be accessed from the Analyser class. ```set_datafile()``` is used to select the data with which you want to proceed with the analysis. ```inflation_calculator()``` calculates the inflation rate from the CPI of the chosen product and country/countries. 

## Technology Stack

- Python ```Version 3.8.10```
- Numpy ```Version 1.22.0```
- Pandas ```Version 1.3.5```
- Matplotlib ```Version 3.5.1```

## Data Flow

## User Interface


