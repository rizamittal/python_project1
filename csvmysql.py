import pandas as pd

df = pd.read_csv(r'C:\Users\Consultants\Desktop\customers.csv')

print(df)
import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
                       user='riza',
                       password ='password',
                       database ='db1')
cursor = db1.cursor()

csv_data = csv.reader(file('customers.csv'))
for row in csv_data:

    cursor.execute('SELECT * FROM customers')
#close the connection to the database.
db1.commit()
cursor.close()
print ("Done")