#!/usr/bin/python3

import argparse
import math
import os


primeList = []

def isEvenOr5(candidate):
    # if the last digit is 0,2,4,6,8 or 5 its not prime
    notPrime = [0,2,4,5,6,8]
    strcand = str(candidate)
    strlen = len(strcand)
    lastchar = strcand[strlen-1]
    
    lastInt = int(lastchar)
    if lastInt == 5 and strlen ==1:
        # if the candidate = 5 then its prime.
        return False

    if lastInt in notPrime:
        return True
    else:
        return False

def sumDiv3(candidate):
    if candidate != 3 and (candidate % 3) == 0:
        return True
    else:
        return False

def divSqr(candidate, primeList):
    
    sqrRoot = math.sqrt(candidate)
    # Divide by prime numbers < sqr root
    for x in primeList:
        if x < sqrRoot and x !=1:
            if candidate % x == 0:
                return True

    return False


def main(start,stop):

#    start = int(args.start)
#    stop = int(args.stop)
    start  = int(start)
    stop  = int(stop)

    primeList = []

    for current in range(start, stop):
        if isEvenOr5(current):
            # not a prime
            continue
        if sumDiv3(current):
            #not a prime
            continue
        if divSqr(current, primeList):
            #not a prime
            continue
        else:
            primeList.append(current)

    
    return(primeList)

if __name__ == "__main__":
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--start", required=True, help='Start Number')
    # parser.add_argument("--stop", required=True, help='Stop Number')


    # args = parser.parse_args()
    # outputList = main(args)

    start = os.environ['START_INT']
    stop = os.environ['STOP_INT']

    outputList = main(start,stop)

    print(outputList)

