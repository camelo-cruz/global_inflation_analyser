# Requirements

Our project is divided into three main functionalities, namely:

1. Preprocessing
2. Analysis
3. Plotting

Each of these functionalities are addressed following Object Oriented Programming, splitted in to three classes: 1) Preprocessor, 2) Analysis, 3) Plotter. We have 

# Functional Requirements

## Preprocessor

### User stories

- As a user, I would like to have a better **summarized version of the data with information of chosen countries, years and product**, so that the available scattered and incomplete datasets are ready for analysis.
- As a user, I would like to know **which countries are available in which specific regions**, so that I can formulate my inputs.
- As a user, I would like the program to tell me **which countries do not have available data for specific products or years**, so that I can make a decision based on the completeness of the data..
- As a user, I would like to know **which of the data were incomplete/deleted after the cleaning and filtering**, so that I can make a decision on the result to fit my summary,

| Must                                                |                       Should                        |                           Could                            | Would |
| :-------------------------------------------------- | :-------------------------------------------------: | :--------------------------------------------------------: | :---: |
| **Cleaning:** dealing with missing data             | inform which countries, years, products are missing | Report a summary of actions taken after cleaning filtering |       |
| **Filtering:** filtering countries, years, products |                                                     |                                                            |       |

## Analyzer

### User stories

- As a researcher, I want to know the inflation rate of a product in multiple countries so that I can analyze which country has recorded the highest or the lowest inflation rate. 
- As a researcher, I want to know products’ inflation rate of a country, so that I can see which product has inflated or deflated in a specific period of time. 
- As a researcher, I want to know countries inflation rate of a specific product , so that I can see how much product's inflation has changed for countries in months or years.
- As a researcher, I want to know specific product’s inflations rate of countries in a continent so that I can see in which that continent country has the highest or the lowest inflation rate. 

#### Priority

| Must                                                         |                  Should                   |                            Could                             |           Would            |
| :----------------------------------------------------------- | :---------------------------------------: | :----------------------------------------------------------: | :------------------------: |
| Calculate products’ inflation rate of a country in a period of time. | Provide action selection option for users | Calculate countries' highest and lowest inflation recorded month. | Forecasting Inflation Rate |
| Calculate overall inflation rate of a country in a period of time. |                                           |                                                              |                            |
| Calculate inflation rate of countries in a continent.        |                                           |                                                              |                            |
| Calculate monthly inflation rate                             |                                           |                                                              |                            |
| Calculate product's inflation rate of countries in a period of time.. |                                           |                                                              |                            |



## Plotter

### User stories

- As a researcher, I want to plot a graph of product inflation rate so that I can see which product has recorded the highest or the lowest inflation rate through time. 
- As a researcher, I want to plot a graph for all products inflation rate of a country, so that I can see which product has inflated or deflated in a specific period of time for the specific country. 

#### Priority

| Must                                                 |                            Should                            | Could |                            Would                             |
| :--------------------------------------------------- | :----------------------------------------------------------: | :---: | :----------------------------------------------------------: |
| Plot a graph that shows product inflation rate       | Plot a variety of appropriate graph that clearly shows analysis result |       | Plot a map that shows all countries' of  inflation rate in the continent |
| Plot a graph that shows all products' inflation rate |                                                              |       |                                                              |



# Non-Functional requirements

The following non-functional requirements are intended to specify qualities that are not directly related to program's functionality. 

- The output of the application (analysis result) will be easy to read and understand.
- The application will guide the user with clear error messages and recommended input possibilities.
- The application result can easily be exported or saved to a standard file type.