import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user='root', password = 'Apc@2007#CS')

if mydb.is_connected():
    print("Connection established")
else:
    print("Connection Failed")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE password2")

mycursor.execute("USE password2")
#mycursor.execute("CREATE TABLE manager(Website VARCHAR(15), Username VARCHAR(15), Password VARCHAR(15))")

web = "Website"
User = "Username"
pswd = "Password"

sql = "INSERT INTO manager (Website, Username, Password) VALUES (%s,%s,%s)"
val = (web,User,pswd)
mycursor.execute(sql,val)

for i in mycursor.fetchall():
    print(i)
mydb.commit()
