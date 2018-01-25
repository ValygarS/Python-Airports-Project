class Aircraft:
    def __init__(self, airType, units, airManufacturer, airRange):
        self.__type = airType
        self.__units = units
        self.__manufacturer = airManufacturer
        self._range = int(airRange)

    def __str__(self):
        return ('Aircraft Type: %s \nUnits: %s \nAircraft Manufacturer: %s \nAircraft Range: %s'
                % (self.__type, self.__units, self.__manufacturer, self.__range))
