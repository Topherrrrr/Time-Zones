from random import random
import storeValues
import tkinter as tk

popupList=[]
popup2 = tk.Tk()


def openAll():
    print(f"Full List: {storeValues.fetchData()}")

    for i in storeValues.fetchData():
        popup2 = tk.Tk()
        popup2.geometry("200x100")
        popup2.wm_title("Filler1")
        label2 = tk.Label(popup2, text=f"{i[1]}: Time zone for {i[0]}")
        label2.place(x=0, y=0)
        popupList.append(label2)
        # pool = mp.Pool()
        # p1 = pool.map_async(updateTime(label2))
        updateTime()

def updateTime():

    for i in popupList:
        r=random()
        i.config(text=f"R {r}")
        print(f"R: {r}")

    popup2.after(1000,updateTime)

openAll()
popup2.withdraw()
popup2.mainloop()
