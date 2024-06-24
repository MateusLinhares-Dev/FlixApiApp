import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService


def show_genres():
    genre_services = GenreService()
    genres = genre_services.get_genres()
    
    if genres:
        st.write('Lista de Gêneros: ')
        genres_df = pd.json_normalize(genres)
        
        AgGrid(data=genres_df,
            reload_data=True,
            key='genres_grid',

            )#Atualizaros  dados reload_data para cada vez a tela atualizar, atualizar os dados também
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Cadastrar novo gênero')

    if st.button('Cadastrar'):
        new_genre = genre_services.create_genres(
            name=name,
        )
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')
