drop table if exists actors_test cascade;
drop table if exists directors_test cascade;
drop table if exists writers_test cascade;
drop table if exists movies_test cascade;
drop table if exists movie_actors_test cascade;
drop table if exists movie_directors_test cascade;
drop table if exists movie_writers_test cascade;

create table if not exists movies_test (
    id serial primary key,
    title varchar,
    studio varchar,
    runtime decimal,
    description varchar,
    release_date timestamp,
    year integer
);

create table if not exists actors_test (
    id serial primary key,
    name varchar(50)
);

create table if not exists directors_test (
    id serial primary key,
    name varchar(50)
);

create table if not exists writers_test (
    id serial primary key,
    name varchar(50)
);

create table if not exists movie_actors_test (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    constraint fk_movie_actors_test_movie foreign key (movie_id) references movies_test (id),
    constraint fk_movie_actors_test_actor foreign key (actor_id) references actors_test (id)
);


create table if not exists movie_directors_test (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    director_id INTEGER NOT NULL,
    constraint fk_movie foreign key (movie_id) references movies_test (id),
    constraint fk_director foreign key (director_id) references directors_test (id)
);

create table if not exists movie_writers_test (
    id serial primary key,
    movie_id INTEGER NOT NULL,
    writer_id INTEGER NOT NULL,
    constraint fk_movie foreign key (movie_id) references movies_test (id),
    constraint fk_writer foreign key (writer_id) references writers_test (id)
);





