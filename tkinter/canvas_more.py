from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Python_class")

canvas = Canvas(root, width = 300, height = 300)

img = PhotoImage(file = "C:\\Users\\Prince Jain\\OneDrive\\Pictures\\Screenshots\\Screenshot 2023-08-26 230505.png")

# coordinates and then anchor direction for the image
canvas.create_image(300, 300, anchor = CENTER, image = img)

canvas.pack()

root.mainloop()