from datetime import timedelta
from datetime import datetime
import storeValues
import tkinter as tk

class timeWidget(object):
    def __init__(self, modifier, timeChanger, description, label):
        self.modifier=modifier
        self.timeChanger=int(timeChanger)
        self.description=description
        self.label=label
        self.negative=False


widgetList=[]

popup2 = tk.Tk()

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


def openAll():
    # Clearing the widget list
    widgetList.clear()
    print(f"Full List: {storeValues.fetchData()}")

    # Create a new widget object for each entry in the SQL table
    for i in storeValues.fetchData():
        addWidget(i[0], i[1][1], i[1][0])

    updateTime()

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

openAll()
popup2.withdraw()
popup2.mainloop()
