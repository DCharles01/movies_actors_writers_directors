from flask import Flask, jsonify, render_template, request
import sqlite3
# from settings import DB_NAME
import psycopg2
from api.models import Actor, Movie


def create_app(database, user):

    app = Flask(__name__, static_folder='static', template_folder='views')

    app.config.from_mapping(
        DATABASE=database,
        USER=user
    )


    @app.route('/movies/search', methods=['GET', 'POST'])
    def search():
        conn = sqlite3.connect(app.config['DATABASE'])
        if request.method == 'POST':

            query = request.form.get('search_query')
            cursor = conn.cursor()
            if query == "":
                cursor.execute('''
                    select 
                    * 
                    from
                        movies;

                ''')
                results = cursor.fetchall()
                # results = jsonify(results)
                # results = results.get_json()
                return render_template('index.html', results=results)

            else:    
                cursor.execute('''
                    select 
                    * 
                    from
                        movies 
                    where 
                        title like ? or 
                        studio like ? or 
                        runtime = ? or 
                        description like ? or
                        release_date = ? or
                        year = ?;

                ''', ('%' + query + '%', '%' + query + '%', query, '%' + query + '%', query, query))
                results = cursor.fetchall()
                # results = jsonify(results)
                # results = results.get_json()
                return render_template('index.html', results=results)
                # return jsonify(results)
        return render_template('index.html')
        

        # cursor.execute('select * from movies where title = ? or studio = ? or runtime = ? or description = ?;', (query,))
    
    @app.route('/movies')
    def movies():
        conn = sqlite3.connect(app.config['DATABASE'])
        # title = request.args.get('title')
        # studio = request.args.get('studio')

        cursor = conn.cursor()
        cursor.execute('select * from movies')
        movie_records = cursor.fetchall()

        # return render_template('movie.html')
        return jsonify(movie_records)

    @app.route('/movies/search/title')
    def movies_name():
        conn = sqlite3.connect(app.config['DATABASE'])
        title = request.args.get('title')
        # studio = request.args.get('studio')

        cursor = conn.cursor()
        cursor.execute('select * from movies where title = ?;', (title,))
        movie_records = cursor.fetchall()

        # return render_template('movie.html')
        return jsonify(movie_records)
    
    @app.route('/movies/search/studio')
    def movies_studio():
        conn = sqlite3.connect(app.config['DATABASE'])
        studio = request.args.get('studio')
        # studio = request.args.get('studio')

        cursor = conn.cursor()
        cursor.execute('select * from movies where studio = ?;', (studio,))
        movie_records = cursor.fetchall()

        # return render_template('movie.html')
        return jsonify(movie_records)
    
    @app.route('/movies/search/id')
    def movies_id():
        conn = sqlite3.connect(app.config['DATABASE'])
        id = request.args.get('id')
        # studio = request.args.get('studio')

        cursor = conn.cursor()
        cursor.execute('select * from movies where id = ?;', (id,))
        movie_records = cursor.fetchall()

        # return render_template('movie.html')
        return jsonify(movie_records)
    
    @app.route('/movies/search/runtime')
    def movies_runtime():
        conn = sqlite3.connect(app.config['DATABASE'])
        runtime = request.args.get('runtime')
        # studio = request.args.get('studio')

        cursor = conn.cursor()
        cursor.execute('select * from movies where runtime = ?;', (runtime,))
        movie_records = cursor.fetchall()

        # return render_template('movie.html')
        return jsonify(movie_records)

    # query: grab movie by id
    # todo: grab movie by name, use fuzzy matching to return similar movie names
    # todo: add a search bar on movie page 
    # todo: add images for movie
    @app.route('/movies/<id>')
    def movies_lookup_id(id):
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('select * from movies where id = ?;', (id,))
        movie_details = cursor.fetchone()
        # movie = Movie(*movie_details)
        return jsonify(movie_details)
    

    @app.route('/actors')
    def actors():
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('select * from actors;')
        actor_records = cursor.fetchall()

        return jsonify(actor_records)
    
    # search for actors name
    @app.route('/actors/search/name')
    def actors_name():
        name = request.args.get('name')
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        
        cursor.execute('select * from actors where name = ?;', (name,))
        actor_records = cursor.fetchall()

        return jsonify(actor_records)

    # search by actor id
    @app.route('/actors/search/id')
    def actors_lookup_id():

        id = request.args.get('id')
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        
        cursor.execute('select * from actors where id = ?;', (id,))
        actor_details = cursor.fetchall()
        # actor = Actor(*actor_details)

        # return render_template('actor.html', id=id)
        return jsonify(actor_details)
    return app


