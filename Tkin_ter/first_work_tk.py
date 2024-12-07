import tkinter
win=tkinter.Tk()
win.title("first window")
win.geometry("200x200")
win.maxsize(400,400)
win.minsize(100,100)
win.config(bg="red")
l1=tkinter.Label(win,text="hello",fg="blue")
l1.pack()
l1.place(x=100,y=100)
win.mainloop()

