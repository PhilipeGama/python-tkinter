# python-tkinter


Inicio: 13/02/2021 Fim:16/03/2021
[Playlist - Curso de Python Tkinter - João Ribeiro](https://www.youtube.com/playlist?list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h)
>>>>>>> ee5f2ccbb7914523c6ad604cb5e2702a21eddd3d

```python
from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Primeiro app')

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

menu_inicial = Tk()
menu_inicial.title('Primeiro app')

menu_inicial.geometry('300x400+600+200')
menu_inicial.resizable(0, 0)
btn = Button(menu_inicial, text='Executar')
btn.pack()

menu_inicial.mainloop()
```
## AULA 07
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
## AULA 08
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
## AULA 09
```python
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
## AULA 10
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

## AULA 11
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

## AULA 12 
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

## AULA 13
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
## AULA 14
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
## AULA 15
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

## AULA 16
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
## 017 - Python tkinter - INTRODUÇÃO AO LAYOUT EM GRID
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
## 019 - Python tkinter - QUADRO DE LOGIN COM GRID E STICKY
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
## 020 - Python tkinter - COLUMNSPAN EM GRID
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

## 020 - Python tkinter - COLUMNSPAN EM GRID
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
## 021 - Python tkinter - PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS
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
```

## 022 - Python tkinter - PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS
```python
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

## 023 - Python tkinter - FAHRENHEIT PARA CELSIUS
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

## 024 - Python tkinter - FOCUS E TAB ORDER
```python
from tkinter import *

# ---------------------------------------
# GUI
root = Tk()
root.title('Login')
var_celsius = StringVar()
# ---------------------------------------
# funcoes


def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()


# ---------------------------------------
# widgets
t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

l1 = Label(root)
l2 = Label(root)
l3 = Label(root)
b1 = Button(root, text='Executar', command=executar)
# ---------------------------------------
# layout
t1.grid()
t2.grid()
t3.grid()

l1.grid()
l2.grid()
l3.grid()
b1.grid()

t1.focus()

root.mainloop()
```

## 025 - Python tkinter - INTRODUÇÃO A FRAME WIDGET
```python
from tkinter import *

# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

# ---------------------------------------
# widgets
frame_login = Frame(root)
label_usuario = Label(frame_login, text='Usuário')
label_password = Label(frame_login, text='Password')
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar = Button(frame_login, text='Entrar')

frame_login.grid()

# ---------------------------------------
# layout
label_usuario.grid(row=0, column=0)
label_password.grid(row=1, column=0)
text_usuario.grid(row=0, column=1)
text_password.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=1, sticky=E)


root.mainloop()
```

## 026 - Python tkinter - EXERCÍCIO COM UTILIZAÇÃO DE DUAS FRAMES
```python
from tkinter import *

# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

# ---------------------------------------
# funcoes
def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()


# ---------------------------------------
# widgets
frame_nome = Frame(root)
frame_morada = Frame(root)
label_nome = Label(frame_nome, text='Nome')
label_apelido = Label(frame_nome, text='Apelido')
label_rua = Label(frame_morada, text='Rua')
label_cidade = Label(frame_morada, text='Cidade')

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

cmd_salvar = Button(root, text='Salvar')


# ---------------------------------------
# layout
label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
text_nome.grid(row=0, column=1)
text_apelido.grid(row=1, column=1)

label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)


frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)
cmd_salvar.grid()

root.mainloop()
```
## 027 - Python tkinter - CRIAR O NOSSO PRÓPRIO WIDGET
```python

from tkinter import *


# ---------------------------------------
# O meu wigdet
class FrameNome(Frame):
    def __init__(self, meu_master):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text='Nome:')
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)


# ---------------------------------------
# GUI
root = Tk()
root.title('Login')

frame_nome_1 = FrameNome(root).grid()
frame_nome_2 = FrameNome(root).grid()
frame_nome_3 = FrameNome(root).grid()
frame_nome_4 = FrameNome(root).grid()
root.mainloop()

```
```python




```
## 028 - Python tkinter - SELF, INIT E SUPER
```python
from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'blue'


root = Tk()

frame1 = MinhaFrame(root).pack()

root.mainloop()




```
## 029 - Python tkinter - USANDO HELP PARA VER PROPRIEDADES E MÉTODOS DE UMA CLASS
```python
from tkinter import *


class MinhaFrame(Frame):
    def __init__():
        super().__init__()
        self['bg'] = 'red'


print(help(MinhaFrame))



```
## 030 - Python tkinter - EXERCÍCIO PRÁTICO COM FRAME E INSTANCIAÇÃO
```python
from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()

        self['bg'] = 'red'
        self['bd'] = '5'
        self['relief'] = 'solid'
        self.text1_text = StringVar()
        self.label1_text = StringVar()

        # widgets
        self.label1 = Label(self, textvariable=self.label1_text).grid()
        text1 = Entry(self, textvariable=self.text1_text).grid()
        cmd1 = Button(self, text='Clique', command=self.Executar).grid()

    def Executar(self):
        self.label1_text.set('Olá, ' + self.text1_text.get() + '!')


root = Tk()
root.geometry('300x300')
frame1 = MinhaFrame(root).grid()
frame2 = MinhaFrame(root).grid()
root.mainloop()
```

## 031 - Python tkinter - ADICIONAR IMAGEM A UM LAYOUT
```python

from tkinter import *

root = Tk()
img = PhotoImage(file="image-1024.png")
label_imagem = Label(root, image=img).pack()

root.mainloop()

# https://pixlr.com/br/x/#editor redimesionar imagem

```
## 032 - Python tkinter - CHECKBUTTON
```python

from tkinter import *

root = Tk()

valor_check = IntVar()


def apresentar():
    print(valor_check.get())


check = Checkbutton(
    root,
    text='Esta é uma checkbox',
    variable=valor_check,
    command=apresentar
).pack()


root.mainloop()
```
## 033 - Python tkinter - LISTBOX
```python

from tkinter import *

root = Tk()

valor_check = IntVar()


def executar():
    print(lista_2.get(ACTIVE))
    lista_2.delete(ACTIVE)


lista_1 = Listbox(root)
lista_1.pack()

lista_2 = Listbox(root, selectmode=EXTENDED)
lista_2.pack()

# inseri um item de cada vez
lista_1 .insert(0, 'Primeiro item da lista')
lista_1 .insert(1, 'Segundo item da lista')
lista_1 .insert(END, 'Terceiro item da lista')
lista_1 .insert(END, 'Quarto item da lista')
lista_1 .insert(END, 'Quinto item da lista')

# inserir vários itens a partir de uma list
nomes = ['João', 'Ana', 'Carlos', 'Philipe',
         'Ana Carolina', 'Vanessa', 'Carol']
for nome in nomes:
    lista_2.insert(END, nome)

#lista_2.delete(1, 1)
#lista_2.delete(1, END)
cmd = Button(root, text='Clique', command=executar).pack()
root.mainloop()

```
## 034 - Python tkinter - SCALE
```python

from tkinter import *


def vervalor(v):
    print(v)


root = Tk()
root.geometry('300x300')
slide = Scale(root,
              from_=0,
              to=100,
              orient=HORIZONTAL,
              resolution=0.5)
slide.pack()

cmd = Button(root, text='Ver valor', command=vervalor)
root.mainloop()

```
## 035 - Python tkinter - MESSAGE
```python

from tkinter import *

root = Tk()
# root.geometry('400x300')

t = Message(
    root,
    text='Este é o texto do message widget',
    width=100)
t.pack()


root.mainloop()

```
## 036 - Python tkinter - RADIOBUTTON
```python

from tkinter import *


def ver_radio():
    print(val_a.get())


def ra1():
    print('Opção 1')


root = Tk()

frameA = Frame(root)
frameB = Frame(root)

val_a = IntVar()
val_b = IntVar()

ra_1 = Radiobutton(frameA, text='Opção A 1', variable=val_a,
                   value=1, command=ra1)
ra_2 = Radiobutton(frameA, text='Opçaõ A 2', variable=val_a,
                   value=2)
ra_3 = Radiobutton(frameA, text='Opçao A 3', variable=val_a,
                   value=3, indicatoron=1)
ra_1.pack()
ra_2.pack()
ra_3.pack()
ra_1.select()

rb_1 = Radiobutton(frameB, text='Opção B 1', variable=val_b,
                   value=1, command=ra1)
rb_2 = Radiobutton(frameB, text='Opçaõ B 2', variable=val_b,
                   value=2, indicatoron=0)
rb_3 = Radiobutton(frameB, text='Opçao B 3', variable=val_b,
                   value=3, indicatoron=1)
rb_1.pack()
rb_2.pack()
rb_3.pack()
rb_1.select()

frameA.pack()
frameB.pack()

cmd = Button(root, text='Executar', command=ver_radio).pack()
```

## 037 - Python tkinter - SPINBOX
```python

from tkinter import *

root = Tk()
root.geometry('300x200')

s1 = Spinbox(root, from_=0, to=10)
s1.pack()

s2 = Spinbox(root, values=(10, 20, 30, 40, 50), wrap=True)
s2.pack()

s3 = Spinbox(root, values=('João', 'Ana', 'Carlos'))
s3.pack()


def executar():
    print(s2.get())


cmd = Button(root, text='Clique', command=executar)
cmd.pack()

root.mainloop()

```
## 038 - Python tkinter - ADICIONAR MENUS À APLICAÇÃO
```python

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

```
## 039 - Python tkinter - TOPLEVEL
```python

from tkinter import *


def abrir_formulario():
    # top level
    top = Toplevel()
    top.title('Novo formulário')
    top.geometry('200x100')
    lb1 = Label(top, text='Label da nova janela')
    lb1.pack()


root = Tk()
root.geometry('300x200')


btn = Button(root, text='Novo...', command=abrir_formulario)
btn.pack()


root.mainloop()

```
## 041 - Python tkinter - SITES DE REFERÊNCIA
```
https:// www.python.org/
https://www.python.org/
https://tkdocs.com/tutorial/widgets.html
https://effbot.org/
https://www.pyinstaller.org/
```
