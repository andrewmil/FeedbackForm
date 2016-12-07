import psycopg2
import json
import requests
from time import gmtime, strftime
import uuid


class govDataEx():

	def __init__(self):
		# host = input("Input host ip:")
		# port = input("Input port:")
		# database = input("Input database name:")
		# user= input("Input username:")
		password= input("Input password:")
		
		self.dbSQL = psycopg2.connect(database="feedback2", user="andrew", password=password, host="172.28.78.195", port="5432")
		self.cursor =  self.dbSQL.cursor()  

	def send(self, sDate, eDate, url):
		self.cursor.execute("SELECT satisfaction, COUNT(satisfaction) FROM feedback WHERE timeentered >='" + sDate +"' AND timeentered <='" + eDate +"' GROUP BY satisfaction")
		results = self.cursor.fetchall()

		satisfactionList=[['very dissatisfied',0], ['dissatisfied',0], ['neither',0], ['satisfied',0] ,['very satisfied',0]]

		for row in results:
			i =0
			while i<len(satisfactionList):
				if(row[0]==satisfactionList[i][0]):
					satisfactionList[i][1]=row[1]
				i+= 1
		self.dbSQL.close()

		##sending data using http POST 
		data = json.dumps({'_id':str(uuid.uuid4()),'_timestamp':strftime("%Y-%m-%dT%H:%M:%SZ", gmtime()),satisfactionList[0][0]:satisfactionList[0][1], satisfactionList[1][0]:satisfactionList[1][1], satisfactionList[2][0]:satisfactionList[2][1], satisfactionList[3][0]:satisfactionList[3][1], satisfactionList[4][0]:satisfactionList[4][1]})
		headers = {'Content-Type':'application/json','Authorization':'Bearer abcdrandomtokenthings'}
		r = requests.post(url, data= data, headers=headers)
		print(r.status_code)
		print(r.content)

exchange = govDataEx()
	
sDate = input("select a start date for feedback (yyyy-mm-dd)")
eDate = input("select a end date for feedback (yyyy-mm-dd)")
# requestURL = input("POST request URL:")
exchange.send(sDate,eDate,'http://172.28.88.179:5000/data/ONS/satisfaction')





###############
   # satisfaction enum('very satisfied', 'satisfied', 'neither', 'unsatisfied', 'very unsatisfied'),
    # dateTime DateTime,
    # comment text,
    # surveyID int,
    # PRIMARY KEY (id)


# US		vd	d	n|	s	vs
# 87.3%	17	35	87	434	969
		# 00	25	50	75	100
# {
  # "_count": 7.0, 
  # "_end_at": "2015-12-14T00:00:00+00:00", 
  # "_start_at": "2015-12-07T00:00:00+00:00", 
  # "rating_1:sum": 8.0, 
  # "rating_2:sum": 28.0, 
  # "rating_3:sum": 53.0, 
  # "rating_4:sum": 424.0, 
  # "rating_5:sum": 877.0, 
  # "total:sum": 1390.0
# }


# ##############################EXAMPLE gov.uk api request format
# #POST /data/carers-allowance/transaction-count HTTP/1.1
# #Host: www.performance.service.gov.uk
# #Authorization: Bearer abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz01
# #Content-Type: application/json

# #[
# #  {
# #    "_id": "unique-identifier-1",
# #    "_timestamp": "2015-01-01T00:00:00Z",
# #    "count": 123
# #  },
# #  {
# #    "_id": "unique-identifier-2",
# #    "_timestamp": "2015-01-02T00:00:00Z",
# #    "count": 456
# #  }
# #]