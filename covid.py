import pymysql
import flask
from flask import Flask, render_template
from itertools import groupby
from operator import itemgetter


db = pymysql.connect("localhost","root","gayatri","test" )
cursor = db.cursor()
cursor.execute("create database test")

cursor.execute("DROP TABLE IF EXISTS Covid_Tab")
sql = "CREATE TABLE Covid_Tab ( \
   Country CHAR(20) ,\
   Date DATE,\
   Confirmed INT, Deaths INT, Recovered INT )"

cursor.execute(sql)

for country in data.keys():
    for each_country in data[str(country)]:
        country1 = str(country)
        str_date = str(each_country['date'])
        confirmed = each_country['confirmed']
        deaths = each_country['deaths']
        recovered = each_country['recovered']
        
        print (country1,str_date,confirmed,deaths,recovered)

        sql = "INSERT INTO Covid_Tab(Country, \
        Date, Confirmed, Deaths, Recovered) \
        VALUES ('%s', '%s', '%d', '%d', '%d')" %\
        (country1 , str_date , confirmed , deaths , recovered)

        try:
            cursor.execute(sql)
            db.commit()

        except:
            db.rollback()

sql = "select * from Covid_Tab where country = 'India' and month(Date) = 4 order by date desc;"
cursor.execute(sql)
data = cursor.fetchall() #data from database
data1 = list(data)
# print(type(data))
# render_template("covid_india.html", value=data)

mytuple = data1
print(mytuple)

FULL_HTML = []
for name, rows in groupby(mytuple, itemgetter(0)):
      table = []
        
      for country_name, value1, value2, value3, value4 in rows:
         table.append(
             "<tr>\
             <td>{},</td>\
             <td>{},</td>\
             <td>{},</td>\
             <td>{},</td>\
             <td>{}</td>\
             </tr>".format(name, value1, value2, value3, value4))
      table = "<table>\n{}\n</table>".format('\n'.join(table))
      FULL_HTML.append(table)
 
FULL_HTML = "<html>\n{}\n</html>".format('\n'.join(FULL_HTML))
print(len(FULL_HTML))
# print(FULL_HTML)

f1 = open("final.html","w")
f1.write(FULL_HTML)

import csv

data2 = data1

with open('covid_india.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Country','Date','Confirmed','Deaths','Recovered'])
    for row in data2:
        csv_out.writerow(row)
        
import pandas as pd 
  
# to read csv file named "samplee" 
a = pd.read_csv("covid_india.csv") 
  
# to save as html file 
# named as "Table" 
a.to_html("covid_india.htm") 
  
# assign it to a  
# variable (string) 
html_file = a.to_html() 

db.close()
