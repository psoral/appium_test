from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartPage(BasePage):
    TEST_ITEM = (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    FIRST_NAME = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    POSTAL_CODE = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    FINISH = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")

    def wait_for_item(self):
        self._wait_for_element_presence(self.TEST_ITEM)

    def enter_first_name(self, first_name: str = "FN"):
        self.input_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name: str = "LN"):
        self.input_text(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code: str = "12345"):
        self.input_text(self.POSTAL_CODE, postal_code)

    def click_on_continue(self):
        self.click(self.CONTINUE)

    def enter_data_and_continue(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_postal_code()
        self.click_on_continue()

    def click_finish(self):
        self.click(self.FINISH)

    def return_item_in_cart(self):
        self.wait_for_item()
        parent = self.get_element((AppiumBy.ACCESSIBILITY_ID, "test-Description"))
        text_views = parent.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView"
        )
        return text_views[0].text

    def wait_for_checkout_completion(self):
        self.get_element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT: COMPLETE!"]')
        )
