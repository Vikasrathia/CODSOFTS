import tkinter as tk
calculation =""

def clr_calc():
    global calculation
    calculation = ""
    text_res.delete(1.0,"end")

def add_calc(symbol):
    global calculation
    calculation +=str(symbol)
    text_res.delete(1.0,"end")
    text_res.insert(1.0,calculation)

def eval_calc():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_res.delete(1.0,"end")
        text_res.insert(1.0,calculation)
    except:
        clear_field()
        text_res.insert(1.0,"Error")
    

root =tk.Tk()
root.geometry("300x275")
root.title(" 📅  Multitasker Calculator")
text_res=tk.Text(root,height=1.2,width=17,font=("Arial",24),bg="grey")
text_res.grid(columnspan=5)
btn_1 = tk.Button(root,text="1",command=lambda:add_calc(1), width=5,font=("Arial",14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root,text="2",command=lambda:add_calc(2), width=5,font=("Arial",14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root,text="3",command=lambda:add_calc(3), width=5,font=("Arial",14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root,text="4",command=lambda:add_calc(4), width=5,font=("Arial",14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root,text="5",command=lambda:add_calc(5), width=5,font=("Arial",14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root,text="6",command=lambda:add_calc(6), width=5,font=("Arial",14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root,text="7",command=lambda:add_calc(7), width=5,font=("Arial",14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root,text="8",command=lambda:add_calc(8), width=5,font=("Arial",14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root,text="9",command=lambda:add_calc(9), width=5,font=("Arial",14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root,text="0",command=lambda:add_calc(0), width=5,font=("Arial",14))
btn_0.grid(row=5, column=2)
btn_00 = tk.Button(root,text="00",command=lambda:add_calc(00), width=5,font=("Arial",14))
btn_00.grid(row=6, column=2)
btn_add = tk.Button(root,text="+",command=lambda:add_calc("+"), width=5,font=("Arial",14))
btn_add.grid(row=2, column=4)
btn_sub = tk.Button(root,text="-",command=lambda:add_calc("-"), width=5,font=("Arial",14))
btn_sub.grid(row=3, column=4)
btn_mul = tk.Button(root,text="x",command=lambda:add_calc("*"), width=5,font=("Arial",14))
btn_mul.grid(row=4, column=4)
btn_div= tk.Button(root,text="/",command=lambda:add_calc("/"), width=5,font=("Arial",14))
btn_div.grid(row=5, column=4)
btn_open= tk.Button(root,text="(",command=lambda:add_calc("("), width=5,font=("Arial",14))
btn_open.grid(row=5, column=1)
btn_close= tk.Button(root,text=")",command=lambda:add_calc(")"), width=5,font=("Arial",14))
btn_close.grid(row=5, column=3)
btn_dot= tk.Button(root,text=".",command=lambda:add_calc("."), width=5,font=("Arial",14))
btn_dot.grid(row=6, column=1)
btn_clear= tk.Button(root,text="C",command=clr_calc, width=5,font=("Arial",14))
btn_clear.grid(row=6, column=3)
btn_equal= tk.Button(root,text="=",command=eval_calc,width=5,font=("Arial",14))
btn_equal.grid(row=6, column=4)
root.mainloop()