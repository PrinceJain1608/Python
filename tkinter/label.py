import tkinter
window=tkinter.Tk()
window.title("label")
label=tkinter.Label(window,text="this is a label").pack()
window.geometry("600x400")
window.mainloop()