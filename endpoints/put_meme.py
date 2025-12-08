import requests
import allure
from endpoints.endpoint import EndPoint


class PutMeme(EndPoint):
    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Change all in meme')
    def put_meme(self, meme_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{meme_id}',
                                     json=body, headers=headers)

        # self.json = self.response.json()
        return self.response

    def check_response_text_is_correct(self, text):
        with allure.step(f'Check response name == {text}'):
            response_json = self.response.json()
            assert response_json["text"] == text, 'text не совпадает'
