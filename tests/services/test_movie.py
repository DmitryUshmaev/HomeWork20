from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


# Фикстура с моком для MovieDAO

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    dune = Movie(id=1, title='Дюна', description='Описание дюны',
                 trailer='https://www.youtube.com/watch?v=DOlTmIhEsg0',
                 year=2018, rating=9, genre_id=1, director_id=1)
    venom = Movie(id=1, title='Веном', description='Описание венома',
                  trailer='https://www.youtube.com/watch?v=DOlTmIhEsg0',
                  year=2018, rating=9, genre_id=2, director_id=2)
    django = Movie(id=1, title='Джанго', description='Описание джанго',
                  trailer='https://www.youtube.com/watch?v=DOlTmIhEsg0',
                  year=2018, rating=9, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=dune)
    movie_dao.get_all = MagicMock(return_value=[dune, venom, django])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


# Тесты для MovieService

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {"name": "New Movie"}

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {"name": "New Movie"}

        self.movie_service.update(movie_d)
