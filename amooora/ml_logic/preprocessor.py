import pandas as pd
import nltk
from colorama import Fore, Style
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from amooora.utils import simple_time_and_memory_tracker
from amooora.ml_logic.registry import load_text_length_scaler

@simple_time_and_memory_tracker
def preprocess_texts(df: pd.DataFrame) -> pd.DataFrame:
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    def basic_preprocessing(sentence):
        tokenized_sentence = word_tokenize(sentence) ## tokenize

        stop_words = set(stopwords.words('english')) ## define stopwords

        tokenized_sentence_cleaned = [ ## remove stopwords
            w for w in tokenized_sentence if not w in stop_words
        ]

        lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos = "v")
            for word in tokenized_sentence_cleaned
        ]

        # 2 - Lemmatizing the nouns
        noun_lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos = "n")
            for word in lemmatized
        ]

        cleaned_sentence = ' '.join(word for word in noun_lemmatized)


        return cleaned_sentence

    print(Fore.MAGENTA + f"\n ⭐️ #preprocess_texts: running" + Style.RESET_ALL)

    clean_preprocessed_df = df['combined_clean'].apply(basic_preprocessing)
    print(Fore.MAGENTA + f"\n ⭐️ #preprocess_texts: DONE ✅" + Style.RESET_ALL)

    new_names = dict(
        combined_clean="combined_preprocessed"
    )
    clean_preprocessed_df = clean_preprocessed_df.to_frame().rename(columns=new_names)
    return clean_preprocessed_df

@simple_time_and_memory_tracker
def vectorize_texts(df: pd.DataFrame) -> pd.DataFrame:
    tf_idf_vectorizer = TfidfVectorizer(min_df=0.1, ngram_range=(1,2))

    # Training it on the texts
    combined_weighted_words = pd.DataFrame(tf_idf_vectorizer.fit_transform(df.combined_preprocessed.values).toarray(),
                    columns = tf_idf_vectorizer.get_feature_names_out())

    return tf_idf_vectorizer


def preprocess_text_length(df: pd.DataFrame) -> pd.DataFrame:
    df['text_length'] = df.combined_preprocessed.str.len()

    # Scaled min max text-length
    # load text_length_scaler

    # Clip values above the 99th percentile
    upper_threshold = df['text_length'].quantile(0.99)
    df['text_length_clipped'] = df['text_length'].clip(upper=upper_threshold)

    scaler = load_text_length_scaler()

    df['text_length_scaled'] = scaler.fit_transform(df[['text_length_clipped']])

    return df
