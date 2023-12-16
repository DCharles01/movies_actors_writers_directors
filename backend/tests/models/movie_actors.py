import api.models as models

class Movie_Actor(models.BaseClass):
    __table__='movie_actors_test'
    columns = ['id', 'movie_id', 'actor_id']

    # def __init__(self, values):
    #     self.__dict__ = dict(zip(self.columns, values))

    