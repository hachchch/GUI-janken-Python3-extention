from tkinter import *
import nonZeroSum.janken as jk
root = Tk()
root.title("janken")

label = Label(text="choose your hand")
label.pack()

# プレイヤーの選択肢
r_button = Button(
    text="rock",
    width=10,
    command=lambda:jk.janken(1)
)
p_button = Button(
    text="paper",
    width=10,
    command=lambda:jk.janken(2)
)
s_button = Button(
    text="scissors",
    width=10,
    command=lambda:jk.janken(3)
)
e_button = Button(
    text="shoe",
    width=10,
    command=lambda:jk.janken(4)
)
r_button.pack()
p_button.pack()
s_button.pack()
e_button.pack()

root.mainloop()
