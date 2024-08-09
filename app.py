import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the movie list and similarity matrix
movies_df = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract movie titles
movies_list = movies_df['title'].values

def recommend(movie):
    # Get the index of the selected movie
    movie_index = np.where(movies_list == movie)[0][0]
    
    # Get similarity scores
    distances = similarity[movie_index]
    
    # Get indices of the top 5 similar movies
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Get the movie titles
    recommended_movies = []
    for i in movie_indices:
        movie_id=i[0]
        recommended_movies.append(movies_list[i[0]])
    
    return recommended_movies

def main():
    st.title("Movie Recommendation System")
    st.subheader("Welcome to the Movie Recommendation System")
    st.text("Here you can find the best movies to watch")
    st.text("We have a collection of movies from different genres")
    st.text("Select a genre and we will recommend you the best movies from that genre")
    st.text("Enjoy the movies!")

    # Dropdown menu for selecting a movie
    selected_movie_name = st.selectbox('Select a movie:', movies_list)
    
    # Recommend button
    if st.button('Recommend'):
        recommendations = recommend(selected_movie_name)
        for movie in recommendations:
            st.write(movie) 

if __name__ == "__main__":
    main()
