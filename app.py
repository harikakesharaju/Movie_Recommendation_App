import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list_df[movies_list_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies:
        movie_id=i[0]
        recommended.append(movies_list_df.iloc[i[0]]['title'])

    return recommended

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list_df = pickle.load(open('movies.pkl', 'rb'))
st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies_list_df['title'].values)

if st.button('Recommend'):
    recommends = recommend(selected_movie)
    for i in recommends:
        st.write(i)
