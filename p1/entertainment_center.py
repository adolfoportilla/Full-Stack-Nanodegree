import media
import fresh_tomatoes

toystoryImage = "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450" #NOQA
toystoryYoutube = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
avatarImage = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg" #NOQA
avatarYoutube = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
intestellarImage = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg" #NOQA
interstellarYoutube = "https://www.youtube.com/watch?v=sRLc9OlrZZw"
schoolImage = "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg" #NOQA
schoolYoutube = "https://www.youtube.com/watch?v=3PsUJFEBC74"
midnigthImage = "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg" #NOQA
midnigthYoutube = "https://www.youtube.com/watch?v=FAfR8omt-CY"
hungerImage = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg" #NOQA
hungerYoutube = "https://www.youtube.com/watch?v=mfmrPu43DF8"


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that comes to life", 
						toystoryImage, toystoryYoutube)
avatar = media.Movie("Avatar", "A marine on an alien planet", avatarImage, avatarYoutube )
interstellar = media.Movie("Interestellar", "A group of scientist are trying to discover" 
							"a planet to move the human race to it", intestellarImage, 
							interstellarYoutube)
school_of_rock = media.Movie("School of Rock", "A professor that plays songs in a band", 
							schoolImage, schoolYoutube)
midnight_in_paris = media.Movie("Midnight in Paris", "A movie about a screnwriter", 
								midnigthImage, midnigthYoutube)
the_hunger_games = media.Movie("The hunger games", "A story about a girl that gets chosen "
								"to play a game that depends on her life", hungerImage, hungerYoutube)

movies = [toy_story, avatar, school_of_rock, interstellar, the_hunger_games, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
