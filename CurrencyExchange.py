class CurrencyExchange:
    def __init__(self, currName, toEuro):
        self._currencyName = currName
        self.toEuro = float(toEuro)
        
    def __str__(self):
        return('Currency: %s. Exchange rate to EUR: %s' % (self._currencyName, self.toEuro))
