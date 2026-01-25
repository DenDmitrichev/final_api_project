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

            # body = {"id": create_meme_id,
            #         "text": f'my new text{random.randint(1, 100)}',
            #         "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
            #         "tags": [
            #             "druzko",
            #             "funny",
            #             "memas"
            #         ],
            #         "info": {
            #             "data": "september",
            #             "year": "1989"
            #         }
            #
            #         }
    def check_response_id_is_correct(self, ids):
        with allure.step(f'Check response name == {ids}'):
            response_json = self.response.json()
            assert response_json["ids"] == ids, 'id не совпадает'

    def check_response_url_is_correct(self, url):
        with allure.step(f'Check response name == {url}'):
            response_json = self.response.json()
            assert response_json["url"] == url, 'url не совпадает'

    def check_response_tags_is_correct(self, tags):
        with allure.step(f'Check response name == {tags}'):
            response_json = self.response.json()
            assert response_json["tags"] == tags, 'tags не совпадает'

    def check_response_info_is_correct(self, info):
        with allure.step(f'Check response name == {info}'):
            response_json = self.response.json()
            assert response_json["info"] == info, 'info не совпадает'

    def put_meme_without_auth(self, meme_id, body):
        headers = {'content-type': 'application/json'}
        self.response = requests.put(f'{self.url}/{meme_id}',
                                     json=body, headers=headers)
        return self.response


