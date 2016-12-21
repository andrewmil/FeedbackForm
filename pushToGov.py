import psycopg2
import json
from datetime import datetime, timedelta
import requests
from time import gmtime, strftime
import sys


class govDataEx():

	def __init__(self):
		# host = input("Input host ip:")
		# port = input("Input port:")
		# database = input("Input database name:")
		# user= input("Input username:")
		#password= input("Input password:")

		self.dbSQL = psycopg2.connect(database="feedback2", user="andrew", password='password', host="172.28.109.182", port="5432")
		self.cursor =  self.dbSQL.cursor()

	def send(self, sDate, eDate, url):
		self.cursor.execute("SELECT satisfaction, COUNT(satisfaction) FROM feedback WHERE timeEntered >= %s AND timeEntered <= %s GROUP BY satisfaction", (sDate,eDate))
		results = self.cursor.fetchall()

		satisfactionList=[['very dissatisfied',0], ['dissatisfied',0], ['neither',0], ['satisfied',0] ,['very satisfied',0]]

		for row in results:
			i =0
			while i<len(satisfactionList):
				if(row[0]==satisfactionList[i][0]):
					satisfactionList[i][1]=row[1]
				i+= 1
		self.dbSQL.close()

		total = satisfactionList[0][1] + satisfactionList[1][1] + satisfactionList[2][1] + satisfactionList[3][1] + satisfactionList[4][1]
		timestamp = strftime("%Y-%m-%dT%H:%M:%S", gmtime())
		period="week"
		id = "gov-wifi-user-satisfaction-"+period +"-"+ timestamp[:13]+timestamp[14:16]+timestamp[17:]
		##sending data using http POST
		data = json.dumps({'_id':id,'_timestamp':timestamp,'service':"gov-wifi", 'dataType':"user-satisfaction",'period':period,'rating_1':satisfactionList[0][1], 'rating_2':satisfactionList[1][1], 'rating_3':satisfactionList[2][1], 'rating_4':satisfactionList[3][1], 'rating_5':satisfactionList[4][1], 'total':total})
		headers = {'Content-Type':'application/json','Authorization':'Bearer abcdrandomtokenthings'}
		r = requests.post(url, data= data, headers=headers)
		if(r.status_code != 200):
			print("POST status not 'OK'")
			sys.exit(-1)
		else:
			print(r.status_code)
			print(r.content)




exchange = govDataEx()

#sDate = raw_input("select a start date for feedback (yyyy-mm-dd)")
#eDate = raw_input("select a end date for feedback (yyyy-mm-dd)")
# requestURL = input("POST request URL:")

now = datetime.now()
eDate =str(now.year) + "-" + str(now.month) + "-" +str(now.day)
eDate = datetime.strptime(eDate, "%Y-%m-%d")
sDate = eDate - timedelta(days=7)

#print("start: " + str(sDate)[:10] + "  end: " + str(eDate)[:10])
#exchange.send(str(sDate)[:10],str(eDate)[:10],'http://localhost:5000/data/ONS/satisfaction')
exchange.send(str(sDate)[:10],str(eDate)[:10],'http://requestb.in/sobcwtso')

