import requests
import allure
from endpoints.endpoint import EndPoint
import random


class DeleteMeme(EndPoint):
    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Delete meme')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{meme_id}',
                                        headers=headers)
        return self.response

    @allure.step('Delete non-existent meme')
    def delete_non_existent_meme(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/id{random.randint(1000,2000)}',
                                        headers=headers)
        return self.response

    @allure.step('Delete meme without id')
    def delete_meme_without_id(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}',
                                        headers=headers)
        return self.response
