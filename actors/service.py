from actors.repository import ActorRepository
import streamlit as st

class ActorService:

    def __init__(self):
        self.actors_repository = ActorRepository()
    
    def get_actors(self):
         #verifica se já foi feito a requisição para actors, se for somente retorna a sessão já salva
        if 'actors' in st.session_state:
            return st.session_state.actors
        
        actors = self.actors_repository.get_actors()
        st.session_state.actors = actors
        return actors
    
    def create_actors(self, name, birthday, nationality):
        #tratamento dos dados, transformando sua tipagem para dict -> objeto
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        new_actor = self.actors_repository.create_actors(actors=actor)
        st.session_state.actors.append(new_actor)
        return new_actor
