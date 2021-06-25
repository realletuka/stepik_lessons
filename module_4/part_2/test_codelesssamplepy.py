# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCodelesssamplepy():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_codelesssamplepy(self):
    self.driver.get("http://selenium1py.pythonanywhere.com/ru/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.ID, "login_link").click()
    self.driver.find_element(By.ID, "register_form").click()
    self.driver.find_element(By.ID, "id_registration-email").click()
    self.driver.find_element(By.ID, "id_registration-email").send_keys("sweetrosmarin@gmail.com")
    self.driver.find_element(By.ID, "id_registration-password1").click()
    self.driver.find_element(By.ID, "id_registration-password1").send_keys("catinhome")
    self.driver.find_element(By.ID, "id_registration-password2").click()
    self.driver.find_element(By.ID, "id_registration-password2").send_keys("catinhome")
    self.driver.find_element(By.NAME, "registration_submit").click()
  
