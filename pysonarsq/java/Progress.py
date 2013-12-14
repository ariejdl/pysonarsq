#!/usr/bin/env python
""" generated source for module Progress """
# package: org.yinwang.pysonar
class Progress(object):
    """ generated source for class Progress """
    startTime = long()
    total = long()
    dotInterval = long()
    reportInterval = long()
    count = long()
    mark = long()

    #@overloaded
    def __init__(self, *args):
        if len(args) == 3:
            return self.init0(*args)
        else:
            return self.init1(*args)
        
    def init0(self, dotInterval, width, total):        
        """ generated source for method __init__ """
        self.startTime = System.currentTimeMillis()
        self.dotInterval = dotInterval
        self.reportInterval = width * dotInterval
        self.total = total
        #  for calculating ETA
        self.count = 0
        self.mark = self.reportInterval

    #@__init__.register(object, long, long)
    def init1(self, dotInterval, width):
        """ generated source for method __init___0 """
        self.startTime = System.currentTimeMillis()
        self.dotInterval = dotInterval
        self.reportInterval = width * dotInterval
        self.total = -1
        self.count = 0
        self.mark = self.reportInterval

    #@overloaded
    def tick(self, n=1):
        oldCount = self.count
        self.count += n
        if self.count % self.dotInterval == 0:
            print ".",
        #  if the count goes cross the mark, report interval speed etc.
        if oldCount < self.mark and self.count >= self.mark:
            self.mark += self.reportInterval
            intervalReport()

    def end(self):
        """ generated source for method end """
        intervalReport()
        print 

    def intervalReport(self):
        """ generated source for method intervalReport """
        if self.count % self.reportInterval == 0:
            if seconds == 0:
                seconds = 1
            _.msg("\n" + self.count + " items processed" + ", time: " + _.formatTime(totalTime) + ", rate: " + self.count / seconds)
            if self.total > 0:
                _.msg("ETA: " + _.formatTime(eta * 1000))

