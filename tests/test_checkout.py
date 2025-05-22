def test_basic_checkout(driver, pages):
    pages.login.login_with_credentials()

    products_page = pages.products
    products_page.select_first_product()
    selected_name = products_page.return_product_name()
    products_page.swipe_up()
    products_page.add_product_to_cart()
    products_page.go_to_cart()

    cart_page = pages.cart
    item_name_in_cart = cart_page.return_item_in_cart()
    assert selected_name == item_name_in_cart

    products_page.click_checkout()
    cart_page.enter_data_and_continue()
    cart_page.swipe_up()
    cart_page.click_finish()
    cart_page.wait_for_checkout_completion()
