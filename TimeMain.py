import tkinter as tk
from tkinter import *
from datetime import date
from datetime import datetime

root=tk.Tk()
root.geometry("500x500")

#Possible times that could be added to a dropdown, and populating it with numbers 1-23
timeNums=[]
for i in range(1,24):
     timeNums.append(str(i))
print(f"Timenums: {timeNums}")

#Used to determine if the time is before or after the current
timeAds=["-","+"]

#Getting data from the fields. Runs after the user hits the submit button
def getFields():
    title=timeDesc.get("1.0", "end-1c")
    time1=timeDD.get()
    adTime=time2.get()
    print(f"{title}, {adTime}, {time1}")

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
tk.mainloop()