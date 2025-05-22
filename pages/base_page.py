from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from typing import Tuple, Optional
from selenium.common.exceptions import TimeoutException


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def _wait(self, condition, timeout: Optional[int] = None):
        actual_timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, actual_timeout).until(condition)

    def _wait_for_element_presence(
        self, locator: Tuple[str, str], timeout: Optional[int] = None
    ):
        logger.info(f"Waiting for presence of element: {locator}")
        return self._wait(EC.presence_of_element_located(locator), timeout)

    def _wait_for_element_visibility(
        self, locator: Tuple[str, str], timeout: Optional[int] = None
    ):
        logger.info(f"Waiting for visibility of element: {locator}")
        return self._wait(EC.visibility_of_element_located(locator), timeout)

    def _wait_for_element_clickable(
        self, locator: Tuple[str, str], timeout: Optional[int] = None
    ):
        logger.info(f"Waiting for element to be clickable: {locator}")
        return self._wait(EC.element_to_be_clickable(locator), timeout)

    def click(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> None:
        logger.info(f"Clicking on element: {locator}")
        self._wait_for_element_clickable(locator, timeout).click()

    def get_element(self, locator: Tuple[str, str], timeout: Optional[int] = None):
        logger.info(f"Getting element: {locator}")
        return self._wait_for_element_presence(locator, timeout)

    def input_text(
        self, locator: Tuple[str, str], text: str, timeout: Optional[int] = None
    ) -> None:
        logger.info(f"Typing into element {locator}: {text}")
        element = self._wait_for_element_visibility(locator, timeout)
        element.clear()
        element.send_keys(text)

    def swipe_up(self, duration=800):
        logger.info("Swiping up")
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.4
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def is_element_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> bool:
        logger.info(f"Checking visibility of element: {locator}")
        try:
            self._wait_for_element_visibility(locator, timeout)
            return True
        except TimeoutException:
            return False

    def swipe_down_until_visible(
            self,
            locator: Tuple[str, str],
            max_swipes: int = 5,
            timeout: int = 1
    ) -> bool:
        logger.info(f"Swiping down to find element: {locator}")
        for attempt in range(max_swipes):
            if self.is_element_visible(locator, timeout):
                logger.info(f"Element found after {attempt} swipe(s): {locator}")
                return True
            self.swipe_up()
            logger.debug(f"Swiped down ({attempt + 1}/{max_swipes})")
        logger.warning(f"Element not found after {max_swipes} swipes: {locator}")
        return False
