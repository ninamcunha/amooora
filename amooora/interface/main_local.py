import os
import pandas as pd
from amooora.ml_logic.data import clean_text_data
from amooora.ml_logic.preprocessor import preprocess_texts, vectorize_texts
from amooora.ml_logic.images import retrieve_images
from amooora.ml_logic.registry import load_model, load_vectorizer
from sklearn.preprocessing import MinMaxScaler

from colorama import Fore, Style

def clean_and_preprocess() -> None:
    # 0. Get data from CSV
    # PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # filename = os.path.join(PROJECT_FOLDER, "raw_data",
    #  "okcupid_profiles.csv")
    # original_df = pd.read_csv(filename)

    df = pd.DataFrame(
        {
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

    # 1. Clean texts
    cleaned_df = clean_text_data(df)

    # 2. Preprocessing texts
    clean_preprocessed_df = preprocess_texts(cleaned_df)
    print(clean_preprocessed_df.columns)
    print(clean_preprocessed_df)

    # 3. Add text_length columns
    clean_preprocessed_df['text_length'] = clean_preprocessed_df.combined_preprocessed.str.len()

    # Scaled min max text-length
    # Clip values above the 99th percentile
    upper_threshold = clean_preprocessed_df['text_length'].quantile(0.99)
    clean_preprocessed_df['text_length_clipped'] = clean_preprocessed_df['text_length'].clip(upper=upper_threshold)
    scaler = MinMaxScaler()
    clean_preprocessed_df['text_length_scaled'] = scaler.fit_transform(clean_preprocessed_df[['text_length_clipped']])
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

    # Get image from recommendation
    print(Fore.MAGENTA + f"\n ⭐️ #retrieve_images: running" + Style.RESET_ALL)

    ids = [22670, 36389, 4295, 44270, 136]
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
    clean_and_preprocess()
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
