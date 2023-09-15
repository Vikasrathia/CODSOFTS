
import random
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.configure(bg="pink")
frame=tk.Frame(root,bg="green")
root.geometry("340x340")
root.title("Rock Paper Scissor Game")
comp_value = {
	"0": "Rock",
	"1": "Paper",
	"2": "Scissor"
}

def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player  ")
	l3.config(text="Computer")
	l4.config(text="")
	

def btn_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player selected rock

def rock():
	comp = comp_value[str(random.randint(0, 2))]
	if comp == "Rock":
		result = "Match Draw"
	elif comp == "Scissor":
		result = "Player Win"
	else:
		result = "Computer Win"
	l4.config(text=result)
	l1.config(text="Rock ")
	l3.config(text=comp)
	btn_disable()

# If player selected paper

def paper():
	comp = comp_value[str(random.randint(0, 2))]
	if comp == "Paper":
		result = "Match Draw"
	elif comp == "Scissor":
		result = "Computer Win"
	else:
		result = "Player Win"
	l4.config(text=result)
	l1.config(text="Paper ")
	l3.config(text=comp)
	btn_disable()

# If player selected scissor

def scissor():
	comp = comp_value[str(random.randint(0, 2))]
	if comp == "Rock":
		result = "Computer Win"
	elif comp == "Scissor":
		result = "Match Draw"
	else:
		result = "Player Win"
	l4.config(text=result)
	l1.config(text="  Scissor ")
	l3.config(text=comp)
	btn_disable()

# Add Labels, Frames and Button
Label(root,
	text="Rock Paper Scissor",
	font="normal 20 bold",
	fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text="Player ",
		font=10)

l2 = Label(frame,
		text="VS",
		font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
			font=10, width=7,
			command=rock)

b2 = Button(frame1, text="Paper ",
			font=10, width=7,
			command=paper)

b3 = Button(frame1, text="Scissor",
			font=10, width=7,
			command=scissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
frame.pack()

Button(root, text="Reset Game",
	font=10, fg="red",
	bg="black", command=reset_game).pack(pady=20)

# Execute code
root.mainloop()
