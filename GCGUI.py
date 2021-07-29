from tkinter import *

rows = list(range(25,300,35))
column = list(range(120,1000,100))
program = Tk()

#text
credit_label = Label(program,font = 24,fg="red",text="credits").place(x=column[0],y=0)
score_label = Label(program,font = 24,fg="red",text="score").place(x=column[1],y=0)
s1 = Label(program,text = "S1",font=36).place(x=0,y=rows[0])
s2 = Label(program,text = "S2",font=36).place(x=0,y=rows[1])
s3 = Label(program,text = "S3",font=36).place(x=0,y=rows[2])
s4 = Label(program,text = "S4",font=36).place(x=0,y=rows[3])
s5 = Label(program,text = "S5",font=36).place(x=0,y=rows[4])
s6 = Label(program,text = "S6",font=36).place(x=0,y=rows[5])
s7 = Label(program,text = "S7",font=36).place(x=0,y=rows[6])

#Set resolution and title
program.title("Grade Calculator")
program.geometry("360x380")
program.mainloop()
