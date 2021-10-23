import tkinter as tk
from tkinter import *
from datetime import timedelta
from datetime import datetime
import storeValues

root=tk.Tk()
root.title('Time Zone App')
root.geometry("500x300")

class timeWidget(object):
    def __init__(self, modifier, timeChanger, description, label):
        self.modifier=modifier
        self.timeChanger=int(timeChanger)
        self.description=description
        self.label=label
        self.negative=False

    #
    # def destroyLabel(self):
    #     self.label.destroy()

widgetList=[]

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
    popup2 = tk.Tk()
    popup2.geometry("200x100")
    popup2.wm_title("Filler1")
    description = title
    timeModifier = time1
    symbol = adTime
    label2 = tk.Label(popup2, text=f" Time zone for {description}")
    label2.place(x=0, y=0)
    newTimeWidget = timeWidget(symbol, timeModifier, description, label2)
    widgetList.append(newTimeWidget)
    updateTime()

def updateTime():
    now=datetime.now()
    for i in widgetList:
        if i.modifier=="-" and i.negative==False:
            i.timeChanger*=-1
            i.negative=True
        hours=i.timeChanger
        hoursAdded=timedelta(hours=hours)
        futureTime=datetime.now()+hoursAdded
        mins=futureTime.minute
        hours=futureTime.hour
        if mins <10:
            mins="0"+str(mins)
        i.label.config(text=f"{hours}:{mins}\t{i.description}")

    root.after(1000,updateTime)

def openAll():
    print(f"Full List: {storeValues.fetchData()}")
    widgetList.clear()
    for i in storeValues.fetchData():
        popup2=tk.Tk()
        popup2.geometry("200x100")
        popup2.wm_title("Filler1")
        description=i[0]
        timeModifier=i[1][1]
        symbol=i[1][0]
        label2=tk.Label(popup2, text=f"{i[1]}: Time zone for {i[0]}")
        label2.place(x=0, y=0)
        newTimeWidget=timeWidget(symbol, timeModifier, description,label2)

        widgetList.append(newTimeWidget)
        # pool = mp.Pool()
        # p1 = pool.map_async(updateTime(label2))
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