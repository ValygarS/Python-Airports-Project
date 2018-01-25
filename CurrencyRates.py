import csv
import sys
from CurrencyExchange import CurrencyExchange

class CurrencyRates:
    def __init__(self, csvFile):
        self._ratesDict = {}
        self.loadData(csvFile)

    def loadData(self, csvFile):
        try:
            with open(csvFile, encoding = 'utf-8') as csvFile:
                fieldnames = ['currency_name', 'currency_code', 'exchange_to_EUR', 'exchange_from_EUR']
                reader = csv.DictReader(csvFile, fieldnames = fieldnames)
                try:
                    for row in reader:
                        self._ratesDict[row['currency_code']] = CurrencyExchange(row['currency_name'], row['exchange_to_EUR'])
                except Exception:
                    print('Cant read row')
        except FileNotFoundError:
            print('CSV file not found!')
            sys.exit(1)

    def getCurrencyRate(self, code):
        if code in self._ratesDict:
            return(self._ratesDict[code])
        else:
            return('Currency code not in the file')
            sys.exit(1)


