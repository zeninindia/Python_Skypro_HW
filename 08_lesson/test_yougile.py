from page_yougile import PageYougile
from dotenv import load_dotenv
import os
import pytest

load_dotenv()


@pytest.fixture(scope='session')
def yougile():
    base_url = "https://ru.yougile.com/api-v2/"
    return PageYougile(base_url)


@pytest.fixture
def project_id(yougile):
    title = 'WTF'
    user_id = os.getenv("USERID")
    status_code, project = yougile.sozdanie_project(title, user_id)
    assert status_code == 201, "Не удалось создать проект для теста"
    yield project


def test_sozdanie_project(yougile):
    title = "chto_nibud"
    user_id = os.getenv("USERID")
    status_code, response = yougile.sozdanie_project(title, user_id)
    assert status_code == 201
    assert response['id'] is not None


def test_sozdanie_project_neg(yougile):
    title = "chto_nibud"
    user_id = os.getenv("USERID_FAIL")
    status_code, response = yougile.sozdanie_project(title, user_id)
    assert status_code == 400
    assert (response['message'] ==
            'Сотрудники со следующими ID не найдены в компании:'
            ' 123')
    assert response['error'] == 'Bad Request'


def test_poluchenie_project(yougile, project_id):
    stats, project_num = yougile.poluchenie_project(project_id['id'])
    assert stats == 200
    assert project_num['id'] == project_id['id']


def test_poluchenie_project_neg(yougile):
    stats, project_num = yougile.poluchenie_project(yougile)
    assert stats == 404
    assert 'Проект не найден' in project_num.get('message')


def test_izminenie_project(yougile, project_id):
    new_title = "chto_to"
    user_id = os.getenv("USERID")
    status_code, new_project_id = yougile.izminenie_project(
        project_id['id'], new_title, user_id)
    assert status_code == 200
    assert new_project_id is not None


def test_izminenie_project_neg(yougile):
    new_title = "chto_to"
    user_id = os.getenv("USERID")
    status_code, new_project_id = yougile.izminenie_project(
        "123456778", new_title, user_id)
    assert status_code == 404
    assert 'Проект не найден' in new_project_id.get('message')
