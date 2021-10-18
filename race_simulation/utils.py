
import random
import numpy as np
from collections import defaultdict

def getBootstrappedVehicles(allVehicles):
    """
    Bootstrap 6 vehicles from a list of 9 vehicles.
    Check if the bootstrapped vehicles have all types and return bootstrapped vehicles, else reiterate until true
    """
    bsVehicles = np.random.choice(list(allVehicles.keys()),replace = True, size = 6)
    bsVehicletype = set()
    for i in bsVehicles:
        bsVehicletype.add(i[:-1])
    if ('car' in bsVehicletype) and ('truck' in bsVehicletype) and ('motorcycle' in bsVehicletype):
        return bsVehicles
    getBootstrappedVehicles(allVehicles)
    

def race_simulate(bsVehicles, allVehicles, N):
    """
    Run race simulation N times for bootstrapped vehicles
    Reset odometer after every simulation
    For each vehicle, increment minute and update miles on the odometer using setOdometer() method
    Using a count dictionary to track winner in each simulation

    """
    raceWinnerCount = {}
    for i in range(N):
        raceFinished = False
        mins = 0
        try: 
            if bsVehicles is None:
                bsVehicles = getBootstrappedVehicles(allVehicles)
                continue
            else:
                for v in bsVehicles:
                    allVehicles[v].reset()
                while not raceFinished:
                    mins += 1
                    for v in bsVehicles:
                        raceFinished = allVehicles[v].setOdometer()
                        if raceFinished:
                            raceWinnerCount[v] = raceWinnerCount.get(v,0) + 1
                            break
        except:
            continue
    return getOverallWinner(raceWinnerCount, allVehicles)



def getOverallWinner(raceWinnerCount, allVehicles):
    """
    Get fastest vehicle name and vehicle properties
    """
    winner = (list(raceWinnerCount.keys())[list(raceWinnerCount.values()).index(max(raceWinnerCount.values()))])
    winnerProperties = allVehicles[winner].__dict__
    return winner, winnerProperties