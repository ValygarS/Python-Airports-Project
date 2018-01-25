import csv
import sys
from Aircraft import Aircraft

class AircraftAtlas:
    def __init__(self, csvFile):
        self._aircraftDict = {}
        self.loadData(csvFile)

    def loadData(self, csvFile):
        try:
            with open (csvFile) as csvFile:
                reader = csv.DictReader(csvFile)
                try:
                    for row in reader:
                        self._aircraftDict[row['code']] = Aircraft(row['type'], row['units'], row['manufacturer'], row['range'])
                except Exception:
                    pass
        except FileNotFoundError:
            return('CSV file not found!')
            sys.exit(1)

    def getAircraft(self, code):
        if code in self._aircraftDict:
            return self._aircraftDict[code]
        else:
            return('Aircraft code not in the file')
            sys.exit(1)

    

    
