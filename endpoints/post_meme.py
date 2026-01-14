import requests
import allure
from endpoints.endpoint import EndPoint


class PostMeme(EndPoint):
    def __init__(self, headers=None):
        super().__init__(headers)

    @allure.step('Create meme')
    def create_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.json

    @allure.step('Check text')
    def check_response_text_is_correct(self, text):
        with allure.step(f'Check response name == {text}'):
            assert self.json["text"] == text, 'name не совпадает'

    @allure.step('Check tags')
    def check_response_tags_is_correct(self, tags):
        with allure.step(f'Check response tags == {tags}'):
            assert self.json["tags"] == tags, 'tags не совпадают'

    @allure.step('Check url')
    def check_response_url_is_correct(self, url):
        with allure.step(f'Check response url == {url}'):
            assert self.json["url"] == url, 'url не совпадает'

    @allure.step('Check info')
    def check_response_info_is_correct(self, info):
        with allure.step(f'Check response info == {info}'):
            assert self.json["info"] == info, 'url не совпадает'
