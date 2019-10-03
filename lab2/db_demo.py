import mysql.connector as db
from pymongo import MongoClient

DATABASE="test1"
def test_mysql(addr):
  con = db.connect(host=addr, user="root", passwd="", db=DATABASE)
  cursor = con.cursor()
  cursor.execute("describe Payroll")
  res = cursor.fetchall()
  print(res)

  cursor.execute("select * from Payroll")
  res = cursor.fetchall()
  print(res)

def test_mongo(addr):
  mc = MongoClient(addr, 27017)
  logDb = mc["test"]["scientist"]
  res = logDb.find({})
  for v in res:
    print(v)
