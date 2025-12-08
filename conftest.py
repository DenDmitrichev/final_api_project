import pytest
import requests
import allure

from endpoints.check_authorize import CheckAuthorize
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMeme
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from endpoints.authorization import Authorization


@pytest.fixture()
def create_meme_endpoint(headers_with_auth):
    return PostMeme(headers=headers_with_auth)


@pytest.fixture()
def put_meme_endpoint(headers_with_auth):
    return PutMeme(headers=headers_with_auth)


@pytest.fixture(scope="session")
def authorization():
    return Authorization()


@pytest.fixture(scope="session")
def check_authorize():
    return CheckAuthorize()


@pytest.fixture()
def get_meme_endpoint(headers_with_auth):
    return GetAllMemes(headers=headers_with_auth)


@pytest.fixture()
def get_one_meme_endpoint(headers_with_auth):
    return GetOneMeme(headers=headers_with_auth)


@pytest.fixture()
def delete_meme_endpoint(headers_with_auth):
    return DeleteMeme(headers=headers_with_auth)


@pytest.fixture()
def create_meme_id(headers_with_auth):
    body = {
        "text": "New_meme22",
        "url": "https://static.eldorado.ru/promo/src/chto-takoe-memy/img/img1.jpg",
        "tags": ["котики", "собачки"],
        "info": {"date": "monday",
                 "description": "new description"
                 }
    }
    with allure.step('Create new object'):
        response = requests.post('http://memesapi.course.qa-practice.com/meme', json=body,
                                 headers=headers_with_auth)
    obj_id = response.json()['id']
    yield obj_id
    with allure.step('Delete object'):
        requests.delete(f'http://memesapi.course.qa-practice.com/meme/{obj_id}', headers=headers_with_auth)


@pytest.fixture(scope="session")
def auth_token():
    """Только токен (строка)"""
    auth = Authorization()
    response = auth.auth_response()
    return Authorization.extract_token(response)


@pytest.fixture(scope="session")
def auth_username():
    """Только имя пользователя (строка)"""
    auth = Authorization()
    response = auth.auth_response()
    return Authorization.extract_username(response)


@pytest.fixture
def headers_with_auth(auth_token):
    """Заголовки с авторизацией"""
    return Authorization.create_headers(auth_token)

