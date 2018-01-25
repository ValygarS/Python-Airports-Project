class Airport:
    def __init__(self, airportID, airportName, country, cityName, latitude, longitude):
        self.airportID = int(airportID)
        self.airportName = airportName
        self.country = country
        self.cityName = cityName
        self.latitude = float(latitude)
        self.longitude = float(longitude)      

    def __str__(self):
        return('Airport ID: %s \nAirport Name: %s \nCountry Name: %s \nCity Name: %s \nLatitude: %s\nLongitude: %s' % (self.airportID, self.airportName, self.country, self.cityName, self.latitude, self.longitude))
        
        
