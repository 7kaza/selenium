import unittest
import capitalize

class test_strings(unittest.TestCase):

    def test_kapitaliki(self):
        wynik = capitalize.capitalize()
        self.assertEqual(wynik, 'Ala ma kota')

    def test_liczenie(self):
        wynik = capitalize.count('kota')
        self.assertEqual(wynik, 1)

    def test_alfabet(self):
        wynik = capitalize.isalpha()
        self.assertEqual(wynik, 'True')

    def test_cyfry(self):
        wynik = capitalize.isdigit()
        self.assertEqual(wynik, 'False')

    def test_male_litery(self):
        wynik = capitalize.islower()
        self.assertEqual(wynik, 'True')

if __name__ == '__main__':
    unittest.main()
