from tkinter import *
import time
import sys
import random
score = 1
i=0
while True: 
    player_1 = Tk()
    def _next_():
        global y
        y = random.randint(1,3)
        player_1.destroy()
    def Write_r():
        global x
        x = 1
        lbl = Label(player_1,text="......Rock....").grid(row=2,column=2)
    def Write_s():
        global x
        x = 2
        lbl = Label(player_1,text="....Scissors..").grid(row=2,column=2)
    def Write_p():
        global x
        x = 3
        lbl = Label(player_1,text="....Paper.....").grid(row=2,column=2)
    rock = PhotoImage(file="C:\\Users\\rushil\\Pictures\\Camera Roll\\Rock.png")
    Rock = Button(player_1,text="ROCK",image=rock,command=Write_r)
    Rock.grid(row=1,column=1)
    scissors = PhotoImage(file="C:\\Users\\rushil\\Pictures\\Camera Roll\\Scissors.png")
    Scissors = Button(player_1,text="Scissors",image=scissors,command=Write_s)
    Scissors.grid(row=1,column=2)
    paper = PhotoImage(file="C:\\Users\\rushil\\Pictures\\Camera Roll\\Paper.png")
    Paper = Button(player_1,text="Scissors",image=paper,command=Write_p)
    Paper.grid(row=1,column=3)
    Next = Button(player_1,text="NEXT",command=_next_).grid(row=3,column=2)
    player_1.mainloop()
    #################################################################################################################
    play = Tk()
    if x == 1:
        your_choice = Label(play,text="Your: Rock",padx=100).pack()
    elif x == 2:
        your_choice = Label(play,text="Your: Scissors",padx=100).pack()
    elif x == 3:
        your_choice = Label(play,text="Your: Paper",padx=100).pack()
    else:
        ok = 1
    vs = Label(play,text="VS").pack()
    if y == 1:
        com_choice = Label(play,text="Computer's: Rock",padx=100).pack()
    elif y == 2:
        com_choice = Label(play,text="Computer's: Scissors",padx=100).pack()
    elif y == 3:
        com_choice = Label(play,text="Computer's: Paper",padx=100).pack()
    else:
        ok = 1
    ################################################################################################################
    play.mainloop()
    result = Tk()
    if x==1:
        if y==1:
            lblblblbl = Label(result,text="Tie").pack()
        elif y==2:
            lblblblbl = Label(result,text="You win").pack()
            score=score+1
        elif y==3:
            lblblblbl = Label(result,text="You lost").pack()
            score=score-1
    elif x==2:
        if y==2:
            lblblblbl = Label(result,text="Tie").pack()
        elif y==3:
            lblblblbl = Label(result,text="You win").pack()
            score=score+1
        elif y==1:
            lblblblbl = Label(result,text="You lost").pack()
            score=score-1
    elif x==3:
        if y==3:
            lblblblbl = Label(result,text="Tie").pack()
        elif y==1:
            lblblblbl = Label(result,text="You win").pack()
            score=score+1
        elif y==2:
            lblblblbl = Label(result,text="You lost").pack()
            score=score-1
    def next_2():
        result.destroy()
    def stop_game():
        sys.exit(0)
    score_4 = "■" * score
    next_1 =  Button(result,text="Play again",command=next_2).pack()
    stop = Button(result,text="Stop playing",command=stop_game).pack()
    score_1 = Label(result,text="Score is").pack()
    score_2 = Label(result,text=score).pack()
    score_3 = Label(result,text=score_4).pack()
    if score <= -1:
        print("Score",score)
        print("Game over")
        sys.exit()
    else:
        i=i+1
        print(i,"Chanse's")
    result.mainloop()