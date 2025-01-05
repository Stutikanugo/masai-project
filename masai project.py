import random 
board=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
person= "X"
person2= "O"
def resetboard():
    for i in range(3):
        for j in range(3):
            board[i][j]=" "
def showboard():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"---+---+---")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print(f"---+---+---")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")
def isempty(row,col):
    if board[row-1][col-1]==" ":
        return True
def isfull():
    emptyspaces=9
    for i in range(3):
        for j in range(3):
            if board[i][j]!=" ":
                emptyspaces-=1
    return emptyspaces==0
def personmove():
    x=int(input("Enter the row between (1-3):"))
    y=int(input("Enter the column between (1-3):"))
    if isempty(x,y):
        board[x-1][y-1]=person
    else:
        print("That place is already occupied. Try again!")
    return board[x-1][y-1]
def person2move():
    x=int(input("Enter the row between (1-3): "))
    y-int(input("Enter the column between (1-3): "))
    if isempty(x,y):
        board[x-1][y-1]=person2
    else:
        person2move()
    return board[x-1][y-1]
def checkwinner():
    for i in range(3):
        if board[i][0]==board[i][i]==board[i][2]==person:
            return person
        elif board[i][0]==board[i][i]==board[i][2]==person2:
            return person2
        elif board[0][i]==board[1][i]==board[2][i]==person:
            return person
        elif board[0][i]==board[1][i]==board[2][i]==person2:
            return person2
    if board[0][0]==board[1][1]==board[2][2]==person:
        return person
    elif board[0][0]==board[1][1]==board[2][2]==person2:
        return person2
    elif board[0][2]==board[1][1]==board[2][0]==person:
        return person
    elif board[0][2]==board[1][1]==board[2][0]==person2:
        return person2
    return " "
def printwinner():
    if checkwinner()==person:
        print("Congratulations ! You won ! ")
    elif checkwinner()==person2:
        print("You lost ! Better luck next time ! ")
    else:
        print("It's a tie ! ")
def tictactoe():
    print("Let's play tic tac toe ! ")
    print("Here is the board: ")
    resetboard()
    print("*"* 20)
    showboard()
    print("*"*20)
    while not isfull():
        personmove()
        print("*"*20)
        showboard()
        print("*"*20)
        if checkwinner() !=" ":
            printwinner()
            break
        person2move()
        print("*"*20)
        if checkwinner() !=" ":
            printwinner()
            break
    print("Game Over !")
    print("Do you want to play again ?")
    playagain=input("Enter 'yes' or 'no' : ")
    if playagain.lower()=='yes':
        tictactoe()
    else:
        print("Thanks for playing ! ")
tictactoe()

