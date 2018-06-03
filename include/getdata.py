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
        percent = int(int(day)*2)
    
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