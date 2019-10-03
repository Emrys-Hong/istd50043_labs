import requests
from db_demo import *
ADDR = "http://172.17.71.157:5000"
HEADER = {"Content-Type": "application/json"}
def test_hello():
  res = requests.get("{}/hello".format(ADDR))
  if (res.ok):
    print(res.json())
  else:
    print("Query /hello failed")

def test_greeting(name):
  res = requests.get("{}/hello/{}".format(ADDR, name))
  if (res.ok):
    print(res.json())
  else:
    print("Query /hello/<name> failed")

def test_query(msg):
  res = requests.get("{}/query".format(ADDR), json={"query": msg}, headers=HEADER)
  if (res.ok):
    print(res.json())
  else:
    print("Query /query failed")

def test_insert(msg):
  res = requests.post("{}/insert".format(ADDR), json={"data": msg}, headers=HEADER)
  if (res.ok):
    print(res.json())
  else:
    print("Query /insert failed")

