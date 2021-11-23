import json
import requests

key = 'e036d8d25b5f3b5440fdc48155cc4e11'
pages = range(1, 21)

genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=ko-KR'.format(key)


genres = requests.get(genre_url).text
genre_data = json.loads(genres)
data_dict = []
for genre in genre_data["genres"]:
    data = {
        "model": "movies.genre",
        "pk": genre["id"],
        "fields": {
            "name": genre["name"]
        }
    }
    data_dict.append(data)

for page in pages:
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key={}&language=ko-KR&page={}'.format(key, page)
    content = requests.get(URL).text
    datas = json.loads(content)
    for data in datas["results"]:
        movie_data = {
            "model": "movies.movie",
            "fields": {
                "title": data["title"],
                "release_date": data["release_date"],
                "popularity": data["popularity"],
                "vote_count": data["vote_count"],
                "vote_average": data["vote_average"],
                "overview": data["overview"],
                "poster_path": data["poster_path"],
                "genres": data["genre_ids"] 
            }
        }
        data_dict.append(movie_data)




with open("data.json", "w") as f:
    json.dump(data_dict, f)