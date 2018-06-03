import json, requests

class _getdata:
	def getAllData(self, login):
		users = []
		with open('data/db.json', encoding='utf-8') as data_file:
		    users = json.loads(data_file.read())
		if users != []:
			i = 0
			while i < len(users['users']):
				if users['users'][i][1] == login:
					res = users['account'][i]
					res.append(users['users'][i][0])
					return res # returning an object
				i += 1
			return "err"
		else:
			return "db_err"
		pass

	def getMoney(self, login):
		users = []
		with open('data/db.json', encoding='utf-8') as data_file:
		    users = json.loads(data_file.read())
		if users != []:
			i = 0
			while i < len(users['account']):
				if users['account'][i][0] == login:
					users['account'][i][1] = str(float(users['account'][i][1]) + 150.00)
					file = open("data/db.json","w")
					json.dump(users ,file, indent=4)
					return "ok"
				i += 1
			return "err"
		else:
			return "db_err"

	def getCurrentRate(self):
		# Курс валют
		url = "https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22USDRUB,EURRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
		res = json.loads(requests.get(url).text)
		return res['query']['results']['rate'][0]['Rate']

	def changeUserValute(self, login):
		users = []
		with open('data/db.json', encoding='utf-8') as data_file:
		    users = json.loads(data_file.read())
		if users != []:
			i = 0
			while i < len(users['account']):
				if users['account'][i][0] == login:
					if users['account'][i][2] == "USD":
						users['account'][i][1] = str(float(users['account'][i][1]) / float(self.getCurrentRate()))
					else:
						users['account'][i][1] = str(float(users['account'][i][1]) * float(self.getCurrentRate()))
					users['account'][i][1] = str(float(users['account'][i][1]) + 150.00)
					file = open("data/db.json","w")
					json.dump(users ,file, indent=4)
					return "ok"
				i += 1
			return "err"
		else:
			return "db_err"