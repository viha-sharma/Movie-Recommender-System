import streamlit as st
import pandas as pd
import pickle
import requests

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://wallpaperaccess.com/full/3968079.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()


df = pd.read_csv('movies_info.csv')

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w300/' + data['poster_path']

def fetch_runtime(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return str(data['runtime']) + ' minutes'

def fetch_summary(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return  str(data['overview'])

def fetch_actors(movie_id):
    cast_list = df['cast'][df['movie_id']==movie_id]
    return cast_list

def fetch_director(movie_id):
    director = df['crew'][df['movie_id']==movie_id]
    return director

def fetch_genre(movie_id):
    genre = df['genres'][df['movie_id']==movie_id]
    return genre

def fetch_keywords(movie_id):
    keyword = df['keywords'][df['movie_id']==movie_id]
    return keyword

def release_date(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return (data['release_date'])

def fetch_voting(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return str(data['vote_average'])+ '/10'

def fetch_movie_budget(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'USD ' + str(data['budget'])

def fetch_movie_revenue(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9929fa51f8a285339f1ec596d538b8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'USD ' + str(data['revenue'])

def recommend(movie):
    '''
    provides 5 movie recommendations based on the input movie
    '''
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters=[]
    recommended_movies_runtime = []
    recommended_movie_overview = []
    recommended_movie_actors = []
    recommended_movie_director = []
    recommended_movie_genres = []
    recommended_movie_keywords = []
    recommended_movie_date = []
    recommended_movie_vote = []
    recommended_movie_budget = []
    recommended_movie_revenue = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_runtime.append(fetch_runtime(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_overview.append(fetch_summary(movie_id))
        recommended_movie_actors.append(fetch_actors(movie_id))
        recommended_movie_director.append(fetch_director(movie_id))
        recommended_movie_genres.append(fetch_genre(movie_id))
        recommended_movie_keywords.append(fetch_keywords(movie_id))
        recommended_movie_date.append(release_date(movie_id))
        recommended_movie_vote.append(fetch_voting(movie_id))
        recommended_movie_budget.append(fetch_movie_budget(movie_id))
        recommended_movie_revenue.append(fetch_movie_revenue(movie_id))
    return recommended_movies,recommended_movies_posters, recommended_movies_runtime,recommended_movie_overview, recommended_movie_actors, recommended_movie_director,recommended_movie_genres, recommended_movie_keywords,recommended_movie_date,recommended_movie_vote, recommended_movie_budget, recommended_movie_revenue

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.markdown("<h1 style='text-align: center; color: white;'>Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown(' ')
selected_movie_name = st.selectbox(
    'Which Movie do you want recommendations for?',
    movies['title'].values)

columns = st.columns((2, 1, 2))

if columns[1].button('Recommend'):
    import time

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1) 
    names,posters,runtime, overview, actors, directors,genres, keywords, date, vote, budget, revenue = recommend(selected_movie_name)
    st.write('Top 5 Suggested Movies for {}'.format(selected_movie_name))

    col1, col2, col3, col4, col5 = st.tabs(['1️', '2️', '3️', '4️', '5️'])

    with col1:
        st.header(names[0])
        st.image(posters[0])
        st.success('Overview')
        st.write(overview[0])
        st.info('Release Date')
        st.write(date[0])
        st.info('Rating')
        st.write(vote[0])
        st.info('Runtime')
        st.markdown(runtime[0])
        st.info('Genres')
        st.write(genres[0])
        st.info('Cast Members')
        st.write(actors[0])
        st.info('Director')
        st.write(directors[0])
        st.info('Related Keywords')
        st.write(keywords[0])
        st.info('Movie Budget')
        st.write(budget[0])
        st.info('Box Office (Revenue)')
        st.write(revenue[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])
        st.success('Overview')
        st.write(overview[1])
        st.info('Release Date')
        st.write(date[1])
        st.info('Rating')
        st.write(vote[1])
        st.info('Runtime')
        st.markdown(runtime[1])
        st.info('Genres')
        st.write(genres[1])
        st.info('Cast Members')
        st.write(actors[1])
        st.info('Director')
        st.write(directors[1])
        st.info('Related Keywords')
        st.write(keywords[1])
        st.info('Movie Budget')
        st.write(budget[1])
        st.info('Box Office (Revenue)')
        st.write(revenue[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])
        st.success('Overview')
        st.write(overview[2])
        st.info('Release Date')
        st.write(date[2])
        st.info('Rating')
        st.write(vote[2])
        st.info('Runtime')
        st.markdown(runtime[2])
        st.info('Genres')
        st.write(genres[2])
        st.info('Cast Members')
        st.write(actors[2])
        st.info('Director')
        st.write(directors[2])
        st.info('Related Keywords')
        st.write(keywords[2])
        st.info('Movie Budget')
        st.write(budget[2])
        st.info('Box Office (Revenue)')
        st.write(revenue[2])

    with col4:  
        st.header(names[3])
        st.image(posters[3])
        st.success('Overview')
        st.write(overview[3])
        st.info('Release Date')
        st.write(date[3])
        st.info('Rating')
        st.write(vote[3])
        st.info('Runtime')
        st.markdown(runtime[3])
        st.info('Genres')
        st.write(genres[3])
        st.info('Cast Members')
        st.write(actors[3])
        st.info('Director')
        st.write(directors[3])
        st.info('Related Keywords')
        st.write(keywords[3])
        st.info('Movie Budget')
        st.write(budget[3])
        st.info('Box Office (Revenue)')
        st.write(revenue[3])

    with col5:
        st.header(names[4])
        st.image(posters[4])
        st.success('Overview')
        st.write(overview[4])
        st.info('Release Date')
        st.write(date[4])
        st.info('Rating')
        st.write(vote[4])
        st.info('Runtime')
        st.markdown(runtime[4])
        st.info('Genres')
        st.write(genres[4])
        st.info('Cast Members')
        st.write(actors[4])
        st.info('Director')
        st.write(directors[4])
        st.info('Related Keywords')
        st.write(keywords[4])
        st.info('Movie Budget')
        st.write(budget[4])
        st.info('Box Office (Revenue)')
        st.write(revenue[4])
