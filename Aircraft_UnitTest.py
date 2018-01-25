import unittest
from AircraftAtlas import AircraftAtlas

class AircraftTestMethods(unittest.TestCase):

    def setUp(self):
        print('Before the test')

        self.known_values = (("A320", 12000), ("MD11", 12670))
        self.testAtlas = AircraftAtlas('aircraft.csv')

    def test_wrongCodeEntered(self):

        code = 'SU27'
        result = self.testAtlas.getAircraft(code)
        self.assertEqual('Aircraft code not in the file', result)

    def test_getAircraftRange(self):

        for code, aircraftRange in self.known_values:
            result = self.testAtlas._aircraftDict[code]._range
            self.assertEqual(result, aircraftRange)

    def test_wrongFileOpen(self):

        self.testAtlas = AircraftAtlas('file.csv')
        self.assertTrue('CSV file not found!')
        

    def tearDown(self):
        print('After the test')


if __name__ == '__main__':
    unittest.main()

