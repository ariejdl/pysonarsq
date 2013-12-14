#!/usr/bin/env python
""" generated source for module FancyProgress """
# package: org.yinwang.pysonar

import time

from _ import _

class FancyProgress(object):
    """ generated source for class FancyProgress """
    MAX_SPEED_DIGITS = 5
    startTime = long()
    lastTickTime = long()
    lastCount = long()
    lastRate = int()
    lastAvgRate = int()
    total = long()
    count = long()
    width = long()
    segSize = long()

    def __init__(self, total, width):
        """ generated source for method __init__ """
        self.startTime = int(round(time.time() * 1000))
        self.lastTickTime = int(round(time.time() * 1000))
        self.lastCount = 0
        self.lastRate = 0
        self.lastAvgRate = 0
        self.total = total
        self.width = width
        self.segSize = total / width
        if self.segSize == 0:
            self.segSize = 1

    #@overloaded
    def tick(self, n=1):
        """ generated source for method tick """
        self.count += n
        if self.count > self.total:
            self.total = self.count
        elapsed = int(round(time.time() * 1000)) - self.lastTickTime
        if elapsed > 500 or self.count == self.total:
            import math
            dlen = int(math.ceil(math.log10(self.total)))            
            
            print("\r")

            str_part = " (" + _.formatNumber(self.count, dlen) + " of " + _.formatNumber(self.total, dlen) + ")"
            print(_.percent(self.count, self.total) + str_part)
            
            if elapsed > 1:
                rate = int(((self.count - self.lastCount) / (elapsed / 1000.0)))
            else:
                rate = self.lastRate
            self.lastRate = rate
            print("   SPEED: " + _.formatNumber(rate, self.MAX_SPEED_DIGITS) + "/s")

            totalElapsed = int(round(time.time() * 1000)) - self.startTime
            avgRate = None
            
            if totalElapsed > 1:
                avgRate = int((self.count / (totalElapsed / 1000.0)))
            else:
                avgRate = self.lastAvgRate
            avgRate = 1 if avgRate == 0 else avgRate
            
            remain = self.total - self.count
            remainTime = remain / avgRate * 1000
            
            print("   AVG SPEED: " + _.formatNumber(avgRate, self.MAX_SPEED_DIGITS) + "/s")
            print("   ETA: " + _.formatTime(remainTime))
            print("       ")
            #  overflow area
            self.lastTickTime = int(round(time.time() * 1000))
            self.lastAvgRate = avgRate
            self.lastCount = self.count

