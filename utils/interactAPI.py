import json, urllib2
from urllib2 import Request, urlopen, URLError

moviedb = urllib2.urlopen('https://api.themoviedb.org/3/search/movie?api_key=0c28ca3c9002dc1725a0f55971a73b4b&language=en-US&query=Avatar&page=1&include_adult=false')
json.load(urllib2.urlopen(moviedb)


try:
	response = urlopen(request)
	movies = response.read()
	print movies
except URLError, e:
    print 'Movie not found. Got an error code:', e
