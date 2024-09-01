# prompt: generate a code for streamlit using the pickle model

import streamlit as st
import pickle

# Load the pickled model
with open('yuva.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("Biryani Price Prediction")

# Input fields for features
chicken_price = st.number_input("Chicken Price")
rice_price = st.number_input("Rice Price")
spice_price = st.number_input("Spice Price")
vegetable_price = st.number_input("Vegetable Price")
chef_experience = st.number_input("Chef Experience (years)")

# Prediction button
if st.button("Predict Biryani Price"):
    input_data = [[chicken_price, rice_price, spice_price, vegetable_price, chef_experience]]
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Biryani Price: {prediction:.2f}")

