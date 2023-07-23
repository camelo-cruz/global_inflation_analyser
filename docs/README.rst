About The Project
-----------------

This project is named as Global Inflation Analyzer (GIA). It is a python
library, and written to give a comprehensive analysis of inflation rate.
The library can be used to perform analysis based on a given dataset
with the classification standard of classification of individual
consumption by purpose (COICOP 2-5-digit hierarchy).

With the dataset contained data about consumer price index for group of
products and services, the library will analyze the following main
questions or features:

::

     1. How much has inflation changed during the given range of years? 
     2. In what amount, inflation recorded after or before specific year (e.g. COVID-19 or UKRAIN WAR)? 
     3. Which group of products or services is highly affected after specific year? 
     4. In which year was high inflation recorded?
     5. What is the inflation rate of a specific products or services globally?
     6. What is the inflation rate of a specific products or services group (specific Country)?

Installation
------------

Repository
~~~~~~~~~~

Install Global_Inflation_Analyser and go to root folder:

::

   git clone https://gitup.uni-potsdam.de/kar/global_inflation_analyser
   cd global_inflation_analyser

After you downloaded our repository, make sure you have Python installed
and all the dependencies needed for the project.

   Make sure you are in the folder containing the software. Check it
   running pwd in terminal. it should end in global_inflation_analyser

If you are using conda, you can download all the dependencies, while
being in the root folder, with the following command:

::

   conda install -e .

Otherwhise, for installing it with pip, run:

::

   pip install -e .

Usage Guide
-----------

After you have moved yourself in the repository where you saved the
project. You will notice that you have three classes provided to you:
preprocessor, analysis and the plotter class. With the Preprocessor
class the provided data will be cleaned and filtered to your User needs.
The Analysis class calculates the Inflation rate of the given data set
and merge all products inflation rate of a given country for specific
period of time. The plotter class provides plots with the previous
analysed data. Generally if you want to use the Project we would
recommend to use the provided Jupyter Notebook and to run all the cells
in their given order. While running the cells you will notice you need
to choose your data set and the years you want. After you executed the
plotting part, your results will be saved in the results directory where
you can look up all the plots.

Although all the classes allow independent use from the terminal, the
plotter class allows to use all of them and product a visual output in
the results folder

use from terminal
=================

Plotter with analysis and preprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The plotter function takes both the analyser and the preprocessor and
serves as the main entry point for the command-line interface of the
Global Inflation Analyser. It analyzes inflation data for different
countries and products and generates bar and line charts based on the
analysis results. This function takes command-line arguments to specify
the analysis type, countries, time period, and plot preferences.

Use
~~~

while in root:

::

   python global_inflation_analyser/plotter.py [-h] [-p PRODUCT] -c COUNTRIES COUNTRIES -t START STOP [-g GRAPHIC] -a ANALYSIS [--plotparams PLOTPARAMS]

Arguments
~~~~~~~~~

-  ``-h``, ``--help``: Show help message and exit.
-  ``-p PRODUCT``: Product name (optional).
-  ``-c COUNTRIES``: List of countries for analysis (required).
-  ``-t START STOP``: Start and stop months for analysis (required,
   format: “MMM_YYYY”).
-  ``-g GRAPHIC``: Type of plot: “line” for line plot, “bar” for bar
   plot, “all” for both (default).
-  ``-a ANALYSIS``: Type of analysis: “total” for total analysis,
   “product” for product-specific analysis (required).
-  ``--plotparams PLOTPARAMS``: Matplotlib parameters options: “bigplot”
   or “smallplot” (optional).

Description
~~~~~~~~~~~

This function performs inflation analysis for either total or
product-specific scenarios based on the user’s input. It generates bar
and/or line charts showing inflation rates across different countries
over a specified time period.

Analysis Types
~~~~~~~~~~~~~~

-  **Total Analysis**: Provides inflation rates for a single country
   across all products.
-  **Product-Specific Analysis**: Provides inflation rates for a
   specific product across multiple countries.

Plot Types
~~~~~~~~~~

-  **Line Plot**: Displays inflation rates as a line plot for each
   country over time.
-  **Bar Plot**: Shows inflation rates as a bar chart for each country
   over time.
-  **All Plots**: Generates both line and bar charts for the selected
   analysis.

Example Usage
~~~~~~~~~~~~~

To run the Global Inflation Analyser for total analysis, plotting both
bar and line charts:

::

   python global_inflation_analyser/plotter.py -c Country1 Country2 -t Jan_2021 Dec_2022 -a total

To run the Global Inflation Analyser for product-specific analysis,
plotting only line charts:

::

   python global_inflation_analyser/plotter.py -p ProductName -c Country1 Country2 -t Jan_2021 Dec_2022 -g line -a product

To apply custom plot settings for big plots:

::

   python global_inflation_analyser/plotter.py -c Country1 Country2 -t Jan_2021 Dec_2022 -a total --plotparams bigplot

Features
--------

-  Comparison Table
-  Line Plot Diagramm
-  Bar Plot Diagramm
-  Dataset can be adjusted

   -  Years adjustable
   -  Product adjustable
   -  Countries adjustable

Documentation
-------------

Please see `Global Inflation Analyzer documentation <#>`__ for more
information.

Code of conduct
---------------

Our code of conduct can be found in the code of
`CONDUCT.md <./CONDUCT.md>`__ file in the global_inflation_analyser
repository.

Contribution Guidelines
-----------------------

Contributions are always welcome, if you want to find out how to
contribute to the Project read the
`CONTRIBUTING.md <./CONTRIBUTING.md>`__.

License
=======

   GPL-3.0-or-later

::

   Copyright (C) 2023 Alejandra Camelo Cruz, Kshitij Kar, Bruk Asrat Tsega, Leon Oparin

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

Full license text can be recovered `here <LICENSE.txt>`__

Citation
========

::

   cff-version: 1.2.0
   title: Global_Inflation_Analyser
   message: >-
     If you use this software, please cite it using the
     metadata from this file.
   type: software
   authors:
     - given-names: Kshitij
       family-names: Kar
       email: kar@uni-potsdam.de
       affiliation: Universität Potsdam
     - given-names: Camelo Cruz
       family-names: Alejandra
       email: camelocruz@uni-potsdam.de
       affiliation: Universität Potsdam
     - given-names: Leon
       family-names: Oparin
       email: leon.oparin@uni-potsdam.de
       affiliation: Universität Potsdam
     - given-names: Bruk Asrat
       family-names: Tsega
       email: tsega@uni-potsdam.de
       affiliation: Universität Potsdam
   abstract: >-
     This project is named as Global Inflation Analyzer (GIA).
     It is a python library, and written to give a
     comprehensive analysis of inflation rate. The library can
     be used to perform analysis based on a given dataset with
     the classification standard of classification of
     individual consumption by purpose (COICOP 2-5-digit
     hierarchy).
   keywords:
     - Consumer Price Index
     - Inflation Rate
   license: GPL-3.0-or-later

The information for citation can be used from the `.cff
file <CITATION.cff>`__ in the root folder

Contact Information
-------------------

If you have any question regarding this library, please feel free to get
in touch with us:

-  leon.oparin@uni-potsdam.de
-  tsega@uni-potsdam.de
-  kar@uni-potsdam.de
-  `camelocruz@uni-potsdam.de <mailto:Camelocruz@uni-potsdam.de>`__

Acknowledgement
---------------

We would like to thank the whole Group and the University of Potsdam for
the Opportunity to work on such a project and give us the needed
knowledge in order to make such a project.
