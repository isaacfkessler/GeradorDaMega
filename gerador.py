from tkinter import *
from random import randint

def Gerador():
    x = []
    for c in range(0,6):
        v = randint(1,60)
        while v in x:
            v = randint(1,60)
        x.append(v)
    x.sort()
    texto_jg['text'] = 'Jogo GERADO!'
    texto_gerador['text'] = f'{x[0]}, {x[1]}, {x[2]}, {x[3]}, {x[4]}, {x[5]}'

janela = Tk()

janela.title('Gerador da MEGA SENA')

texto_descritivo = Label(janela, text= 'GERADOR DE JOGOS DA MEGA SENA', font='Arial 20 bold')
texto_descritivo.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='GERAR JOGO', bg='black', fg='white', font='20', command=Gerador)
botao.grid(column=0, row=1, padx=10, pady=10)


texto_jg = Label(janela, text='', font='Arial 15')
texto_jg.grid(column=0, row=2)
texto_gerador = Label(janela, text='', font='Arial 20 bold')
texto_gerador.grid(column=0, row=3, pady=10)

janela.mainloop()