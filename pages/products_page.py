from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from loguru import logger


class ProductsPage(BasePage):
    PRODUCTS_LIST = (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
    PRODUCT_ITEMS_XPATH = "//android.view.ViewGroup[@content-desc='test-Item']"
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")

    def get_product_list(self):
        prod_list = self.get_element(self.PRODUCTS_LIST)
        prod_items = prod_list.find_elements(AppiumBy.XPATH, self.PRODUCT_ITEMS_XPATH)
        logger.info(f"Found {len(prod_items)} product(s): {prod_items}")
        return prod_items

    def return_item_from_products_list(self, index=0):
        prod_items = self.get_product_list()
        if prod_items:
            return prod_items[index]
        logger.warning("No products found in the list.")
        return None

    def get_first_product(self):
        return self.return_item_from_products_list(index=0)

    def add_product_to_cart(self):
        self.swipe_down_until_visible(self.ADD_TO_CART_BUTTON)
        self.click(self.ADD_TO_CART_BUTTON)

    def select_first_product(self):
        self.get_first_product().click()

    def go_to_cart(self):
        self.click((AppiumBy.ACCESSIBILITY_ID, "test-Cart"))

    def return_product_name(self):
        parent = self.get_element((AppiumBy.ACCESSIBILITY_ID, "test-Description"))
        text_views = parent.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView"
        )
        return text_views[0].text

    def click_checkout(self):
        self.click((AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT"))
