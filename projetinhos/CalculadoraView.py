from tkinter import *
from calculadora import Calculadora

root = Tk()
# ----------------------------------------
# funcoes
resultado = StringVar()
calc = Calculadora()


def somar():
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    resultado.set(calc.soma(numero1, numero2))


def subtracao():
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    resultado.set(calc.subtracao(numero1, numero2))


def multiplicacao():
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    resultado.set(calc.multiplicacao(numero1, numero2))


def divisao():
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    resultado.set(calc.divisao(numero1, numero2))


# ----------------------------------------
# widgets
root.resizable(0, 0)
img = PhotoImage(file='image/calculator-icon-96.png')
img_plus = PhotoImage(file='image/plus-icon-32.png')
img_minus = PhotoImage(file='image/minus-icon-32.png')
img_x = PhotoImage(file='image/x-icon-32.png')
img_divide = PhotoImage(file='image/divide-icon-32.png')

frame1 = Frame(root)
frame2 = Frame(root)
label_img = Label(frame1, image=img)
label1 = Label(frame1, text='Valor 1:')
label2 = Label(frame1, text='Valor 2:')

txt_numero1 = Entry(frame1)
txt_numero2 = Entry(frame1)
txt_resultado = Entry(frame1, textvariable=resultado)

label3 = Label(frame1, text='RESULTADO')

btn_adicao = Button(frame1, image=img_plus, command=somar)
btn_subtracao = Button(frame1, image=img_minus, command=subtracao)
btn_multiplicacao = Button(frame1, image=img_x, command=multiplicacao)
btn_divisao = Button(frame1, image=img_divide, command=divisao)


# ----------------------------------------
# layout
label_img.grid(columnspan=2)
frame1.grid()

label1.grid(row=1, column=0)
txt_numero1.grid(row=1, column=1)
label2.grid(row=2, column=0)
txt_numero2.grid(row=2, column=1)

btn_adicao.grid(row=3, column=1, stick='W')
btn_subtracao.grid(row=3, column=1, padx=7)
btn_multiplicacao.grid(row=3, column=1, stick='E')
btn_divisao.grid(row=3, column=0, stick='W')
label3.grid(row=4, columnspan=2)
txt_resultado.grid(row=5, columnspan=2)


root.mainloop()
