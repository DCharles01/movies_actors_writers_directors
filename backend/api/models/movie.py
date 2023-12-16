import api.models as models

class Movie(models.BaseClass):
    __table__ = 'movies'
    columns = ['id', 'title', 'studio', 'runtime', 'description', 'release_date', 'year']

    # def __init__(self, values):
    #     self.__dict__ = dict(zip(self.columns, values))

    # # todo: figure out way to autogenerate id and check against database to see if exists
    # def add_actor(self, name):
    #     pass

