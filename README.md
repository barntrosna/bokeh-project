# bokeh-project
##College project using python and bokeh

##Project
This college project investigates the use of the Python programming language, coupled with the Bokeh Python/JavaScript libraries, for the purposes of processing data, and turning that data into useful visuals for the purposes of data analysis, presentations, and business dashboards. 

##Technologies
Python, Jupyter Notebook, Pandas, Bokeh.

##Environment
All the tools needed for the project are available to download and install separately for Linux, Mac or Windows operating systems. However, the quickest and most straightforward option may be to install them using a data science platform called Anaconda. The open source version of Anaconda has over 700 popular data science packages for Python, R and Scala. Python packages include Pandas, Matplotlib and Jupyter Notebook, and of course Bokeh. There is also an inbuilt package and environment manager, Conda, that can be used from the command line, so you can work in an isolated environment with managed dependencies.

##Bokeh
The main Bokeh documentation and reference material is available at http://bokeh.pydata.org/en/0.12.1/. It includes a User Guide for getting started, and for setting up Jupyter Notebook to use bokeh. Examples of Bokeh plots are available in the Gallery.
A set of sample data for the examples used in the documentation can be downloaded with the terminal command:

```
Bokeh sampledata
```

Detailed reference information about using the various classes, models and objects is in the Reference Guide.

A lot of the bokeh development takes place through github and there are some examples and tutorials available at https://github.com/bokeh/bokeh.
Bokeh is developing rapidly so some sources of information are out of date, but there are some good video tutorials available from recent Python and data science conferences, such as Strata Hadoop, PyData and PyCon.

##Other tools
Jupyter Notebook documentation including quickstart guides can be found at http://jupyter.readthedocs.io/en/latest/index.html. It is quite intuitive to use.
The notebook dashboard also ties in with conda environments, so you can create a new notebook in a particular environment. 

Pandas documentation for the latest version 0.18.1 is at http://pandas.pydata.org/pandas-docs/version/0.18.0/ with a _10 Minutes to pandas_ guide for beginners.

##Data
###Rainfall
Notebook: rainfall.ipynb

Data file: TotalRainfall.csv

Source:
Rainfall by Meteorological Weather Station, Month and Statistic on CSO website (source: Met Eireann)

http://www.cso.ie/px/pxeirestat/statire/SelectVarVal/Define.asp?Maintable=MTM01&Planguage=0

###Cars
Notebook: cars_notebook.ipynb

Data files: newcars25.csv, bands.csv

Source:
CSO  - Vehicle Registrations for Passenger Vehicles (Category A) by Engine Capacity cc, Car Make, Type of Fuel, Emission Band, Month and Statistic

http://www.cso.ie/px/pxeirestat/statire/SelectVarVal/Define.asp?MainTable=TDM02&PLanguage=0&PXSId=0

###Map
Notebook: Map.ipynb

Data files: ireland.json, county_pop_2002_2016.csv

Source:

county_pop_2002_2016.csv 

CSO  - EP001: Population and Actual and Percentage Change 2011 to 2016 by Sex, Province County or City, Census Year and Statistic

http://www.cso.ie/px/pxeirestat/Statire/SelectVarVal/Define.asp?maintable=EP001&PLanguage=0

ireland.json

This geoJSON data for the 26 counties is from a github gist at https://gist.github.com/eoiny/2183412 (thanks to Eoin O Loideain)

###Employment
Notebook: employment.ipynb, employment_notebook.ipynb

Application: employment folder

Data files: Employment.csv, total_employ.csv, percent_temp.csv, subsectors2.csv

Source:
DATA.GOV.ie Annual Employment Survey 2015 - Licensed under Standard Irish PSI Licence (CC-BY 4.0)
The Annual Employment Survey provides an analysis of employment levels in Industrial (including Primary Production) and Services companies under the remit of IDA Ireland, Enterprise Ireland and Údarás na Gaeltachta. This 2015 Annual Employment Survey report looks at employment trends over the 10-year period 2006-2015.

https://data.gov.ie/dataset/annual-employment-survey-2015

###Calls
Notebook: calls_notebook.ipynb

Data files: calls_one_day.csv

Source: 
Real data from a call centre serving a bank. The data was made available online as part of a university engineering course.

http://ie.technion.ac.il/serveng/callcenterdata/index.html 
