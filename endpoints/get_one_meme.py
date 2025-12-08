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
        return self.response
