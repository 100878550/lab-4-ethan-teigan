#Names: Teigan Pritchard, Ethan Smallwood
#Program Name: test_Lab4_Ethan_Teigan.py
#Date: 03/14/2025
#Description: selenium testing code for a body fat calculator

# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestBodyFatIndex:

  def setup_method(self,method):
    # Initialize the WebDriver
    self.driver = webdriver.Chrome()
    self.driver.set_window_size(1936,1048)
  
  def teardown_method(self,method):
     self.driver.quit()

  def test_lab4EthanTeiganFemale(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    time.sleep(3)
    
    gender = "male"

    male_radio = self.driver.find_element(By.ID, "csex1")
    female_radio = self.driver.find_element(By.ID, "csex2")


    if gender == "female":

      self.driver.execute_script("arguments[0].click();", female_radio)
      self.driver.find_element(By.NAME, "cage").clear()
      self.driver.find_element(By.NAME, "cage").send_keys("40")
      self.driver.find_element(By.NAME, "cweightkgs").clear()
      self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
      self.driver.find_element(By.ID, "cheightmeter").clear()
      self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
      self.driver.find_element(By.ID, "cneckmeter").clear()
      self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
      self.driver.find_element(By.ID, "cwaistmeter").clear()
      self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
      self.driver.find_element(By.ID, "chipmeter").clear()
      self.driver.find_element(By.ID, "chipmeter").send_keys("100")
      time.sleep(3)
      self.driver.find_element(By.NAME,"x").click()
      result_text = self.driver.find_element(By.XPATH, "//div[@class='rightresult']").text
      assert "Body Fat: 23.0%" in result_text, "Unexpected result for female"
      print("Body Fat Calculation Result:", result_text)
      
    else:
      self.driver.execute_script("arguments[0].click();", male_radio)
      self.driver.find_element(By.NAME, "cage").clear()
      self.driver.find_element(By.NAME, "cage").send_keys("15")
      self.driver.find_element(By.NAME, "cweightkgs").clear()
      self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
      self.driver.find_element(By.ID, "cheightmeter").clear()
      self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
      self.driver.find_element(By.ID, "cneckmeter").clear()
      self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
      self.driver.find_element(By.ID, "cwaistmeter").clear()
      self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
      self.driver.find_element(By.NAME,"x").click()
      result_text = self.driver.find_element(By.XPATH, "//div[@class='rightresult']").text
      assert "Body Fat: 60.7%" in result_text, "Unexpected result for male"
      print("Body Fat Calculation Result:", result_text)
      # Add values for male as per task requirements


  