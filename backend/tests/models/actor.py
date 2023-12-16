import api.models as models
from db.db_utilities import *

class Actor(models.Actor):
    __table__ = 'actors_test'
    columns = ['id', 'name']
    

    