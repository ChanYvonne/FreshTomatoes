import urllib2
import json

tmdb_key="0c28ca3c9002dc1725a0f55971a73b4b"

def get_ids(query):
    url="http://api.themoviedb.org/3/search/movie?api_key=%s&query=%s&page=1"%(tmdb_key, query.replace(" ", "%20"))
    j = json.loads(urllib2.urlopen(url).read())
    ids = []
    for res in j['results']:
        ids += [res['id']]
    return ids

def get_search_details(query):
    ids = get_ids(query)
    info = []
    for id in ids:
        url="http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, tmdb_key)
        j = json.loads(urllib2.urlopen(url).read())
        movie = [j['title'], j['release_date'][0:4], id]
        info += [movie]
    return info

def get_movie_details(id):
    url="http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, tmdb_key)
    j = json.loads(urllib2.urlopen(url).read())
    genres = []
    for genre in j['genres']:
        genres += [genre['name']]
    return [j['title'], j['release_date'][:4], j['overview'], j['tagline'], [genres]]

