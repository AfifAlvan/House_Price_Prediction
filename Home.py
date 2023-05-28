import streamlit as st
from PIL import Image



# Set the page configuration
st.set_page_config(
    page_title="House Prediction",
    page_icon=":house:",
    # layout="wide",
    initial_sidebar_state="auto"
)


def run():
    st.title('House Prediction')
    # st.subheader('Exploratory Data Analyst House Predict')
    st.write("---")
    #image
    image = Image.open('house.jpg')
    st.image(image, caption = 'Give the Price in Balance with Your Dream House')
    #Description
    st.write('''
             In achieving the dream of having a comfortable residence for your family, the steps that must be taken are to survey which house is right for your family.
Apart from price, convenience is an important factor to note. In every city, the price of each house is different. Many things factor into the difference in house prices. It must be very confusing if we do these calculations manually and personally.
''')
    image2= Image.open('think.jpg')
    st.image(image2)
    st.write('''
             So with the arrival of this House Price Prediction model, you can predict house prices according to your destination house. Several parameters have been provided in this model; you only need to fill in the values of these parameters, and the appropriate price will appear.
This price can be a consideration for you and your family to determine the price of a decent house for you to buy.
''')
    st.write('---')
    
    #barplot
    

if __name__ == '__main__':
    run()