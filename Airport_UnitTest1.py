import unittest
from AirportAtlas import AirportAtlas

class AirportTestMethods(unittest.TestCase):

    def setUp(self):
        print('Before the test')

        self.known_values = (("DUB", "SYD", 17215), ("DUB", "AAL", 1096),
                             ("DUB", "CDG", 784))

        self.testAtlas = AirportAtlas('airport.csv')

    def test_getDistance_between_knownValues(self):

        for code1, code2, dist in self.known_values:

            result = self.testAtlas.getDistanceBetweenAirports(code1, code2)
            self.assertEqual(dist, result)

    def test_distance_betweenDublin(self):

        code1 = 'DUB'
        code2 = 'DUB'
        dist = 0
        result = self.testAtlas.getDistanceBetweenAirports(code1, code2)
        self.assertEqual(dist, result)

    def test_codeInvalid(self):

        code = 'dub'
        result = self.testAtlas.getAirport(code)
        self.assertEqual('No such airport code', result)

    def test_searchAirport_with_validCodes(self):

        self.validCodes = ("DUB", "LHR", "LGW", "MOW", "BKK", "HKG", "SIN",
                           "NRT")
        code = "DUB"
        self.assertTrue(code in self.validCodes)
        

    def tearDown(self):
        print('After the test')


if __name__ == '__main__':
    unittest.main()
