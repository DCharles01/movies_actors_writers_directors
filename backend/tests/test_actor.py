from db.db_utilities import *
import pytest
import tests.models as models

@pytest.fixture()
def clean_tables():
    drop_create_tables(conn, cursor)

    yield

    drop_create_tables(conn, cursor)

@pytest.fixture()
def build_actor():
    drop_create_tables(conn, cursor)

    params = {'id':1, 'name': 'Chadwick Boseman'}
    actor = models.Actor(**params)
    print(actor.__table__)

    # save to db
    save(actor, conn, cursor)
    yield
    drop_create_tables(conn, cursor)

def build_actors():
    params = {'id':1, 'name': 'Chadwick Boseman'}
    actor = models.Actor(**params)

    # save to db
    save(actor, conn, cursor)

    params = {'id':2, 'name': 'Michael B. Jordan'}
    actor = models.Actor(**params)

    # save to db
    save(actor, conn, cursor)
    yield
    drop_create_tables(conn, cursor)

def build_movie():
    drop_create_tables(conn, cursor)

    params = {'id': 1, 'name': 'Black Panther'}
    movie = models.Movie(**params)
    save(movie, conn, cursor)

    yield

    drop_create_tables(conn, cursor)

@pytest.fixture()
def build_movie_actors():
    drop_create_tables(conn, cursor)

    params = {'id':1, 'name': 'Chadwick Boseman'}
    actor = models.Actor(**params)

    # save to db
    save(actor, conn, cursor)

    params2 = {'id':2, 'name': 'Michael B. Jordan'}
    actor2 = models.Actor(**params2)

    # save to db
    save(actor2, conn, cursor)

    params3 = {'id': 1, 'title': 'Black Panther', 'studio': 'Marvel Studio'}
    movie = models.Movie(**params3)
    save(movie, conn, cursor)

    params4 = {'id': 1, 'movie_id': 1, 'actor_id': 1}
    movie_actor = models.Movie_Actor(**params4)
    save(movie_actor, conn, cursor)

    params5 = {'id': 2, 'movie_id': 1, 'actor_id': 2}
    movie_actor = models.Movie_Actor(**params5)
    save(movie_actor, conn, cursor)

    yield

    drop_create_tables(conn, cursor)


def test_actor_name(build_actor):
    cursor.execute('select * from actors_test')
    record = cursor.fetchone()

    actor = build_from_record(models.Actor, record)

    assert actor.name == 'Chadwick Boseman'

def test_movies(build_movie_actors):
    cursor.execute('select * from actors_test where id = 1')
    record = cursor.fetchone()

    chadwick_boseman = build_from_record(models.Actor, record)

    movies = [movie.title for movie in chadwick_boseman.movies(cursor)]

    assert movies == ['Black Panther']









