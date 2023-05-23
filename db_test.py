import sqlite3

Testdaten = [["2023-05-23", 5], ["2023-05-23", 12], ["2023-05-23", 17], ["2023-05-24", 18]]

connect = sqlite3.connect("datenbank.db")
cursor = connect.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS Temperaturen(Datum date, Temperatur int)")
#
# for Datum, Temperatur in Testdaten:
#     cursor.execute("INSERT INTO Temperaturen(Datum, Temperatur) VALUES (?, ?)", (Datum, Temperatur))

befehl2 =cursor.execute("SELECT MAX(Temperatur) FROM Temperaturen WHERE Datum LIKE '%24'")

print(cursor.fetchall())

befehl = cursor.execute("SELECT MIN(Temperatur), MAX(Temperatur), AVG(Temperatur) FROM Temperaturen")

print(cursor.fetchall())

connect.commit()
connect.close()