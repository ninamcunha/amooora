import os
import pandas as pd
import numpy as np
from amooora.ml_logic.data import clean_text_data
from amooora.ml_logic.preprocessor import preprocess_texts, preprocess_text_length
from amooora.ml_logic.images import retrieve_images
from amooora.ml_logic.registry import load_model, load_vectorizer
from amooora.ml_logic.model import predict_similar_people

from colorama import Fore, Style

def clean_and_preprocess(user_input_df: pd.DataFrame) -> None:
    # 1. Clean texts
    cleaned_df = clean_text_data(user_input_df)

    # 2. Preprocessing texts
    clean_preprocessed_df = preprocess_texts(cleaned_df)

    # 3. Add text_length columns ( FUNCTION PREPROCESSING TEXT_LENGTH)
    clean_preprocessed_df = preprocess_text_length(clean_preprocessed_df)

    print(clean_preprocessed_df.columns)

    # Load vectorizer fitted with the whole DS
    vectorizer = load_vectorizer()
    print(vectorizer)

    print(Fore.MAGENTA + f"\n ⭐️ #vectorize_texts: running" + Style.RESET_ALL)
    # 4. Vectorize texts
    combined_weighted_words = vectorizer.transform(clean_preprocessed_df.combined_preprocessed.values)
    print(Fore.MAGENTA + f"\n ⭐️ #vectorize_texts: DONE ✅" + Style.RESET_ALL)

    # 5. load model
    # loading LDA Model
    lda_model = load_model()
    print(lda_model)
    # Model da nina usa o primeiro topic ou o mais bem sucedido

    # Transform essays into topics
    print(Fore.MAGENTA + f"\n ⭐️ #lad model running" + Style.RESET_ALL)
    document_topic_mixture = lda_model.transform(combined_weighted_words)
    print(Fore.MAGENTA + f"\n ⭐️ lda model DONE ✅" + Style.RESET_ALL)

    print(document_topic_mixture)

    # recommend (predict)
    # LDA + MODELO DA NINA
    # Antes de enviar para predição
    # precisamos incluir
    # text_length_scaled
    #=> já está dentro do dataFrame pq foi incluido no #preprocess_text_length
    user_input_df['text_length_scaled'] = clean_preprocessed_df.text_length_scaled

    # Quanto que o texto esta dentro do topic_0_from_two
    # incluir topic_0_from_two no DataFrame
    # => document_topic_mixture[0]
    user_input_df['topic_0_from_two'] = document_topic_mixture[0][0]

    user_input_df = user_input_df.drop(columns=['essay0', 'essay1', 'essay2', 'essay3', 'essay4', 'essay5', 'essay6', 'essay7', 'essay8', 'essay9'])
    print(user_input_df.columns)
    print(user_input_df.topic_0_from_two)

    top_5 = predict_similar_people(user_input_df)

    # Get image from recommendation
    print(Fore.MAGENTA + f"\n ⭐️ #retrieve_images: running" + Style.RESET_ALL)

    ids = np.array(top_5.index)

    print(ids)

    print(top_5.bio)

    for idx in ids:
        message = retrieve_images(idx)
        print(message)

    print(Fore.MAGENTA + f"\n ⭐️ #retrieve images: DONE ✅" + Style.RESET_ALL)
    # match_1	match_2	match_3	match_4	match_5
    # 0	22670	36389	4295	44270	136
    # 1	36507	26895	58469	39768	55205
    # 2	50006	48841	12933	46852	42873
    # 3	7635	3356	48076	7123	28862
    # 4	109	4427	23631	33688	40679



if __name__ == '__main__':

    df = pd.DataFrame(
        {
        'age_scaled': 23,
        'height_scaled': 1.75,
        'female': 1,
        'single': 1,
        'orientation_bisexual': 0,
        'orientation_gay': 0,
        'orientation_straight': 1,
        'diet_type_vegetarian': 0,
        'education_type_college_univ': 0,
        'education_type_grad_or_professional_edu': 0,
        'education_type_two_year_college_or_less': 0,
        'education_status_graduated': 1,
        'education_status_working': 0,
        'speaks_english': 1,
        'speaks_spanish': 1,
        'speaks_portuguese': 0,
        'speaks_other': 0,
        'has_dogs_yes': 1,
        'no_of_kids_more_than_one': 0,
        'no_of_kids_one': 0,
        'education_type_not_disclosed': 0,
        'education_status_not_disclosed': 0,
        "essay0":"I would love to think that I was some kind of intellectual...",
        "essay1":"Currently working as an international agent for an NGO...",
        "essay2":"I'm really good at listening and being there for my friends. I'm very dependable, honest and a great communicator.",
        "essay3":"My eyes are the first thing people notice when they look and my sense of humor is what they notice when they talk to me.",
        "essay4":"I'm die hard christopher moore fan. I don't really watch a lot of tv unless there is humor involved. I'm kind of stuck on 90's alternative music. I'm pretty much a fan of everything though...I do need to draw a line at most types of electronica.",
        "essay5":"hot chocolate, running, a good meal, a good read, stimulating conversation, time alone to recharge, laughter, hope.... maybe 8 things...",
        "essay6":"my mind is always being distracted by planning some adventure out of the city, creating music and international travel.",
        "essay7":"having dinner and drinks with friends and/or working",
        "essay8":"when i was a kid i thought steven segal was really cool. please don't judge me.",
        "essay9":"you want to be swept off your feet! you are tired of the norm. you want to catch a coffee or a bite. or if you want to talk philosophy."
        },
        index=[0]
    )

    clean_and_preprocess(df)
    # try:
    #     # preprocess_and_train()
    #     preprocess()
    #     train()
    #     pred()
    # except:
    #     import sys
    #     import traceback

    #     import ipdb
    #     extype, value, tb = sys.exc_info()
    #     traceback.print_exc()
    #     ipdb.post_mortem(tb)



# GUARDAR AS INFORMAÇÔES DOS USUARIOS QUE FOREM USANDO


#        female  age_scaled  single  height_scaled  ...  text_length_scaled  topic_0_from_two                                                bio  cluster
# 6366        1    1.000000       1       0.423077  ...            0.007868          0.500000  69 years old woman, currently single. Zodiac s...      204
# 3872        1    0.901961       1       0.384615  ...            0.431129          0.644636  64 years old woman, currently single. Zodiac s...      204
# 17344       1    0.862745       1       0.307692  ...            0.132345          0.670186  62 years old woman, currently single. Zodiac s...      204
# 3837        1    0.862745       1       0.153846  ...            0.150704          0.842800  62 years old woman, currently single. Zodiac s...      204
# 11738       1    0.843137       1       0.346154  ...            0.333283          0.668358  61 years old woman, currently single. Zodiac s...      204
