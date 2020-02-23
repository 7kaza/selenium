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
numer = '568303983'
email = 'karamaster.pl'
haslo = 'Diyfhiv2'
kraj = 'Polska'

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

        narodowosc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        narodowosc.click()

        polska = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//li[@data-test="PL"]')))
        polska.click()

        telefon_input = driver.find_element_by_name('phoneNumberValidDigits')
        telefon_input.send_keys(numer)

        email_input = driver.find_element_by_name('email')
        email_input.send_keys(email)

        haslo_input = driver.find_element_by_name('password')
        haslo_input.send_keys(haslo)

        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        country_to_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
        kraj_input = country_to_choose.find_elements_by_tag_name("label")

        for label in kraj_input:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == kraj:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break

        akceptacja = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        akceptacja.click()

        zarejestruj = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj.click()

#TEST oCZEKIWANEGO REZULTATU
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        # Zapisuję widoczne błędy do listy visible_error_notices
        visible_error_notices = []
        for error in error_notices:
            # Jesli jest widoczny, to dodaj do listy
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == "Nieprawidłowy adres e-mail"
    #def tearDown(self):
        #self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
