from translator import englishToFrench,frenchToEnglish
import unittest

class TEST(unittest.TestCase):
    def test01(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Merci'),'Hi')

        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Bye'),'Merci')

unittest.main()