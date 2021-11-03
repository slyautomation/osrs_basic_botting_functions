import time
class collectStats:
    def __init__(self, *args):
        self.gold = 0
        
        self.goldPerHour = 0
        self.killsPerHour = 0
        self.bossPints = 0
        self.inBossFight = None
        self.timeList = [0] 
        self.startTime = time.time()
        self.inTime = 0
        self.currTime = 0
        self.totSinStart = 0
        
    def calculateStats(self):
        '''x =  random.randint(1,120)
        self.timeList += [0] * x
        for i in range(len(self.timeList)):
            n = random.randint(17,52)
            self.timeList[i] += n'''

        '''f of x  where x = avgKillTime 
                    or
        f(x)= x*((k*Kt) - h) / x'''
        #get the avg of all kill times, and hour constant
        kills = len(self.timeList) - 1
        betweenKill = 3.734389
        avgKillTime = (sum(self.timeList) / kills) + betweenKill#x
        hInSecs = 3600#h
        
        #total kills * avg time equals avg total time spent 
        avgTotTime = (kills*(avgKillTime)) #kn and Kt
        print(kills, avgKillTime, avgTotTime, self.totSinStart)
        if self.totSinStart + avgKillTime >= hInSecs:
            
            print('over the hour mark')
        else:
            #time left in the hour given avg kill time
            tleftInH = hInSecs - self.totSinStart
            #kills left in this hour
            kLeftinH = tleftInH // avgKillTime
            print('kills possible in this hour: ' + str(kLeftinH + kills))
    
    def calcKTime(self):
        self.totSinStart = self.currTime - self.startTime
        kTime = self.currTime - self.inTime
        self.timeList.insert(0,kTime)
        print(self.totSinStart, kTime)
