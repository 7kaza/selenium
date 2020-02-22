#!/usr/bin/python3
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select

email = 'mamo@data.com'
name = 'Anna'
lastname = 'Smith'
password = 'koty'
birthday = '28'
birthmonth = '11'
birthyear = '2018'
adress = 'Maystreet 12/1'
city = 'New York'
state = 'New York'
postcode ='10001'
country = 'United States'
phone = '5638091'

class APRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(3)

    def testCorrectRegistration(self):

        #1.Odnajdz sing in
        driver = self.driver
        sign_in = driver.find_element_by_class_name('login')
        #Kliknij
        sign_in.click()

        #2.wpisz adress email
        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(email)

        #3.kliknik przycisk
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        #sleep(2)

        #4.wybieramy plec
        gender=driver.find_element_by_id('id_gender2')
        gender.click()

        #5.wpisac imie
        name_input=driver.find_element_by_id('customer_firstname')
        name_input.send_keys(name)

        #6.wpisac nazwisko
        lastname_input=driver.find_element_by_id('customer_lastname')
        lastname_input.send_keys(lastname)

        #7.Sprawdzenie maila
        email_potem = driver.find_element_by_id('email')
        email_fact = email_potem.get_attribute('value')
        assert email == email_fact
        self.assertEqual(email, email_fact)

        #8.Niepoprawne haslo
        password_input=driver.find_element_by_id('passwd')
        password_input.send_keys(password)

        #9.Data urodzenia
        day_of_birth_select = Select(driver.find_element_by_id('days'))
        day_of_birth_select.select_by_value(birthday)

        month_of_birth_select = Select(driver.find_element_by_id('months'))
        month_of_birth_select.select_by_value(birthmonth)

        year_of_birth_select = Select(driver.find_element_by_id('years'))
        year_of_birth_select.select_by_value(birthyear)

        #10.Sprawdzic imie
        name_next = driver.find_element_by_id('firstname')
        name_fact = name_next.get_attribute('value')
        self.assertEqual(name,name_fact)

        #11.Sprawdzic nazwisko
        lastname_next = driver.find_element_by_id('lastname')
        lastname_fact = lastname_next.get_attribute('value')
        self.assertEqual(lastname,lastname_fact)

        #12. Podaj adress
        adress_input=driver.find_element_by_id('address1')
        adress_input.send_keys(adress)

        #13.Podaj miasto
        city_input = driver.find_element_by_id('city')
        city_input.send_keys(city)

        #14.Podaj stan
        state_select = Select(driver.find_element_by_id('id_state'))
        state_select.select_by_visible_text(state)

        #15.Kod pocztowy
        postcode_input = driver.find_element_by_id('postcode')
        postcode_input.send_keys(postcode)

        #16.kraj
        country_select = Select(driver.find_element_by_id('id_country'))
        country_select.select_by_visible_text(country)

        #17.telefon
        phone_input = driver.find_element_by_id('phone_mobile')
        phone_input.send_keys(phone)

        #18. Allias
        alias_input = driver.find_element_by_id('alias')
        alias_input.send_keys('alias')

        #19.Zapisz sie

        sleep(5)


    #def tearDown(self):
        #self.driver.quit()


if __name__ == '__main__':
        unittest.main(verbosity=2)
