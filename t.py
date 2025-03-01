from tkinter import *
tk = Tk()
tk.title("Triangle Movement")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.update()
guyup = PhotoImage(file = 'mit.png')
canvas.create_image(5, 5, image = guyup, anchor = NW)
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -4)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 4)
    elif event.keysym == 'Left':
        canvas.move(1, -4, 0)
    elif event.keysym == 'Right':
        canvas.move(1, 4, 0)
    elif event.keysym == 'w':
        canvas.move(2, 0, -4)
    elif event.keysym == 's':
        canvas.move(2, 0, 4)
    elif event.keysym == 'a':
        canvas.move(2, -4, 0)
    else:
        canvas.move(2, 4, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-w>', movetriangle)
canvas.bind_all('<KeyPress-s>', movetriangle)
canvas.bind_all('<KeyPress-a>', movetriangle)
canvas.bind_all('<KeyPress-d>', movetriangle)