# FreshTomatoes

### Installations/programs needed (you probably already have this):
* sqlite3
* bootstrap
* jquery

## Features
* Register and login
* Click on "I'm feeling bored" for a random movie suggestion
* Search for a keyword in a movie title
* Click on a movie to view information about it
 * Read a review of the movie in The New York Times (for many, but not all)
 * Add this movie to "your list"
* Click on "My List" to view your list and remove movies from it

## Bugs, Limitations, etc
* We have limited the movie language to English because some languages (e.g., Swedish, Arabic, Russian) were throwing weird errors with Unicode characters and Python's inability to convert them to ASCII -- we didn't want these errors impeding the user experience so we just took away foreign films altogether.
* Some Unicode characters (like the joined ellipses ...) still throw errors, so watch out for those.
* Not all of the styling envisioned in the site map (e.g., image, TMDB API data, NYT API data laid out side-by-side) was implemented.
* There are some random HTML errors that don't persist (i.e., adding a certain movie will throw an error the first time you try it and then not throw it the second time) and we're not quite sure why.

## For The Future
* We wanted to implement an actor search but doing so became more involved than we thought it would be, so we had to "discontinue" the feature (it is commented out).
* Since we have rudimentary profiles and "list" pages, if we were to take this project further, we might implement a social aspect where people can make friends, view each other's lists, etc.