# FreshTomatoes

A site that is essentially the google of movies! Users can:
  -search for any movie they like or have heard of to obtain information about it
  -search for specifc actors they follow and research what movies that actor is in
  -have profiles and accounts where they can save their movies, document their favorite genre and movie of all time, and edit the information as time goes on

If users are feeling adventurous, they can also click the "I'm feeling bored" button to discover a random movie to watch that may or may not be intereting.

Enjoy and feel free to bingewatch some movies!


#BUGS you may encounter
* When displaying a movie page (you are most likely to encounter this error when clicking the "I'm feeling bored" button searching for a random movie; when you use the search feature and access a movie through there it is most likely because you had a movie in mind and that movie is most likely not going to have these errors):
 * If the title, blurb, or quote has a unicode character that can't be translated into ASCII (usually stuff in other languages), the movie page won't load
 * We're unclear why, but certain titles don't get parsed correctly by the get_link() function in interactAPI.py. When we trace out the same calls made by get_link in the python shell, everything works fine - the NYT API is able to access the info the get_link() fxn tries to access. But, for some reason, in these cases the get_link() fxn itself is throwing an error.