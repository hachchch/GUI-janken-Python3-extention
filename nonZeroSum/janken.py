import tkinter.messagebox as mb
import random

def janken(you):
    hands = ['rock','paper','scissors','shoe']
    you_hand = hands[you]
    com = random.randint(0,3)
    com_hand = hands[com]
#e-vs-e
#e-vs>
#e-vs>
    j = (you - com +3)
    if j == 3:
        txt = 'draw: '
    elif j == 1:
        txt = 'You win!: '
    elif j == 2:
        txt = 'You lose: '

    txt += ' you:' + you_hand + ' com:' + com_hand
    mb.showinfo('result',txt)
