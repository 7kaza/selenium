#!/usr/bin/python3
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

imie1 = 'Piotr'
nazwisko1 = 'Nowak'
gender = 'male'

class WizzarRegistration(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl#/')

    def testWrongEmail(self):

        driver =self.driver
        zaloguj_sie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//button[@data-test="navigation-menu-signin"]')))
        zaloguj_sie.click()

        rejestracja = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//button[text()=" Rejestracja "]')))
        rejestracja.click()

        imie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME,'firstName')))
        imie.send_keys(imie1)

        nazwisko = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME,'lastName')))
        nazwisko.send_keys(nazwisko1)


        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            imie.click()
            m.click()
        else:
            f = driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]')
            f.click()

        narodowosc = driver.find_element_by_xpath('//div[@class='phone-number__calling-code-selector__filled__country__name']')
        narodowosc.click()



    #def tearDown(self):
        #self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
