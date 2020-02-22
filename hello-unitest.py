#!/usr/bin/python3
from selenium import webdriver
from time import sleep
import unittest

#tworze klase WSB.pl dziedziczaca po TestCase
#z modulu unittest
class WsbPlCheck(unittest.TestCase):

#warunki wstepne
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()


#wlasciwe Testowy

    def testWsb2(self):
        driver=self.driver
        driver.get('http://www.wsb.pl')
        self.assertIn("Bankowe",driver.title)
        print(driver.title)
        


#sprzatanie po tescie

    def teardown(self):
        self.driver.quit()

#jesli to glowny plik - uruchom metode main, ktora uruchomi test
if __name__ == '__main__':
    unittest.main(verbosity=2)
