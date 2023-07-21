# Requirements

Our project is divided into three main functionalities

1. Preprocessing
2. Analysis
3. Plotting

Each of these functionalities are addressed following Object Oriented Programming, split in three classes: 
    1) Preprocessor, 2) Analysis, 3) Plotter. We made for every class User Stories with which we can find out what 
    potential must-, should- or would- requirements need to be met.

# Functional Requirements

## Preprocessor

### User stories

- As available datasets are scattered and inc omplete, I would like to have a better **summarized version of the data with information of chosen countries, years and product**. 
 
- I would like to know **which countries are available in which specific regions**.

- I would like the program to tell me **which countries do not have available data for specific products or years**.

- After the cleaning and filtering of the data, it would be nice to know **which of the data were incomplete/deleted to fit my summary**.

### must

- **cleaning:** dealing with missing data 
- **filtering:** filtering countries, years, products

### should

- inform which countries, years, products are missing

### could

- Report a summary of actions taken after cleaning filtering


## Analyser

### User stories

- As an economic analyst, I want to calculate the inflation rate 
for a specific country over a particular period to understand the economic development.

- As a data scientist, I want to analyze all available products for a specific country 
over a period to identify trends and patterns in consumer prices.

- As a researcher, I want to compare inflation rates for different products in a specific 
country to examine the impact of price changes on the economy and consumers.

### must

- It should return the calculated inflation rate as a numeric value or a percentage.

- The DataFrame should be properly labeled with product names and time points for easy comparison.
### could

- The method could handle missing data or incomplete data for certain time points and provide a warning or appropriate handling.


## Plotter

### User stories

- After I have chosen my Dataset, I want to have a clear visualisation of the data as an appropriate plot. 

- When my plot is output it should show me data of the products in the previous chosen countries.

- I would like the plot to show me a legend with all important information, in order to quickly understand what the plot tries to show me.

### must

- The Plot should be visually clear

- The Data must be ploted out correctly

### could

- Gives out a legend with the used information

# Nonfunctional requirements

- The Analyser should provide timely responses to user inputs and deliver analysis results promptly to support real-time decision-making.

- The class should be designed in a way that allows it to work with other relevant software or libraries commonly used in data analysis and manipulation.

- The calculated inflation rates and other analytical results should be accurate, with a high level of precision, to ensure reliable analysis and decision-making.