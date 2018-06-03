import sys, json, os, requests

from itertools import islice
### ------------------------------------- ###
users = []
with open('data/db.json', encoding='utf-8') as data_file:
    users = json.loads(data_file.read())
### ------------------------------------- ###

class _getdata:
    chance = 0.00
    rate = 0.00
    _min = 0.00
    _max = 0.00
    rub = 0.00
    usd = 300.00
    values = []
    
    def doAll(self, day):
        percent = int(day*2)
        '''self.getDays(day)
        self.getChance(day)
        self.getRate(day)
        self.getMin(day)'''
        
    '''def getChance(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 0, 1):
                print("Chance is " + str(line))
                self.chance = line[:-2]
    
    def getRate(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 1, 2):
                print("Chance is " + str(line))
                self.chance = line[:-2]
    
    def getDays(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 2, 32):
                self.values.append(line[:-2])
                
    def getMin(self, day):
        i = 0
        self._max = float(self.getMax(day))
        while i < len(self.values):
            if float(self.values[i].replace(",", ".")) > float(self._max) and float(self.values[i].replace(",", ".")) < float(self.rate):
                self._max = self.values[i]
            i += 1
        print(str(self._min))
        return "ok"
            
    
    def getMax(self, day):
        i = 0
        while i < len(self.values):
            if float(self.values[i].replace(",", ".")) > self._max and float(self.values[i].replace(",", ".")) < float(self.rate):
                self._max = self.values[i]
            i += 1
        return self._max'''
        
        '''self.getRate(day)
        print("done 1")
        self.getChance(day)
        print("done 2")
        arr = self.parseDays(day)
        print("done 3")
        print("MAx: " + str(self.parseMaxArray(arr)))
        print("done 4")
        print("Min: " + str(self.parseMinArray(arr)))'''
        
    '''def getRate(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 1, 2):
                print("Rate is " + str(line))
                self.rate = line
                
    def getChance(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 0, 1):
                print("Chance is " + str(line))
                self.chance = line
        
    def parseDays(self, day):
        filename = "data/key_files/values" + str(day) + ".json"
        with open(filename) as fin:
            for line in islice(fin, 1, 32):
                self.values.append(line[:-2])
        print(self.values)
        return self.values
    
    def parseMaxArray(self, arr):
        i = 0
        _max = 0.00
        while i < len(arr):
            if int(arr[i][:-2].replace(",", "")) > _max and int(arr[i][:-2].replace(",", "")) < int(self.rate):
                _max = arr[i][:-2]
            i += 1
        return str(_max)
    
    def parseMinArray(self, arr):
        i = 0
        _min = float(self.parseMaxArray(self.parseDays(5)).replace(",", ""))
        while i < len(arr):
            if int(arr[i][:-2].replace(",", "")) < _min and int(arr[i][:-2].replace(",", "")) > int(self.rate):
                _min = arr[i][:-2]
            i += 1
        return str(_min)'''
    
    def getEID(self, login):
        i = 0
        while i < len(users['users']):
            if users['users'][i][1] == login:
                return users['users'][i][0]
            i += 1
        return "err"
    
    def myMoney(self, login):
        i = 0
        while i < len(users['users']):
            if users['users'][i][1] == login:
                return users['users'][i][6]
            i += 1
        return "err"