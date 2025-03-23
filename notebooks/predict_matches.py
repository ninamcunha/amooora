import pandas as pd
import joblib
import os
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import DBSCAN


# Get the directory containing predict_matches.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths to the model and scaler files
dbscan_path = os.path.join(current_dir, "dbscan_model.pkl")
age_scaler_path = os.path.join(current_dir, "age_scaler.pkl")
height_scaler_path = os.path.join(current_dir, "height_scaler.pkl")

# Load the pre-trained model and scalers
dbscan = joblib.load(dbscan_path)
age_scaler = joblib.load(age_scaler_path)
height_scaler = joblib.load(height_scaler_path)

# Define the path to the dataset
dataset_path = "/Users/nina2012/code/ninamcunha/amooora/raw_data/ok_stream.csv"

# Load the dataset
ok = pd.read_csv(dataset_path)

# Precompute cluster labels for the dataset (using the pre-trained DBSCAN model)
ok_numeric = ok.drop(columns=['bio'])  # Drop the 'bio' column
ok['cluster'] = dbscan.fit_predict(ok_numeric)  # Assign cluster labels

def predict_similar_people(user_input_df):
    """
    Takes a DataFrame of user input and returns the top 5 most similar people from the dataset.
    Uses DBSCAN to find similar people within the same cluster. Falls back to Euclidean distance if the user is in the noise cluster (-1).
    """
    # Ensure the user input has the same columns as the dataset (excluding 'bio')
    user_input_df = user_input_df.reindex(columns=ok_numeric.columns, fill_value=0)
    
    # Exclude the 'bio' column from the similarity calculation (if it exists)
    user_input_numeric = user_input_df  # No need to drop 'bio' since it doesn't exist in user_input_df
    
    # Ensure the columns match
    if not user_input_numeric.columns.equals(ok_numeric.columns):
        raise ValueError("Column mismatch between user input and dataset. Please check the columns.")
    
    # Assign the user input to a cluster by finding the nearest core point in the dataset
    core_point_mask = dbscan.core_sample_indices_  # Indices of core points in the dataset
    core_points = ok_numeric.iloc[core_point_mask]  # Core points in the dataset
    core_labels = ok.iloc[core_point_mask]['cluster']  # Cluster labels of core points
    
    # Calculate distances between the user input and core points
    distances = euclidean_distances(user_input_numeric, core_points)
    nearest_core_index = distances.argmin()  # Find the index of the nearest core point
    user_cluster = core_labels.iloc[nearest_core_index]  # Assign the cluster of the nearest core point
    
    if user_cluster != -1:
        # If the user is in a valid cluster, filter the dataset to include only individuals in the same cluster
        same_cluster = ok[ok['cluster'] == user_cluster]
        
        # Calculate pairwise Euclidean distances between the user input and individuals in the same cluster
        distances = euclidean_distances(user_input_numeric, same_cluster.drop(columns=['bio', 'cluster']))
        
        # Find the top 5 most similar people (excluding self, if applicable)
        similar_indices = distances.argsort(axis=1)[:, :5]  # Get the top 5 for the first row
        top_5_similar_people = same_cluster.iloc[similar_indices[0]]  # Get the top 5 for the first row (including 'bio')
    else:
        # If the user is in the noise cluster (-1), use Euclidean distance on the entire dataset
        distances = euclidean_distances(user_input_numeric, ok_numeric)
        
        # Find the top 5 most similar people (excluding self, if applicable)
        similar_indices = distances.argsort(axis=1)[:, :5]  # Get the top 5 for the first row
        top_5_similar_people = ok.iloc[similar_indices[0]]  # Get the top 5 for the first row (including 'bio')
    
    return top_5_similar_people