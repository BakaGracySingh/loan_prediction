import pickle
import streamlit as st
import pandas as pd


loan = pd.read_csv("loan-dataset.csv")


with open('logistic.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def preprocess_input(data):

    df = pd.DataFrame(data, index=[0])

    df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 0})
    df['Married'] = df['Married'].replace({'Yes': 1, 'No': 0})
    df['Education'] = df['Education'].replace({'Graduate': 1, "Not Graduate": 0})
    df['Property_Area'] = df['Property_Area'].replace({'Rural': 0, 'Semiurban': 1, 'Urban': 2})
    df["Credit_History"] = pd.to_numeric(df['Credit_History'], errors='coerce').astype(int)
    df["LoanAmount"] = pd.to_numeric(df['LoanAmount'], errors='coerce').astype(int)

    df[["ApplicantIncome", "LoanAmount"]] = scaler.fit_transform(df[["ApplicantIncome", "LoanAmount"]])

    
    return df


def predict_loan_status(data):
    # Preprocess input
    scaled_data = preprocess_input(data)

    # Make prediction using pickled model
    prediction = model.predict(scaled_data)

    # Return prediction
    return prediction

# Define Streamlit app
def app():
    # Define app title
    st.title('Loan Status Prediction')

    # Define app inputs
    inputs = {
        'Gender': st.selectbox('Gender', ['Male', 'Female']),
        'Married': st.selectbox('Married', ['Yes', 'No']),
        'Dependents': st.number_input('Number of Dependent', min_value=0, max_value=3),
        'Education': st.selectbox('Gender', ['Graduate', 'Not Graduate']),
        'ApplicantIncome': st.number_input('Applicant Income', min_value=loan.ApplicantIncome.min(), max_value=loan.ApplicantIncome.max()),
        'LoanAmount': st.number_input('Loan Amount', min_value=loan.LoanAmount.min()*1000, max_value=loan.LoanAmount.max()*1000),
        'Credit_History': st.number_input('Credit History', 0, 1),
        'Property_Area': st.selectbox('Property area', ['Urban', 'Semiurban', 'Rural'])
    }

    # Preprocess input and make prediction
    prediction = predict_loan_status(inputs)

    # Display prediction
    if prediction == 0:
        st.write('Loan application denied')
    else:
        st.write('Loan application approved')

# Run Streamlit app
if __name__ == '__main__':
    app()
