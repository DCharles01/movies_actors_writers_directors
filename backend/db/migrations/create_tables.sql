drop table if exists actors;
drop table if exists directors;
drop table if exists writers;
drop table if exists movies;
drop table if exists movie_actors;
drop table if exists movie_directors;
drop table if exists movie_writers;


create table if not exists movies (
    id serial primary key,
    title varchar,
    studio varchar,
    runtime decimal,
    description varchar,
    release_date timestamp,
    year integer
);

create table if not exists actors (
    id serial primary key,
    name varchar(50)
);

create table if not exists directors (
    id serial primary key,
    name varchar(50)
);

create table if not exists writers (
    id serial primary key,
    name varchar(50)
);

create table if not exists movie_actors (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    constraint fk_movie_actors_movie foreign key (movie_id) references movies (id),
    constraint fk_movie_actors_actor foreign key (actor_id) references actors (id)
);


create table if not exists movie_directors (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    director_id INTEGER NOT NULL,
    constraint fk_movie foreign key (movie_id) references movies (id),
    constraint fk_director foreign key (director_id) references directors (id)
);

create table if not exists movie_writers (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    writer_id INTEGER NOT NULL,
    constraint fk_movie foreign key (movie_id) references movies (id),
    constraint fk_writer foreign key (writer_id) references writers (id)
);





