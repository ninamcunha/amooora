import pandas as pd
import joblib
import os
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import DBSCAN

# --- Constants ---
FEATURES_TO_KEEP = [
    'age_scaled',
    'single',
    'height_scaled',
    'education_type_college_univ',
    'education_type_grad_or_professional_edu',
    'education_type_not_disclosed',
    'education_type_two_year_college_or_less',
    'education_status_graduated',
    'education_status_not_disclosed',
    'education_status_working',
    'speaks_english',
    'speaks_spanish',
    'speaks_other',
    'diet_type_vegetarian',
    'has_dogs_yes',
    'no_of_kids_more_than_one',
    'no_of_kids_one',
    'text_length_scaled',  # Note: Check spelling consistency in your data
    'topic_0_from_two'
]

# Get the directory containing predict_matches.py
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Define paths to the model and scaler files in the "pkl" folder
dbscan_path = os.path.join(current_dir, "..", "..", "pkl", "dbscan_model.pkl")  # Updated path
age_scaler_path = os.path.join(current_dir, "..", "..", "pkl", "age_scaler.pkl")  # Updated path
height_scaler_path = os.path.join(current_dir, "..", "..", "pkl", "height_scaler.pkl")  # Updated path

# Load the pre-trained model and scalers
dbscan = joblib.load(dbscan_path)
age_scaler = joblib.load(age_scaler_path)
height_scaler = joblib.load(height_scaler_path)

# Define the path to the dataset
dataset_path = os.path.join(current_dir, "..", "..", "raw_data", "ok_stream_demo_day.csv")  # Updated path

# --- Data Preparation ---
ok = pd.read_csv(dataset_path)

# Verify all features exist in the dataset
missing_features = [f for f in FEATURES_TO_KEEP if f not in ok.columns]
if missing_features:
    raise ValueError(f"Missing features in dataset: {missing_features}")

ok_numeric = ok[FEATURES_TO_KEEP].copy()
ok['cluster'] = dbscan.fit_predict(ok_numeric)

# --- Main Function ---
def predict_similar_people(user_input_df):
    """
    Returns top 5 most similar profiles
    Args:
        user_input_df: DataFrame containing user profile data
    Returns:
        DataFrame with top 5 similar profiles including their bios
    """
    # 1. Filter and validate input
    missing_input_features = [f for f in FEATURES_TO_KEEP if f not in user_input_df.columns]
    if missing_input_features:
        raise ValueError(f"Missing features in input: {missing_input_features}")

    user_input_numeric = user_input_df[FEATURES_TO_KEEP].copy()

    # 2. Debug checks
    print("=== Shape Verification ===")
    print(f"User input shape: {user_input_numeric.shape} (should be (1, 19))")
    print(f"Dataset shape: {ok_numeric.shape} (should be (N, 19))")

    # 3. Cluster assignment
    core_samples = ok_numeric.iloc[dbscan.core_sample_indices_]
    distances = euclidean_distances(user_input_numeric, core_samples)
    nearest_core_idx = distances.argmin()
    user_cluster = ok.iloc[dbscan.core_sample_indices_]['cluster'].iloc[nearest_core_idx]

    # 4. Find similar profiles
    if user_cluster != -1:  # If in a cluster
        cluster_members = ok[ok['cluster'] == user_cluster]
        comparison_features = cluster_members[FEATURES_TO_KEEP]
    else:  # Noise point - compare to all
        comparison_features = ok_numeric

    distances = euclidean_distances(user_input_numeric, comparison_features)
    top_5_indices = distances.argsort(axis=1)[0, :5]  # Get top 5 for first row

    # Return full profiles (including bio) of top matches
    return ok.iloc[top_5_indices]
