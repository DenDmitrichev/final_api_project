import pytest


def test_check_token_is_live(check_authorize, auth_token):
    check_authorize.assert_token_valid(auth_token)


@pytest.mark.parametrize("invalid_data", [982335436, True, None, "", "124115116136161"])
def test_check_token_is_invalid_format(check_authorize, invalid_data):
    check_authorize.assert_token_invalid(invalid_data)
