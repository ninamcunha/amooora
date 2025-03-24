import os
import glob
import pickle
from pathlib import Path

from colorama import Fore, Style

def load_vectorizer():
    """
    Load vectorizer already fitted with all the original texts
    """
    # load
    with open('pkl/tf_idf_vectorizer.pkl', 'rb') as f:
        tfidf_vec = pickle.load(f)
    return tfidf_vec

def load_model(): # o que retorna aqui?
    """
    Return saved model:

    Return None (but do not Raise) if no model is found
    """

    # define model path
    model_filepath = Path("pkl/model.pkl")
    print(Fore.BLUE + f"\nLoad latest model from local registry (pkl folder)..." + Style.RESET_ALL)


    # check if there is a file at MODEL_LOCATION
    if not model_filepath.is_file():
        print(f"❌ There is no file at {model_filepath}")
    # Return none if there is no file
        return None

    # Return model if there is a file
    with open(model_filepath, 'rb') as f:
        lda = pickle.load(f)

    print("✅ Model loaded from local disk")

    return lda


load_model()
