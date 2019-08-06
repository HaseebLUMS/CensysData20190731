import json
import random

def giveFileName():
	token = 'censysData_0000000000'
	# r = random.randint(0, 100)
	for r in range(0, 20):
		r = str(r)
		if len(r) == 1:
			yield token + '0' + r + '.json'
		if len(r) == 2:
			yield token + r + '.json'

def giveRecord():
	i = 1
	for file in giveFileName():
		print('file: ', i)
		i+=1
		with open(file) as f: data = f.read()
		data = data.split("\n")
		for d in data:
			try:
				d = json.loads(d)
				yield d
			except:
				pass

def getIPs():
	ips = []
	count = 0
	COUNT = 0
	ipDictionary = {}

	for ele in giveRecord():
		try:
			if ('ftpBanner' in ele) or ('telnetBanner' in ele):
				if 'description' in ele:
					ipDictionary[ele['ip']] = ele
		except:
			pass
	ipDictionary = json.dumps(ipDictionary, indent=4)
	with open('ipDictionary.json', 'w') as f: f.write(ipDictionary)
getIPs()