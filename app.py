# 038 - Python tkinter - ADICIONAR MENUS À APLICAÇÃO
from tkinter import *


def fileNew_click():
    print('New')


root = Tk()
root.geometry('300x200')

meuMenu = Menu(root)
# meuMenu.add_command(label='File')

# Menu File
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label='New', command=fileNew_click)
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_radiobutton()
fileMenu.add_command(label='Exit')
meuMenu.add_cascade(label='File', menu=fileMenu)

# Menu Edit
fileEdit = Menu(meuMenu, tearoff=0)
fileEdit.add_command(label='Copy')
fileEdit.add_command(label='Paste')
fileEdit.add_command(label='Select All')
meuMenu.add_cascade(label='Edit', menu=fileEdit)


root.config(menu=meuMenu)

root.mainloop()
