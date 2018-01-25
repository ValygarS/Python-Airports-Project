from itertools import permutations
from AirportAtlas import AirportAtlas
from CurrencyRates import CurrencyRates
from CurrencyCountry import CurrencyCountry
from AircraftAtlas import AircraftAtlas
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Frame, Style
import csv


# making interface window
class BestRoute(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Finding best route between airports")
        self.master.geometry("450x280")

        self.label1 = Label(self, text = "Airport 1:")
        self.label1.place(x=10, y=25)
        self.text1 = Entry(self, name = "code 1")
        self.text1.place(x=75, y=25)
        self.label1b = Label(self, text = "Please, enter IATA code for each airport \n in CAPITAL letters. (Example: DUB)")
        self.label1b.place(x=215, y=55)

        self.label2 = Label(self, text = "Airport 2:")
        self.label2.place(x=10, y=55)
        self.text2 = Entry(self, name = "code 2")
        self.text2.place(x=75, y=55)

        self.label3 = Label(self, text = "Airport 3:")
        self.label3.place(x=10, y=85)
        self.text3 = Entry(self, name = "code 3")
        self.text3.place(x=75, y=85)

        self.label4 = Label(self, text = "Airport 4:")
        self.label4.place(x=10, y=115)
        self.text4 = Entry(self, name = "code 4")
        self.text4.place(x=75, y=115)

        self.label5 = Label(self, text = "Airport 5:")
        self.label5.place(x=10, y=145)
        self.text5 = Entry(self, name = "code 5")
        self.text5.place(x=75, y=145)

        self.button1 = Button(self, text = "Find most economic route", command = self.OnClicked)
        self.button1.place(x=75, y=180)

        Style().configure("TFrame", background="#333")

        self.label6 = Label(self, width=55, height=2, bg="#333", activebackground="gray95", wraplength=300, justify=LEFT)
        self.label6.place(x=20, y=220)

    def OnClicked(self):
        ap1 = self.text1.get()
        ap2 = self.text2.get()
        ap3 = self.text3.get()
        ap4 = self.text4.get()
        ap5 = self.text5.get()
        airportsList = [ap1, ap2, ap3, ap4, ap5]
        
        self.label6.config(state=ACTIVE, text = startFindRoute(airportsList))

airportData = AirportAtlas('airport.csv')
currencyData = CurrencyCountry('countrycurrency.csv')
exchangeData = CurrencyRates('currencyrates.csv')
aircraftData = AircraftAtlas('aircraft.csv')


# return exchange rate to EUR for selected airport
def findExchangeRate(airportCode): 
    return exchangeData._ratesDict[currencyData._countryDict[airportData.airportDict[airportCode].country]._currCode].toEuro

# function to check if route leg is longer that max plane range
def checkRoutePossible(distance):
    rangesList = []
    for key in aircraftData._aircraftDict:
        rangesList.append(aircraftData._aircraftDict[key]._range)
    longestFlight = max(rangesList)

    if longestFlight < distance:
        return False
    else:
        return True
    
# check if entry fields not empty
def checkInput(airportsList):
    counter = 0
    for item in airportsList:
        if item == "":
            counter +=1

    if counter > 0:
        return ('Please, fill in %s fields' % counter)

    else:
        return True

# check if correct airport codes entered
def checkCodes(airportsList):
    counter = 0
    for code in airportsList:
        if code not in airportData.airportDict:
            counter +=1

    if counter > 0:
        return ('%s of your codes are wrong, please check capital letters or mistakes.' % counter)

    else:
        return True

# check if any duplicate codes entered
def checkDupes(airportsList):
    if len(set(airportsList)) != len(airportsList):
        return 'Some codes are duplicates, please enter unique codes'
    
    else:
        return True

# write to csv
def writeToCsv(routeList, routeDistance, filename):
    try:
        with open(filename, 'w') as csvfile:
            fieldnames = ['Airport1', 'Airport2', 'Airport3', 'Airport4', 'Airport5', 'Distance']
            listWriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            listWriter.writeheader()
            listWriter.writerow({'Airport1':routeList[0],'Airport2':routeList[1],'Airport3':routeList[2],'Airport4':routeList[3],
                                 'Airport5':routeList[4],'Distance':routeDistance})
    except IOError:
        return 'Can"t write file!'

# function called on button click, calls other function to calculate most economical route
def startFindRoute(airportsList):
      if checkInput(airportsList) == True:
          if checkCodes(airportsList) == True:
              if checkDupes(airportsList) == True:
                  return findBestRoute(airportsList)

              else:
                  return checkDupes(airportsList)
          else:
              return checkCodes(airportsList)
      else:
          return checkInput(airportsList)
    
# main algorithm
def findBestRoute(airportsList):
    
    workingAirList = airportsList[-4:] #list for permutations
    aListNew = []   #list of airports for 1 route
    aDistancesList = [] #list of final distances for each route
    weightedDistances = []  #same as above, including weights - prices for fuel
    routesFailed = 0    #counter for failed routes, where distance exceeds plane max range
    for i in range(len(list(permutations(workingAirList)))):   #making complete list of airports for i route variant
        aListNew = [airportsList[0]]
        for item in (list(permutations(workingAirList))[i]):
            aListNew.append(item)
        aListNew.append(airportsList[0])
        distTotal = 0
        distTotalWeighted = 0
        
        #calculating distance of every segment in total route and adding it to get total distance
        
        for m in range(len(aListNew)-1):                      
            distance = airportData.getDistanceBetweenAirports(aListNew[m], aListNew[m+1])
            
        #checking if route is not longer than possible max range of an aircraft

            if checkRoutePossible(distance) == False:
                routesFailed += 1
                
                continue
            distanceWeighted = distance * findExchangeRate(aListNew[m])
            distTotal += distance
            distTotalWeighted += distanceWeighted
           
            
        aDistancesList.append(distTotal)
        weightedDistances.append(distTotalWeighted)    

    if routesFailed == len(list(permutations(workingAirList))):
        return 'Selected route is not possible, because maximum plane fleet range is shorter than one of the route leg.'

    #checking whatever is smaller: actual distance or distance with weights (fuel prices)

    if min(aDistancesList) <= min(weightedDistances):
        
        bestRouteValue = min(aDistancesList)
        
        bestRoute = [airportsList[0]]  #making list of airport for best route
        for item in (list(permutations(workingAirList))[aDistancesList.index(bestRouteValue)]):
            bestRoute.append(item)
        bestRoute.append(airportsList[0])

        bestRouteDistance = bestRouteValue
        bestRouteCost = int(weightedDistances[aDistancesList.index(bestRouteValue)])
        
    else:

        bestRouteValue = min(weightedDistances)
        
        bestRoute = [airportsList[0]]  #making list of airport for best route
        for item in (list(permutations(workingAirList))[weightedDistances.index(bestRouteValue)]):
            bestRoute.append(item)
        bestRoute.append(airportsList[0])

        bestRouteDistance = aDistancesList[weightedDistances.index(bestRouteValue)]
        bestRouteCost = int(bestRouteValue)

    writeToCsv(bestRoute, bestRouteDistance, 'bestroute.csv')
    
    return('Most economical route is: %s of %s km and cost: %s units' % (bestRoute, bestRouteDistance, bestRouteCost))
   
            

def main():
    BestRoute().mainloop()

if __name__ == "__main__":
    main()
 

    
    
