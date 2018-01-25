import unittest
from main import checkInput, checkCodes, checkDupes, checkRoutePossible
from AirportAtlas import AirportAtlas
from AircraftAtlas import AircraftAtlas

class MainTestMethods(unittest.TestCase):

    def setUp(self):
        print('Before the test')
        self.testAirportData=AirportAtlas('airport.csv')
        self.testAircraftData=AircraftAtlas('aircraft.csv')
    
    def test_noCodeEntered(self):

        code =""
        listCodes=[code]
        result = checkInput(listCodes)
        self.assertEqual('Please, fill in 1 fields', result)

    def test_wrongCodeEntered(self):
        
        wrongList = ['dub', 'SKg', 'MoW', 'ff']
        result = checkCodes(wrongList)
        self.assertEqual('4 of your codes are wrong, please check capital letters or mistakes.', result)

    def test_duplicatesInList(self):
        
        dupesList = ['DUB', 'MOW', 'SIN', 'HKG', 'MOW']
        result = checkDupes(dupesList)
        self.assertEqual('Some codes are duplicates, please enter unique codes', result)

    def test_checkDistancePossible(self):

        distanceOverMaxRange = 14000
        self.assertFalse(checkRoutePossible(distanceOverMaxRange))

    def tearDown(self):
        print('After the test')


if __name__ == '__main__':
    unittest.main()

