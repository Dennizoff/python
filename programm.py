from tkinter import *

def multi(e):
    num1 = entry1.get()
    num2 = entry2.get()
    label.config(text=int(num1)+int(num2))



w=Tk()



w.geometry("300x300")

w.title("window")

entry1 = Entry(w,width=20)
entry1.place(x=10,y=10)

entry2 = Entry(w,width=20)
entry2.place(x=10,y=40)

button1 = Button(w,text="помножити")
button1.place(x=40,y=70)
button1.bind("<Button-1>", multi)

label = Label(w, text="glg")
label.place(x=50,y=100)

w.mainloop()