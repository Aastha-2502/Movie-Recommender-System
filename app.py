import streamlit as st
import os
import time
from data_preprocessing import load_data, load_cosine_matrix
from recommender import get_recommendations

@st.cache_data
def memorized_load_data(file_path):
    return load_data(file_path)

@st.cache_resource
def memorized_load_cosine_matrix(file_path_model):
    return load_cosine_matrix(file_path_model)

def main():
    st.header('Movie Recommender System')

    start_time = time.time()
    with st.spinner('Loading data...'):
        package_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(package_dir, 'movies.csv')
        data = memorized_load_data(file_path)
    st.write(f"Data loaded in {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    with st.spinner('Loading similarity matrix...'):
        file_path_sim = os.path.join(package_dir, 'cosine_matrix.pkl')
        cosine_sim = memorized_load_cosine_matrix(file_path_sim)
    st.write(f"Similarity matrix loaded in {time.time() - start_time:.2f} seconds")

    movies_list = [''] + list(data['title'].values)
    movie = st.selectbox('Enter Movie Title', movies_list)

    if st.button('Get Recommendations'):
        if movie:
            start_time = time.time()
            with st.spinner('Fetching recommendations...'):
                recommendations, posters = get_recommendations(movie, cosine_sim, data)
                cols = st.columns(5)

                for col, recommend, poster in zip(cols, recommendations, posters):
                    with col:
                        st.write(recommend)
                        if poster:
                            st.image(poster, use_column_width=True)
                        else:
                            st.write('Poster not available')
            st.write(f"Recommendations fetched in {time.time() - start_time:.2f} seconds")
        else:
            st.warning('Please select a movie')

if __name__ == '__main__':
    main()
