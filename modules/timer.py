#Aardvark.library
from Aardvark import *
import time


@Aardvark.function('waitSeconds')
def waitSeconds(name, seconds):
    time.sleep(seconds)


@Aardvark.function('waitMinutes')
def waitMinutes(name, mins):
    time.sleep(mins * 60)


@Aardvark.function('waitHours')
def waitHours(name, hrs):
    time.sleep(hrs * 3600)


@Aardvark.function("currentTime")
def currentTime(name):
    return time.time()
