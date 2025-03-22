import os
import pandas as pd
from amooora.ml_logic.data import clean_text_data
from amooora.ml_logic.preprocessor import preprocess_texts, vectorize_texts
from amooora.ml_logic.images import retrieve_images
from colorama import Fore, Style

def clean_and_preprocess() -> None:
    # 0. Get data from CSV
    PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    filename = os.path.join(PROJECT_FOLDER, "raw_data", "okcupid_profiles.csv")
    df = pd.read_csv(filename)

    # 1. Clean texts
    cleaned_df = clean_text_data(df)

    # 2. Preprocessing texts
    clean_preprocessed_df = preprocess_texts(cleaned_df)
    print(clean_preprocessed_df.columns)
    print(clean_preprocessed_df)

    # 3. Add text_length columns
    clean_preprocessed_df['text_length'] = clean_preprocessed_df.combined_preprocessed.str.len()
    print(clean_preprocessed_df.columns)

    print(Fore.MAGENTA + f"\n ⭐️ #vectorize_texts: running" + Style.RESET_ALL)
    # 4. Vectorize texts
    combined_weighted_words = vectorize_texts(clean_preprocessed_df)
    print(Fore.MAGENTA + f"\n ⭐️ #vectorize_texts: DONE ✅" + Style.RESET_ALL)
    print(combined_weighted_words)

    # 5. Train and save model

    # recommend

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
