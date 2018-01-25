import unittest
from main import findExchangeRate
from AirportAtlas import AirportAtlas
from AircraftAtlas import AircraftAtlas
from CurrencyCountry import CurrencyCountry
from CurrencyRates import CurrencyRates

class CurrencyTestMethods(unittest.TestCase):

    def setUp(self):
        print('Before the test')
        self.testAirportData=AirportAtlas('airport.csv')
        self.testAircraftData=AircraftAtlas('aircraft.csv')
        self.testCurrencyData = CurrencyCountry('countrycurrency.csv')
        self.testExchangeData = CurrencyRates('currencyrates.csv')

    # find currency name by airport code
    def test_getCurrencyName_ByAirport(self):

        self.known_values = [('DUB','Euro'), ('LED','Russian Ruble'), ('SIN', 'Singapore Dollar')]

        for airportCode, currencyName in self.known_values:
            result = self.testCurrencyData._countryDict[self.testAirportData.airportDict[airportCode].country]._currName
            self.assertEqual(result, currencyName)

    # find exchange rate to Euro by airport code
    def test_getCurrencyExRate_ByAirport(self):

        self.known_values = [('DUB', 1), ('LHR', 1.4029), ('SIN', 0.6825)]
        for code, exchangeRate in self.known_values:
            result = findExchangeRate(code)
            self.assertEqual(result, exchangeRate)

    def tearDown(self):
        print('After the test')


if __name__ == '__main__':
    unittest.main()

