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
    #
    # def destroyLabel(self):
    #     self.label.destroy()

widgetList=[]

popup2 = tk.Tk()


def openAll():
    print(f"Full List: {storeValues.fetchData()}")

    for i in storeValues.fetchData():
        popup2 = tk.Tk()
        popup2.geometry("200x100")
        popup2.wm_title("Filler1")
        description = i[0]
        timeModifier = i[1][1]
        symbol = i[1][0]
        label2 = tk.Label(popup2, text=f"{i[1]}: Time zone for {i[0]}")
        label2.place(x=0, y=0)
        newTimeWidget = timeWidget(symbol, timeModifier, description, label2)

        widgetList.append(newTimeWidget)
        # pool = mp.Pool()
        # p1 = pool.map_async(updateTime(label2))
    updateTime()

def updateTime():
    now=datetime.now()
    for i in widgetList:
        if i.modifier=="-":
            i.timeChanger*=-1
        hours=i.timeChanger
        hoursAdded=timedelta(hours=hours)
        futureTime=datetime.now()+hoursAdded
        mins=futureTime.minute
        hours=futureTime.hour
        if mins <10:
            mins="0"+str(mins)
        i.label.config(text=f"{hours}:{mins}\t{i.description}")

    popup2.after(1000,updateTime)

openAll()
popup2.withdraw()
popup2.mainloop()
