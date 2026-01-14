def test_delete_meme(delete_meme_endpoint, create_meme_id):
    """Удаление существующего мема"""
    delete_meme_endpoint.delete_meme(create_meme_id)
    delete_meme_endpoint.check_that_status_is_200()


def test_delete_non_existent_meme(delete_meme_endpoint):
    """Удаление несуществующего мема"""
    delete_meme_endpoint.delete_non_existent_meme()
    delete_meme_endpoint.check_that_status_is_404()


def test_delete_meme_without_id(delete_meme_endpoint):
    """Удаление мема без переданного айди"""
    delete_meme_endpoint.delete_meme_without_id()
    delete_meme_endpoint.check_that_status_is_405()


def test_delete_deleted_meme(delete_meme_endpoint, create_meme_id):
    """Повторное удаление удаленного мема"""
    delete_meme_endpoint.delete_meme(create_meme_id)
    delete_meme_endpoint.delete_meme(create_meme_id)
    delete_meme_endpoint.check_that_status_is_404()
