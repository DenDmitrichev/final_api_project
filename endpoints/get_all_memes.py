import requests
import allure
from endpoints.endpoint import EndPoint


class GetAllMemes(EndPoint):
    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Get all memes')
    def get_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}',
                                     headers=headers)

        return self.response

    @allure.step('Check response structure')
    def check_response_structure(self):
        """Проверяет структуру ответа (assert внутри метода - ок)"""
        if self.response.status_code == 200:
            response_data = self.response.json()
            assert isinstance(response_data, dict), "Ответ должен быть словарем"

