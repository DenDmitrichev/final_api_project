import requests
import allure
from endpoints.endpoint import EndPoint
import random


class Authorization(EndPoint):
    url = 'http://memesapi.course.qa-practice.com/authorize'

    def __init__(self, headers=None):
        super().__init__(headers)

    def auth_response(self, username=f"Denis{random.randint(1, 1000)}", headers=None):

        with allure.step('Get authorization token'):
            headers = headers if headers else self.headers
            self.response = requests.post(
                self.url,
                headers=headers,
                json={"name": username}
            )
        return self.response.json()

    @staticmethod
    def extract_token(auth_response):
        """Извлекает токен из ответа"""
        return auth_response["token"]

    @staticmethod
    def extract_username(auth_response):
        """Извлекает имя из ответа"""
        return auth_response["name"]

    @staticmethod
    def create_headers(token):
        """Создает заголовки с токеном"""
        return {
            'Content-Type': 'application/json',
            'Authorization': token
        }
