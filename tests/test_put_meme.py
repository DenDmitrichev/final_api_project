import random
import pytest


def test_put_meme(put_meme_endpoint, create_meme_id):
    body = {"id": create_meme_id,
            "text": f'my new text{random.randint(1, 100)}',
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
    put_meme_endpoint.put_meme(create_meme_id, body)
    put_meme_endpoint.check_that_status_is_200()
    put_meme_endpoint.check_response_text_is_correct(body["text"])


@pytest.mark.parametrize("body", [
    # 1. Без id
    {
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 2. Без text
    {
        "id": "create_meme_id",  # Это заменится в тесте
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 3. Без url
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 4. Без tags
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "info": {"data": "september", "year": "1989"}
    },

    # 5. Без info
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"]
    },

    # 6. Только id
    {
        "id": "create_meme_id"
    },

    # 7. Только id и text
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}'
    },

    # 8. Пустой body
    {},

    # 9. без id и text
    {
        "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # 10. Только tags и info
    {
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    }
])
def test_put_meme_without_field(put_meme_endpoint, create_meme_id, body):
    """Тестируем PUT с разными неполными телами запроса"""

    # Заменяем placeholder "create_meme_id" на реальный ID
    if "id" in body and body["id"] == "create_meme_id":
        body["id"] = create_meme_id
    put_meme_endpoint.put_meme(create_meme_id, body)
    put_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize("body", [
    # Пустые строки
    {
        "id": "create_meme_id",
        "text": "",  # Пустой текст
        "url": "https://example.com/image.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "url": "",  # Пустой URL
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },

    # Пустые массивы/объекты
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://example.com/image.jpg",
        "tags": [],  # Пустой массив tags
        "info": {"data": "september", "year": "1989"}
    },
    {
        "id": "create_meme_id",
        "text": f'my new text{random.randint(1, 100)}',
        "url": "https://example.com/image.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {}  # Пустой объект info
    },

    # Все поля пустые
    {
        "id": "create_meme_id",
        "text": "",
        "url": "",
        "tags": [],
        "info": {}
    },

    # Пробелы как значения
    {
        "id": "create_meme_id",
        "text": "   ",  # Только пробелы
        "url": "https://example.com/image.jpg",
        "tags": ["druzko", "funny", "memas"],
        "info": {"data": "september", "year": "1989"}
    },


])
def test_put_meme_with_empty_values(put_meme_endpoint, create_meme_id, body):
    """PUT с пустыми значениями полей"""
    if "id" in body and body["id"] == "create_meme_id":
        body["id"] = create_meme_id

    put_meme_endpoint.put_meme(create_meme_id, body)
    put_meme_endpoint.check_that_status_is_200()
