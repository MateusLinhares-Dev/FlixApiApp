import requests


class Auth:

    def __init__(self):
        #Boa prática usar dois dunders para métodos que iremos utilizar na própria classe somente
        #propriedade e métodos usados somente dentro da classe, recomenda utilizar dois dunders
        self.__base_url = 'https://linhares23342teste.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_paylod = {
            'username':username,
            'password':password
        }

        auth_response = requests.post(
            self.__auth_url,
            data=auth_paylod
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}