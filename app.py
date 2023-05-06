import pickle
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import xgboost

pipe = pickle.load(open('pipe.pkl', 'rb'))
teams = [
    'India',
    'Australia',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]
eligible_cities = [
    'Colombo',
    'Mirpur',
    'Johannesburg',
    'Dubai',
    'Auckland',
    'Cape Town',
    'Pallekele',
    'Barbados',
    'London',
    'Sydney',
    'Melbourne',
    'Durban',
    'St Lucia',
    'Wellington',
    'Lauderhill',
    'Hamilton',
    'Centurion',
    'Manchester',
    'Abu Dhabi',
    'Nottingham',
    'Southampton',
    'Mount Maunganui',
    'Mumbai',
    'Chittagong',
    'Kolkata',
    'Lahore',
    'Delhi',
    'Nagpur',
    'Cardiff',
    'Chandigarh',
    'Adelaide',
    'Bangalore',
    'St Kitts',
    'Christchurch',
    'Trinidad'
]

st.title('T20 Cricket Score Prediction Application')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(eligible_cities))

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs_done = st.number_input('Overs Done (should be >5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Enter the runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs_done * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs_done
    input_df = pd.DataFrame({
        'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],
        'current_score': [current_score], 'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr],
        'last_five': [last_five]
    })
    # st.table(input_df)
    result = pipe.predict(input_df)
    st.header("Predicted Score: " + str(int(result)))
