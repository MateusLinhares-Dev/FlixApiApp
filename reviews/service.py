from reviews.repository import ReviewRepository
import streamlit as st

class ReviewService:

    def __init__(self):
        self.review_repository = ReviewRepository()
    
    def get_review(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews
    
    def create_review(self, movie, stars, comment):
        #tratamento dos dados, transformando sua tipagem para dict -> objeto
        review = dict(
            movie=movie,
            stars=stars,
            comment=comment,
        )
        new_review = self.review_repository.create_reviews(review=review)
        st.session_state.reviews.append(new_review)
        return new_review
