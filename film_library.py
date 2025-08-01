import random
import datetime

class Film():
    def __init__(self,title,release_year, genre, views_num):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views_num = views_num
    
    def __str__(self):
        return f'{self.title} ({self.release_year})'
    
    def play(self):
        self.views_num += 1
    


class Series(Film):
    def __init__(self, episode_num, season_num,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_num = episode_num
        self.season_num = season_num
    
    def __str__(self):
        return f'{self.title} S{self.season_num:02}E{self.episode_num:02}'
    
    def __eq__(self, other):
        return self.title == other.title and self.episode_num == other.episode_num and self.season_num == other.season_num
    

def get_objects(list, object_class):
    objects = []
    for i in list:
        if type(i) == object_class:
            objects.append(i)
    objects.sort(key = lambda x: x.title)
    return objects

def get_movies(list):
    return get_objects(list, Film)

def get_series(list):
    return get_objects(list, Series)

def search(title,list):
    for i in list:
        if i.title == title:
            print(f'Film o tytule {title} znajduje się w bibliotece')
        else:
            print(f'Film o tytule {title} nie znajduje się w bibliotece')

def generate_views(list):
    random.choice(list).views_num = random.randrange(1,101)

def generate_view_10_times(list):
    for i in range(10):
        generate_views(list)

def top_titles(list, num, content_type):
    selected = [i for i in list if type(i) == content_type]
    selected.sort(reverse=True,key = lambda x: x.views_num)
    return selected[0:num]

def add_whole_season(list, title, release_date, genre, season_num, episodes_num):
    series = [i for i in list if type(i) == Series]
    for i in range(1,(episodes_num + 1)):
        ep_to_add = Series(i,season_num,title,release_date,genre,0)
        if not ep_to_add in series:
            list.append(ep_to_add)

print("Biblioteka filmów")

library = []

film1 = Film("Pulp Fiction", 1994, "Crime", 1000)
film2 = Film("The Matrix", 1999, "Sci-Fi", 850)
film3 = Film("Inception", 2010, "Sci-Fi", 1200)
film4 = Film("The Godfather", 1972, "Crime", 900)

serial1 = Series(1, 5, "The Simpsons", 1989, "Comedy", 1000)
serial2 = Series(1, 6, "Stranger Things", 1989, "Comedy", 980)
serial3 = Series(2, 1, "Peaky Blinders", 1990, "Comedy", 950)
serial4 = Series(1, 1, "The Umbrella Academy", 2008, "Drama", 1300)
serial5 = Series(1, 2, "Friends", 2008, "Drama", 1250)
serial6 = Series(2, 1, "The Office", 2009, "Drama", 1150)

library.extend([
    film1, film2, film3, film4,
    serial1, serial2, serial3,
    serial4, serial5, serial6
])


generate_views(library)

today = (datetime.datetime.now()).strftime('%d.%m.%Y')
print(f'Najpopularniejsze filmy i seriale dnia {today}')
print('\nFILMY')
top_films = top_titles(library,3,Film)
for i in top_films:
    print(i.title)

print('\nSERIALE')  
top_series = top_titles(library,3,Series)
for i in top_series:
    print(i.title)


