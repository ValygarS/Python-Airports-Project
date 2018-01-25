class Currency:
    def __init__(self, name, code):
        self._currName = name
        self._currCode = code
        
    def __str__(self):
        return('Currency name: %s. Currency code: %s' % (self._currName, self._currCode))


        
