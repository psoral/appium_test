from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from loguru import logger


class LoginPage(BasePage):
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "test-Error message")
    MENU = (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
    username_1 = "standard_user"
    password_1 = "secret_sauce"

    def enter_username(self, username: str = username_1):
        self.input_text(self.USERNAME, username)

    def enter_password(self, password: str = password_1):
        self.input_text(self.PASSWORD, password)

    def click_on_login_button(self):
        self.click(self.LOGIN)

    def enter_credentials(self, username: str = None, password: str = None):
        if username is not None:
            self.enter_username(username)
        if password is not None:
            self.enter_password(password)

    def login(self, username: str = username_1, password: str = password_1):
        self.enter_credential_and_login(username, password)
        self._wait_for_element_presence(self.MENU)

    def enter_credential_and_login(
        self, username: str = None, password: str = None
    ):
        logger.info(f"Logging in with credentials: {username=} {password=}")
        self.enter_credentials(username, password)
        self.click_on_login_button()

    def get_error_message(self):
        parent = self.get_element(self.ERROR_MESSAGE)
        return parent.find_element(AppiumBy.CLASS_NAME, "android.widget.TextView").text
