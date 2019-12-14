import unittest
import capitalize

class test_strings(unittest.TestCase):

    def test_kapitaliki(self):
        wynik = capitalize.capitalize()
        self.assertEqual(wynik, 'Ala Ma Kota')

    def test_liczenie(self):
        wynik = capitalize.count('kota')
        self.assertEqual(wynik, 1)


if __name__ == '__main__':
    unittest.main()
