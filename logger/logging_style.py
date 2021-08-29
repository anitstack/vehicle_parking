from termcolor import colored
import logging

LOG_FILENAME = 'vehicle_parking.log'
logging.basicConfig(filename=LOG_FILENAME, format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
CHAIN1 = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
CHAIN2 = '______________________________________________________________'
CHAIN3 = '**************************************************************'


def green_log(msg):
    logging.info(colored(msg, 'green'))

def yellow_log(msg):
    logging.warning(colored(msg, 'yellow'))

def red_log(msg):
    logging.error(colored(msg, 'red'))

def orange_log(msg):
    logging.warning(colored(msg, 'orange'))

def status_update(msg):
    logging.info(colored(msg, 'cyan'))

def begin_status_update(msg):
    logging.info(colored(CHAIN1, 'green'))
    logging.info(colored(msg, 'green'))
    logging.info(colored(CHAIN1, 'green'))

def end_status_update(msg):
    logging.info(colored(CHAIN2, 'green'))
    logging.info(colored(msg, 'green'))
    logging.info(colored(CHAIN2, 'green'))

def queue_full_log(msg):
    logging.info(colored(CHAIN3, 'yellow'))
    logging.info(colored(msg, 'yellow'))
    logging.info(colored(CHAIN3, 'yellow'))
