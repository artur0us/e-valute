import json
### ------------------------------------- ###
users = []
with open('data/db.json', encoding='utf-8') as data_file:
    users = json.loads(data_file.read())
### ------------------------------------- ###

class _reg:
	def doReg(self, login, pwd, fullname, email, phone):
		if users != []:
			i = 0
			while i < len(users['users']):
				if users['users'][i][1] == login:
					return "user_err"
				i += 1
			last_id = len(users['users'])
			new_user = [str(last_id), login, pwd, fullname, email, phone]
			new_account = [login, "-1"]
			users['users'].append(new_user)
			users['account'].append(new_account)
			file = open("data/db.json","w")
			json.dump(users ,file, indent=4)
			return "ok"
		else:
			return "db_err"
		pass