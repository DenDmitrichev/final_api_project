import requests
import allure
from endpoints.endpoint import EndPoint


class CheckAuthorize(EndPoint):

    url = 'http://memesapi.course.qa-practice.com/authorize'

    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Отправить токен на проверку')
    def check_token(self, auth_token,  headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{auth_token}',
                                     headers=headers)
        return self.response

    @allure.step('Check token and assert is valid')
    def assert_token_valid(self, token, headers=None):
        response = self.check_token(token, headers)
        assert response.status_code == 200, f"Токен невалиден. Status: {response.status_code}"
        return response

    @allure.step('Check token and assert is invalid')
    def assert_token_invalid(self, token, headers=None):
        response = self.check_token(token, headers)
        assert response.status_code != 200, f"Токен оказался валиден!. Status: {response.status_code}"
        assert not (500 <= response.status_code < 600), \
            f"СЕРВЕРНАЯ ОШИБКА! Status: {response.status_code}. Токен '{token}' вызвал падение сервера! "

        return response
