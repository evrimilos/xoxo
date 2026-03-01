import tkinter as tk
from tkinter import messagebox
import random

# Pencereyi oluştur
window = tk.Tk()
window.title("XOXO")
window.geometry("600x600") 

turn="X"
moveCount = 0
squares= []

# kazanılan ve beraberlik olan durumları belirleme
def checkWinner():

    global moveCount

    for i in range(3):
        rowControl = (squares[i][0]["text"] == squares[i][1]["text"] == squares[i][2]["text"] != " ")
        if rowControl:
            return squares[i][0]["text"]
        
        columnControl = (squares[0][i]["text"] == squares[1][i]["text"] == squares[2][i]["text"] != " ") 
        if columnControl:
            return squares[0][i]["text"]

    diagonalControl1 = (squares[0][0]["text"] == squares[1][1]["text"] == squares[2][2]["text"] != " ")
    if diagonalControl1:
        return squares[0][0]["text"] 
     
    diagonalControl2 = (squares[0][2]["text"] == squares[1][1]["text"] == squares[2][0]["text"] != " ")
    if diagonalControl2:
        return squares[0][2]["text"]
     
    if moveCount == 9:
        return "beraberlik"
     
    return None 
    

def click(row,column):

   global turn, moveCount

   if squares [row][column]["text"] == " ":
      squares[row][column].config(text=turn, state="disabled", disabledforeground="black")

      ai = (random.randint(0,2),random.randint(0,2))
      moveCount += 1
    
      result = checkWinner()

      if result:
          if result == "beraberlik" :
              messagebox.showinfo("Game Over", "DRAW!")
          else:
                messagebox.showinfo("Game Over", "Congrtulations, %s win!" % result)
          window.destroy()   
      else:
            # Sırayı değiştir
            turn= "O" if turn == "X" else "X"

            if turn == "X":
                emptyCells = [(r, c) for r in range(3) for c in range(3) if squares[r][c]["text"] == " "]
                if emptyCells:
                    ai_row, ai_col = random.choice(emptyCells)
                    window.after(400, lambda: click(ai_row, ai_col))


#3x3 squares
for i in range(3):
    rowSquares = []
    for j in range(3):
        sqr = tk.Button(window, text= " ", font=( "Arial", 20, "bold"), height=4, width=10, 
                        command=lambda r=i, c=j: click(r,c))
        sqr.grid(row=i, column=j)
        rowSquares.append(sqr)
    squares.append(rowSquares)

#AI PLAYER
# click(random.randint(0,2),random.randint(0,2))
# moveCount +1

# while True:
    # moveSide = moveCount % 2
    # if( moveSide == 1):
        # click(random.randint(0,2),random.randint(0,2))
        # moveCount +1
    # else:
        # pass
    # print(moveCount)
    # print(moveSide)

window.after(400, lambda: click(random.randint(0, 2), random.randint(0, 2)))

window.mainloop()
 