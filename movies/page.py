import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
import pandas as pd
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService

def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movie()

    if movies:
        st.write('Lista de Filmes: ')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors','genres.id'])

        AgGrid(movies_df,
            reload_data=True,
            key='movies_grid',

            )#Atualizaros  dados reload_data para cada vez a tela atualizar, atualizar os dados também
    else:
        st.warning('Nenhum filme encontrado!')

    st.title('Cadastrar novo Filme')

    name = st.text_input('Titulo')
    realease_date = st.date_input(label='Data de lançamento',
                             value=datetime.today(),
                             min_value=datetime(1800, 1, 1).date(),
                             max_value=datetime.today(),
                             format='DD/MM/YYYY',
                             )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_name = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_name.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actor_name = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actor_name]

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=name,
            realase_date=realease_date,
            genre=genre_name[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')

       
