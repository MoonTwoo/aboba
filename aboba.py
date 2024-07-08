from tkinter import *
from tkinter import ttk
import random
from  tkinter.messagebox import showinfo, askyesnocancel

Window = Tk()
Comp = PhotoImage(file = "Нолики\Нолик Синий.png")
pystoi = PhotoImage(file = "Пустой.png")
igrok = PhotoImage(file = "Крестики\Крестик Красный.png")
nolic = PhotoImage(file = "Нолики\Нолик Синий.png")
krestik = PhotoImage(file = "Крестики\Крестик Красный.png")
mas = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
masIgrok = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
masComp = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]

def Sosdanie():
    Window1.withdraw()
    global pystoi
    global igrok
    def zapolni1(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 0, column = 0)
        mas[0][0]=1
        masIgrok[0][0] = 1
        s_masivom()
        win_Igrok()
    def zapolni2(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 1, column = 0)
        mas[0][1]=1
        masIgrok[0][1]=1
        s_masivom()
        win_Igrok()
    def zapolni3(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 2, column = 0)
        mas[0][2]=1
        masIgrok[0][2]=1
        s_masivom()
        win_Igrok()
    def zapolni4(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 0, column = 1)
        mas[1][0]=1
        masIgrok[1][0]=1
        s_masivom()
        win_Igrok()
    def zapolni5(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 1, column = 1)
        mas[1][1]=1
        masIgrok[1][1]=1
        s_masivom()
        win_Igrok()
    def zapolni6(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 2, column = 1)
        mas[1][2]=1
        masIgrok[1][2]=1
        s_masivom()
        win_Igrok()
    def zapolni7(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 0, column = 2)
        mas[2][0]=1
        masIgrok[2][0]=1
        s_masivom()
        win_Igrok()
    def zapolni8(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 1, column = 2)
        mas[2][1]=1
        masIgrok[2][1]=1
        s_masivom()
        win_Igrok()
    def zapolni9(): 
        global igrok
        label1 = ttk.Label(Window2, image = igrok).grid(row = 2,column = 2)
        mas[2][2]=1
        masIgrok[2][2]=1
        s_masivom()
        win_Igrok()

    def s_masivom():
        global mas
        a=0
        for i in range(len(mas)):
            for j in range(len(mas[i])):
                a+=mas[i][j]
        if a!=9:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            while mas[x][y]!=0:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            label = ttk.Label(Window2, image = Comp).grid(row = y, column = x)
            mas[x][y]=1
            masComp[x][y]=1
    winstr=""
    def win_Comp():
        def filee1():
            f = open("Статистика побед Компьютера.txt", "a+")
            x = f.read()
            x+="0"
            f.write(x)
            f.close()

        global winstr
        global masComp
        if masComp[0][0] == masComp[0][1] == masComp[0][2] == 1 or masComp[1][0] == masComp[1][1] == masComp[1][2] == 1 or masComp[2][0] == masComp[2][1] == masComp[2][2] == 1:
            winstr ="Победил комп, ты лох "
            filee1()
            Win()
        elif masComp[0][0] == masComp[1][0] == masComp[2][0] == 1 or masComp[0][1] == masComp[1][1] == masComp[2][1] == 1 or masComp[0][2] == masComp[1][2] == masComp[2][2] == 1:
            winstr ="Победил комп, ты лох "
            filee1()
            Win()
        elif masComp[0][0] == masComp[1][1] == masComp[2][2] == 1 or masComp[2][0] == masComp[1][1] == masComp[0][2] == 1:
            winstr ="Победил комп, ты лох "
            filee1()
            Win()
        elif mas==[[1,1,1],[1,1,1],[1,1,1]]:
            winstr = "НИЧЬЯ "
            f = open("Статистика Ничья.txt", "a+")
            x = f.read()
            x+="0"
            f.write(x)
            f.close()
            Win()

    def win_Igrok():
        def filee():
            f = open("Статистика побед Игрока 1.txt", "a+")
            x = f.read()
            x+="0"
            f.write(x)
            f.close()

        global winstr
        global masIgrok
        if masIgrok[0][0]==masIgrok[0][1]==masIgrok[0][2]==1 or masIgrok[1][0]==masIgrok[1][1]==masIgrok[1][2]==1 or masIgrok[2][0]==masIgrok[2][1]==masIgrok[2][2]==1:
            winstr ="Ты победил! "
            filee()
            Win()
        elif masIgrok[0][0]==masIgrok[1][0]==masIgrok[2][0]==1 or masIgrok[0][1]==masIgrok[1][1]==masIgrok[2][1]==1 or masIgrok[0][2]==masIgrok[1][2]==masIgrok[2][2]==1:
            winstr ="Ты победил! "
            filee()
            Win()
        elif masIgrok[0][0]==masIgrok[1][1]==masIgrok[2][2]==1 or masIgrok[2][0]==masIgrok[1][1]==masIgrok[0][2]==1:
            winstr ="Ты победил! "
            filee()
            Win()
        else:
            win_Comp()
    def Win():
        global winstr
        global Window3
        Window3 = Tk()
        Window3.geometry("300x200")
        Window3.minsize(300,200)
        Window3.maxsize(300,200)
        f = open("Статистика побед Игрока 1.txt", "r")
        label1 = ttk.Label(Window3, text = winstr+"Хотите начать заново?").pack()
        btn_Yes = ttk.Button(Window3, text= "Да",command=clickbtn1).pack()
        btn_No = ttk.Button(Window3, text = "Нет", command=lambda: Window3.destroy()).pack()

    global Window2
    Window2 = Toplevel()
    Window2.protocol("WM_DELETE_WINDOW", lambda: Window1.destroy())
    Window2.geometry("400x400")
    Window2.minsize(400,400)
    Window2.maxsize(400,400)
    btn1 = ttk.Button(Window2, image = pystoi, command = zapolni1).grid(column = 0, row = 0)
    btn2 = ttk.Button(Window2, image = pystoi, command = zapolni2).grid(column = 0, row = 1)
    btn3 = ttk.Button(Window2, image = pystoi, command = zapolni3).grid(column = 0, row = 2)
    btn4 = ttk.Button(Window2, image = pystoi, command = zapolni4).grid(column = 1, row = 0)
    btn5 = ttk.Button(Window2, image = pystoi, command = zapolni5).grid(column = 1, row = 1)
    btn6 = ttk.Button(Window2, image = pystoi, command = zapolni6).grid(column = 1, row = 2)
    btn7 = ttk.Button(Window2, image = pystoi, command = zapolni7).grid(column = 2, row = 0)
    btn8 = ttk.Button(Window2, image = pystoi, command = zapolni8).grid(column = 2, row = 1)
    btn9 = ttk.Button(Window2, image = pystoi, command = zapolni9).grid(column = 2, row = 2)

def krestiki():
    global igrok
    global Comp
    Comp = PhotoImage(file = "Нолики\Нолик Синий.png")
    igrok = PhotoImage(file = "Крестики\Крестик Красный.png")
    Sosdanie()
def nolici():
    global Window1 
    global igrok
    global Comp
    Comp = PhotoImage(file = "Крестики\Крестик Красный.png")
    igrok = PhotoImage(file = "Нолики\Нолик Синий.png")
    Sosdanie()

def clickbtn1():
    Window.withdraw()
    global mas
    global masIgrok
    global masComp
    global nolic
    mas = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
    masIgrok = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
    masComp = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
    global Window1
    Window1 = Toplevel()
    Window1.protocol("WM_DELETE_WINDOW", lambda: Window.destroy())
    Window1.protocol("WM_DELETE_WINDOW", lambda: Window2.destroy())
    Window1.protocol("WM_DELETE_WINDOW", lambda: Window3.destroy())
    Window1.geometry("400x400")
    Window1.minsize(400,400)
    Window1.maxsize(400,400)
    lbl = ttk.Label(Window1, text="Выберите команду").pack(side = TOP)
    btnnolic = ttk.Button(Window1, image = nolic, command = nolici).pack(side = LEFT)
    btnkrestik = ttk.Button(Window1, image = krestik, command = krestiki).pack(side = RIGHT)

def Status():
    WindowStatus = Tk()
    WindowStatus.geometry("400x400")
    WindowStatus.minsize(400,400)
    WindowStatus.maxsize(400,400)

    f = open("Статистика побед Игрока 1.txt", "r+")
    x = f.read()
    x1 = len(x)
    str(x1)
    StatusIgrok = "Побед игрока 1 = ", x1
    label = ttk.Label(WindowStatus, text = StatusIgrok).pack()

    f = open("Статистика побед Компьютера.txt", "r+")
    y = f.read()
    y1 = len(y)
    str(y1)
    StatusIgrok = "Побед компьютера = ", y1
    label = ttk.Label(WindowStatus, text = StatusIgrok).pack()

    f = open("Статистика Ничья.txt", "r+")
    z = f.read()
    z1 = len(z)
    str(z1)
    StatusIgrok = "Ничья = ", z1
    label = ttk.Label(WindowStatus, text = StatusIgrok).pack()

Goose =  PhotoImage(file="Гусь.png")
label = ttk.Label(Window, image=Goose).pack()
btn1 = ttk.Button(text="Начать игру", command=clickbtn1).pack()
btn2 = ttk.Button(text ="Статистика", command = Status).pack()
Window2 = Tk()
Window2.withdraw()
Window3 = Tk()
Window3.withdraw()
Window.geometry("400x400")
Window.minsize(400,400)
Window.maxsize(400,400)
Window.mainloop()