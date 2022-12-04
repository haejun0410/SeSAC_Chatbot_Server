import streamlit as st
from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('preg_help_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

def chatbot_response(user_response):
    user_input = user_response
    embedding = model.encode(user_input)
    df['similarity'] = df['embedding'].map(lambda x: cosine_similarity([embedding],[x]).squeeze())
    answer = df.loc[df['similarity'].idxmax()]
    return answer['챗봇']
