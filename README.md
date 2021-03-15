# python-tkinter

Inicio: 13/02/2021 Fim:
https://www.youtube.com/playlist?list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h

```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Primeiro app')
'''
menu_inicial.geometry('300x400+600+200')
# menu_inicial.resizable(False, False)
menu_inicial.resizable(0, 0)
# menu_inicial['bg'] = 'blue'
# menu_inicial.minsize(width=250, height=250)
# menu_inicial.maxsize(400, 400)
btn = Button(menu_inicial, text='Executar')
btn.pack()
# menu_inicial.wm_attributes('-zoomed', 1)
# menu_inicial.wm_attributes('-alpha', 1)

menu_inicial.mainloop()
'''

menu_inicial = Tk()
menu_inicial.title('Primeiro app')

menu_inicial.geometry('300x400+600+200')
menu_inicial.resizable(0, 0)
btn = Button(menu_inicial, text='Executar')
btn.pack()

menu_inicial.mainloop()
```
# AULA 07
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Primeiro app')
menu_inicial.geometry('300x400+600+200')
menu_inicial.resizable(0, 0)


def cmd_click(mensagem):
    print(mensagem)


cmd = Button(menu_inicial, text='Executar',
             command=lambda: cmd_click("Nova mensagem"))
cmd.pack()

cmd2 = Button(menu_inicial, text='Clicar',
              command=lambda: print("OK"))
cmd2.pack()

menu_inicial.mainloop()
```
# AULA 08
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')

# dimnesões da janela
largura = 500
altura = 300

# resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
print(largura_screen, altura_screen)

# posicao da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
menu_inicial.resizable(False, False)

menu_inicial.mainloop()
```
# AULA 09
```
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')

label_1 = Label(menu_inicial, text='Este é o label 1.')
label_2 = Label(menu_inicial, text='Este é o label 2.')

cmd = Button(menu_inicial, text='Executar')

# pack
cmd.pack()
label_2.pack()
label_1.pack()

menu_inicial.mainloop()
```
# AULA 10
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('300x400+750+300')
label_1 = Label(menu_inicial, text='Este é o label 1.',
                bg='#ffffff',
                fg='black',
                font='Arial')
label_2 = Label(menu_inicial, text='Este é o label 2.',
                bg='#ffffff',
                fg='black',
                font='Arial 20 bold italic')
label_3 = Label(menu_inicial, text='Este é o label 3.',
                fg='#aaaaaa',
                font='Verdana 25 bold')

# pack
label_1.pack()
label_2.pack()
label_3.pack()

menu_inicial.mainloop()
```

# AULA 11
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
label_1 = Label(menu_inicial, text='Este é o label 1.',
                font='Arial 20',
                bg='red',
                width=20)
label_1.pack()
label_2 = Label(menu_inicial, text='Este é o label 1.',
                font='Arial 40',
                bg='red',
                width=20)
label_2.pack()
```

# AULA 12 
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')

border = 20
label_1 = Label(
    menu_inicial,
    text='solid',
    font='Arial 20',
    bd=border,
    relief='solid'
).pack()
label_1 = Label(
    menu_inicial,
    text='flat',
    font='Arial 20',
    bd=border,
    relief='flat'
).pack()
label_1 = Label(
    menu_inicial,
    text='raised',
    font='Arial 20',
    bd=border,
    relief='raised'
).pack()
label_1 = Label(
    menu_inicial,
    text='sunken',
    font='Arial 20',
    bd=border,
    relief='sunken'
).pack()
label_1 = Label(
    menu_inicial,
    text='ridge',
    font='Arial 20',
    bd=border,
    relief='ridge'
).pack()
label_1 = Label(
    menu_inicial,
    text='groove',
    font='Arial 20',
    bd=border,
    relief='groove'
).pack()
# label_1.pack()


menu_inicial.mainloop()
```

# AULA 13
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')

label1 = Label(
    menu_inicial,
    text='012345679',
    font='Arial 20',
    bd=2,
    relief='solid',
    width=25,
    height=4,
    anchor=NW
).pack()

menu_inicial.mainloop()
```
# AULA 14
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')

label1 = Label(
    menu_inicial,
    text='frase de testes\nteste',
    font='Arial 20',
    bd=2,
    width=50,
    height=5,
    relief='solid',
    justify=LEFT,
    anchor=NW
).pack()

label1 = Label(
    menu_inicial,
    text='frase de testes',
    font='Arial 20',
    bd=2,
    relief='solid',
    padx=50,
    pady=50
).pack()

label1 = Label(
    menu_inicial,
    text='frase de testes\noutra frase teste\ntes',
    font='Arial 20',
    bd=2,
    relief='solid',
    padx=50,
    pady=50,
    justify=CENTER
).pack()

label1 = Label(
    menu_inicial,
    text='frase de testes\noutra frase teste\ntes',
    font='Arial 20',
    bd=2,
    relief='solid',
    padx=10,
    pady=10,
    justify=LEFT
).pack()

label1 = Label(
    menu_inicial,
    text='frase de testes\noutra frase teste\ntes',
    font='Arial 20',
    bd=2,
    relief='solid',
    padx=10,
    pady=10,
    justify=RIGHT
).pack()
menu_inicial.mainloop()
```
# AULA 15
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')

label2 = Label(menu_inicial)
label2['text'] = 'Texto da label2'
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = 'solid'
label2.pack()


for item in label2.keys():
    print(item, ' : ', label2[item])

menu_inicial.mainloop()
```

# AULA 16
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')

texto = StringVar()
texto.set('Novo texto')

label1 = Label(
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto
)

label2 = Label(
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto
)

label3 = Label(
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto
)

label4 = Label(
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto
)

label1.pack()
label2.pack()
label3.pack()
label4.pack()

texto.set('João Ribeiro')

menu_inicial.mainloop()
```
# 017 - Python tkinter - INTRODUÇÃO AO LAYOUT EM GRID
```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
# menu_inicial.geometry('500x500')

label1 = Label(
    text='Label1',
    bg='red',
    font='Arial 20'
)
label2 = Label(
    text='Label2',
    bg='green',
    font='Arial 20'
)
label3 = Label(
    text='Label3',
    bg='blue',
    font='Arial 20'
)

btn1 = Button(menu_inicial, text='Click1')
btn2 = Button(menu_inicial, text='Click2')
btn3 = Button(menu_inicial, text='Click3')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

menu_inicial.mainloop()
```
# 019 - Python tkinter - QUADRO DE LOGIN COM GRID E STICKY
```python
from tkinter import *

root = Tk()
root.title('Login')

Label(root, text='Usuário').grid(row=0, sticky=W)
Label(root, text='Senha').grid(row=1, sticky=W)

txt_usuario = Entry(root).grid(row=0, column=1)
txt_login = Entry(root).grid(row=1, column=1)

cmd_login = Button(text='Login').grid(row=2, column=1, sticky=E)

root.mainloop()
```
# 020 - Python tkinter - COLUMNSPAN EM GRID
```python
from tkinter import *

root = Tk()
root.title('Login')

Label(root, text='texto',  bg='red').grid()
Label(root, text='texto',  bg='green').grid(column=1)
Label(root, text='texto',  bg='green').grid(column=2)
Label(root, text='texto',  bg='blue').grid(columnspan=3, sticky='we')

root.mainloop()

```

# 020 - Python tkinter - COLUMNSPAN EM GRID
```python
from tkinter import *

# ---------------------------------------
# funcoes


def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

# ---------------------------------------
# widgets

t3 = Entry(root)
t1 = Entry(root)
t2 = Entry(root)

l1 = Label(root)
l2 = Label(root)
l3 = Label(root)

b = Button(root, text='Executar', command=executar)


# ---------------------------------------
# layout

t1.grid()
t2.grid()
t3.grid()

l1.grid(sticky=W)
l2.grid()
l3.grid()

b.grid()

t1.focus()

root.mainloop()
```
# 021 - Python tkinter - PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS
```python
from tkinter import *


# ---------------------------------------
# funcoes
def mostrar_nome():
    l2['text'] = 'Meu nome é '+t1.get()


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

# ---------------------------------------
# widgets
l1 = Label(root, text='O seu nome:')
t1 = Entry(root)
b = Button(root, text='Executar', command=executar)
l2 = Label(root)

l1.grid()
t1.grid()
b.grid()
l2.grid()

t1.focus()

root.mainloop()

# 021 - Python tkinter - PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS
from tkinter import *


# ---------------------------------------
# funcoes
def mostrar_nome():
    l2['text'] = 'Meu nome é '+t1.get()


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

# ---------------------------------------
# widgets
l1 = Label(root, text='O seu nome:')
t1 = Entry(root)
b = Button(root, text='Executar', command=executar)
l2 = Label(root)

l1.grid()
t1.grid()
b.grid()
l2.grid()

t1.focus()

root.mainloop()


# 022 - Python tkinter - PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS
from tkinter import *


# ---------------------------------------
# funcoes
def mostrar_nome():
    vartexto.set('Seu nome é: '+textbox1.get().title())


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

vartexto = StringVar()

# ---------------------------------------
# widgets
label1 = Label(root, text='O seu nome:')
textbox1 = Entry(root)
button1 = Button(root, text='Executar', command=mostrar_nome)
label2 = Label(root, textvariable=vartexto)
label3 = Label(root, textvariable=vartexto)
label4 = Label(root, textvariable=vartexto)

# ---------------------------------------
# layout
label1.grid()
textbox1.grid()
button1.grid()
label2.grid()
label3.grid()
label4.grid()

textbox1.focus()

root.mainloop()
```

# 023 - Python tkinter - FAHRENHEIT PARA CELSIUS
```python
from tkinter import *
# ---------------------------------------
# funcoes
# C = (F- 32) * 5/9

def calcular_celsius():
    f = float(textbox1.get())
    c = (f - 32) * 5/9
    var_celsius.set(str(round(c, 2))+' graus Celsius')


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')
var_celsius = StringVar()
# ---------------------------------------
# widgets
label1 = Label(root, text='Inserir Fahrenheit:')
textbox1 = Entry(root)
button1 = Button(root, text='Calcular', command=calcular_celsius)
label2 = Label(root, textvariable=var_celsius)
# ---------------------------------------
# layout
label1.grid()
textbox1.grid()
button1.grid()
label2.grid()
textbox1.focus()

root.mainloop()
```

