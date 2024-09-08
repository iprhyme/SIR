import streamlit as st
st.set_page_config(
    page_title="SIR",
    page_icon="https://cdn-icons-png.flaticon.com/512/11469/11469451.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.write("Developed by SIR's Team")
st.logo("b019d1f9-fe62-4653-bbc3-6f5093c68a28.jpg")


# Set up session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Predefined valid credentials (you can replace this with a more secure method)
VALID_USERNAME = "LinaCEO"
VALID_PASSWORD = "pass123"


# Login Page
if not st.session_state.logged_in:
    st.title("Login Page")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label="Login")

        if submit_button:
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")
else:
    # Display the dashboard or secured content if the user is logged in
    st.title("WELCOME YOU'VE LOGGED IN !")

    # Provide a logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.info("You have logged out")
        st.experimental_rerun()
