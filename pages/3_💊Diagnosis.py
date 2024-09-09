import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="SIR",
    page_icon="https://cdn-icons-png.flaticon.com/512/11469/11469451.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.write("Developed by SIR's Team")

st.title("Diagnosis!")
st.image("https://cdn-icons-png.flaticon.com/128/4435/4435747.png")
st.logo("b019d1f9-fe62-4653-bbc3-6f5093c68a28.jpg")


def generate_input_boxes(df):
    user_input = {}
    
    st.write("Please provide input for the following fields:")
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Use number input for numeric columns
            user_input[column] = st.number_input(f"Enter value for {column}:", min_value=0, step=1)
        else:
            # Use text input for non-numeric columns
            
            user_input[column] = st.text_input(f"Enter value for {column}")
    
    return user_input

df= pd.read_csv("Patient_Data_ds.csv")
df = df.drop(columns=['Diagnosis_Type', 'Recommendations', "Vaccination Status"])

user_input_data = generate_input_boxes(df)

user_input_df = pd.DataFrame([user_input_data])
st.write("Prepared Data for Model:", user_input_df)

if st.button("Predict "):
    st.write("Diagnosis: ......")
    st.write("Recommendations: .....")
    st.write("Alert: .......")
