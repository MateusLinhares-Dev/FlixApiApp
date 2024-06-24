import streamlit as st
import plotly.express as px
from movies.service import MovieService

def show_home():
    service_movie = MovieService()
    movie_stats = service_movie.get_movie_stats()
    st.title('Estatísticas de Filmes')
    
    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Genêro')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes cadastrados: ')
    st.write(movie_stats['total_movies'])

    st.subheader('Quantidade de Filmes por Gênero:')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliações cadastradas: ')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média geral de estrelas nas avaliações: ')
    st.write(movie_stats['total_reviews'])