import pandas as pd
import numpy as np
import string
from colorama import Fore, Style

def access_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Acces just text columns by their name.
    Columns must be named: 'essay0' up to 'essay9'
    """
    print(Fore.MAGENTA + "\n ⭐️ #access_text_columns: running" + Style.RESET_ALL)
    text_df = df.loc[
        :,
        ['essay0',
        'essay1',
        'essay2',
        'essay3',
        'essay4',
        'essay5',
        'essay6',
        'essay7',
        'essay8',
        'essay9']
    ]
    print(Fore.MAGENTA + "\n ⭐️ #access_text_columns: DONE ✅" + Style.RESET_ALL)
    return text_df

def replace_nan_by_empty_string(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace all empty essays by an empty string ('').
    """
    print(Fore.MAGENTA + "\n ⭐️ #replace_nan_by_empty_string: running" + Style.RESET_ALL)
    text_df = access_text_columns(df)
    no_nan_df = text_df.replace(np.nan, '')
    print(Fore.MAGENTA + "\n ⭐️ #replace_nan_by_empty_string: DONE ✅" + Style.RESET_ALL)
    return no_nan_df

def combine_all_texts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine all essays responses into one new column called `combined`

    return a DataFrame
    """
    print(Fore.MAGENTA + "\n ⭐️ #combine_all_texts: running" + Style.RESET_ALL)
    no_nan_df = replace_nan_by_empty_string(df)
    no_nan_df['combined'] = no_nan_df.apply(
        lambda row: ' '.join(row.values.astype(str)), axis=1
    )
    print(Fore.MAGENTA + "\n ⭐️ #combine_all_texts: DONE ✅" + Style.RESET_ALL)
    return no_nan_df


def clean_text_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw text data.
    Remove whitespaces, remove numbers, remove punctuations and lowercase texts

    return DataFrame with columns: `essayN_clean` + `combined_clean`
    """
    def basic_cleaning(sentence):
        # Basic cleaning
        sentence = sentence.strip() # remove whitespaces
        sentence = sentence.lower() # lowercase
        sentence = ''.join(char for char in sentence if not char.isdigit()) # remove numbers

        # Advanced cleaning
        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, '')

        return sentence

    cleaned_df = pd.DataFrame()

    print(Fore.MAGENTA + "\n ⭐️ #clean_text_data: running" + Style.RESET_ALL)
    # Criar Novas colunas essayN_clean
    no_nan_df = combine_all_texts(df)
    essays = no_nan_df.columns[:10]
    for essay in essays:
        print(Fore.MAGENTA + f"\n ⭐️ cleaning {essay}: running" + Style.RESET_ALL)
        cleaned_df[f"{essay}_clean"] = no_nan_df[essay].apply(basic_cleaning)
        print(Fore.MAGENTA + f"\n ⭐️ cleaning {essay}: DONE ✅" + Style.RESET_ALL)

    print(Fore.MAGENTA + f"\n ⭐️ cleaning combined: running" + Style.RESET_ALL)
    # Create new column combined_clean
    cleaned_df['combined_clean'] = no_nan_df.combined.apply(basic_cleaning)
    print(Fore.MAGENTA + f"\n ⭐️ cleaning combined: DONE ✅" + Style.RESET_ALL)

    print(Fore.MAGENTA + "\n ⭐️ #clean_text_data: DONE ✅" + Style.RESET_ALL)

    return cleaned_df



# CODE TO TEST THIS FILE!!!
# MUST BE REMOVED!

# import os
# print(os.path.dirname(__file__))
# root_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# df = pd.read_csv(root_folder + '/raw_data/okcupid_profiles.csv')

# clean_df = clean_text_data(df)
# print(clean_df.columns)
