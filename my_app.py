import streamlit as st
import joblib
import numpy as np

st.title("Hello, World App")
st.write("Hello, World!")

'''



# Load the models
model_reel = joblib.load("model_reel (1).pkl")
model_photo = joblib.load("model_photo (1).pkl")
model_carousel = joblib.load("model_carousel (1).pkl")



# Option to select type
option = st.selectbox(
    "Select the type of content you want to predict engagement for:",
    ("Reel", "Photo", "Carousel")
)

# Input features for Reels
if option == 'Reel':
    followers = st.number_input('Number of Followers', min_value=0)
    avg_engagement = st.number_input('Average Engagement', min_value=0.0)
    viewership_rate = st.number_input('Viewership Rate', min_value=0.0)
    viewership_score = st.slider('Viewership Score (0 to 10)', min_value=0.0, max_value=10.0)
    engagement_score = st.slider('Engagement Score (0 to 10)', min_value=0.0, max_value=10.0)
    
    avg_views = st.number_input('Average Views', min_value=0.0)
    
    # Prepare input data
    input_data = np.array([[followers, avg_engagement, viewership_rate, viewership_score, engagement_score, avg_views]])
    
    # Make predictions
    if st.button('Predict Engagement Rate'):
        prediction_reel = model_reel.predict(input_data)[0]
        st.write(f'Predicted Engagement Rate for Reel: {prediction_reel:.2f}')

# Input features for Photos and Carousels
else:
    followers = st.number_input('Number of Followers', min_value=0)
    avg_engagement = st.number_input('Average Engagement', min_value=0.0)
    engagement_score = st.slider('Engagement Score (0 to 10)', min_value=0.0, max_value=10.0)
    
    
    # Prepare input data
    input_data = np.array([[followers, avg_engagement, engagement_score]])
    
    # Make predictions
    if option == 'Photo' and st.button('Predict Engagement Rate'):
        prediction_photo = model_photo.predict(input_data)[0]
        st.write(f'Predicted Engagement Rate for Photo: {prediction_photo:.2f}')
    elif option == 'Carousel' and st.button('Predict Engagement Rate'):
        prediction_carousel = model_carousel.predict(input_data)[0]
        st.write(f'Predicted Engagement Rate for Carousel: {prediction_carousel:.2f}')

'''
