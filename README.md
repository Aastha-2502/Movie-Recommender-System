## Movie Recommendation System

This project is a content-based movie recommendation system designed to suggest movies based on user input. The system utilizes the TMDB 5000 Movie Dataset, sourced from Kaggle. 
By leveraging TF-IDF vectorisation, the system converts movie descriptions into numerical vectors to determine the similarity between movies. 
This approach enables the recommendation of movies that are most similar to the ones liked by the user. 
The front-end of the application is built using Streamlit, providing a user-friendly interface for input and displaying recommendations.

To use the application, ensure you have Python 3.x installed along with the required libraries. 
Once the environment is set up, you can run the application using the command streamlit run app.py in the terminal. 
This will launch the Streamlit interface, where you can input your favorite movies and receive recommendations. 
The combination of content-based filtering and TF-IDF vectorisation ensures accurate and relevant movie suggestions based on the user’s preferences.
