
import tkinter as tk
import random 
import string

def password_generator():
    pass_length=int(len_entry.get())
    character=string.ascii_letters  + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(pass_length))
    pass_label.config(text="Generated Password : " + password,height=3)

# main window is here 

root = tk.Tk()
root.geometry("300x200")
root.title("Password generator !")

# create element
length_label = tk.Label(root, text="Enter Password Length : ",pady=10)
length_label.pack()

len_entry = tk.Entry(root)
len_entry.pack()

button = tk.Button(root, text="Click to Generate Password", command=password_generator,bg="green",pady=7)
button.pack()

pass_label = tk.Label(root, text="")
pass_label.pack()

# main loop here

root.mainloop()