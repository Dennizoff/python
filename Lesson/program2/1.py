from tkinter import *
w=Tk()

w.title("Моє вікно")

w.geometry("500x500")
def multi(e):
    num1 = entery1.get()
    num2 = entery2.get()
    if num1 == "" or num2 == "":
        label1.config(text=f"одне або два поля пусті")
    else:
        num1 = int(num1)
        num2 = int(num2)
        label1.config(text=f"{num1} * {num2} = {num1*num2}")


def sizeAdd(e):
    global size
    size += 1
def sizeMinus(e):
    global size, img1
    size += 1
    img1 = img1.subsample(size, size)
    label2 = Label(w, image=img1)
    label2.place(x=100, y=200)
    
size = 1
img1 = PhotoImage(file="pictures/car2.png")



entery1 = Entry(w, width=10, font=50)
entery1.place(x=10, y=10)
entery2 = Entry(w, width=10, font=50)
entery2.place(x=130, y=10)

btn1 = Button(w, text="помножити")
btn1.place(x=250, y=10)
btn1.bind("<Button-1>", multi)

label1 = Label(w, text=f"Натисніть кнопку")
label1.place(x=50, y=100)







btn2 = Button(w, text="Збільшити")
btn2.place(x=250, y=100)
btn2.bind("<Button-1>", sizeAdd)

btn3 = Button(w, text="Зменшити")
btn3.place(x=350, y=100)
btn3.bind("<Button-1>", sizeMinus)

w.mainloop()