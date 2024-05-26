# Import libraries

from tkinter import *
from time import strftime
import subprocess


#! Pembuatan window (Rafi Ramdhani)

root = Tk()
root.title('TOOLS LAUNCHER')
root.resizable(False, False) 
root.config(bg = '#CCDBDC')


#! Pembuatan Icon Window (Rafi Ramdhani)

app_icon = PhotoImage(file = 'Images/Icons/launchericon.png')
root.iconphoto(False, app_icon)


#? Function pembukaan file aplikasi dan penutupan launcher (Danendra)

def whiteboard():
   root.destroy()
   subprocess.call(['python', 'Programs/whiteboard.prm'])

def kalkulator():
   root.destroy()
   subprocess.call(['python', 'Programs/kalkulator.prm'])

def notepad():
   root.destroy()
   subprocess.call(['python', 'Programs/notepad.prm'])

def todo():
   root.destroy()
   subprocess.call(['python', 'Programs/todolist.prm'])


#^ Function animasi tombol (Rafie Rojagat)

def on_enter(event):
   event.config(relief = SUNKEN)

def on_leave(event):
   event.config(relief = RAISED)


#^ Pembuatan dan penempatan label menggunakan grid (Rafie Rojagat)

teks_kanvas = Label(root, text = 'TOOLS LAUNCHER', bg = '#CCDBDC', font = ('Helvetica', 18, 'bold'), anchor = 'e', justify = LEFT)
teks_kanvas.grid(row = 0, column = 0)

jam = Label(root, font = ('Helvetica', 18, 'bold'), bg = '#CCDBDC', fg = '#BA1F33')
jam.grid(row = 0, column = 1)


#! Function format dan loop jam (Rafi Ramdhani)

def display():
   jam.config(text = strftime(' %H:%M:%S %p '))
   jam.after(1, display)

display()


#? Pembuatan dan penempatan semua tombol serta penggabungan dengan aktivasi function animasi serta pembukaan file aplikasi dan penutupan launcher (Danendra)

whiteboard_icon = PhotoImage(file = 'Images/whiteboard.png')
tombol_whiteboard = Button(root, image = whiteboard_icon, width = 225, height = 100, bg = '#9AD1D4', command = whiteboard)
tombol_whiteboard.grid(row = 1, column = 0, padx = 10, pady = 10)
tombol_whiteboard.bind('<Enter>', lambda x: on_enter(tombol_whiteboard))
tombol_whiteboard.bind('<Leave>', lambda x: on_leave(tombol_whiteboard))

kalkulator_icon = PhotoImage(file = 'Images/calculator.png')
tombol_kalkulator = Button(root, image = kalkulator_icon, width = 225, height = 100, bg = '#80CED7', command = kalkulator)
tombol_kalkulator.grid(row = 1, column = 1, padx = 10, pady = 10)
tombol_kalkulator.bind('<Enter>', lambda x: on_enter(tombol_kalkulator))
tombol_kalkulator.bind('<Leave>', lambda x: on_leave(tombol_kalkulator))

notepad_icon = PhotoImage(file = 'Images/notepad.png')
tombol_notepad = Button(root, image = notepad_icon, width = 225, height = 100, bg = '#003249', command = notepad)
tombol_notepad.grid(row = 2, column = 0, padx = 10, pady = 10)
tombol_notepad.bind('<Enter>', lambda x: on_enter(tombol_notepad))
tombol_notepad.bind('<Leave>', lambda x: on_leave(tombol_notepad))

todo_icon = PhotoImage(file = 'Images/todolist.png')
tombol_todo = Button(root, image = todo_icon, width = 225, height = 100, bg = '#007EA7', command = todo)
tombol_todo.grid(row = 2, column = 1, padx = 10, pady = 10)
tombol_todo.bind('<Enter>', lambda x: on_enter(tombol_todo))
tombol_todo.bind('<Leave>', lambda x: on_leave(tombol_todo))


#! Aktivasi function format dan loop jam (Rafi Ramdhani)

display()


# Pembuatan aplikasi

root.mainloop()