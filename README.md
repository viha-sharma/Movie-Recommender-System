# Movie Recommender System

## Project Objective

A content based recommender system provides recommendations based on the similarity of content between two itmes, in this project's case- two movies. 

The recommender uses natural language processing and cosine similarity to determine and generate 5 movie recommendations based on a selected movie. The TMDB API has been used to extract additional information about the 5000 movies in the TMDB database. 

The user interface of the website is displayed below:

<img width="1280" alt="image" src="https://user-images.githubusercontent.com/106082126/208078054-10c4f1f7-a9bb-4ef1-aa7e-ac45aca658d1.png">

Each movie recommendation includes the movie title, poster, overview, release date, rating, cast, director, keywords, genres, budget and revenue. 

<img width="1026" alt="image" src="https://user-images.githubusercontent.com/106082126/208078151-1d698d33-c34f-47d5-a462-e5dac697184f.png">

---

## Technologies used

1. Pandas
2. Streamlit
3. Requests
4. Pickle


## Steps to run my website on your local server:

(i) Ensure you run the ipynb file to obtain the similarity.pkl file and put it in the same folder as other files.   
(ii) Open your anaconda command prompt and run the following lines of code:  

-> cd <folder path>

(iii) install all the libraries mentioned in the requirements.txt file using pip.    
(iv) to open the website, enter this code in your terminal

-> streamlit run app.py



