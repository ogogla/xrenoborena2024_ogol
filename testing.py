import tkinter
from PIL import Image, ImageTk


def quitGame(event):
    window.destroy()


window = tkinter.Tk()
window.geometry("500x500")
canvas = tkinter.Canvas(window, width=1400, height=793)
canvas.pack()
# creating background
bgImage = ImageTk.PhotoImage(Image.open("background.png"))
bg = canvas.create_image(0, 0, image=bgImage, anchor=tkinter.NW)
# creating button which supports png transparency
quitImage = ImageTk.PhotoImage(Image.open("стенки.png"))
quitButton = canvas.create_image(400, 400, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", quitGame)
window.mainloop()
