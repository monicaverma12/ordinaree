import streamlit as st
import joblib

# Title
st.header("Ordinaree Machine Learning Web Page")

# Input bar 1
Sale = st.number_input("Enter Expected Sales")

# If button is pressed
if st.button("Click to get result"):
    # Unpickle classifier
    clf = joblib.load("No_of_Orders_predictor.pkl")

    # Get prediction
    prediction = clf.predict([[Sale]])[0]

    # Output prediction
    st.text(f"Total no of orders would be : {prediction}")
