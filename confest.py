import pytest as pytest

from framework.workplace import Workplace


@pytest.fixture(scope="session")
def workplace():
    yield Workplace()


@pytest.fixture(scope='function')
def create_cats():
    cats = []

    def create():
        pass

    yield create

    for cat in cats:
        cat.delete()


@pytest.fixture(scope='function')
def create_bird():
    """ Возвращает объект с полями, идентичными базе данных"""
    birds = []

    def create():
        #bird = workplace.db.create_bird()
        pass

    yield create

    for bird in birds:
        bird.delete()
