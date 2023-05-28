import streamlit as st
import Home
import prediction


navigation = st.sidebar.selectbox('Page:', ('Home', 'Predict Price'))

if navigation == 'Home':
    Home.run()
else:
    prediction.run()