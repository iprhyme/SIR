import streamlit as st 
import pandas as pd
import plotly_express as px
st.set_page_config(
    page_title="SIR",
    page_icon="https://cdn-icons-png.flaticon.com/512/11469/11469451.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
with st.sidebar:
    
   
    st.sidebar.write("Developed by SIR's Team")
st.title("Pateints Analysis!")
st.logo("b019d1f9-fe62-4653-bbc3-6f5093c68a28.jpg")

if st.session_state.logged_in:
    uploaded_file= st.file_uploader("Upload", type=["csv", "xlsx"])

    if uploaded_file is not None:
        file_name = uploaded_file.name
        file_extension = file_name.split(".")[-1]
        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
        #  st.dataframe(df)
            styled_df = df.style.set_properties(**{
        'font-weight': 'bold'
        })
            st.markdown(styled_df.to_html(), unsafe_allow_html=True)
        elif file_extension == 'xlsx':
            df = pd.read_excel(uploaded_file)
            styled_df = df.style.set_properties(**{
        'font-weight': 'bold'
        })
            st.markdown(styled_df.to_html(), unsafe_allow_html=True)
        
        fig = px.pie(df, 'Diagnosis_Type', title="Count of Patients by Diagnosis Type",hole=0.4)
        st.plotly_chart(fig)
        fig2 = px.strip(df, x='Diagnosis_Type', y='Age', color='Diagnosis_Type', 
                    title="Age vs Diagnosis Type", stripmode='overlay',hover_data=['patient name'])
        st.plotly_chart(fig2)
else: 
    st.subheader("Please Log in, to get access to this page ")
            
        
