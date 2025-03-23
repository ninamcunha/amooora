import streamlit as st
import pandas as pd
from predict_matches import predict_similar_people  # Import the prediction function
import os


# Change the working directory to the folder containing app.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set page config (MUST BE THE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="Amooora: a world of belonging and freedom", layout="wide")

# Custom CSS to change the color of selected elements to purple
st.markdown(
    """
    <style>
    /* Change the color of selected radio buttons */
    div[role="radiogroup"] > label > div:first-child {
        background-color: purple !important;
        border-color: purple !important;
    }

    /* Change the color of selected checkboxes */
    div.stCheckbox > label > div:first-child {
        background-color: purple !important;
        border-color: purple !important;
    }

    /* Ensure the checkbox color is applied correctly */
    div.stCheckbox > div > div > div > div {
        background-color: purple !important;
        border-color: purple !important;
    }

    /* Change the color of selected toggle buttons */
    div[role="button"] > div:first-child {
        background-color: purple !important;
        border-color: purple !important;
    }

    /* Change all markdown headers to purple */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: purple !important;
    }

    /* Top navigation bar styling */
    .stButton button {
        background: none !important;
        border: none !important;
        color: purple !important;
        font-size: 16px;
        font-weight: bold;
        padding: 0 !important;
        margin-right: 20px;
        cursor: pointer;
    }
    /* Remove hover effect */
    .stButton button:hover {
        background: none !important;
        color: purple !important;
    }
    /* Ensure no hover effect on the span inside the button */
    .stButton button:hover span {
        color: purple !important;
    }

    /* Custom checkbox style */
    div.stCheckbox > div > div > div > div {
        background-color: purple !important;
        border-color: purple !important;
    }
    div.stCheckbox > div > div > div > div > div > svg {
        color: white !important;  /* Change tick color to white */
        fill: white !important;
    }

    /* Adjust the width of input fields and their containers */
    div.stTextInput > div > div > input,
    div.stNumberInput > div > div > input {
        width: 200px !important;  /* Adjust this value as needed */
        max-width: 100% !important;  /* Ensure it doesn't overflow */
    }
    /* Reduce the container width */
    div.stTextInput > div > div,
    div.stNumberInput > div > div {
        width: fit-content !important;  /* Make the container fit the input width */
        padding-right: 0 !important;  /* Remove extra padding */
    }
    /* Remove extra white space around the input fields */
    div.stTextInput > div,
    div.stNumberInput > div {
        width: fit-content !important;  /* Make the parent container fit the content */
        padding-right: 0 !important;  /* Remove extra padding */
    }

    /* Adjust column layout to reduce spacing */
    div.stColumn > div {
        padding: 0 !important;  /* Remove padding in columns */
        margin: 0 !important;  /* Remove margins in columns */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS to centering content of the page
st.markdown(
    """
    <style>
    /* Center the whole page content */
    .block-container {
        max-width: 900px;  /* Adjust width as needed */
        margin: auto;
    }

    /* Ensure form inputs stay aligned */
    .stTextInput, .stNumberInput, .stRadio, .stSelectbox, .stCheckbox {
        width: 100% !important; /* Ensures full width inside columns */
    }

    /* Prevent radio buttons and checkboxes from being centered */
    div[data-baseweb="radio"] {
        display: flex !important;
        justify-content: flex-start !important;
    }

    /* Keep columns properly aligned */
    .stColumns {
        display: flex;
        justify-content: center;
    }

    /* Adjust margins for better spacing */
    .stRadio > div, .stCheckbox > div, .stSelectbox > div, .stNumberInput > div {
        margin-bottom: 5px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Connections"
    
# Custom CSS to center the navigation menu and page content
st.markdown(
    """
    <style>
    /* Center the navigation menu */
    .stButton button {
        display: inline-block;
        margin: 0 auto;
        text-align: center;
        width: 100%;
    }

    /* Ensure page content is left-aligned */
    .block-container {
        max-width: 900px;  /* Adjust width as needed */
        margin: auto;
        text-align: left;  /* Keep text left-aligned */
    }

    /* Ensure form inputs stay aligned */
    .stTextInput, .stNumberInput, .stRadio, .stSelectbox, .stCheckbox {
        width: 100% !important; /* Ensures full width inside columns */
    }

    /* Prevent radio buttons and checkboxes from being centered */
    div[data-baseweb="radio"] {
        display: flex !important;
        justify-content: flex-start !important;
    }

    /* Keep columns properly aligned */
    .stColumns {
        display: flex;
        justify-content: center;
    }

    /* Adjust margins for better spacing */
    .stRadio > div, .stCheckbox > div, .stSelectbox > div, .stNumberInput > div {
        margin-bottom: 5px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)  
# Navigation Menu
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Connections"):
        st.session_state.page = "Connections"
with col2:
    if st.button("About"):
        st.session_state.page = "About"
with col3:
    if st.button("Methodology"):
        st.session_state.page = "Methodology"
with col4:
    if st.button("The Team"):
        st.session_state.page = "The Team"
        
if st.session_state.page == "Connections":
    st.image(os.path.join(current_dir, "..", "images", "0_colagem_header_2.jpg"), width=700)
elif st.session_state.page == "About":
    st.image(os.path.join(current_dir, "..", "images", "1_colagem_astro.jpg"), width=700)
elif st.session_state.page == "Methodology":
    st.image(os.path.join(current_dir, "..", "images", "2_servicos.jpg"), width=700)
elif st.session_state.page == "The Team":
    st.image(os.path.join(current_dir, "..", "images", "3_colagem_suporte.jpg"), width=700)
elif st.session_state.page == "Contact Us":
    st.image(os.path.join(current_dir, "..", "images", "contato.jpg"), width=700)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Connections"

# Connections Page
if st.session_state.page == "Connections":
    # Title of the app
    st.write("### Join our community and meet 5 people who share your vibe.", unsafe_allow_html=True)

    # Initialize an empty dictionary to store user inputs
    user_input = {}

    # Create two columns for the form
    col1, col2, col3 = st.columns(3)

    # Column 1
    with col1:
        
        # Name field (not used for analysis)
        user_input['name'] = st.text_input("Name")

        # Create two columns for Age and Height
        age_col, height_col = st.columns(2)  # Two equal-width columns

        # Age (scaled) in the first column
        with age_col:
            user_input['age_scaled'] = st.number_input("Age", min_value=18, max_value=100, value=30)

        # Height (scaled) in the second column
        with height_col:
            user_input['height_scaled'] = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, value=1.75, step=0.01)

        # Gender
        gender_options = ["Male", "Female", "Non-Binary", "Transgender", "Other"]
        selected_gender = st.radio("Gender", gender_options)
            
        # Recode gender as female (1) or male (0)
        if selected_gender in ["Female", "Non-Binary", "Transgender", "Other"]:
            user_input['female'] = 1  # Recode as female
        else:
            user_input['female'] = 0  # Recode as male
        
        # Relationship Status
        user_input['single'] = st.radio("Relationship Status", ["Single", "In a Relationship"])
        user_input['single'] = 1 if user_input['single'] == "Single" else 0 
            
    # Column 2
    with col2:
        
        # Orientation
        orientation = st.radio("Orientation", ["Bisexual", "Gay", "Straight"])
        user_input['orientation_bisexual'] = 1 if orientation == "Bisexual" else 0
        user_input['orientation_gay'] = 1 if orientation == "Gay" else 0
        user_input['orientation_straight'] = 1 if orientation == "Straight" else 0

        # Diet Type
        diet_type = st.radio("Diet Type", ["Vegetarian", "Non-Vegetarian"])
        user_input['diet_type_vegetarian'] = 1 if diet_type == "Vegetarian" else 0


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

    
    # Column 3
    with col3:
    
    # Initialize session state for checkboxes
        if "english_checked" not in st.session_state:
            st.session_state.english_checked = False  # Default to checked
        if "spanish_checked" not in st.session_state:
            st.session_state.spanish_checked = False
        if "portuguese_checked" not in st.session_state:
            st.session_state.portuguese_checked = False
        if "other_checked" not in st.session_state:
            st.session_state.other_checked = False
     
        # Languages Spoken
        # Languages Spoken
        st.write("Languages Spoken:")

        # Custom HTML checkboxes with session state
        st.markdown(
            f"""
            <style>
            .custom-checkbox {{
                display: flex;
                align-items: center;
                margin-bottom: 10px;
            }}
            .custom-checkbox input {{
                display: none;
            }}
            .custom-checkbox label {{
                position: relative;
                padding-left: 25px;
                cursor: pointer;
            }}
            .custom-checkbox label:before {{
                content: "";
                position: absolute;
                left: 0;
                top: 0;
                width: 18px;
                height: 18px;
                border: 2px solid purple;
                border-radius: 4px;
                background: white;
            }}
            .custom-checkbox input:checked + label:before {{
                background: purple;
            }}
            .custom-checkbox input:checked + label:after {{
                content: "✓";
                position: absolute;
                left: 4px;
                top: 2px;
                color: white;
                font-size: 14px;
            }}
            </style>

            <div class="custom-checkbox">
                <input type="checkbox" id="english" {"checked" if st.session_state.english_checked else ""}>
                <label for="english">English</label>
            </div>
            <div class="custom-checkbox">
                <input type="checkbox" id="spanish" {"checked" if st.session_state.spanish_checked else ""}>
                <label for="spanish">Spanish</label>
            </div>
            <div class="custom-checkbox">
                <input type="checkbox" id="portuguese" {"checked" if st.session_state.portuguese_checked else ""}>
                <label for="portuguese">Portuguese</label>
            </div>
            <div class="custom-checkbox">
                <input type="checkbox" id="other" {"checked" if st.session_state.other_checked else ""}>
                <label for="other">Other</label>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Update user_input dictionary
        user_input['speaks_english'] = int(st.session_state.english_checked)
        user_input['speaks_spanish'] = int(st.session_state.spanish_checked)
        user_input['speaks_portuguese'] = int(st.session_state.portuguese_checked)
        user_input['speaks_other'] = int(st.session_state.other_checked)

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

    # New Section: Tell us a little bit more about yourself
    st.write("### Tell us a little bit more about yourself")

    # Create two columns for the new text fields
    col4, col5, col6 = st.columns(3)

    # Column 3
    with col4:
        user_input['hobby_1'] = st.text_input("What is your favorite hobby?")
        user_input['hobby_2'] = st.text_input("What is your second favorite hobby?")
        user_input['hobby_3'] = st.text_input("What is your third favorite hobby?")

    # Column 5
    with col5:
        user_input['movie_genre'] = st.text_input("What is your favorite movie genre?")
        user_input['music_genre'] = st.text_input("What is your favorite music genre?")
        user_input['travel_destination'] = st.text_input("What is your dream travel destination?")
        
    # Column 6
    with col6:
        user_input['book_genre'] = st.text_input("What is your favorite book genre?")
        user_input['sport'] = st.text_input("What is your favorite sport?")
        user_input['food'] = st.text_input("What is your favorite food?")

    # Add placeholders for essay variables
    for i in range(10):
        user_input[f'essay{i}'] = ""  # Placeholder for essay variables

        
    # Custom CSS to center the button
    # Add a unique class to the "Find Connections" button
    st.markdown(
        """
        <style>
        /* Center the "Find Connections" button */
        div.stButton > button {
            display: block;
            margin: 0 auto;
            font-size: 20px !important; /* Adjust font size */
            font-weight: bold !important; /* Make text bold */
            padding: 12px 24px !important; /* Adjust padding */
            border-radius: 10px !important; /* Optional: rounded corners */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    
    # Predict matches when the user submits the form
    if st.button("Find Connections"):
        # Convert user input to a DataFrame
        user_input_df = pd.DataFrame([user_input])
        
        # Ensure the DataFrame has all the required columns in the correct order
        required_columns = [
            'female', 'age_scaled', 'single', 'height_scaled', 'orientation_bisexual', 
            'orientation_gay', 'orientation_straight', 'education_type_college_univ', 
            'education_type_grad_or_professional_edu', 'education_type_not_disclosed', 
            'education_type_two_year_college_or_less', 'education_status_graduated', 
            'education_status_not_disclosed', 'education_status_working', 'speaks_english', 
            'speaks_spanish', 'speaks_portuguese', 'speaks_other', 'diet_type_vegetarian', 
            'has_dogs_yes', 'no_of_kids_more_than_one', 'no_of_kids_one', 'text_length_scaled', 
            'topic_0_from_two', 'hobby_1', 'hobby_2', 'hobby_3', 'movie_genre', 'music_genre', 
            'travel_destination', 'book_genre', 'sport', 'food', 'essay0', 'essay1', 'essay2', 
            'essay3', 'essay4', 'essay5', 'essay6', 'essay7', 'essay8', 'essay9'
        ]
        
        # Reindex the DataFrame to match the required columns and fill missing values with 0
        user_input_df = user_input_df.reindex(columns=required_columns, fill_value=0)
        
        # Call your prediction function
        top_5_similar_people = predict_similar_people(user_input_df)
        
        # Display the bios of the top 5 matches
        st.write("### Meet Your Top 5 Community Connections:")
        for i, bio in enumerate(top_5_similar_people['bio'], start=1):
            st.write(f"#### Connection {i}")
            st.write(bio)  # Display the bio as a single block of text
            st.write("---")  # Add a separator between bios


# About Page
elif st.session_state.page == "About":
    st.write("## About Amooora and the project")
    st.write("""
    Amooora is a transformative platform designed to create a world of belonging and freedom, with a focus on the LGBTQ+ community in Brazil. 
    It serves as a safe and inclusive space for cisgender women, bisexual individuals, transgender people, and non-binary individuals to find visibility, representation, and meaningful connections. 
    Our mission is to empower this vibrant community by offering high-quality content, information, and services created by and for them.
    
    Amooora fills a critical gap by uniting the Brazilian lesbian community, which has long lacked a dedicated platform for connection and specialized resources. 
    Through features like a community map, users can discover and connect with others who share their interests and values. 
    The platform also acts as a marketplace, enabling women to offer or access professional services—from legal and psychological support to creative and technical expertise—creating a trusted network for growth and collaboration.
    
    For this specific project, we use a dataset from OkCupid to explore innovative ways of creating meaningful connections. 
    By analyzing patterns and similarities within the data, we aim to develop a model that fosters genuine relationships within the community. 
    For more details on our approach, please refer to the Methodology section.
    
    More than just a platform, Amooora is a movement celebrating diversity and fostering authentic connections. 
    By joining us, you become part of a community that empowers individuals to live freely and find their place in the world. 
    Together, we can build a future where everyone belongs.
    """)

# Methodology Page
# Methodology Page
elif st.session_state.page == "Methodology":
    st.write("## Methodology")
        
    st.write("""
    For this project, we worked with the **OK Cupid dataset**, which contains nearly **60,000 observations** and **31 columns** of user profile information. 
    The dataset, available on [Kaggle](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles/code), includes details such as demographics, interests, and personal preferences. 
    Since the dataset does not include information about user interactions or matches, we explored a **deep learning model** to suggest meaningful connections based on **similarity**. 
    Our goal was to create a robust model that could effectively group users with shared characteristics and interests.
    """)

    st.write("### Model Exploration")
    st.write("""
    We began by evaluating three clustering models to determine the best approach for grouping users based on similarity. The models explored were:
    1. **K-Nearest Neighbors (KNN)**
    2. **K-Means Clustering**
    3. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

    The performance of each model was assessed using metrics such as **Silhouette Score**, **Inertia (SSE)**, **Davies-Bouldin Index**, and others. Below is a comparison of the models:
    """)

    model_comparison_data = {
        "Model": ["KNN", "KMeans", "DBSCAN"],
        "Silhouette ↑": [None, 0.2378, 0.6175],
        "Inertia (SSE) ↓": [64639.9396, 64639.9396, None],
        "Davies-Bouldin ↓": [None, 1.5695, 0.5893],
        "Calinski-Harabasz ↑": [None, 6963.6418, 1832.8004],
        "MAD ↓": [0.1525, None, None],
        "MaxD ↓": [1.7614, None, None],
        "MinD ↓": [0.0000, None, None],
        "Score (Lower is Better)": [5, 6, 4]
    }
    model_comparison_df = pd.DataFrame(model_comparison_data)
    st.dataframe(model_comparison_df, use_container_width=True)

    st.write("""
    ##### Best Model:
    1️⃣ **Model 3 (DBSCAN)** – Best overall, with the highest Silhouette score and lowest Davies-Bouldin score.  
    2️⃣ **Model 2 (KMeans)** – A solid choice, though with lower performance than DBSCAN.  
    3️⃣ **Model 1 (KNN)** – The least favorable based on clustering metrics (e.g., no Silhouette or Davies-Bouldin score).
    """)

    st.write("### Text Column Reduction")
    st.write("""
    To handle the text columns in the dataset, we applied **Latent Dirichlet Allocation (LDA)** for topic modeling. 
    This approach reduced the dimensionality of the text data by identifying key topics within user profiles. 
    We compared several text reduction methods to determine the most effective approach:
    """)

   # Table 2: Text Reduction Model Comparison
    text_reduction_data = {
        "Model": [
            "Text KMeans Cluster", "Therapist", "General", "5 LDA Topics", "2 LDA Topics", 
            "PCA SDV", "PCA Word2Vec", "PCA TF-IDF"
        ],
        "Silhouette ↑": [0.1844, 0.1686, 0.1982, 0.1453, 0.2209, 0.2060, 0.2075, 0.2060],
        "Inertia (SSE) ↓": [101693.6377, 100305.4067, 81460.9735, 95745.2212, 67059.5664, 72612.6824, 70680.4075, 72613.2315],
        "Davies-Bouldin ↓": [1.7407, 2.1442, 1.8188, 2.1358, 1.5017, 1.6309, 1.7744, 1.6309],
        "Calinski-Harabasz ↑": [9744.4874, 4654.6152, 5482.3137, 4626.3059, 6683.6448, 5854.6708, 6234.4083, 5854.6146],
        "AMD ↓": [0.1773, 0.1835, 0.1543, 0.2095, 0.1647, 0.1683, 0.1404, 0.1683],
        "Score (Lower is Better)": [5, 7, 6, 8, 1, 3, 4, 4]
    }
    text_reduction_df = pd.DataFrame(text_reduction_data)
    st.dataframe(text_reduction_df, use_container_width=True)

    st.write("""
    ##### **Best Models:**
    1️⃣ **Model 5 (2 LDA Topics)** – Best overall with the highest Silhouette score, a moderate Davies-Bouldin score, and relatively low AMD.  
    2️⃣ **Model 6 (PCA SDV)** – Solid second choice with a good balance of performance and lower AMD compared to the others.  
    3️⃣ **Model 7 (PCA Word2Vec)** – Strong contender with a slight increase in Silhouette and lower AMD than other models.  
    4️⃣ **Model 8 (PCA TF-IDF)** – Same performance as Model 7, but more consistent.
    """)

    st.write("### Feature Selection Process")
    st.write("""
    To optimize the model, we conducted a thorough feature selection process. We started by adding features one by one and evaluating their impact on the model's performance. Below is a summary of the results:""")
    
    st.write("##### Feature Inclusion One-by-One")

# Create a DataFrame for the table
    data = {
    "Model": [
        "Model 1: First LDA Topic only", "Model 2: Adding LDA 2 Topics", "Model 3: Adding Age",
        "Model 4: Adding Single", "Model 5: Adding Gender", "Model 6: Adding Orientation",
        "Model 7: Adding Body Type", "Model 8: Adding Diet Type", "Model 9: Adding Drink",
        "Model 10: Adding Has Kids", "Model 11: Adding Wants Kids", "Model 12: Adding Has Dog",
        "Model 13: Adding Likes Dog", "Model 14: Adding Likes Cat", "Model 15: Adding Religion",
        "Model 16: Adding Smokes"
    ],
    "Silhouette ↑": [0.5358, 0.5340, 0.3392, 0.3561, 0.4059, 0.4214, 0.4919, 0.2924, 0.1905, 0.1375, 0.1022, 0.0787, 0.1049, 0.0835, 0.0825, 0.0702],
    "Inertia (SSE) ↓": [22.4772, 44.2808, 626.4378, 916.2438, 1646.2831, 4042.7787, 23761.3141, 54981.2490, 86119.1756, 108120.9289, 125245.3447, 139426.0870, 155476.2675, 192555.5129, 234397.6699, 260182.5113],
    "Davies-Bouldin ↓": [0.5047, 0.5072, 0.8347, 0.8427, 0.7757, 0.8159, 1.1433, 1.4925, 2.0949, 2.1793, 2.2350, 2.4819, 2.3097, 2.6658, 2.9154, 3.0105],
    "Calinski-Harabasz ↑": [495648.7711, 503201.5262, 48362.3012, 54818.5556, 75799.0390, 47682.7808, 14937.8450, 6980.5454, 4341.3648, 3869.3748, 3566.3926, 3256.4672, 3367.3100, 3084.4088, 2680.5108, 2407.7145],
    "AMD ↓": [0.0000, 0.0000, 0.0014, 0.0022, 0.0037, 0.0063, 0.0192, 0.0364, 0.0774, 0.1267, 0.1921, 0.2513, 0.3092, 0.4575, 0.7785, 0.9226],
    "Score (Lower is Better)": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    "Best Model Consideration": [
        "Best Overall (Best Silhouette & low AMD)", "Second Best (Good LDA performance)",
        "Not Recommended (Lower Silhouette)", "Not Recommended (Lower Silhouette & higher AMD)",
        "Solid Option (Balanced performance)", "Good Option (Strong Silhouette)",
        "Not Recommended (High Davies-Bouldin & AMD)", "Not Recommended (Low Silhouette & High Davies-Bouldin)",
        "Not Recommended (Low Silhouette & High Davies-Bouldin)", "Not Recommended (Low Silhouette & High Davies-Bouldin)",
        "Not Recommended (Low Silhouette & High Davies-Bouldin)", "Not Recommended (Low Silhouette & High Davies-Bouldin)",
        "Not Recommended (Low Silhouette & High Davies-Bouldin)", "Not Recommended (Low Silhouette & High Davies-Bouldin)",
        "Not Recommended (Low Silhouette & High Davies-Bouldin)", "Not Recommended (Low Silhouette & High Davies-Bouldin)"
    ],
    "Compare to Previous Model": [
        "N/A", "Silhouette slightly decreased", "Significant drop in Silhouette",
        "Silhouette and AMD worsened", "Silhouette increased, AMD lower",
        "Good improvement in Silhouette", "Silhouette increased, but high Davies-Bouldin",
        "Significant drop in Silhouette and high Davies-Bouldin", "Significant drop in Silhouette, High Davies-Bouldin",
        "Silhouette decreased, Davies-Bouldin increased", "Significant drop in Silhouette, High Davies-Bouldin",
        "Further drop in Silhouette, High Davies-Bouldin", "Drop in Silhouette and higher Davies-Bouldin",
        "Silhouette slightly improved, but Inertia and Davies-Bouldin worsened",
        "Silhouette decreased, Davies-Bouldin worsened", "Further decrease in Silhouette, Davies-Bouldin worsened, AMD increased"
    ],
    "Recommendation": [
        "Keep (Strong performance)", "Keep (Still strong)", "Remove (Negative impact)",
        "Remove (Negative impact)", "Keep (Positive effect)", "Keep (Positive effect)",
        "Remove (Negative impact)", "Remove (Negative impact)", "Remove (Negative impact)",
        "Remove (Negative impact)", "Remove (Negative impact)", "Remove (Negative impact)",
        "Remove (Negative impact)", "Remove (Negative impact)", "Remove (Negative impact)",
        "Remove (Negative impact)"
    ]
}

# Convert to DataFrame
    df = pd.DataFrame(data)

# Display the table using st.dataframe
    st.dataframe(df, use_container_width=True)
    
    st.write("### Final Model and Features")
    st.write("""
    After extensive testing, we selected **DBSCAN** as our best-performing model, combined with **2 LDA topics** for text reduction. 
    The final model uses a combination of features including gender, age, relationship status, 
   height, sexual orientation, education level and status, languages spoken, dietary preferences, pet ownership,  number of children, text length of open ended questions, and the dominant topic from the LDA approach.
    This combination of features and the DBSCAN model provided the best balance of clustering quality and interpretability, ensuring meaningful connections for users.
    """)


# The Team Page
elif st.session_state.page == "The Team":
    st.write("## Meet the amazing team behind the project:")
    
        # Custom CSS to adjust image alignment
    st.markdown(
        """
        <style>
        .team-image {
            margin-top: 20px;  /* Adjust this value to move the image down */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write("---")  # Add a separator between team members

    # Function to check if file exists
    def check_file_exists(file_path):
        if not os.path.exists(file_path):
            st.error(f"File not found: {file_path}")
            st.error(f"Current working directory: {os.getcwd()}")
            st.error(f"Files in directory: {os.listdir()}")
            return False
        return True

    # Nina Menezes Cunha
    col1, col2 = st.columns([1, 4])  # Adjust column widths (1:3 ratio)
    with col1:
        nina_image_path = os.path.join(current_dir, "..", "images", "img_nina.png")  # Direct path (same folder as app.py)
        if check_file_exists(nina_image_path):
            st.image(nina_image_path, width=200)  # Adjust width as needed
    with col2:
        st.write("### Nina Menezes Cunha")
        st.write("""
        Nina Menezes Cunha is a data scientist with over a decade of experience in machine learning, causal inference, and impact evaluation. 
        She holds a Ph.D. in Economics of Education from Stanford University and has expertise in predictive modeling, A/B testing, and big data analytics. 
        In the U.S., she worked as a Senior Researcher at FHI 360 and consulted for the World Bank, contributing to peer-reviewed research and global projects. 
        She has led data-driven policy research, built scalable data solutions, and collaborated with international organizations. 
        After returning to Brazil, she founded Amooora, a startup focused on products and services for the lesbian community. 
        She recently completed the Data Science Bootcamp at Le Wagon, further strengthening her expertise in AI and data science. 
        Passionate about using data for social good, she is committed to leveraging AI for meaningful impact.
        """)

    st.write("---")  # Add a separator between team members

    # Thais Felipelli
    col3, col4 = st.columns([1, 4])  # Adjust column widths (1:3 ratio)
    with col3:
        thais_image_path = os.path.join(current_dir, "..", "images", "img_thais.jpeg")  # Direct path (same folder as app.py)
        if check_file_exists(thais_image_path):
            st.image(thais_image_path, width=200)  # Adjust width as needed
    with col4:
        st.write("### Thais Felipelli")
        st.write("""
        Thais Felipelli is a mechatronics engineer with experience in software development, specializing in Laboratory Information Management Systems (LIMS) 
        to automate processes and enable data-driven decision-making. After earning an MBA from MIT, she transitioned into venture capital, 
        playing a key role in developing and founding startups such as Evino. Combining a passion for math and technology, 
        she completed the Data Science Bootcamp at Le Wagon, furthering her expertise in AI and data science.
        """)

    st.write("---")  # Add a separator between team members

    # André Menezes
    col5, col6 = st.columns([1, 4])  # Adjust column widths (1:3 ratio)
    with col5:
        andre_image_path = os.path.join(current_dir, "..", "images", "img_andre.jpeg")  # Direct path (same folder as app.py)
        if check_file_exists(andre_image_path):
            st.image(andre_image_path, width=200)  # Adjust width as needed
    with col6:
        st.write("### André Menezes")
        st.write("""
        André Menezes has a diverse professional background, spanning civil engineering, economics, social communication, and the events industry 
        before transitioning into tech. After completing the Web Development course at Le Wagon, he discovered a passion for coding and quickly 
        joined the school as a Teacher Assistant. He was soon promoted to Teacher and later took on the role of Batch Manager, supporting students 
        and overseeing program operations. With a growing interest in data science, he completed Le Wagon’s Data Science Bootcamp to expand his 
        expertise in AI and data-driven product development.
        """)