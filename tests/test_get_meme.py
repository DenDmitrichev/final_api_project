def test_get_existing_meme(get_one_meme_endpoint, create_meme_id):
    get_one_meme_endpoint.get_one_meme(create_meme_id)
    get_one_meme_endpoint.check_that_status_is_200()


def test_get_nonexistent_meme(get_one_meme_endpoint):
    get_one_meme_endpoint.get_one_meme("non_existent_id_999")
    get_one_meme_endpoint.check_that_status_is_404()


def test_meme_is_actually_deleted(delete_meme_endpoint, get_one_meme_endpoint, create_meme_id):
    """После DELETE мема его нельзя получить"""
    get_one_meme_endpoint.get_one_meme(create_meme_id)
    get_one_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.delete_meme(create_meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.get_one_meme(create_meme_id)
    get_one_meme_endpoint.check_that_status_is_404()
