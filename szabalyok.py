import unittest

a=int(input("adjon megy egy számot"))
b=int(input("adjon meg még egy számot"))
szamolas=a+b
szorzas=a*b
print(szorzas)
print(szamolas)

class Testek(unittest.TestCase):
    def test_nagyobb_nulla(self):
        nagyobb=int(szamolas)
        self.assertGreater(nagyobb,0)

class Testek2(unittest.TestCase):
    def test_nagyobb_nulla(self):
        nagyobb=int(szorzas)
        self.assertGreater(nagyobb,5)

unittest.main()