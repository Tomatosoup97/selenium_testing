import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreatingUserTestCase(StaticLiveServerTestCase):
    """
    Testing creating new user
    """
    SLOW_DOWN = True

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.app_root_url = self.live_server_url + '/user/'
        self.driver.implicitly_wait(5)
        self.driver.get(self.app_root_url)

    def tearDown(self):
        if self.SLOW_DOWN:
            time.sleep(5)
        self.driver.quit()

    def fill_create_user_form(self, user, **data):
        if not data:
            data = {
                'id_first_name': 'first_name',
                'id_last_name': 'last_name',
                'id_username': user,
                'id_email': 'example@gmail.com',
                'id_password1': 'complex_password123',
                'id_password2': '',
            }
            data['id_password2'] = data['id_password1']

        form = self.driver.find_element_by_css_selector(
                        'main > form')
        form_inputs = form.find_elements_by_css_selector(
                        'div .controls input')

        for form_input in form_inputs:
            input_id = form_input.get_attribute('id')
            form_input.clear()
            form_input.send_keys(data[input_id])
            if self.SLOW_DOWN:
                time.sleep(1)
        if self.SLOW_DOWN:
            time.sleep(1)
        form.submit()

    def fill_sign_in_form(self, username, password):
        form = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "login_form"))
        )
        username_input = WebDriverWait(form, 5).until(
            EC.presence_of_element_located((By.NAME, "username")))

        password_input = WebDriverWait(form, 5).until(
            EC.presence_of_element_located((By.NAME, "password")))

        username_input.send_keys(username)
        password_input.send_keys(password)

        if self.SLOW_DOWN:
            time.sleep(2)

        form.submit()

    # def test_user_registration_success_page(self):
    #     self.driver.implicitly_wait(5)
    #     sign_up = self.driver.find_element_by_link_text("Sign Up")
    #     sign_up.click()
    #     self.fill_create_user_form('user1')

    #     assert "Your account has been created" in self.driver.title

    def test_user_profile_page(self):
        username = 'user1'
        sign_up = self.driver.find_element_by_link_text('Sign Up')
        sign_up.click()
        self.fill_create_user_form(username)
        user = User.objects.get(username=username)

        if self.SLOW_DOWN:
            time.sleep(2)
        self.driver.get(self.app_root_url + user.username)

        assert user.username + " - User Profile" in self.driver.title

    # def test_user_sign_in(self):
    #     username = 'user1'
    #     sign_up = self.driver.find_element_by_link_text('Sign Up')
    #     sign_up.click()
    #     self.fill_create_user_form(username)

    #     self.driver.get(self.app_root_url)
    #     sign_in = self.driver.find_element_by_link_text('Sign In')
    #     sign_in.click()
    #     self.fill_sign_in_form(username, 'complex_password123')
    #     user = User.objects.get(username=username)

    #     assert "Signed in successfully" in self.driver.title

    # def test_failed_user_sign_in(self):
    #     self.driver.get(self.app_root_url + '/sign-in/')
    #     self.fill_sign_in_form(
    #         username='non_existing_user',
    #         password='definitely_not_password')

    #     assert "Invalid login or password" in self.driver.title
