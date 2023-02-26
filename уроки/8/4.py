import tkinter

window = tkinter.Tk()

window.title("Моє вікно")

window.geometry("500x500")


# def text():
#     print("text")
def left(e):
    print("left")
    if entery1.get() > 0:
        label.configure(text=("додатнє"))
    else:
        label.configure(text=("відємне"))
       
    

def right(e):
    print("right")

def enter(e):
    print("навів")
    


# button = tkinter.Button(text="натисни на мене", command=text)
button = tkinter.Button(text="run", font=50)
button.bind("<Enter>", enter)
button.bind("<Button-1>", left)
button.bind("<Button-3>", right)

label = tkinter.Label(text="перевірка", font=50)

entery1 = tkinter.Entry(width=10, font=50)

label.grid(column=0,row=0)
entery1.grid(column=1,row=0)
button.grid(column=3,row=0)


# label.pack()
# entery1.pack()
# entery2.pack()
# button.pack()

window.mainloop()