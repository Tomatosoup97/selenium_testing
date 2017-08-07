import unittest
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from order.models import Order, Product


class OrderActivationTestCase(StaticLiveServerTestCase):
    """
    Functional testing order activation
    """
    SLOW_DOWN = True

    def create_products(self, n):
        for i in range(1, n):
            Product.objects.create(
                name="Product" + str(i), description="description")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.create_products(4)
        self.driver.get(self.live_server_url + '/order/')

    def tearDown(self):
        if self.SLOW_DOWN:
            time.sleep(5)
        self.driver.quit()

    def fill_form(self, **data):
        if not data:
            data = {
                'id_name': 'name',
                'id_surname': 'surname',
                'id_email': 'example@gmail.com',
                'id_quantity': 1,
                'id_product': 1,
            }
        form = self.driver.find_element_by_css_selector(
                        'main > form')
        form_inputs = form.find_elements_by_css_selector(
                        'div .controls input')
        form_select = Select(form.find_element_by_css_selector(
                        'div .controls select'))
        for form_input in form_inputs:
            input_id = form_input.get_attribute('id')
            form_input.clear()
            form_input.send_keys(data[input_id])
            if self.SLOW_DOWN:
                time.sleep(1)

        form_select.select_by_index(data['id_product'])
        if self.SLOW_DOWN:
            time.sleep(1)
        form.submit()

    # def test_product_order_success_page(self):
    #     self.fill_form()
    #     if self.SLOW_DOWN:
    #         time.sleep(3)

    #     assert "The product have been ordered" in self.driver.title

    def test_order_activation_page(self):
        self.fill_form()

        order_id = int(self.driver.current_url.replace(
                        self.live_server_url + '/order/confirm-', ""))
        order = Order.objects.get(id=order_id)
        if self.SLOW_DOWN:
            time.sleep(3)

        self.driver.get(
            self.live_server_url + \
            '/order/confirmation/' + \
            str(order.activation_key))

        assert "Your order have been confirmed" in self.driver.title

    # def test_order_already_confirmed_page(self):
    #     self.fill_form()

    #     order_id = int(self.driver.current_url.replace(
    #                     self.live_server_url + '/order/confirm-', ""))
    #     order = Order.objects.get(id=order_id)
    #     confirmation_url = (
    #         self.live_server_url + \
    #         '/order/confirmation/' + \
    #         str(order.activation_key))
    #     self.driver.get(confirmation_url)
    #     if self.SLOW_DOWN:
    #         time.sleep(2)
    #     self.driver.get(confirmation_url)

    #     assert "This order have already been confirmed" in self.driver.title

    # def test_expired_order_key_page(self):
    #     self.fill_form()

    #     order_id = int(self.driver.current_url.replace(
    #                     self.live_server_url + '/order/confirm-', ""))
    #     order = Order.objects.get(id=order_id)
    #     order.date = order.date - datetime.timedelta(1/8) # -3 hours
    #     order.save()
    #     confirmation_url = (
    #         self.live_server_url + \
    #         '/order/confirmation/' + \
    #         str(order.activation_key))
    #     self.driver.get(confirmation_url)

    #     assert "This order key has expired" in self.driver.title


if __name__ == '__main__':
    unittest.main()
