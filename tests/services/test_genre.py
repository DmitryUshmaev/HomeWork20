from unittest.mock import MagicMock

import pytest

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


# Фикстура с моком для GenreDAO

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    """Тестовые значения"""

    comedy = Genre(id=1, name='Комедия')
    fantasy = Genre(id=2, name='Фэнтези')
    triller = Genre(id=3, name='Трилер')

    """Симуляция выполнения dao методов"""

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, fantasy, triller])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


# Тесты для GenreService

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    """Тест получения одного жанра по его id"""

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    """Тест получения всех жанров"""

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    """Тест создание нового жанра"""

    def test_create(self):
        genre_d = {"name": "New Genre"}

        genre = self.genre_service.create(genre_d)

        assert genre.id is not None

    """Тест удаление жанра по id"""

    def test_delete(self):
        self.genre_service.delete(1)

    """Тест обновления жанра"""

    def test_update(self):
        genre_d = {"name": "New Genre"}

        self.genre_service.update(genre_d)
