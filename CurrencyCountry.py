import csv
import sys
from Currency import Currency

class CurrencyCountry:
    def __init__(self, csvFile):
        self._countryDict = {}
        self.loadData(csvFile)

    def loadData(self, csvFile):
        try:
            with open(csvFile, encoding = 'utf-8') as csvFile:
                reader = csv.DictReader(csvFile)
                try:
                    for row in reader:
                        self._countryDict[row['name']] = Currency(row['currency_name'], row['currency_alphabetic_code'])
                except Exception:
                    pass
                
        except FileNotFoundError:
            print('CSV file not found!')
            sys.exit(1)

    def getCountryCurrency(self, code):
        if code in self._countryDict:
             return self._countryDict[code]
        else:
            print('Country is not in the file')
            sys.exit(1)

        

