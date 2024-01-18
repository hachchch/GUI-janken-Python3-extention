import tkinter.messagebox as mb

def janken(you):
    hands = ['rock','paper','scissors']
    you_hand = hands[you]
    jankenII(youII):
    handsII = ['rock','paper','scissors']
    youII_hand = handsII[youII]

    j = (you - youII +3) % 3
    if j == 0:
        txt = 'draw: '
    elif j == 1:
        txt = 'Player1 win!: '
    elif j == 2:
        txt = 'Player2 win!: '

    txt += ' Player1:' + you_hand + ' Player2:' + youII_hand
    mb.showinfo('result',txt)
