# %%writefile app.py

import pickle
import streamlit as st


# load trained weight or model
picked_weight = open('saved_weight/loan_classfier.pkl', 'rb')
loan_classfier = pickle.load(picked_weight)

@st.cache()


# prediction function
def predict(Gender, Married, Dependents, Education, Self_Employed, Property_Area,
           ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History):
    
    ## Preprocess user input for categorical
    if Gender == "Male": 
        Gender = 0 
    else:
        Gender = 1
    
    if Married == "No":
        Married = 0
        
    else:
        Married = 1
        
    if Dependents == "No":
        Dependents = 0
    else:
        Dependents = 1
        
    if Education == "Not Graduate":
        Education = 0
    else:
        Education = 1
        
    if Self_Employed == "No":
        Self_Employed = 0
    else:
        Self_Employed = 1
        
    if Property_Area == "Rural":
        Property_Area = 0
    else:
        Property_Area = 1
        
        
    # Making Predictions
    predict = loan_classfier.predict([[Gender, Married, Dependents, Education, Self_Employed, Property_Area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History]])
    
    if predict == 0:
        pred = 'Rejected. Not fit for loan.'
    else:
        pred = 'Approved. Lets start filling the forms.'
        
    
    return pred


    
# This where the webpage is defined
def main():
    
    st.title('Loan Predictor')
    
    # Frontend 
    html = """
        <div style ="background-color:toamto;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Deploy with Streamlit Loan Prediction ML App demo</h1>
    
    """
    # displat front end
    st.markdown(html, unsafe_allow_html=True)
    
    
    # Create boxes for user input
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Married = st.selectbox('Married', ('Yes', 'No'))
    Dependents = st.selectbox('Dependents', ('Yes', 'No')) 
    Education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
    Self_Employed = st.selectbox('Self Employed', ('Yes', 'No'))  
    Property_Area = st.selectbox('Property Area', ('Urban', 'Rural')) 
    
    x = lambda a : a / 10000 # sample standard scaler
    
    ApplicantIncome = x(st.text_input('Applicant Income', '0'))
    CoapplicantIncome = x(st.text_input('Coapplicant Income', '0')) 
    LoanAmount = x(st.text_input('Loan Amount', '0'))
    Loan_Amount_Term = x(st.text_input('Loan Amount Term', '0'))
    Credit_History = x(st.text_input('Credit_History', '0')) 
    
    answer = ""
    
    
    # on-click predict, make prediction and keep
    if st.button('Predict'):
        answer = predict(Gender, Married, Dependents, Education, Self_Employed, Property_Area,
                        ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History)
        st.success(answer)
#         print('Done.')


if __name__=='__main__':
    
#     from pyngrok import ngrok
#     public_url = ngrok.connect('8501')
#     public_url
    
    main()
    
    
    
    
    
    
    
    
    
    
    
     
                                     
                  