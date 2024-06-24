from movies.repository import MovieRepository
import streamlit as st

class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()
    
    def get_movie(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies
    
    def create_movie(self, title, realase_date, genre, actors, resume):
        #tratamento dos dados, transformando sua tipagem para dict -> objeto
        movie = dict(
            title=title,
            realase_date=realase_date,
            genre=genre,
            actors=actors,
            resume=resume
        )
        new_movie = self.movie_repository.create_movies(movie=movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_moves_stats()