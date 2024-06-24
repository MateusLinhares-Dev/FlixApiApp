import streamlit as st
from api.service import Auth

def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )

    if response.get('error'):
        st.error(f'Falha ao realizar login: {response.get("error")}')
    else:
        #session_state.token -> usado para armazenar(atribuir) valores, o token é a variável(propriedade) que é usada para armazenar esse valor e que foi escolhida por nós
        st.session_state.token = response.get('access')
        #rerun é usado para rodar novamente o sistema, como se fosse um f5 para atualizar a tela
        st.rerun

def logout():
    #limpar todas variáveis de ambiente para que não haja nenhuma variável do token armazenada
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun