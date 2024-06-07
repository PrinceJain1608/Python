import tkinter
window=tkinter.Tk()
button=tkinter.Button(window,text="button",width=20,height=10,command=window.destroy).pack()
window.mainloop()