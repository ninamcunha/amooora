import os
import pandas as pd

def retrieve_images(id: int) -> None:
    # load okcupid csv
    PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    filename = os.path.join(PROJECT_FOLDER, "raw_data", "okcupid_profiles.csv")
    df = pd.read_csv(filename)
    # find row matching id
    recommendation_row = df.iloc[id]
    # read age
    recommendation_age = recommendation_row.age
    # read sex
    recommendation_sex = recommendation_row.sex
    # retrieve image matching age and sex

    ## load images CSV
    filename_img = os.path.join(PROJECT_FOLDER, "raw_data", "output_images_ages_adjusted.csv")
    images_df = pd.read_csv(filename_img).dropna()

    ## create age min and age max from range
    images_df[['age_min', 'age_max']] = images_df['age'].str.extract(r'\((\d+)-(\d+)\)').astype(int)

    ## filter rows to have only row between recommendation age
    valid_rows = images_df[(images_df['age_min'] <= recommendation_age) & (images_df['age_max'] >= recommendation_age)]

    # convert m to male and f to female to match dataframe
    if recommendation_sex == 'm':
        recommendation_sex = 'male'

    if recommendation_sex == 'f':
        recommendation_sex = 'female'

    # filter rows to have only row with recommendation sex
    valid_rows = valid_rows[(valid_rows['gender'] == recommendation_sex)]

    # select a random row
    if not valid_rows.empty:
        selected_row = valid_rows.sample(n=1).iloc[0]
        print(f"Picture selected randomly based on sex: {recommendation_sex} and age: {recommendation_age}")
        print(f"image path is: {selected_row.image_path}")
    else:
        print("No matching row found.")

    return f"Recommendation age is {recommendation_age}\nRecommendation sex is {recommendation_sex}"



# ids = [22670, 36389, 4295, 44270, 136]
# for idx in ids:
#     message = retrieve_images(idx)
#     print(message)

# # match_1	match_2	match_3	match_4	match_5
# # 0	22670	36389	4295	44270	136
# # 1	36507	26895	58469	39768	55205
# # 2	50006	48841	12933	46852	42873
# # 3	7635	3356	48076	7123	28862
# # 4	109	4427	23631	33688	40679
