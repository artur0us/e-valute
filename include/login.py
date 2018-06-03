import json
### ------------------------------------- ###
users = []
with open('data/db.json', encoding='utf-8') as data_file:
    users = json.loads(data_file.read())
### ------------------------------------- ###

class _login:
	def checkUserLogin(self, login, pwd):
		if users != []:
			j = 0
			res = False
			while j < len(users['users']):
				if users['users'][j][1] == login:
					if users['users'][j][2] == pwd:
						res = True
					else:
						res = False
				j += 1
			if res == True:
				return "ok"
			else:
				return "user_err"
		else:
			return "db_err"
		pass