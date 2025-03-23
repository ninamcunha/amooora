import streamlit as st
import pandas as pd
from predict_matches import predict_similar_people  # Import the prediction function

# Display the logo at the top of the app
#st.image("1_logoV.png", width=200)  # Adjust the width as needed

# Title of the app
st.title("Find Your Matches")
st.write("Fill out the form to find your top 5 matches.")

# Initialize an empty dictionary to store user inputs
user_input = {}

# Create two columns for the form
col1, col2 = st.columns(2)

# Column 1
with col1:
    # Gender
    user_input['female'] = st.radio("Gender", ["Male", "Female"])
    user_input['female'] = 1 if user_input['female'] == "Female" else 0

    # Age (scaled)
    user_input['age_scaled'] = st.number_input("Age", min_value=18, max_value=100, value=30, help="Enter your age (18-100).")

    # Relationship Status
    user_input['single'] = st.radio("Relationship Status", ["Single", "In a Relationship"])
    user_input['single'] = 1 if user_input['single'] == "Single" else 0

    # Height (scaled)
    user_input['height_scaled'] = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, value=1.75, step=0.01, help="Enter your height in meters (1.0-2.5).")

    # Orientation
    orientation = st.radio("Orientation", ["Bisexual", "Gay", "Straight"])
    user_input['orientation_bisexual'] = 1 if orientation == "Bisexual" else 0
    user_input['orientation_gay'] = 1 if orientation == "Gay" else 0
    user_input['orientation_straight'] = 1 if orientation == "Straight" else 0

    # Diet Type
    diet_type = st.radio("Diet Type", ["Vegetarian", "Non-Vegetarian"])
    user_input['diet_type_vegetarian'] = 1 if diet_type == "Vegetarian" else 0

# Column 2
with col2:
    # Level of Education
    education_level = st.radio("Level of Education", [
        "College/University", "Grad or Professional Education", "Two-Year College or Less"
    ])
    user_input['education_type_college_univ'] = 1 if education_level == "College/University" else 0
    user_input['education_type_grad_or_professional_edu'] = 1 if education_level == "Grad or Professional Education" else 0
    user_input['education_type_two_year_college_or_less'] = 1 if education_level == "Two-Year College or Less" else 0

    # Education Status
    education_status = st.radio("Education Status", ["Graduated", "In progress"])
    user_input['education_status_graduated'] = 1 if education_status == "Graduated" else 0
    user_input['education_status_working'] = 1 if education_status == "In progress" else 0

    # Languages Spoken
    st.write("Languages Spoken:")
    user_input['speaks_english'] = 1 if st.checkbox("English", value=True) else 0
    user_input['speaks_spanish'] = 1 if st.checkbox("Spanish") else 0
    user_input['speaks_other'] = 1 if st.checkbox("Other") else 0

    # Pets
    user_input['has_dogs_yes'] = st.radio("Do you have dogs?", ["Yes", "No"])
    user_input['has_dogs_yes'] = 1 if user_input['has_dogs_yes'] == "Yes" else 0

    # Number of Kids
    no_of_kids = st.radio("Number of Kids", ["None", "One", "More than One"])
    user_input['no_of_kids_more_than_one'] = 1 if no_of_kids == "More than One" else 0
    user_input['no_of_kids_one'] = 1 if no_of_kids == "One" else 0

# Add columns for "not disclosed" options with default value 0
user_input['education_type_not_disclosed'] = 0
user_input['education_status_not_disclosed'] = 0

# Add empty columns for variables that will be processed in a separate .py file
user_input['text_length_scaled'] = 0  # Placeholder for text_length_scaled
user_input['topic_0_from_two'] = 0    # Placeholder for topic_0_from_two

# Predict matches when the user submits the form
if st.button("Find Matches"):
    # Convert user input to a DataFrame
    user_input_df = pd.DataFrame([user_input])
    
    # Ensure the DataFrame has all the required columns in the correct order
    required_columns = [
        'female', 'age_scaled', 'single', 'height_scaled', 'orientation_bisexual', 
        'orientation_gay', 'orientation_straight', 'education_type_college_univ', 
        'education_type_grad_or_professional_edu', 'education_type_not_disclosed', 
        'education_type_two_year_college_or_less', 'education_status_graduated', 
        'education_status_not_disclosed', 'education_status_working', 'speaks_english', 
        'speaks_spanish', 'speaks_other', 'diet_type_vegetarian', 'has_dogs_yes', 
        'no_of_kids_more_than_one', 'no_of_kids_one', 'text_length_scaled', 'topic_0_from_two'
    ]
    
    # Reindex the DataFrame to match the required columns and fill missing values with 0
    user_input_df = user_input_df.reindex(columns=required_columns, fill_value=0)
    
    # Call your prediction function
    top_5_similar_people = predict_similar_people(user_input_df)
    
    # Display the bios of the top 5 matches
    st.write("### Top 5 Most Similar People:")
    for i, bio in enumerate(top_5_similar_people['bio'], start=1):
        st.write(f"#### Match {i}")
        st.write(bio)  # Display the bio as a single block of text
        st.write("---")  # Add a separator between bios