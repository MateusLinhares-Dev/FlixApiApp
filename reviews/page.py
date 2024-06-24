import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
import pandas as pd
from reviews.service import ReviewService

def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_review()

    if reviews:
        st.write('Lista de avaliações: ')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(reviews_df,
            reload_data=True,
            key='reviews_grid',

            )#Atualizaros  dados reload_data para cada vez a tela atualizar, atualizar os dados também
    else:
        st.warning('Nenhuma avaliação encontrada')

    st.title('Cadastrar nova avaliação: ')

    # movies_service = MovieService()
    # movies = movies_service.get_movie()
    # movie_title = {movie['title']: movie['id'] for movie in movies}
    # selected_movie_title = st.selectbox('Filme', list(movie_title.keys()))

    stars = st.number_input('Estrelas',
                            min_value=0,
                            max_value=5,
                            step=1,
                            )
    comment = st.text_area(label='Comentário')
    
    # if st.button('Cadastrar'):
    #     new_review = review_service.create_review(movie=movie_title[selected_movie_title],
    #                                               stars=stars,
    #                                               comment=comment
    #                                               )
    #     if new_review:
    #         st.rerun()
    #     else:
    #         st.error('Erro ao cadastrar. Verifique os campos')
