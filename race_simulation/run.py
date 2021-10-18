import os,sys
from config import Config
from commons import vehicle,car,motorcycle,truck
from utils import *
import logging

sys.setrecursionlimit(10000)

if __name__ == '__main__':

    logger = logging.getLogger('connectivity_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(Config.LOG_FILE_PATH)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    # Initialize 9 vehicles - 3 cars, 3 motorcycles and 3 trucks
    print('------------------------------------')
    print('Initializing all vehicles...')
    logger.info('------------------------------------')
    logger.info('Initializing vehicles with different characteristics -----')
    carA = car('Semi','gradeAA',0,108.0,200)
    carB = car('Full','gradeA',0,115.0,220)
    carC = car('Auto','gradeB',0,130.0,225)
    motorcycleA = motorcycle('14,000','450lbs',0,98.0,180)
    motorcycleB = motorcycle('16,000','300lbs',0,102.0,160)
    motorcycleC = motorcycle('12,000','340lbs',0,100.0,190)
    truckA = truck('2276cc','8-speed',0,120.0,200)
    truckB = truck('2900cc','7-speed',0,125.0,190)
    truckC = truck('2750cc','6-speed',0,110.0,175)
    # Create a dictionary mapping vehicle names to class objects
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

    # Get bootstrapped vehicles with atleast 1 car, 1 motorcycle and 1 truck
    print('BootStrapping 6 vehicles including each type ...')
    logger.info('BootStrapping 6 Vehicles including each type -----')
    bsVehicles = getBootstrappedVehicles(allVehicles)
    logger.info('Bootstrapped Vehicles - ')
    logger.info(bsVehicles)

    # Simulate race for N Simulation
    N = Config.N_SIMULATIONS
    print('Simulating ' + str(N) + ' races between bootstrapped vehicles...')
    logger.info('Simulating ' + str(N) + ' races between bootstrapped vehicles -----')
    winner, winnerProperties = race_simulate(bsVehicles, allVehicles, N)

    # Print and log results
    print('------------------------------------')
    print('Winner vehicle:   ' + winner)
    logger.info('Winner:')
    logger.info(winner)
    print('Winning characteristics:')
    logger.info(winnerProperties)
    print(winnerProperties)
    print('------------------------------------')
   




    

       


    

    







    