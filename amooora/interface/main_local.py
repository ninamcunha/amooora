import os
import pandas as pd
from amooora.ml_logic.data import clean_text_data
from amooora.ml_logic.preprocessor import preprocess_texts, vectorize_texts

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

    # 4. Vectorize texts
    combined_weighted_words = vectorize_texts(clean_preprocessed_df)
    print(combined_weighted_words)

    # 5. Train and save model

    # recommend


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
