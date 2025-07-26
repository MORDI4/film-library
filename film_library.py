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
