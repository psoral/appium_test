from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from loguru import logger


class LoginPage(BasePage):
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    MENU = (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
    username_1 = "standard_user"
    password_1 = "secret_sauce"

    def enter_username(self, username: str = username_1):
        self.input_text(self.USERNAME, username)

    def enter_password(self, password: str = password_1):
        self.input_text(self.PASSWORD, password)

    def click_on_login_button(self):
        self.click(self.LOGIN)

    def enter_credentials(self, username: str = username_1, password: str = password_1):
        self.enter_username(username)
        self.enter_password(password)

    def login_with_credentials(
        self, username: str = username_1, password: str = password_1
    ):
        logger.info(f"Logging in with credentials: {username=} {password=}")
        self.enter_credentials(username, password)
        self.click_on_login_button()
        self._wait_for_element_presence(self.MENU)
