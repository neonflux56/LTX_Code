
import random
import numpy as np
from collections import defaultdict
import sys
    
sys.setrecursionlimit(10000)

class vehicle:
    def __init__(self, odo_miles, avg_speed,max_speed):
        self.odo_miles = odo_miles
        self.avg_speed = avg_speed
        self.max_speed = max_speed

    def reset(self):
        self.odo_miles = 0

    def setOdometer(self):
        self.odo_miles += self.avg_speed            
        if self.odo_miles >= 1500:   # RACE_LENGTH
            return True
        self.avg_speed = random.randrange(self.avg_speed, self.max_speed)
        return False


class car(vehicle):
    def __init__(self, battery_type, odo_miles, avg_speed,max_speed):
        self.battery_type=battery_type
        super().__init__(odo_miles, avg_speed,max_speed)

class motorcycle(vehicle):
    def __init__(self, nos, odo_miles, avg_speed,max_speed):
        self.nos=nos
        super().__init__(odo_miles, avg_speed,max_speed)

class truck(vehicle):
    def __init__(self, engine_capacity, odo_miles, avg_speed,max_speed):
        self.engine_capacity=engine_capacity
        super().__init__(odo_miles, avg_speed,max_speed)


def getBootstrappedVehicles(allVehicles):
    bsVehicles = np.random.choice(list(allVehicles.keys()),replace = True, size = 6)
    bsVehicletype = set()
    for i in bsVehicles:
        bsVehicletype.add(i[:-1])
    if ('car' in bsVehicletype) and ('truck' in bsVehicletype) and ('motorcycle' in bsVehicletype):
        return bsVehicles
    getBootstrappedVehicles(allVehicles)
    

def race_simulate(bsVehicles, allVehicles, N):
    raceWinnerCount = {}
    for i in range(N):
        raceFinished = False
        mins = 0
        if bsVehicles is None:
            bsVehicles = getBootstrappedVehicles(allVehicles)
            continue
        else:
            for v in bsVehicles:
                # Reset Odometer miles
                allVehicles[v].reset()
            while not raceFinished:
                mins += 1
                for v in bsVehicles:
                    raceFinished = allVehicles[v].setOdometer()
                    if raceFinished:
                        # Logging mins etc
                        #print(v)
                        #print(mins)
                        # Store v in list
                        raceWinnerCount[v] = raceWinnerCount.get(v,0) + 1
                        break
    return getOverallWinner(raceWinnerCount, allVehicles)

def getOverallWinner(raceWinnerCount, allVehicles):
    winner = (list(raceWinnerCount.keys())[list(raceWinnerCount.values()).index(max(raceWinnerCount.values()))])
    winnerProperties = allVehicles[winner].__dict__
    return winner, winnerProperties



if __name__ == '__main__':

    carA = car('Semi',0,108.0,200)
    carB = car('Full',0,75.0,180)
    carC = car('Auto',0,130.0,240)
    motorcycleA = motorcycle('Semi',0,90.0,180)
    motorcycleB = motorcycle('Full',0,80.0,160)
    motorcycleC = motorcycle('Auto',0,110.0,190)
    truckA = truck('Semi',0,120.0,190)
    truckB = truck('Full',0,90.0,160)
    truckC = truck('Auto',0,85.0,280)

    allVehicles = defaultdict(list)
    allVehicles['carA'] = carA
    allVehicles['carB'] = carB
    allVehicles['carC'] = carC
    allVehicles['motorcycleA'] = motorcycleA
    allVehicles['motorcycleB'] = motorcycleB
    allVehicles['motorcycleC'] = motorcycleC
    allVehicles['truckA'] = truckA
    allVehicles['truckB'] = truckB
    allVehicles['truckC'] = truckC

    bsVehicles = getBootstrappedVehicles(allVehicles)

    # race for n simulations
    N = 1000
    
    winner, winnerProperties = race_simulate(bsVehicles, allVehicles, N)
    print(winner)
    print(winnerProperties)

   




    

       


    

    







    