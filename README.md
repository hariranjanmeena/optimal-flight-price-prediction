# Predicting-Flight-Ticket-Pricing-Using-Machine-Learning

web app link - 

![Python 3.9](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![Scikit-Learn](https://img.shields.io/badge/Library-ScikitLearn-orange.svg)

## Table of Content
  * [Problem Statement](#problem-statement)
  * [ML Framework](#ml-framework)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Future scope of project](#future-scope)

## Problem Statement
- Can we use Machine Learning to help a customer decide the optimal time to purchase a flight ticket?

## Data gathering 

Web scraping is a very powerful tool to learn for any data professional. With web scraping the entire internet becomes your database. In this repository how to parse a web page into a data file (csv) using a Python package called BeautifulSoup Two ways to extract data from a website:

#### Data scraping with Beautiful Soup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

## Dataset

Scrapped 6 month flight data from [Kayak.co.in](https://www.kayak.co.in/). This dataset contains all the flights in the month of January 2022 and June 2022. There are more than 12000 flights in the dataset. The features were manually chosen to do a primary flight price analysis. There are several other features available on their website.

Feature scarpped : 

- Airlines
- date: The date of the journey
- month: The month of the journey
- year: The year of the journey
- weekday: The weekday of the journey
- departure city: The source from which the service begins.
- arrival city: The destination where the service ends.
- travel time duration: Total duration of the flight.
- Dep_Time: The time when the journey starts from the source.
- Arrival_Time: Time of arrival at the destination.
- no. of stops: Total stops between the source and destination.
- price: The price of the ticket
- timestamp: booking time


## ML Framework:
Assume a customer decides to purchase a ticket for a particular flight at time = X
hours before departure. The optimal time to purchase the ticket t_opt is:
- in the range [X hours before dep., 4 hours before dep.]
- time at which we achieve minimum flight price until departure

## Installation
The Code is written in Python 3.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)


## Directory Tree 
```
├── Blueprint 
│   ├── Blueprint.pdf
├── data
│   ├── combined_Data
│   ├── data2
│   ├── combine_Data.ipynb
├── models
│   ├── dtree_model.pkl
│   ├── OneHotEncoder.pkl
│   ├── StandardScaler.pkl
│   ├── xgb_model.pkl
├── Procfile
├── Data_Scrapper.ipynb
├── Exploratory data analysis.ipynb
├── Model building.ipynb
├── app.py
├── chromedriver.exe
├── chromedriver_win32.zip
├── app.py
├── cookies.pkl
├── flight_data.csv
├── Flight_new_Data.xls
├── requirements.txt
├── setup.sh
```

## Future scope
- Access to high quality flight data for multiple routes and over long
time-periods is incredibly important to be able to train the data. It’ll be
interesting to extend the work to more routes, with more data.
- Users generally purchase a ticket on a route, not an individual flight. The
current setup doesn’t capture the majority use case.
- Currently, the agents interaction doesn’t change the environment. However,
in actual ticket purchase problems, the agents behavior can lead to tickets
being sold out etc.
