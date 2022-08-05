import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,director,keywords,duration,genres,rating,year,imdb_score'
)

def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)
    
    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    # for md in movies_list:
    #     m = MovieResult(**md)
    #         # imdb_code=md.get('imdb_code'),
    #         # title=md.get('title'),
    #         # director=md.get('director'),
    #         # keywords=md.get('keywords'),
    #         # duration=md.get('duration'),
    #         # genres=md.get('genres'),
    #         # rating=md.get('rating', 0),
    #         # year=md.get('year', 0),
    #         # imdb_score=md.get('imdb_score', 0.0),
    #     movies.append(m)
    movies.sort(key=lambda m: -m.year)
    return movies


