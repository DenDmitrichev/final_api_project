import random
import pytest


body = {"text": "New text",
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": [
            "druzko",
            "funny",
            "memas"
        ],
        "info": {
            "data": "september",
            "year": "1989"
        }

        }


def test_create_meme(create_meme_endpoint):
    create_meme_endpoint.create_meme(body)
    create_meme_endpoint.check_response_text_is_correct(body['text'])
    create_meme_endpoint.check_response_url_is_correct(body['url'])
    create_meme_endpoint.check_response_info_is_correct(body['info'])
    create_meme_endpoint.check_response_tags_is_correct(body['tags'])


@pytest.mark.parametrize("body2", [
    # 1. Без text (обязательное поле)
    {
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 2. Без url (обязательное поле)
    {
        "text": f'my new text{random.randint(1, 100)}',
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 3. Без tags (обязательное поле)
    {
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "info": {"data": "september", "year": "1989"}
    },

    # 4. Без info (обязательное поле)
    {
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"]
    },

    # 5. Только text
    {
        "text": f'my new text{random.randint(1, 100)}'
    },

    # 6. Пустое тело
    {},

    # 7. Только tags и info (без text и url)
    {
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    }
])
def test_create_meme_without_fields(create_meme_endpoint, body2):
    """Негативные тесты: создание мема без обязательных полей"""
    create_meme_endpoint.create_meme(body2)
    create_meme_endpoint.check_that_status_is_400()


