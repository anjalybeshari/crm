import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Boliboliboli777!..'

	)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE eldercoo")

print("All Done!")