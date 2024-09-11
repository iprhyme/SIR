import streamlit as st
st.set_page_config(
    page_title="SIR",
    page_icon="3-removebg-preview.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    

    st.sidebar.write("Developed by SIR's Team")

st.title("SIR")
st.logo("sir.png")



st.write("SIR provides an innovative platform that leverages AI and machine learning to transform healthcare delivery. Our solutions empower clinicians with real-time data-driven insights to optimize care while eliminating inefficiencies.")

with st.expander("What is SIR?"):
    st.write("SIR is a platform that analyzes patient data using advanced AI to generate personalized treatment plans.")
    st.write("Prescriptions tailored to each patient's genomic profile and health history promote positive outcomes.")
    st.write("SIR puts patients' wellbeing at the center of healthcare with data-driven, individualized treatment plans.")


st.subheader("Kindly fill out the questionnaire below")
st.link_button(help="will move you to the Google form",label="Questionnaire", url="https://docs.google.com/forms/d/e/1FAIpQLScyHj_5FCRN0mukyXG54dOtyVO59ErS-NOBNlGD0MLHlCBtuw/viewform")



with st.expander("Contacts Information"):
    st.text("Contact Us via:")
    st.markdown("[Twitter](https://x.com/laranduil)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/lina-l-alharbi)")
    
    




