import csv
import sqlite3

connection = sqlite3.connect('timeZoneList.db')
c = connection.cursor()

def fetchData():
    fullList=[]
    c.execute(f"SELECT * FROM timeZoneList")
    fullList=c.fetchall()
    return fullList






def startSQL(title, adTime, time1):
    catString=f"{adTime}{time1}"
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='timeZoneList' ''')
    if c.fetchone()[0]==1:
        print("Table exists")
    else:
        print("Table is nonexistent")
        c.execute("""CREATE TABLE timeZoneList (
                        time blob,
                        activity text                  
                        )""")

    c.execute("INSERT INTO timeZoneList VALUES (:activity, :time)", {'activity': title, 'time': catString})
    connection.commit()