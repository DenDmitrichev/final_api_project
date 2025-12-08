def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.check_response_structure()


