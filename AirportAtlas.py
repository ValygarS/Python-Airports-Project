import csv
from Airport import Airport
class AirportAtlas:
    def __init__(self, csvFile):
        self.airportDict = {}
        self.loadData(csvFile)

    def loadData(self, csvFile):
        try:   
            with open('airport.csv') as csvFile:
                fieldnames = ['AirportID', 'AirportName', 'CityName', 'Country', 'code', 'ICAOcode', 'Latitude', 'Longitude', 'Altitude', 'TimeOffset', 'DST', 'Tz']
                reader = csv.DictReader(csvFile, fieldnames = fieldnames)
                try:
                    for row in reader:
                        self.airportDict[row['code']] = Airport(row['AirportID'], row['AirportName'], row['Country'], row['CityName'], row['Latitude'], row['Longitude'])
                except Exception:
                    pass
        except FileNotFoundError:
            print('CSV file not found!')
            
    def getAirport(self, code):
        if code in self.airportDict:
            return self.airportDict[code]
        else:
            return('No such airport code')

    def distance_on_unit_sphere(self, lat1, long1, lat2, long2):
        from math import pi, acos, sin, cos
        
        phi_a = (90 + lat1) * 2 * pi / 360
        phi_b = (90 + lat2) * 2 * pi / 360
        theta_a = long1 * 2 * pi / 360
        theta_b = long2 * 2 * pi / 360
    
        distance = acos(sin(phi_a) * sin(phi_b) * cos(theta_a - theta_b) + cos(phi_a) * cos(phi_b)) * 6371

        return int(distance)

    def getDistanceBetweenAirports(self, code1, code2):
        if code1 in self.airportDict.keys() and code2 in self.airportDict.keys():
            lat1, long1 = self.airportDict[code1].latitude, self.airportDict[code1].longitude
            lat2, long2 = self.airportDict[code2].latitude, self.airportDict[code2].longitude
            return self.distance_on_unit_sphere(lat1, long1, lat2, long2)
            
        else:
            return('No such airport codes in this program.')
            
            
#airDB = AirportAtlas('airport.csv')
#print(airDB.getDistanceBetweenAirports('BKK', 'NYC'))
