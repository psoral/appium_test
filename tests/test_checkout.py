def test_basic_checkout(driver, pages):
    pages.login.login_with_credentials()

    pp = pages.products
    pp.select_first_product()
    item_name = pp.return_product_name()
    pp.swipe_up()
    pp.add_product_to_cart()
    pp.go_to_cart()

    item_name_in_cart = pages.cart.return_item_in_cart()

    assert item_name == item_name_in_cart

    pp.click_checkout()

    cp = pages.cart
    cp.enter_data_and_continue()
    cp.swipe_up()
    cp.click_finish()
    cp.wait_for_checkout_completion()
