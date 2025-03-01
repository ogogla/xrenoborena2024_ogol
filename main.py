from tkinter import *
import tkinter
from tkinter import messagebox, ttk


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("BioStudy")
tk.resizable()
tk.wm_attributes("-topmost", 1)

bg = PhotoImage(file="background.png")  # СДЕЛАТЬ НОРМАЛЬНЫЙ ФОН
ccanvas = Canvas(tk, width=1400,
                 height=793)  # на весь экран должно быть
ccanvas.pack(fill="both", expand=True)
ccanvas.create_image(0, 0, image=bg, anchor="nw")


def open_map():
    pass


# кнопка перехода в теорию
our_button = PhotoImage(file="button_map.png")
# Button(tk, image=our_button, highlightthickness=0, bd=0, command=lambda: print("Clicked!")).place(x=130, y=100)
# Button(tk, image=our_button, highlightthickness=0, bd=0, command=bg_color_red).place(x=130, y=100)
id_button1 = Button(tk, image=our_button, highlightthickness=0, bd=0, command=open_map)
id_button1.place(x=428, y=221)


def next_map():
    pass


def prev_map():
    pass


# кнопки переключения карты на следующую и на предыдущую
n_button = PhotoImage(file="next.png")
id_next = Button(tk, image=n_button, highlightthickness=0, bd=0, command=next_map)
id_next.place(x=998.5, y=370.8)
p_button = PhotoImage(file="prev.png")
id_next = Button(tk, image=p_button, highlightthickness=0, bd=0, command=prev_map)
id_next.place(x=351, y=370.8)


def play_menu():
    pass


# кнопка начала игры
pl_button = PhotoImage(file="play.png")
id_play = Button(tk, image=pl_button, highlightthickness=0, bd=0, command=play_menu)
id_play.place(x=546, y=643)


def schemes():
    pass


# Все схемы
sch_button = PhotoImage(file="all_schemes.png")
id_schemes = Button(tk, image=sch_button, highlightthickness=0, bd=0, command=schemes)
id_schemes.place(x=55, y=643)


def settings():
    pass


# Настройки
set_button = PhotoImage(file="settings.png")
id_setting = Button(tk, image=set_button, highlightthickness=0, bd=0, command=settings)
id_setting.place(x=1261.3, y=47.4)


def statistics():
    pass


# Статистика
st_button = PhotoImage(file="statistics.png")
id_statistics = Button(tk, image=st_button, highlightthickness=0, bd=0, command=statistics)
id_statistics.place(x=1256.9, y=234.3)

# Опыт
bar_button = PhotoImage(file="bar.png")
id_bar = Button(tk, image=bar_button, highlightthickness=0, bd=0)
id_bar.place(x=462, y=47.4)
md_button = PhotoImage(file="medal.png")
id_medal = Label(tk, image=md_button, highlightthickness=0, bd=0)
id_medal.place(x=451.8, y=38.5)

# Шкала опыта
progres_bar = ttk.Progressbar(orient="horizontal", length=370, value=20)
progres_bar.place(x=515, y=60)

tk.mainloop()
