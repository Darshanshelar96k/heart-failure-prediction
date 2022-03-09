# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:50:52 2022

@author: 91960
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
with open('C:/Users/91960/Downloads/p_heart/heart_c.pkl', 'rb') as file:
      data2 = pickle.load(file)
      
      
def load_model():
    with open('C:/Users/91960/Downloads/p_heart/heart_c.pkl', 'rb') as file:
     data2 = pickle.load(file)
     return data2
     data2 = load_model()
model2 = data2["model"]
le_sex = data2["le_sex"]
le_chest = data2["le_chest"]
le_ecg  = data2["le_ecg"]
le_ex  = data2["le_ex"]
le_slop  = data2["le_slop"]
    
def show_predict_page():
  st.title()  

    
Sex	=('M',
      'F')

ChestPainType = ('ASY',
                 'NAP',
                 'ATA',
                 'TA' )

RestingECG=('Normal',
            'LVH',
            'ST')

ExerciseAngina=('N',
                'Y')

ST_Slope=('Flat',
          'Up',
         'Down')
st.title('HEART DIEASES PREDICTION ' )




st.subheader('Read the folloeing information')

'''ChestPainType  TA: Typical Angina  ATA: Atypical Angina  NAP: Non-Anginal Pain ASY: Asymptomatic'''
'''FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]'''
'''RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]'''
'''ExerciseAngina: exercise-induced angina [Y: Yes, N: No]'''
'''Oldpeak: oldpeak = ST [Numeric value measured in depression]'''
'''ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]')'''
    


st.subheader('FEEL FOLLOWING INFORMATION ')
    
Age = st.number_input("AGE OF PERSON",min_value =25,max_value=80,step =1)
Sex = st.selectbox("MALE/FEMALE",Sex)
ChestPainType=st.selectbox("CHEST PAIN TYPE",ChestPainType)
RestingBP= st.number_input("resting blood pressure [mm Hg]",min_value=0,max_value=200,step =1)
Cholesterol=st.number_input("serum cholesterol [mm/dl]",min_value=0,max_value=603,step =1)
FastingBS=st.number_input("fasting blood sugar",min_value =0,max_value=1)
RestingECG = st.selectbox("resting ecg",RestingECG)
MaxHR = st.number_input("MAXIMMUM HEART RATE ",min_value =60,max_value=203,step =1)
ExerciseAngina = st.selectbox("EXCERCISE Y/N",ExerciseAngina)
Oldpeak = st.number_input("ST depression induced by exercise relative to rest ",min_value =2,max_value=2)
ST_Slope = st.selectbox("slop of st",ST_Slope)

ok = st.button("CLICK TO CHEACK")
if ok:
    input_data= np.array([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    input_data[:,1] = le_sex.fit_transform(input_data[:,1])
    input_data[:,2] = le_chest.fit_transform(input_data[:,2])
    input_data[:,6] = le_ecg.fit_transform(input_data[:,6])
    input_data[:,8] = le_ex.fit_transform(input_data[:,8])
    input_data[:,10] = le_slop.fit_transform(input_data[:,10])
    HeartDisease=model2.predict(input_data)
    if HeartDisease ==0:
        st.subheader("THE PERSON IS NORMAL ")
    else:
         st.subheader("PERSON HAVE CHANCES TO HEART FAILURE")
          
 
     
     
   
    
  