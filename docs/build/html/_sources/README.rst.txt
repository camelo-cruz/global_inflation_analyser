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

Usage Guides
------------

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

The second option that you have is to run the separate python files one
after another. It means you would run the preprocessor.py. Please be
aware you need to be in the directory where the code actually is. So if
you are for example in global_inflation_analyser:

::

   # Moving to the Directory
       cd global_inflation_analyser

   # Displaying the help
       python preprocessor.py -h

   # Example: Specify product name
       python preprocessor.py -p Education

   # Example: Specify product name and list of countries
       python preprocessor.py -p Education -c Germany France Italy

   # Example: Specify product name, list of countries, and time period
       python preprocessor.py -p Education -c Germany France Italy -t Jan_2010 Dec_2012

After that you would run the analysis.py.

::

   # Displaying the help
       python analysis.py -h
       
   # Example:     
       python analysis.py -p Education -c Germany France Italy -t Jan_2023 Dec_2023

And in the End the plotter.py.

::

   # Displaing the help 
       python plotter.py

   # Example:     
       python plotter.py -p "productname" -c "country1" "country2" -t "Jan_2021" "Dec_2022" -a "product"

You could only run the plotter, as it calls all the other objects.

After that you should be again able to look up the plots in the results
directory.

Features
--------

-  Comparison Table
-  Line Plot Diagramm
-  Bar Plot Diagramm
-  Boxplot Diagramm
-  Dataset can be adjusted

   -  Years adjustable
   -  Product adjustable

Documentation
-------------

Please see `Global Inflation Analyzer
documentation <https://pypi.org/project/global-inflation-analyser/>`__
for more information.

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

   Copyright (C) 2023 Alejandra Camelo Cruz

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

Full license text can be recovered `here <COPYING.txt>`__

Citation
========

::

   cff-version: 1.0.
   title: Important factors of migration to Germany
   message: >-
     If you use this software, please cite it using the
     metadata from this file.
   type: software
   authors:
     - given-names: Alejandra
       family-names: Camelo Cruz
       email: camelocruz@uni-potsdam.de
       affiliation: University of Potsdam, Institute for Informatics and Computational Science
   repository-code: 'https://gitup.uni-potsdam.de/camelocruz/immigration_rse'
   abstract: >
     This software aims at summarizing important factors of
     immigration  in Germany, such as: number of immigrants,
     origin countries, sex, age, and concentration and movement
     between Bundesländer.
   license: GPL-3.0-or-later
   version: 1.0.
   date-released: '2023-06-04'

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
