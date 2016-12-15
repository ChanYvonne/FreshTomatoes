# FreshTomatoes

Installations/programs needed (you probably already have this):
sqlite3
bootstrap
jquery

A site that is essentially the google of movies! Users can:
  -search for any movie they like or have heard of to obtain information about it
  -search for specifc actors they follow and research what movies that actor is in
  -have profiles and accounts where they can save their movies, document their favorite genre and movie of all time, and edit the information as time goes on

If users are feeling adventurous, they can also click the "I'm feeling bored" button to discover a random movie to watch that may or may not be intereting.

Enjoy and feel free to bingewatch some movies!


## Bugs, Limitations, etc
* We have limited the movie language to English because some languages (e.g., Swedish, Arabic, Russian) were throwing weird errors with Unicode characters and Python's inability to convert them to ASCII -- we didn't want these errors impeding the user experience so we just took away foreign films altogether.
* Some Unicode characters (like the joined ellipses ...) still throw errors, so watch out for those.

## For The Future
* We wanted to implement an actor search but doing so became more involved than we thought it would be, so we had to "discontinue" the feature (it is commented out).
* Since we have rudimentary profiles and "list" pages, if we were to take this project further, we might implement a social aspect where people can make friends, view each other's lists, etc.