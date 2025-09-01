import streamlit as st
import pickle 
import pandas as pd
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values.tolist()

similarity_matrix = pickle.load(open('similarity_matrix.pkl','rb'))

def recommended_movie(movie):
   recommend = []
   idx = movies_list.index(movie)
   distances = similarity_matrix[idx]
   movie_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]
   for i in movie_list:
    recommend.append(movies_list[i[0]])
   return recommend


st.title('Movies Recommender System')
movie_name = st.selectbox("Choose a Movie",movies_list)

if st.button('Submit'):
   recommendations = recommended_movie(movie_name)
   for movie in recommendations:
     st.write(movie) 