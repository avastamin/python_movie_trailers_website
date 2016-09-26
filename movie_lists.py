import media
import fresh_tomatoes

the_equalizer = media.Movie("The Equalizer",
	"A man of mysterious origin who believes he has put the past behind him,",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Equalizer_poster.jpg/220px-The_Equalizer_poster.jpg",
	"https://www.youtube.com/watch?v=VjctHUEmutw")

toy_story = media.Movie("Toy Story",
	"Story about a boy and his Toy",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	"https://www.youtube.com/watch?v=Y_zP__Cm9XE")

avatar = media.Movie("Avatar",
	"A Marin in the alien planet",
	"http://www.noholidaynolife.com/wp-content/uploads/2010/04/avatar-movie-poster-6.jpg",
	"https://www.youtube.com/watch?v=EzETGqZN6dU")

inception = media.Movie("Inception",
	"A thief, who steals corporate secrets through use of dream-sharing technology",
	"https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=YoHD9XEInc0")

django_unchained = media.Movie("Django Unchained",
	"Two years before the Civil War, Django (Jamie Foxx), a slave",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Django_Unchained_Poster.jpg/220px-Django_Unchained_Poster.jpg",
	"https://www.youtube.com/watch?v=eUdM9vrCbow")

#create movie array with all movies
movies= [the_equalizer,toy_story,avatar,inception,django_unchained]

#call and pass movies to open_movies_pagefunction 
fresh_tomatoes.open_movies_page(movies)
