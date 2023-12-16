import api.models as models
from db.db_utilities import *
class Actor(models.BaseClass):
    __table__ = 'actors'
    columns = ['id', 'name']
    
    # def __init__(self, values):
    #     # add attributes to instance
    #     self.__dict__ = dict(zip(self.columns, values))

    # @staticmethod
    # def add_actor(self, name):
    #     pass

    @classmethod
    def find_actor_by_id(cls, id, cursor):
        query = f"select * from {cls.__table__} where id = %s"
        cursor.execute(query, (id,))
        record = cursor.fetchone()

        return build_from_record(cls, record)
    
    @classmethod
    def find_actor_by_name(cls, name, cursor):
        query = f"select * from {cls.__table__} where name = %s"
        cursor.execute(query, (name,))
        record = cursor.fetchone()

        return build_from_record(cls, record)

    # actor can be in many movies
    def movies(self, cursor):
        movie_query = f"""
        select
            movies.*
        from
            movies
        inner join
            movie_actors on movies.id = movie_actors.actor_id
        where
            movie_actors.actor_id = %s
        """
        cursor.execute(movie_query, (self.id,))
        movies = cursor.fetchall()

        return build_from_records(models.Movie, movies)
    
    # actor can work with many writers
    def writers(self, cursor):
        pass
    # actor can work with many directors
    def directors(self, cursor):
        pass

    