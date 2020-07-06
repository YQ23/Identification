# -*-coding: utf-8 -*-

import datetime
import logging
import sys
import time

# logging.basicConfig(level=logging.DEBUG,
#                     filename='output.log',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def RUN_TIME(deta_time):

    time_ = deta_time.seconds * 1000 + deta_time.microseconds / 1000.0
    return time_


def TIME():
    return datetime.datetime.now()


if __name__ == '__main__':
    T0 = TIME()
    # do something
    time.sleep(5)
    T1 = TIME()
    print("rum time:{}ms".format(RUN_TIME(T1 - T0)))

    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.error('Finish')