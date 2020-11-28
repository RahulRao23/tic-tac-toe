from tkinter import *

root = Tk()

frame = LabelFrame(root, borderwidth=4, bg='#EA7773')
frame.grid(row=1, column=1,padx=20, pady=20, sticky=N)

frame_options = LabelFrame(root, borderwidth=4, bg='#EA7773')
frame_options.grid(row=1, column=2,padx=20, pady=20)

r = IntVar()

game_on = True
players = 1
tracker = [None] * 9
rounds = 0
player_1 = 0
player_2 = 0


def change_player():
        global players
        if players == 1:
                players = 0
                label_turn = Label(root, text='Player 2 turn', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20).grid(row=0, column=1, padx=20, pady=20)

        else:
                players = 1
                label_turn = Label(root, text='Player 1 turn', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20).grid(row=0, column=1, padx=20, pady=20)


def winner():
        if rounds < r.get():
                start()

        else:
                if player_1 > player_2:
                        label = Label(root, text='PLAYER 1 WINS THE GAME', font=('Bold', 30), padx=20, pady=20).grid(row=2, column=1, padx=20, pady=20)

                elif player_1 < player_2:
                        label = Label(root, text='PLAYER 2 WINS THE GAME', font=('Bold', 30), padx=20, pady=20).grid(row=2, column=1, padx=20, pady=20)

                elif player_1 == player_2:
                        label = Label(root, text='DRAW MATCH', font=('Bold', 30), padx=20, pady=20).grid(row=2, column=1, padx=20, pady=20)

                button_1 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
                button_2 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=1, padx=5, pady=(20, 5))
                button_3 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
                button_4 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=0, padx=(20, 5), pady=5)
                button_5 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=1, padx=5, pady=5)
                button_6 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=2, padx=(5, 20), pady=5)
                button_7 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
                button_8 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=1, padx=5, pady=(5, 20))
                button_9 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=2, padx=(5, 20), pady=(5, 20))


def conditions():
        global player_1, player_2

        if (tracker[0] == tracker[1] == tracker[2] == 1) \
        or (tracker[3] == tracker[4] == tracker[5] == 1) \
        or (tracker[6] == tracker[7] == tracker[8] == 1) \
        or (tracker[0] == tracker[3] == tracker[6] == 1) \
        or (tracker[1] == tracker[4] == tracker[7] == 1) \
        or (tracker[2] == tracker[5] == tracker[8] == 1) \
        or (tracker[0] == tracker[4] == tracker[8] == 1) \
        or (tracker[2] == tracker[4] == tracker[6] == 1):
                player_1 += 1
                print('player 1 points: '+ str(player_1))
                print('player 2 points: '+ str(player_2))
                print('selected value is: '+ str(r.get()))
                print('total rounds done: '+ str(rounds))
                print('***********END***********')

                winner()


        elif (tracker[0] == tracker[1] == tracker[2] == 0) \
        or (tracker[3] == tracker[4] == tracker[5] == 0) \
        or (tracker[6] == tracker[7] == tracker[8] == 0) \
        or (tracker[0] == tracker[3] == tracker[6] == 0) \
        or (tracker[1] == tracker[4] == tracker[7] == 0) \
        or (tracker[2] == tracker[5] == tracker[8] == 0) \
        or (tracker[0] == tracker[4] == tracker[8] == 0) \
        or (tracker[2] == tracker[4] == tracker[6] == 0):
                player_2 += 1
                print('player 1 points: '+ str(player_1))
                print('player 2 points: '+ str(player_2))
                print('selected value is: '+ str(r.get()))
                print('total rounds done: '+ str(rounds))
                print('***********END***********')

                winner()


        else:
                for i in range(9):
                        if tracker[i] == None:
                                break
                else:
                        if rounds < r.get():
                                print('player 1 points: '+ str(player_1))
                                print('player 2 points: '+ str(player_2))
                                print('selected value is: '+ str(r.get()))
                                print('total rounds done: '+ str(rounds))
                                print('***********END***********')
                                start()

                        else:
                                winner()
                        


def player(button, val):
        if button == 1:
                button_1 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=0, padx=(20, 5), pady=(20, 5))            

        elif button == 2:
                button_2 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=1, padx=5, pady=(20, 5))
                
        elif button == 3:
                button_3 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
                
        elif button == 4:
                button_4 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=0, padx=(20, 5), pady=5)
                
        elif button == 5:
                button_5 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=1, padx=5, pady=5)
                
        elif button == 6:
                button_6 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=1, column=2, padx=(5, 20), pady=5)
                
        elif button == 7:
                button_7 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
                       
        elif button == 8:
                button_8 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=1, padx=5, pady=(5, 20))
                
        elif button == 9:
                button_9 = Button(frame, text=val, font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled').grid(row=2, column=2, padx=(5, 20), pady=(5, 20))
            

def click(players, button):
        
        if players == 1:
                tracker[button-1] = 1
                print(tracker)
                player(button, 'X')
                conditions()
                change_player()
                
        else:
                tracker[button-1] = 0
                print(tracker)
                player(button, 'O')
                conditions()
                change_player()
                

def start():
        global rounds
        print('***********START***********')
        print('selected value is: '+ str(r.get()))
        rounds += 1
        for i in range(9):
                tracker[i] = None

        button_1 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 1)).grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
        button_2 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 2)).grid(row=0, column=1, padx=5, pady=(20, 5))
        button_3 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 3)).grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
        button_4 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 4)).grid(row=1, column=0, padx=(20, 5), pady=5)
        button_5 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 5)).grid(row=1, column=1, padx=5, pady=5)
        button_6 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 6)).grid(row=1, column=2, padx=(5, 20), pady=5)
        button_7 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 7)).grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
        button_8 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 8)).grid(row=2, column=1, padx=5, pady=(5, 20))
        button_9 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 9)).grid(row=2, column=2, padx=(5, 20), pady=(5, 20))


def reset():
        global player_1, player_2, rounds
        rounds = 0
        player_1 = 0
        player_2 = 0


Radiobutton(frame_options, text='1 rounds', variable=r, value=1, font=('bold', 15)).grid(row=0, column=0, padx=20, pady=20)
Radiobutton(frame_options, text='3 rounds', variable=r, value=3, font=('bold', 15)).grid(row=1, column=0, padx=20, pady=20)
Radiobutton(frame_options, text='5 rounds', variable=r, value=5, font=('bold', 15)).grid(row=2, column=0, padx=20, pady=20)
Radiobutton(frame_options, text='7 rounds', variable=r, value=7, font=('bold', 15)).grid(row=3, column=0, padx=20, pady=20)

option_btn = Button(frame_options, text='Start Game', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20, command=start).grid(row=4, column=0, padx=20, pady=20)
reset_btn = Button(frame_options, text='Reset Score', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20, command=reset).grid(row=5, column=0, padx=20, pady=20)


root.mainloop()