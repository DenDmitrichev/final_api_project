def test_authorization_is_ok(authorization):
    authorization.auth_response(username="Denis123")
    authorization.check_that_status_is_200()
    authorization.check_token_validity()
    authorization.test_token_with_real_request()


def test_auth_with_empty_username_should_fail(authorization):
    """Тест: авторизация с пустым именем пользователя должна завершиться ошибкой"""
    authorization.auth_with_empty_username()
    authorization.check_that_status_is_400()
