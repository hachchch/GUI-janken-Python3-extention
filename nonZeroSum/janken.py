import tkinter.messagebox as mb
import random

def janken(you):
    hands = ['rock','paper','scissors','shoe']
    you_hand = hands[you]
    com = random.randint(1,4)
    com_hand = hands[com]
#e-vs-e    e  → r
#e-vs>s    ↓↖↙↑
#e<vs-p    s → p
#e-vs>r
#ナッシュ均衡がpとe
#多分これで非零和状態かな...?
    j = (you - com +5) % 5
    if j == 0:
        txt = 'draw: '
    elif j == 4:
        txt = 'You lose: '
    elif j == 1:
        txt = 'You win!: '
    elif j == 2:
        txt = 'You lose: '
    elif j == 3:
        txt = 'You win!: '

    txt += ' you:' + you_hand + ' com:' + com_hand
    mb.showinfo('result',txt)
