import os,sys
from utils import *
from config import Config
import logging

sys.setrecursionlimit(Config.SET_RECURSION_LIMIT)

if __name__ == '__main__':

    logger = logging.getLogger('connectivity_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(Config.LOG_FILE_PATH)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    print('------------------------------------')
    print('------------------------------------')
    sourceCity = input("Enter the source city: ")
    # Example: 'San Diego'
    destCity = input("Enter the destination city: ")
    # Example: 'Los Angeles'

    logger.info('------------------------------------')
    logger.info('Source City Input:' + sourceCity)
    logger.info('Destination City Input:' + destCity)
    logger.info('Initiating Connecting_Cities class ----')
    # Initiate class instance
    CC = Connecting_Cities(sourceCity, destCity, Config.MY_FILE_PATH)
    logger.info('Creating traversal graph ----')
    # Fetch traversal graph
    graph = CC.process_file()
    logger.info('Connectivity check running ----')
    # DFS on nodes to check for path
    res = CC.connectivity(graph)
    logger.info('Connectivity check running ...')
    logger.info('Connectivity check success!')
    logger.info(res)
    logger.info('------------------------------------')
    print('------------------------------------')
    print(CC.process_result(res))
    print('------------------------------------')