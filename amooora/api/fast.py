import io
import pandas as pd
from fastapi import FastAPI, Response
from amooora.interface.main_local import clean_and_preprocess
from amooora.ml_logic.images import recommendation_images, retrieve_images
app = FastAPI()


# /recommend

@app.get("/")
def root():
    return {
        'PROJECT': "AMOOORA!!!"
    }


@app.get("/recommend")
def recommend(
        age_scaled: int,
        height_scaled: float,
        female: int,
        single: int,
        orientation_bisexual: int,
        orientation_gay: int,
        orientation_straight: int,
        diet_type_vegetarian: int,
        education_type_college_univ: int,
        education_type_grad_or_professional_edu: int,
        education_type_two_year_college_or_less: int,
        education_status_graduated: int,
        education_status_working: int,
        speaks_english: int,
        speaks_spanish: int,
        speaks_portuguese: int,
        speaks_other: int,
        has_dogs_yes: int,
        no_of_kids_more_than_one: int,
        no_of_kids_one: int,
        education_type_not_disclosed: int,
        education_status_not_disclosed: int,
        essay0: str,
        essay1: str,
        essay2: str,
        essay3: str,
        essay4: str,
        essay5: str,
        essay6: str,
        essay7: str,
        essay8: str,
        essay9: str,
    ):
    """
    Make 5 recommendations
    """
    X = dict(
        age_scaled=age_scaled,
        height_scaled=height_scaled,
        female=female,
        single=single,
        orientation_bisexual=orientation_bisexual,
        orientation_gay=orientation_gay,
        orientation_straight=orientation_straight,
        diet_type_vegetarian=diet_type_vegetarian,
        education_type_college_univ=education_type_college_univ,
        education_type_grad_or_professional_edu=education_type_grad_or_professional_edu,
        education_type_two_year_college_or_less=education_type_two_year_college_or_less,
        education_status_graduated=education_status_graduated,
        education_status_working=education_status_working,
        speaks_english=speaks_english,
        speaks_spanish=speaks_spanish,
        speaks_portuguese=speaks_portuguese,
        speaks_other=speaks_other,
        has_dogs_yes=has_dogs_yes,
        no_of_kids_more_than_one=no_of_kids_more_than_one,
        no_of_kids_one=no_of_kids_one,
        education_type_not_disclosed=education_type_not_disclosed,
        education_status_not_disclosed=education_status_not_disclosed,
        essay0=essay0,
        essay1=essay1,
        essay2=essay2,
        essay3=essay3,
        essay4=essay4,
        essay5=essay5,
        essay6=essay6,
        essay7=essay7,
        essay8=essay8,
        essay9=essay9,
    )
    X_pred = pd.DataFrame(X, index=[0])
    recommendations = clean_and_preprocess(X_pred).to_dict()

    return {
        'recommendations': recommendations
    }


@app.get('/images')
def images(id_0: int, id_1: int, id_2: int, id_3: int, id_4: int):
    print("!!!! RODANDO API ENDPOINT !!!!")

    # usar retrieve images para enviar o id e receber o file path


    dict_to_return = {}

    for i, idx in enumerate([id_0, id_1, id_2, id_3, id_4]):
        image_path = retrieve_images(idx)
        image = recommendation_images(image_path)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")  # Change format if needed (PNG, JPEG, etc.)
        img_bytes.seek(0)
        # dict_to_return[f'id_{i}'] = img_bytes.getvalue()
        dict_to_return[f'id_{i}'] = Response(content=img_bytes.getvalue(), media_type="image/png")

    # print(dict_to_return)

    # if image is None:
    #     return Response(content="Image not found", status_code=404)

    # img_bytes = io.BytesIO()
    # image.save(img_bytes, format="PNG")  # Change format if needed (PNG, JPEG, etc.)
    # img_bytes.seek(0)

    # return Response(content=img_bytes.getvalue(), media_type="image/png")

    # return {
        # id_0: Response(content=img_bytes.getvalue(), media_type="image/png")
    # }

    return dict_to_return['id_0']
