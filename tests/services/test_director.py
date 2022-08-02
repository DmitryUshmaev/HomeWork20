from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


# Фикстура с моком для DirectorDAO

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    """Тестовые значения"""

    nikita = Director(id=1, name='Никита Михалков')
    martin = Director(id=2, name='Мартин Скорсезе')
    taylor = Director(id=3, name='Тейлор Шеридан')

    """Симуляция методов dao director"""

    director_dao.get_one = MagicMock(return_value=nikita)
    director_dao.get_all = MagicMock(return_value=[nikita, martin, taylor])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


# Тесты для DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    """Тест получения director по его id"""

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    """Тест получение всех значений director"""

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    """Тест создание нового director"""

    def test_create(self):
        director_d = {"name": "New Director"}

        director = self.director_service.create(director_d)

        assert director.id is not None

    """Тест удаление director по id"""

    def test_delete(self):
        self.director_service.delete(1)

    """Тест обновление director"""

    def test_update(self):
        director_d = {"name": "New Director"}

        self.director_service.update(director_d)
