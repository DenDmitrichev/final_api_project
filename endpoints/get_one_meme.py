import requests
import allure
from endpoints.endpoint import EndPoint


class GetOneMeme(EndPoint):
    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Get meme')
    def get_one_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{meme_id}',
                                     headers=headers)
        # Сохраняем JSON ответа
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except requests.exceptions.JSONDecodeError:
                self.json = None
        return self.response

    @allure.step('Get meme without auth')
    def get_one_meme_without_auth(self, meme_id, headers=None):
        self.response = requests.get(f'{self.url}/{meme_id}',
                                     headers=headers)
        return self.response

    @allure.step('Check ID matches requested')
    def check_id_matches_requested(self, requested_id):
        """Проверяет, что ID в ответе совпадает с запрошенным"""
        assert self.json is not None, "Нет JSON ответа"
        assert "id" in self.json, "В ответе отсутствует поле id"
        assert self.json["id"] == requested_id, \
            f"Ожидался ID {requested_id}, получен {self.json['id']}"
