import streamlit as st
import pickle
from time import strftime
import pandas as pd
import numpy as np

model = pickle.load(open('models/xgb_model.pkl', 'rb'))
sc = pickle.load(open('models/StandardScaler.pkl', 'rb'))
ohe = pickle.load(open('models/OneHotEncoder.pkl', 'rb'))

st.header('FLIGHT OPTIMAL TIME')

Departure = st.selectbox('Select Departure city', ['jaipur', 'Hyderabad'])
Arrival = st.selectbox('Select Arrival city', ['mumbai', 'new delhi', 'Jaipur', 'chennai', 'Bengaluru'])

stops = st.radio('No of stops', ['direct', '1 stops', '2 stops', '3 stops'])

if stops == 'direct':
    n_stop = 0
elif stops == '1 stops':
    n_stop = 2
elif stops == '2 stops':
    n_stop = 2
elif stops == '3 stops':
    n_stop = 3

Airline = st.selectbox('Select Airline ',
                       ['IndiGo', 'Air India', 'GoFirst', 'AirAsia India', 'SpiceJet', 'Multiple Airlines'])

depr_date = st.date_input('Departure Date')
date = pd.to_datetime(depr_date).day
month = pd.to_datetime(depr_date).month
weekday = pd.to_datetime(depr_date).day_of_week

depr_time = st.time_input('Departure time')
depr_hr = int((str(depr_time)).split(':')[0])
depr_min = int((str(depr_time)).split(':')[1])

price = st.number_input('Price in INR', 500, 30000)

flight_duration = st.number_input('flight duration in hr', 1, 50)
flight_duration = 60 * flight_duration

columns_name = ['airlines', 'Date', 'Month', 'Weekday', 'depr_Citie', 'Ar_Citie',
                'Travel_Time', 'no_stops', 'Price', 'Dep_Time_hr', 'Dep_Time_min']

if st.button('Predict'):
    time_differ = pd.to_datetime(str(depr_date) + ' ' + str(depr_time)) - pd.to_datetime(strftime("%Y%m%d-%H%M"))
    time_differ_min = time_differ.components.days * 24 * 60 + time_differ.components.hours * 60 + time_differ.components.minutes

    # Predicting price

    price_dict = {}

    columns_name = ['airlines', 'Date', 'Month', 'Weekday', 'depr_Citie', 'Ar_Citie',
                    'Travel_Time', 'no_stops', 'Dep_Time_hr', 'Dep_Time_min']
    if time_differ_min > 10080:
        for t in range(10080, 48960, 60):
            data = np.reshape(
                [Airline, date, month, weekday, Departure, Arrival, flight_duration, n_stop, depr_hr, depr_min], [1, 10])

            X = pd.DataFrame(data, columns=columns_name)
            X['time_differ_min'] = t

            X['Weekday'] = X['Weekday'].astype(int)

            # let us select the numerical columns that need scaling
            num_col = ['Date', 'Month', 'Travel_Time',
                       'no_stops', 'Dep_Time_hr', 'Dep_Time_min', 'time_differ_min']

            # 1. preprocess
            X[num_col] = sc.transform(X[num_col])
            X_ohe = ohe.transform(X[['airlines', 'depr_Citie', 'Ar_Citie', 'Weekday']])
            X_new = np.hstack((X[num_col].values, X_ohe))

            price_dict[str(t)] = int(model.predict(X_new))

        temp = min(price_dict.values())
        optimal_time = [key for key in price_dict if price_dict[key] == temp]
        for i in optimal_time:
            op_time = int(i)

        wait_days = int(op_time // (24 * 60))
        wait_hr = int((op_time / 60) % 24)

        st.subheader(f'You can wait and buy your ticket after {wait_days} Days {wait_hr} hours and your approx. price will be {temp} INR')
    else:
        st.subheader('Book Now')