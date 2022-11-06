import xgboost as xgb
import streamlit as st
import pandas as pd
import pickle
import numpy as np

#loading model
model = xgb.Booster()
model.load_model("model.pkl")

#Caching the model for faster loading
@st.cache


#defining function
def predict(HighBP, HighChol, BMI, GenHlth, Age):

    if HighBP < 140 and HighBP > 0:
        HighBP = 0
    else:
        HighBP = 1

    if HighChol < 240 and HighChol > 0:
        HighChol = 0
    else: 
        HighChol =1

    BMI = np.log1p(BMI)

    if GenHlth == 'Excellent':
        GenHlth = 1
    elif GenHlth == 'Very Good':
        GenHlth = 2
    elif GenHlth == 'Good':
        GenHlth = 3
    elif GenHlth == 'Fair':
        GenHlth = 4
    elif GenHlth == 'Poor':
        GenHlth = 5

    if Age >= 18 and Age <= 24:
        Age = 1
    elif Age >= 25 and Age <= 29:
        Age = 2
    elif Age >= 30 and Age <= 34:
        Age = 3
    elif Age >= 35 and Age <= 39:
        Age = 4
    elif Age >= 40 and Age <= 44:
        Age = 5
    elif Age >= 45 and Age <= 49:
        Age = 6
    elif Age >= 50 and Age <= 54:
        Age = 7
    elif Age >= 55 and Age <= 59:
        Age = 8
    elif Age >= 60 and Age <= 64:
        Age = 9
    elif Age >= 65 and Age <= 69:
        Age = 10
    elif Age >= 70 and Age <= 74:
        Age = 11
    elif Age >= 75 and Age <= 79:
        Age = 12
    elif Age >= 80:
        Age = 13

    test_df = pd.DataFrame([[HighBP, HighChol, BMI, GenHlth, Age]], columns=['HighBP', 'HighChol', 'BMI', 'GenHlth', 'Age'])
    dtest = xgb.DMatrix(test_df, enable_categorical=True)

    prediction = model.predict(dtest)
    pred_percent = prediction[0]*100

    if prediction >=0.5:
        status = f'You have a {round(pred_percent,2)}% risk of having diabetes. Hence, High Risk of Diabetes'

    else:
        status = f'You have a {round(pred_percent,2)}% risk of having diabetes. Hence, Low risk of Diabetes'

    return status

st.title('Diabetes Risk Prediction')
st.image('https://cdn.punchng.com/wp-content/uploads/2022/03/16094108/causes-of-diabetes.jpeg')
HighBP   = st.number_input('Blood Pressure (mm/Hg):', min_value=60, max_value=300, value=90)
HighChol = st.number_input('Total Cholesterol Level (mg/dL):', min_value=20, max_value=300, value=70)
BMI      = st.number_input('Body Mass Index:', min_value=0, max_value=500, value=20)
GenHlth  = st.selectbox('General Health:', ['Excellent', 'Good', 'Very Good', 'Fair', 'Poor'])
Age      = st.number_input('Total Cholesterol Level (mg/dL):', min_value=18, max_value=200, value=20)


if st.button('Predict Diabetes Risk'):
    prediction = predict(HighBP, HighChol, BMI, GenHlth, Age)
    st.write(prediction)

