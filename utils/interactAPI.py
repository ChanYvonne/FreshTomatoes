import urllib2
import json

tmdb=open("tmdb.txt", "r")
tmdb_key = tmdb.read()[:-1]
tmdb.close()

def get_ids(query, type): #takes search input and gets corresponding ids that match with the movie/actor
    if(type == 'm'):
        url="http://api.themoviedb.org/3/search/movie?api_key=%s&query=%s&page=1"%(tmdb_key, query.replace(" ", "%20"))
    else:
        url="http://api.themoviedb.org/3/search/person?api_key=%s&query=%s&page=1"%(tmdb_key, query.replace(" ", "%20"))
    j = json.loads(urllib2.urlopen(url).read())
    ids = []
    for res in j['results']:
        ids += [res['id']]
    if len(ids) < 20:
        return ids
    else:
        return ids[:20]


def get_search_details_m(ids): #takes movie search ids and returns the corresponding movies
    info = []
    for id in ids:
        url="http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, tmdb_key)
        j = json.loads(urllib2.urlopen(url).read())
        movie = [j['title'], j['release_date'][0:4], id, j['poster_path']]
        info += [movie]
    return info


def get_search_details_a(ids): #takes actor ids and returns the movies he/she is in or affiliated with
    for id in ids:
        url="https://api.themoviedb.org/3/person/%d/movie_credits?api_key=%s&language=en-US"%(id, tmdb_key)
        j = json.loads(urllib2.urlopen(url).read())
        movie_ids = []
        for res in j['cast']:
            movie_ids += [res['id']]
    return get_search_details_m(movie_ids)


def get_movie_details(id): #takes id and retrieves info on the specific movie
    url="http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, tmdb_key)
    j = json.loads(urllib2.urlopen(url).read())
    return [j['title'], j['release_date'][:4], j['overview'], j['tagline'], j['poster_path']]


#def get_reviews(query): #to be implemented with nyt API; retrieves the review for the specific movie if available
