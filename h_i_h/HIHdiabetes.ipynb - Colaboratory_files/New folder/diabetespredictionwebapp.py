import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open(r'C:\Users\ac\Desktop\h_i_h\New folder (3)\trained_model (1).sav', 'rb'))
#creating a function 
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    #giving a title
    st.title('Diabetes Prediction ')
    #getting the input from user
    
    Pregnancies= st.text_input('Number of Pregnancies')
    Glucose= st.text_input('Gulucose Level')
    BloodPressure= st.text_input('Blood Pressure Value')
    SkinThickness= st.text_input('SkinThickness')
    Insulin= st.text_input('Insulin Level')
    BMI= st.text_input('BMI value')
    DiabetesPedigreeFunction= st.text_input(' Diabetes Pedigree Function Value')
    Age= st.text_input('Age of the Person')
    
    #code for prediction
    diagnosis = ''
     
    #creating button
    
    if st.button('Dieabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        st.success(diagnosis)
        
if __name__ == '__main__':
    main()