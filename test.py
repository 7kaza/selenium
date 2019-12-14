import unittest
import capitalize

class test_strings(unittest.TestCase):

    def test_kapitaliki(self):
        wynik = capitalize.capitalize()
        self.assertEqual(wynik, 'Ala ma kota')

    def test_liczenie(self):
        wynik = capitalize.count()
        self.assertEqual(wynik, 2)

    def test_alfabet(self):
        wynik = capitalize.isalpha()
        self.assertFalse(wynik)

    def test_cyfry(self):
        wynik = capitalize.isdigit()
        self.assertTrue(wynik)

    def test_male_litery(self):
        wynik = capitalize.islower()
        self.assertFalse(wynik)

if __name__ == '__main__':
    unittest.main()
