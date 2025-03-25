import os
import pandas as pd
import numpy as np
from PIL import Image

def retrieve_images(id: int) -> None:
    print(f"id dentro de retrieve images: {id}")
    # load okcupid csv
    PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    filename = os.path.join(PROJECT_FOLDER, "raw_data", "ok_stream_with_age.csv")
    df = pd.read_csv(filename)
    # find row matching id
    recommendation_row = df.iloc[id]
    # read age
    recommendation_age = recommendation_row.age
    print(recommendation_age)
    # ONLY FEMALE!
    # read sex
    # recommendation_sex = recommendation_row.sex
    # retrieve image matching age and sex

    ## load images CSV
    filename_img = os.path.join(PROJECT_FOLDER, "raw_data", "unique_female.csv")
    images_df = pd.read_csv(filename_img).dropna()

    images_df = images_df.drop_duplicates(subset='image_path')

    ## create age min and age max from range
    images_df[['age_min', 'age_max']] = images_df['age'].str.extract(r'\((\d+)-(\d+)\)').astype(int)

    ## filter rows to have only row between recommendation age
    valid_rows = images_df[(images_df['age_min'] <= recommendation_age) & (images_df['age_max'] >= recommendation_age)]

    # # convert m to male and f to female to match dataframe
    # if recommendation_sex == 'm':
    #     recommendation_sex = 'male'

    # if recommendation_sex == 'f':
    #     recommendation_sex = 'female'

    # filter rows to have only row with recommendation sex
    # valid_rows = valid_rows[(valid_rows['gender'] == 'female')]

    # select a random row
    if not valid_rows.empty:
        selected_row = valid_rows.sample(n=1).iloc[0]
        print(f"Picture selected randomly based age: {recommendation_age}")
        print(f"image path is: {selected_row.image_path}")
    else:
        print("No matching row found.")

    return selected_row.image_path



def recommendation_images(image_path: str):
    # Acessar a imagem no caminho correto
    PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # filename = os.path.join(PROJECT_FOLDER, "female_images", "flamengo-flag.jpg")
    filename = os.path.join(PROJECT_FOLDER, 'raw_data', 'human_faces', image_path)
    # image_path = '../../female_images/flamengo-flag.jpg'

    if not os.path.exists(filename):
        return 'FILE DOES NOT EXIST!!!'

    ## abrir a imagem usando PIL
    # assim vai conseguir ser interpretado pelo numpy
    image = Image.open(filename)

    #  covert pra um ndarray nauqelas 3 dimensoes das aulas
    # image_array = np.array(image)
    # breakpoint()

    return image
    # retornar o numpy array

# recommendation_images()
