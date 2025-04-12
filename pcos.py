import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load model
model = pickle.load(open(r'C:\Users\uc-18\Desktop\Neutron\pcos_model.pkl', 'rb'))

def main():
    # Title
    st.title('Welcome to your PCOS Predictor!')

    # Header
    st.header('This tool is meant to predict your likelihood of having Polycystic Ovarian Syndrome (PCOS)')

    # Subheader / Intro
    st.markdown(
        'PCOS is a condition that affects 1 in 10 women. It often goes undiagnosed with symptoms like irregular periods, excessive hair growth, weight gain, anxiety and depression. This tool is meant to assess your symptoms and tell you if PCOS could be the cause of them.'
    )

    # Create layout with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.header('Fill out the form:')
        st.subheader('Select Yes - 1 or No - 0 for each symptom:')

        # Create form
        with st.form('pcos_form'):
            weight_gain = st.number_input('Weight gain', min_value=0, max_value=1)
            periods = st.number_input('Irregular Periods', min_value=0, max_value=1)
            hair_growth = st.number_input('Excessive Hair Growth', min_value=0, max_value=1)
            darkskin = st.number_input('Skin darkening', min_value=0, max_value=1)
            fast_food = st.number_input('Do you consume Fast Food regularly?', min_value=0, max_value=1)

            submit = st.form_submit_button('Submit Answers')

        if submit:
            # Ensure input matches model expectations
            inputs = [[weight_gain, hair_growth, darkskin, fast_food]]

            # Make prediction
            result = model.predict(inputs)

            # Show result
            if result[0] == 0:
                st.success("Congrats! Chances are you don't have PCOS!")
            else:
                st.warning("It is likely you suffer from PCOS. Please consult with your physician.")

if __name__ == '__main__':
    main()
