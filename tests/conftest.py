import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dataclasses import dataclass
from decouple import config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = config("PLATFORM_NAME", default="Android")
    options.device_name = config("DEVICE_NAME",  default="emulator-5554")
    options.app = config("APK_PATH")
    options.automation_name = config("AUTOMATION_NAME", default="UiAutomator2")
    options.app_activity = config("APP_ACTIVITY")

    driver = webdriver.Remote(config("APPIUM_URL", default="http://localhost:4723"), options=options)
    yield driver
    driver.quit()


@dataclass
class PageObjects:
    login: LoginPage
    products: ProductsPage
    cart: CartPage


@pytest.fixture
def pages(driver) -> PageObjects:
    return PageObjects(
        login=LoginPage(driver),
        products=ProductsPage(driver),
        cart=CartPage(driver)
    )

