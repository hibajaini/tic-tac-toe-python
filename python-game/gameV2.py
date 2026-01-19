import tkinter as tk
window=tk.Tk()
window.title("X | O Game")
window.geometry("500x500")
window.configure(bg="#0d222f")  
window.resizable(False, False) 


title=tk.Label(window,text ="Tic-Tac-Toe !",font=("Times New Roman",37,"bold"),fg="#f178a1",bg="#0d222f")
title.pack()

miniTitle=tk.Label(window,text ="ready for the game !!",font=("Times New Roman",20,"bold italic"),fg="#f1c8d6",bg="#0d222f")
miniTitle.pack()

text=tk.Label(window,font=("arial",12,"bold italic"),text="the players are : X and O ",fg="#f1c8d6",bg="#0d222f")
text.pack()

frame=tk.Frame(window,bg="#4d5963",width=300,height=300, border=3, relief="ridge")
frame.pack(pady=(10, 5))

frame.pack_propagate(False)

board = []

def check_win(player):
    #checkings rows
    for i in range(3):
        if board[i][0]["text"] == player and board[i][1]["text"] == player and board[i][2]["text"] == player:
            return True
        
    #checkings colums
    for i in range(3):
        if board[0][i]["text"] == player and board[1][i]["text"] == player and board[2][i]["text"] == player:
            return True
        
    #checking diagonnals
    if board[0][0]["text"] == player and board[1][1]["text"] == player and board[2][2]["text"] == player:
            return True
    if board[0][2]["text"] == player and board[1][1]["text"] == player and board[2][0]["text"] == player:
            return True
    
    #no win
    return False

#checking if the board is full
def  check_full():
    for row in board:
          for cell in row:
               if cell["text"] == " ":
                    return False
    return True

#disabling the board 

def disable_board():
    for row in board:
        for cell in row:
            cell.config(state="disabled")

#defining the players 

current_player = 0

def buttonChanged(row,col):
    players = ["X","O"]
    global current_player
    current_btn = board[row][col]
    if current_btn["text"] != " ":
          print("invalid move")
          text.pack(pady=(10, 0))
          text.config(text="invalid move") 
          disable_board()
          return
    
    current_btn.config(
    state="disabled",
    text=players[current_player],
    disabledforeground="#f178a1"
    )

    
     #check if the current player has won

    if check_win(players[current_player]):
           print("player : "+players[current_player] + " wins!")
           text.pack(pady=(10, 0))
           text.config(text="player : "+players[current_player] + " wins!")
           disable_board()
           return
     

     #check if the board is full with no winner
    if check_full():
         print("Tie Game!")
         text.pack(pady=(10, 0))
         text.config(text="Tie Game!")
         disable_board()
         return
     
    

    current_player = (current_player + 1) % 2



def print_board():
    global board
    board = [] 
    for r in range(3):
        row = []
        for c in range(3):
            b = tk.Button(
                frame,
                text=" ",
                width=6,
                height=3,
                border=2,
                bg="#0d222f",
                fg="#f178a1",
                font=("Arial", 12, "bold"),
                command=lambda row=r, col=c: buttonChanged(row, col)
            )
            b.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            row.append(b)  # save button in the row
        board.append(row)  # save the row in the board
    
    
    text.pack(pady=(10, 0))
    text.config(text="Click on any cell to play")


buttonLoad=tk.Button(window,text="load board",bg="#f178a1",fg="#0d222f",width=10,height=2, font=("Arial", 10, "bold"),command=print_board,cursor="hand2")
buttonLoad.pack(pady=(10, 0))


text=tk.Label(window,fg="#f178a1",bg="#0d222f",width=20,height=2, font=("Arial", 14, "bold italic"))
text.pack_forget()  
       




window.mainloop()