import tkinter
window=tkinter.Tk()
label1=tkinter.Label(window,text="username").grid(row=0)
entry1=tkinter.Entry(window).grid(row=0,column=1)
label2=tkinter.Label(window,text="password").grid(row=1)
entry2=tkinter.Entry(window).grid(row=1,column=1)
check=tkinter.Checkbutton(window,text="enter").grid(columnspan=2)
window.mainloop()