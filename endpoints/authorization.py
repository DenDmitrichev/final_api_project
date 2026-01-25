import requests
import allure
from endpoints.endpoint import EndPoint
import random


class Authorization(EndPoint):
    url = 'http://memesapi.course.qa-practice.com/authorize'

    def __init__(self, headers=None):
        super().__init__(headers)
        self.token = None
        self.username = None

    def auth_response(self, username="Denis123", headers=None):
        """
        Возвращает ВЕСЬ ответ авторизации.
        Сохраняет токен и имя в атрибутах объекта.
        """
        with allure.step(f'Authorize user: {username}'):
            headers = headers if headers else self.headers
            self.response = requests.post(
                self.url,
                headers=headers,
                json={"name": username}
            )

        # Сохраняем данные при успешной авторизации
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
                self.token = self.extract_token(self.json)
                self.username = self.extract_username(self.json)
            except requests.exceptions.JSONDecodeError:
                self.json = None
                self.token = None
                self.username = None

        return self.json

    @staticmethod
    def extract_token(auth_response):
        """Извлекает токен из ответа"""
        return auth_response.get("token") if auth_response else None

    @staticmethod
    def extract_username(auth_response):
        """Извлекает имя из ответа"""
        return auth_response.get("name") if auth_response else None

    @staticmethod
    def create_headers(token):
        """Создает заголовки с токеном"""
        return {
            'Content-Type': 'application/json',
            'Authorization': token
        }

    @allure.step('Check auth response structure')
    def check_response_structure(self):
        """Проверяет структуру ответа авторизации"""
        assert self.json is not None, "Нет JSON ответа"
        assert isinstance(self.json, dict), "Ответ должен быть словарем"
        assert "token" in self.json, "В ответе отсутствует токен"
        assert "name" in self.json, "В ответе отсутствует имя"

    @allure.step('Check token is present and valid')
    def check_token_validity(self):
        """Проверяет, что токен присутствует и не пустой"""
        token = self.extract_token(self.json)
        assert token is not None, "Токен не должен быть None"
        assert token != "", "Токен не должен быть пустой строкой"

    @allure.step('Test token with real API request')
    def test_token_with_real_request(self, test_url=None):
        """
        Проверяет, что токен работает в реальном запросе.
        Делает GET запрос к API с этим токеном.

        Args:
            test_url: URL для тестирования (по умолчанию /meme)
        """
        token = self.extract_token(self.json)
        assert token is not None, "Нет токена для проверки"

        if test_url is None:
            test_url = 'http://memesapi.course.qa-practice.com/meme'

        headers = self.create_headers(token)

        with allure.step(f'Test token with GET {test_url}'):
            response = requests.get(test_url, headers=headers)

        assert response.status_code == 200, \
            f"Токен не работает! GET {test_url} вернул {response.status_code}"

        return response

    @allure.step('Authorize with empty username')
    def auth_with_empty_username(self, headers=None):
        """
        Пытается авторизоваться с пустым именем пользователя.
        Должно завершиться ошибкой.
        """
        return self.auth_response(username="", headers=headers)
