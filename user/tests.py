import datetime, unittest, time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, LiveServerTestCase
from django.utils import timezone

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from order.models import Order, Product

class CreatingUserTestCase(StaticLiveServerTestCase):
	"""
	Testing creating new user profile
	"""
	SLOW_DOWN = False

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get(self.live_server_url + '/user/')

	def tearDown(self):
		if self.SLOW_DOWN:
			time.sleep(5)
		self.driver.quit()

	def test_(self):
		
	def test_(self):
		
	def test_(self):

