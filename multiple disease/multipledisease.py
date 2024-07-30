import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open("C:/Users/nehaj/OneDrive/Desktop/multiple disease/saved_models/diabetes_model.sav",'rb'))
heart_model = pickle.load(open("C:/Users/nehaj/OneDrive/Desktop/multiple disease/saved_models/heart_disease_model.sav",'rb'))
parkinson_model = pickle.load(open("C:/Users/nehaj/OneDrive/Desktop/multiple disease/saved_models/parkinsons_model.sav",'rb'))
cancer_model = pickle.load(open("C:/Users/nehaj/OneDrive/Desktop/multiple disease/saved_models/breast_model.sav",'rb'))

#sidebar for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                            

                            icons=['house-door-fill','activity', 'heart', 'person','bookmark-heart'],
                            default_index=0)
if selected == 'Home':
    st.title("Welcome to Multiple Disease Prediction System")
    st.markdown("""
    ### Overview

    This system allows you to predict the likelihood of several diseases based on various health metrics. 
    Use the sidebar to navigate to the desired prediction type. Below you can find detailed descriptions of the attributes used for each prediction type.

    ### Diabetes Prediction
    - **Pregnancies:** Number of times pregnant.
    - **Glucose:** Glucose level in the blood.
    - **BloodPressure:** Blood pressure measurement.
    - **SkinThickness:** Thickness of the skin.
    - **Insulin:** Insulin level in the blood.
    - **BMI:** Body Mass Index.
    - **DiabetesPedigreeFunction:** Diabetes percentage based on family history.
    - **Age:** Age of the person.

    ### Heart Disease Prediction
    - **Age:** Age of the patient.
    - **Sex:** Gender of the patient.
    - **Chest Pain Type:** Type of chest pain experienced.
    - **BP (Blood Pressure):** Blood pressure level.
    - **Cholesterol:** Cholesterol level in blood.
    - **FBS over 120:** Fasting blood sugar level greater than 120 mg/dl.
    - **EKG Results:** Electrocardiogram results.
    - **Max HR:** Maximum heart rate achieved.
    - **Exercise Angina:** Presence of angina induced by exercise.
    - **ST Depression:** Depression of the ST segment in electrocardiogram.

    ### Parkinson’s Prediction
    - **MDVP-Fo(Hz):** Average vocal fundamental frequency.
    - **MDVP-Fhi(Hz):** Maximum vocal fundamental frequency.
    - **MDVP-Flo(Hz):** Minimum vocal fundamental frequency.
    - **MDVP-Jitter(%), MDVP-Jitter(Abs), MDVP-RAP, MDVP-PPQ, Jitter-DDP:** Measures of variation in fundamental frequency.
    - **MDVP-Shimmer, MDVP-Shimmer(dB), Shimmer-APQ3, Shimmer-APQ5, MDVP-APQ, Shimmer-DDA:** Measures of variation in amplitude.
    - **NHR, HNR:** Ratio of noise to tonal components in the voice.
    - **Status:** Health status (1 - Parkinson's, 0 - Healthy).
    - **RPDE, D2:** Nonlinear dynamical complexity measures.
    - **DFA:** Signal fractal scaling exponent.
    - **Spread1, Spread2, PPE:** Nonlinear measures of fundamental frequency variation.

    ### Breast Cancer Prediction
    - **Radius Mean, Radius SE, Radius Worst:** Mean, standard error, and worst value of radius of tumors.
    - **Compactness Mean, Compactness SE, Compactness Worst:** Mean, standard error, and worst value of compactness of tumors.
    - **Texture Mean, Texture SE, Texture Worst:** Mean, standard error, and worst value of texture of tumors.
    - **Concavity Mean, Concavity SE, Concavity Worst:** Mean, standard error, and worst value of concavity of tumors.
    - **Perimeter Mean, Perimeter SE, Perimeter Worst:** Mean, standard error, and worst value of perimeter of tumors.
    - **Concave Points Mean, Concave Points SE, Concave Points Worst:** Mean, standard error, and worst value of concave points of tumors.
    - **Area Mean, Area SE, Area Worst:** Mean, standard error, and worst value of area of tumors.
    - **Symmetry Mean, Symmetry SE, Symmetry Worst:** Mean, standard error, and worst value of symmetry of tumors.
    - **Smoothness Mean, Smoothness SE, Smoothness Worst:** Mean, standard error, and worst value of smoothness of tumors.
    - **Fractal Mean, Fractal SE, Fractal Worst:** Mean, standard error, and worst value of fractal dimension of tumors.

    """)
    
#diabetes prediction page
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction')

    #getting the input data from the user
    #columns for input feilds
    col1,col2,col3 = st.columns(3)

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
    

    #code for prediction
    diab_diagnosis = ''

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'

        else:
            diab_diagnosis = 'The person is not Diabetic'

    st.success(diab_diagnosis)

if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    
    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Gender')
    with col3:
        cp = st.text_input('Chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting blood Pressure > 120 mg/dL')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    with col3:
        exang = st.text_input('Exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by flourospy')
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')


    heart_diagnosis = ''

    if st.button('Heart disease Test Result'):
        try:
            # Convert inputs to appropriate numeric types
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            # Convert all inputs to floats (or ints if you prefer)
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_model.predict([user_input])

            if(heart_prediction[0] == 1):
               heart_diagnosis = 'The person is having Heart Disease'
            else:
               heart_diagnosis = 'The person does not have Heart Disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values for all fields.'


    st.success(heart_diagnosis)



    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction')

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP-Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP-Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP-Flo(Hz)')
    with col4:
        jitter = st.text_input('MDVP-Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP-Jitter(Abs)')
    with col1:
        rap = st.text_input('MDVP-RAP')
    with col2:
        ppq = st.text_input('MDVP-PPQ')
    with col3:
        jitter_ddp = st.text_input('Jitter-DDP')
    with col4:
        shimmer = st.text_input('MDVP-Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP-Shimmer(dB)')
    with col1:
        apq3 = st.text_input('Shimmer-APQ3')
    with col2:
        apq5 = st.text_input('Shimmer-APQ5')
    with col3:
        apq = st.text_input('MDVP-APQ')
    with col4:
        dda = st.text_input('Shimmer-DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')
    
    parkinsons_diagnosis = ''

    if st.button('Parkinsons disease Test Result'):
        try:
            # Convert inputs to appropriate numeric types
            user_input = [fo,fhi,flo,jitter,jitter_abs,rap,ppq,jitter_ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]
            # Convert all inputs to floats (or ints if you prefer)
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinson_model.predict([user_input])

            if(parkinsons_prediction[0] == 1):
               parkinsons_diagnosis = 'The person has Parkinsons Disease'
            else:
               parkinsons_diagnosis = 'The person does not have Parkinsons Disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values for all fields.'


    st.success(parkinsons_diagnosis)


if (selected == 'Breast Cancer Prediction'):
    st.title('Breast Cancer Prediction')

    col1,col2,col3,col4,col5 = st.columns([5,5,5,5,5])
    

    with col1:
        radius_mean = st.text_input('Radius mean')
    with col2:
        texture_mean = st.text_input('Texture mean')
    with col3:
        perimeter_mean = st.text_input('Perimeter mean')
    with col4:
        area_mean = st.text_input('Area mean')
    with col5:
        smoothness_mean = st.text_input('Smoothness mean')
    with col1:
        compactness_mean = st.text_input('Compactness mean')
    with col2:
        concavity_mean = st.text_input('Concavity mean')
    with col3:
        concave_points_mean = st.text_input('Concave points mean')
    with col4:
        symmetry_mean = st.text_input('Symmetry mean')
    with col5:
        fractal_dimension_mean = st.text_input('Fractal mean')
    with col1:
        radius_se = st.text_input('Radius se')
    with col2:
        texture_se = st.text_input('Texture se')
    with col3:
        perimeter_se = st.text_input('Perimeter se')
    with col4:
        area_se = st.text_input('Area se')
    with col5:
        smoothness_se = st.text_input('Smoothness se')
    with col1:
        compactness_se = st.text_input('Compactness se')
    with col2:
        concavity_se = st.text_input('Concavity se')
    with col3:
        concave_points_se = st.text_input('Concave points se')
    with col4:
        symmetry_se = st.text_input('Symmetry se')
    with col5:
        fractal_dimension_se = st.text_input('Fractal se')
    with col1:
        radius_worst = st.text_input('Radius worst')
    with col2:
        texture_worst = st.text_input('Texture worst')
    with col3:
        perimeter_worst = st.text_input('Perimeter worst')
    with col4:
        area_worst = st.text_input('Area worst')
    with col5:
        smoothness_worst = st.text_input('Smoothness worst')
    with col1:
        compactness_worst = st.text_input('Compactness worst')
    with col2:
        concavity_worst = st.text_input('Concavity worst')
    with col3:
        concave_points_worst = st.text_input('Concave points worst')
    with col4:
        symmetry_worst = st.text_input('Symmetry worst')
    with col5:
        fractal_dimension_worst = st.text_input('Fractal worst')


    cancer_diagnosis = ''

    if st.button('Breast Cancer Prediction Result'):
        try:
            user_input = [radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]
            user_input = [float(x) for x in user_input]
            prediction = cancer_model.predict([user_input])

            if(prediction[0] == 1):
               cancer_diagnosis = 'The Breast Cancer is Benign'
            else:
               cancer_diagnosis = 'The Breast cancer is Malignant'
        except ValueError:
            cancer_diagnosis = 'Please enter valid numeric values for all fields.'


    st.success(cancer_diagnosis)

