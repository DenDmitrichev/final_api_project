def test_authorization_is_ok(authorization):
    authorization.auth_response()
    authorization.check_that_status_is_200()




