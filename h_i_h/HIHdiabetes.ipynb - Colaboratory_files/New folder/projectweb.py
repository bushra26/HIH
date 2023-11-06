
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

diabetes_model = pickle.load(open(r'C:\Users\ac\Desktop\h_i_h\HIHdiabetes.ipynb - Colaboratory_files\New folder\diabetes_model (1).sav', 'rb'))

heart_disease_model = pickle.load(open(r'C:\Users\ac\Desktop\h_i_h\HIHdiabetes.ipynb - Colaboratory_files\New folder\heart_disease_model.sav','rb'))

mental_disease_model = pickle.load(open(r'C:\Users\ac\Desktop\h_i_h\HIHdiabetes.ipynb - Colaboratory_files\New folder\mentalhealth_model (1).sav','rb'))

# sidebar for navigation
with st.sidebar:
      selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction','Mental Disease Prediction',
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
print(selected)     
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    print('helloo yhuguhg hjh')
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    # Mental  Disease Prediction Page
if (selected == 'Mental Disease Prediction'):
        print('helloo')
        # page title
        st.title('Mental Disease Prediction using ML')
        
        col1, col2 = st.columns(2)
        
        with col1:
            owncomputerseparate  = st.number_input('own computer separate ')
        
        with col2:
          currentlyemployedatleastparttime = st.number_input('currently employed at least part-time')
            
        with col1:
           legallydisabled = st.number_input('legally disabled')
            
        with col2:
            regularaccesstotheinternet = st.number_input(' regular access to the internet')
            
        with col1:
            liveparents = st.number_input('live with parents')
            
        with col2:
            havegapinresume = st.number_input(' have gap in resume')
            
        with col1:
            Annualincome= st.number_input('Annual income (including any social welfare programs) in USD')
            
        with col2:
            unemployed = st.number_input('unemployed')
            
        with col1:
            readoutsideofworkandschool = st.number_input(' read outside of work and school')
            
        with col2:
            Annualincomefromsocialwelfareprograms = st.number_input('Annual income from social welfare programs')
            
        with col1:
            Iamonsection8housing = st.number_input('I am on section 8 housing')
            
        with col2:
            Anxiety = st.number_input('Anxiety')
        with col1:
            Depression = st.number_input('Depression')
              
        with col2:
             Obsessivethinking= st.number_input('Obsessive thinking')
              
        with col1:
            Moodswings = st.number_input('Mood swings')
        with col2:
             Panicattacks = st.number_input('Panic attacks')         
         
         
        # code for Prediction
        Mental_Health = ''
        
        # creating a button for Prediction
        
        if st.button('Mental Health Test Result'):
             Mental_prediction = mental_disease_model.predict([[owncomputerseparate, currentlyemployedatleastparttime, legallydisabled, regularaccesstotheinternet, liveparents, havegapinresume, Annualincome, unemployed, readoutsideofworkandschool, Annualincomefromsocialwelfareprograms, Iamonsection8housing, Anxiety, Depression, Obsessivethinking, Moodswings, Panicattacks]])                          
            
             if (Mental_prediction[0] == 0):
               Mental_Health = 'The person is having mental disease'
             else:
               Mental_Health = 'The person does not have any mental disease'
            
        st.success(Mental_Health)
            
        
    

