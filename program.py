from tkinter import *

root = Tk()
root.geometry('900x900')

# frame for the game board
frame = LabelFrame(root, borderwidth=4, bg='#EA7773')
frame.grid(row=1, column=1,padx=20, pady=20, sticky=N)

# frame for the options
frame_options = LabelFrame(root, borderwidth=4, bg='#EA7773')
frame_options.grid(row=1, column=2,padx=20, pady=20)

r = IntVar()

players = 1                # If players = 1 then X's turn or O's turn
tracker = [None] * 9       # Array to store values
rounds = 0                 # Keeps count of the rounds completed
p1_points = 0              # Player 1 points
p2_points = 0              # Player 2 points

# function to change player after each turn 
def change_player():
        global players
        if players == 1:
                players = 0
                label_turn = Label(root, text='Player 2 turn', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20)
                label_turn.grid(row=0, column=1, padx=20, pady=20)

        else:
                players = 1
                label_turn = Label(root, text='Player 1 turn', font=('bold', 15), bg='#AE1438', fg='white', padx=20, pady=20)
                label_turn.grid(row=0, column=1, padx=20, pady=20)

# function to decide the winner of the game and print it in the window
def winner():
        if rounds < r.get():
                start()

        else:
                if p1_points > p2_points:
                        winner_label = Label(root, text='PLAYER 1 WINS THE GAME', font=('Bold', 25), padx=20, pady=20)
                        winner_label.grid(row=3, column=1, padx=20)

                        label = Label(root, text='Don\'t forget to reset scores before starting the next game', font=('Bold', 15), padx=20, pady=20)
                        label.grid(row=4, column=1, padx=20)


                elif p1_points < p2_points:
                        winner_label = Label(root, text='PLAYER 2 WINS THE GAME', font=('Bold', 25), padx=20, pady=20)
                        winner_label.grid(row=3, column=1, padx=20)

                        label = Label(root, text='Don\'t forget to reset scores before starting the next game', font=('Bold', 15), padx=20, pady=20)
                        label.grid(row=4, column=1, padx=20)


                elif p1_points == p2_points:
                        winner_label = Label(root, text='DRAW MATCH', font=('Bold', 25), padx=20, pady=20)
                        winner_label.grid(row=3, column=1, padx=20)

                        label = Label(root, text='Don\'t forget to reset scores before starting the next game', font=('Bold', 15), padx=20, pady=20)
                        label.grid(row=4, column=1, padx=20)

                button_1 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_2 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_3 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_4 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_5 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_6 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_7 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_8 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')
                button_9 = Button(frame, text='', font=('Bold', 10), bg='red', width=10, height=4, borderwidth=2, padx=20, pady=20, state='disabled')

                button_1.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
                button_2.grid(row=0, column=1, padx=5, pady=(20, 5))
                button_3.grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
                button_4.grid(row=1, column=0, padx=(20, 5), pady=5)
                button_5.grid(row=1, column=1, padx=5, pady=5)
                button_6.grid(row=1, column=2, padx=(5, 20), pady=5)
                button_7.grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
                button_8.grid(row=2, column=1, padx=5, pady=(5, 20))
                button_9.grid(row=2, column=2, padx=(5, 20), pady=(5, 20))

# function to decide the increment the points of the winner in each round
def conditions():
        global p1_points, p2_points

        if (tracker[0] == tracker[1] == tracker[2] == 1) \
        or (tracker[3] == tracker[4] == tracker[5] == 1) \
        or (tracker[6] == tracker[7] == tracker[8] == 1) \
        or (tracker[0] == tracker[3] == tracker[6] == 1) \
        or (tracker[1] == tracker[4] == tracker[7] == 1) \
        or (tracker[2] == tracker[5] == tracker[8] == 1) \
        or (tracker[0] == tracker[4] == tracker[8] == 1) \
        or (tracker[2] == tracker[4] == tracker[6] == 1):
                p1_points += 1
                # print('player 1 points: '+ str(p1_points))
                # print('player 2 points: '+ str(p2_points))
                # print('total rounds done: '+ str(rounds))
                # print('***********END***********')

                winner()


        elif (tracker[0] == tracker[1] == tracker[2] == 0) \
        or (tracker[3] == tracker[4] == tracker[5] == 0) \
        or (tracker[6] == tracker[7] == tracker[8] == 0) \
        or (tracker[0] == tracker[3] == tracker[6] == 0) \
        or (tracker[1] == tracker[4] == tracker[7] == 0) \
        or (tracker[2] == tracker[5] == tracker[8] == 0) \
        or (tracker[0] == tracker[4] == tracker[8] == 0) \
        or (tracker[2] == tracker[4] == tracker[6] == 0):
                p2_points += 1
                # print('player 1 points: '+ str(p1_points))
                # print('player 2 points: '+ str(p2_points))
                # print('total rounds done: '+ str(rounds))
                # print('***********END***********')

                winner()


        else:
                for i in range(9):
                        if tracker[i] == None:
                                break
                else:
                        if rounds < r.get():
                                # print('player 1 points: '+ str(p1_points))
                                # print('player 2 points: '+ str(p2_points))
                                # print('total rounds done: '+ str(rounds))
                                # print('***********END***********')
                                start()

                        else:
                                winner()
                        
# function to display the entered value in the game board
def update(button, val):
        if button == 1:
                button_1 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_1.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))            

        elif button == 2:
                button_2 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_2.grid(row=0, column=1, padx=5, pady=(20, 5))
                
        elif button == 3:
                button_3 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_3.grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
                
        elif button == 4:
                button_4 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_4.grid(row=1, column=0, padx=(20, 5), pady=5)
                
        elif button == 5:
                button_5 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_5.grid(row=1, column=1, padx=5, pady=5)
                
        elif button == 6:
                button_6 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_6.grid(row=1, column=2, padx=(5, 20), pady=5)
                
        elif button == 7:
                button_7 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_7.grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
                       
        elif button == 8:
                button_8 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_8.grid(row=2, column=1, padx=5, pady=(5, 20))
                
        elif button == 9:
                button_9 = Button(frame, text=val, font=('Bold', 44), bg='#A3CB37', width=3, borderwidth=2, padx=7, state='disabled')
                button_9.grid(row=2, column=2, padx=(5, 20), pady=(5, 20))
            
# function to check current player
def click(players, button):
        
        if players == 1:
                tracker[button-1] = 1
                # print(tracker)
                update(button, 'X')
                conditions()
                change_player()
                
        else:
                tracker[button-1] = 0
                # print(tracker)
                update(button, 'O')
                conditions()
                change_player()
                
# function to create the game board
def start():
        global rounds

        # print('***********START***********')
        # print('Total rounds: '+ str(r.get()))

        rounds += 1
        for i in range(9):
                tracker[i] = None

        button_1 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 1))
        button_2 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 2))
        button_3 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 3))
        button_4 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 4))
        button_5 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 5))
        button_6 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 6))
        button_7 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 7))
        button_8 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 8))
        button_9 = Button(frame, text='', font=('Bold', 10), bg='#A3CB37', width=10, height=4, borderwidth=2, padx=20, pady=20, command=lambda: click(players, 9))


        button_1.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
        button_2.grid(row=0, column=1, padx=5, pady=(20, 5))
        button_3.grid(row=0, column=2, padx=(5, 20), pady=(20, 5))
        button_4.grid(row=1, column=0, padx=(20, 5), pady=5)
        button_5.grid(row=1, column=1, padx=5, pady=5)
        button_6.grid(row=1, column=2, padx=(5, 20), pady=5)
        button_7.grid(row=2, column=0, padx=(20, 5), pady=(5, 20))
        button_8.grid(row=2, column=1, padx=5, pady=(5, 20))
        button_9.grid(row=2, column=2, padx=(5, 20), pady=(5, 20))

# function to reset all the values before new game
def reset():
        global p1_points, p2_points, rounds
        rounds = 0
        p1_points = 0
        p2_points = 0


# Radiobuttons to select number of rounds in a game
Radiobutton(frame_options, text='1 rounds', variable=r, value=1, font=('bold', 20)).grid(row=0, column=0, padx=20, pady=10)
Radiobutton(frame_options, text='3 rounds', variable=r, value=3, font=('bold', 20)).grid(row=1, column=0, padx=20, pady=10)
Radiobutton(frame_options, text='5 rounds', variable=r, value=5, font=('bold', 20)).grid(row=2, column=0, padx=20, pady=10)
Radiobutton(frame_options, text='7 rounds', variable=r, value=7, font=('bold', 20)).grid(row=3, column=0, padx=20, pady=10)

# start button
option_btn = Button(frame_options, text='Start Game', font=('bold', 20), bg='#AE1438', fg='white', padx=20, pady=15, command=start)

# reset button
reset_btn = Button(frame_options, text='Reset Score', font=('bold', 20), bg='#AE1438', fg='white', padx=15, pady=15, command=reset)

option_btn.grid(row=4, column=0, padx=20, pady=10)
reset_btn.grid(row=5, column=0, padx=20, pady=10)


root.mainloop()