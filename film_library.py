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
    
