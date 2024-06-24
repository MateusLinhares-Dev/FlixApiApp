import streamlit as st
import requests
from login.service import logout

class ActorRepository:

    def __init__(self):
        self.__base_url = 'https://linhares23342teste.pythonanywhere.com/api/v1/'
        #concatenção ou interpolaçao
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }
    
    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_actors(self, actors):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actors,
        )
        if response.status_code == 201:
            return response.json
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao registrar os dados. Status code: {response.status_code}')
        