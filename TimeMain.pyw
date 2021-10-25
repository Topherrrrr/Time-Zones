import tkinter as tk
from tkinter import *
from datetime import timedelta
from datetime import datetime
import storeValues

root=tk.Tk()
root.title('Time Zone App')
root.geometry("500x300")

class timeWidget(object):
    def __init__(self, modifier, timeChanger, description, label, tkRoot):
        self.modifier=modifier
        self.timeChanger=int(timeChanger)
        self.description=description
        self.label=label
        self.negative=False
        self.tkRoot=tkRoot

#A list of timeWidget objects
widgetList=[]

#Possible times that could be added to a dropdown, and populating it with numbers 1-23
timeNums=[]
for i in range(1,24):
     timeNums.append(str(i))

#Used to determine if the time is before or after the current
timeAds=["-","+"]

def addWidget(title, time1, adTime):
    popup2 = tk.Tk()

    # Setting size and window title
    popup2.geometry("200x100")
    popup2.wm_title("Filler1")

    # Creating a new label and timeWidget object with the provided values
    description = title
    timeModifier = time1
    symbol = adTime
    label2 = tk.Label(popup2, text=f" Time zone for {description}")
    label2.place(x=0, y=0)
    newTimeWidget = timeWidget(symbol, timeModifier, description, label2, popup2)

    # Adding the new widget to the list and begin updating the time every minute
    widgetList.append(newTimeWidget)
    updateTime()

#Getting data from the fields. Runs after the user hits the submit button
def getFields():
    #Getting values from all of the input fields
    title=timeDesc.get("1.0", "end-1c")
    time1=timeDD.get()
    adTime=time2.get()

    #Creating a new SQL entry with the provided values
    storeValues.startSQL(title, adTime, time1)

    #Creating a popup window to display the new time event
    addWidget(title, time1, adTime)


#Updates the time. Is called once, then runs every second
def updateTime():

    #For each active widget
    for i in widgetList:
        #If the modifier is "-", subtract instead of add
        if i.modifier=="-" and i.negative==False:
            i.timeChanger*=-1
            i.negative=True

        #How many hours difference, input by the user
        hours=i.timeChanger
        hoursAdded=timedelta(hours=hours)

        #Modifying the time
        futureTime=datetime.now()+hoursAdded

        #Getting the hours and minutes from the new time
        mins=futureTime.minute
        hours=futureTime.hour

        #If the minutes are 0-9, add a 0 to the start time
        #Without this, the time might look something like "1:9" instead of "1:09"
        if mins <10:
            mins="0"+str(mins)

        #Updating the label
        i.label.config(text=f"{hours}:{mins}\t{i.description}")

    #Setting this function to run every second
    root.after(1000,updateTime)

#Getting all objects in the SQL table
def openAll():

    #Clearing the widget list
    widgetList.clear()
    print(f"Full List: {storeValues.fetchData()}")

    #Create a new widget object for each entry in the SQL table
    for i in storeValues.fetchData():
        addWidget(i[0], i[1][1], i[1][0])

    updateTime()




#Adding a title and brief description as to the program's function
root.title=("Add Time")
l = tk.Label(root, text ="Use this app to keep track of time in other time zones!")
l.pack()


#Writing the main line for time entry
guideLine=tk.Label(root, text="Setting a time that is                                 hours off from now")
guideLine.place(x=30,y=50)

#Time numbers dropdown
timeDD=StringVar(root)
timeGUI=OptionMenu(root, timeDD, *timeNums)
timeGUI.place(x=190,y=48)

#Adding the + or - sign dropdown
time2=StringVar(root)
time2GUI=OptionMenu(root, time2, *timeAds)
time2GUI.place(x=142,y=48)

#Adding stuff for a description input field
guide2=tk.Label(root, text="Enter a brief description for this time")
guide2.place(x=30, y=100)
timeDesc=tk.Text(root, height=5, width=52)
timeDesc.place(x=30, y=120)


#A submit button that stores the values placed in the fields
submitBTN=tk.Button(root, height=2, width=10, text="Submit time", command=lambda:getFields())
submitBTN.place(x=76, y=210)

openWindows=tk.Button(root, height=2, width=10, text="Open all", command=lambda:openAll())
openWindows.place(x=280, y=210)

tk.mainloop()