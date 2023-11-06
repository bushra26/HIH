# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 03:54:43 2023

@author: ac
"""
import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open(r'C:\Users\ac\Desktop\h_i_h\HIHdiabetes.ipynb - Colaboratory_files\New folder\heartdiseaseprediction_webapp.py', 'rb'))

#creating a function 
def heart_prediction(input_data):
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return'The Person has Heart Disease'
  
  
  
def main():
    #giving a title
    st.title('Heart Prediction ')
    #getting the input from user
    age= st.number_input('age of Person')
    sex=st.text_input('sex')
    if(sex=='M'):
        sex=0
    else:
        sex=1
    cp= st.number_input('chest pain type')
    trestbps= st.number_input('resting blood pressure')
    chol= st.number_input(' cholestrol Level')
    fbs= st.number_input('fasting blood sugar')
    restecg= st.number_input(' resting elecrographic result')
    thalach= st.number_input('maximum heart rate achieve')
    exang= st.number_input('exercise induced angina')
    oldpeak= st.number_input('ST depression induced by exercise relative to rest')
    slope= st.number_input('slope of the peak exercise ST segment')
    ca= st.number_input('calcium')
    thal= st.number_input('thalassemia value')
    
    #code for prediction
    diagnosis = ''
     
    #creating button
    
    if st.button('Heart Test Result'):
        diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        st.success(diagnosis)
        
if __name__ == '__main__':
    main()