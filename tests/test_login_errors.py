import pytest
from dataclasses import dataclass

class ERROR_MESSAGES:
    NO_MATCH = "Username and password do not match any user in this service."
    USER_REQUIRED = "Username is required"
    NO_PASS = "Password is required"

@dataclass
class LoginTestCase:
    test_name: str
    username: str
    password: str
    expected_message: str

test_cases = [
    LoginTestCase("invalid_credentials", "XYZ", "ABC", ERROR_MESSAGES.NO_MATCH),
    LoginTestCase("missing_password", "XYZ", "", ERROR_MESSAGES.NO_PASS),
    LoginTestCase("missing_username", "", "ABC", ERROR_MESSAGES.USER_REQUIRED),
]

@pytest.mark.parametrize("case", test_cases, ids=lambda c: c.test_name)
def test_login_error_messages(driver, pages, case: LoginTestCase):
    pages.login.enter_credential_and_login(case.username, case.password)
    actual_message = pages.login.get_error_message()
    assert actual_message == case.expected_message, (
        f"Expected error message '{case.expected_message}', but got '{actual_message}'"
    )