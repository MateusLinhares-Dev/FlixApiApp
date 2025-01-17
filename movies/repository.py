import streamlit as st
import requests
from login.service import logout

class MovieRepository:

    def __init__(self):
        self.__base_url = 'https://linhares23342teste.pythonanywhere.com/api/v1/'
        self.__movie_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }
    
    def get_movies(self):
        response = requests.get(
            self.__movie_url,
            headers=self.__headers,
        )
        print(response)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_movies(self, movie):
        response = requests.post(
            self.__movie_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao registrar os dados. Status code: {response.status_code}')
    
    def get_moves_stats(self):
        response = requests.get(f'{self.__movie_url}stats/',
                               headers=self.__headers,
                               )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. status code: {response.status_code}')