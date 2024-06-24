import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from actors.service import ActorService

def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes: ')
        actors_df = pd.json_normalize(actors)
        AgGrid(actors_df,
            reload_data=True,
            key='actors_grid',

            )#Atualizaros  dados reload_data para cada vez a tela atualizar, atualizar os dados também
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Cadastrar novo Ator/Atriz')
    birthday = st.date_input(label='Data de nascimento',
                             value=datetime.today(),
                             min_value=datetime(1600, 1, 1).date(),
                             max_value=datetime.today(),
                             format='DD/MM/YYYY',
                             )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actors = actor_service.create_actors(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actors:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o(a) Ator/Atriz, verifique os campos!')
        