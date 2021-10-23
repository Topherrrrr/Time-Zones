import time
import tkinter as tk
from random import random
from tkinter import *
from datetime import date
from datetime import datetime
import storeValues
import multiprocessing as mp

root=tk.Tk()
root.geometry("500x500")

popupList=[]

class desktopWidget:
    def __init__(self, Modifier, Time, Description, Label):
        self.description=Description
        self.time=Time
        self.modifier=Modifier
        self.label=Label

    def updateTime(self):
        nowTime=datetime.now()
        time=nowTime.strftime("%H:%M")
        self.label.config(text=f"It is {time} in {self.description}")

#Possible times that could be added to a dropdown, and populating it with numbers 1-23
timeNums=[]
for i in range(1,24):
     timeNums.append(str(i))

#Used to determine if the time is before or after the current
timeAds=["-","+"]

#Getting data from the fields. Runs after the user hits the submit button
def getFields():
    title=timeDesc.get("1.0", "end-1c")
    time1=timeDD.get()
    adTime=time2.get()
    storeValues.startSQL(title, adTime, time1)



def updateTime():

    for i in popupList:
        r=random()
        i.config(text=f"R {r}")
        print(f"R: {r}")

    root.after(1000,updateTime)

def openAll():
    print(f"Full List: {storeValues.fetchData()}")

    for i in storeValues.fetchData():
        popup2=tk.Tk()
        popup2.geometry("200x100")
        popup2.wm_title("Filler1")
        label2=tk.Label(popup2, text=f"{i[1]}: Time zone for {i[0]}")
        label2.place(x=0, y=0)
        popupList.append(label2)
        # pool = mp.Pool()
        # p1 = pool.map_async(updateTime(label2))
  #  updateTime()




#Adding a title and brief description as to the program's function
root.title=("Add Time")
l = tk.Label(root, text ="Use this app to keep track of time in other time zones!")
l.pack()


#Writing the main line for time entry
guideLine=tk.Label(root, text="Setting a time that is                                 hours off from now")
guideLine.place(x=0,y=50)

#Time numbers dropdown
timeDD=StringVar(root)
timeGUI=OptionMenu(root, timeDD, *timeNums)
timeGUI.place(x=160,y=48)

#Adding the + or - sign dropdown
time2=StringVar(root)
time2GUI=OptionMenu(root, time2, *timeAds)
time2GUI.place(x=112,y=48)

#Adding stuff for a description input field
guide2=tk.Label(root, text="Enter a brief description for this time")
guide2.place(x=0, y=100)
timeDesc=tk.Text(root, height=5, width=52)
timeDesc.place(x=0, y=120)


#A submit button that stores the values placed in the fields
submitBTN=tk.Button(root, height=5, width=10, text="Submit time", command=lambda:getFields())
submitBTN.place(x=0, y=190)

seeBTN=tk.Button(root, height=5, width=10, text="See time", command=lambda:storeValues.fetchData())
seeBTN.place(x=0, y=300)

openWindows=tk.Button(root, height=5, width=10, text="Open all", command=lambda:openAll())
openWindows.place(x=0, y=350)

tk.mainloop()