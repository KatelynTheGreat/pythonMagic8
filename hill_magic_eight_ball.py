import tkinter as tk
import random


root = tk.Tk()
root.title("Magic 8")
root.resizable(False, False)
canvas = tk.Canvas(root, width = 500, height = 400)
canvas.config(bg="black")
canvas.pack()



user_question = tk.Text (root,height=2, width=40) 
canvas.create_window(250, 260, window=user_question)
user_question.config(bg="gray")
user_question.config(fg="red")


Label_answer = tk.Label (root,text="hello") 
canvas.create_window(250, 200, window=Label_answer)
Label_answer.config(bg="gray")
Label_answer.config(fg="red")


def answer_user_question():
    randomnumber = random.randint(0,9)

    if len(user_question.get("1.0", "end-1c")) == 0:
        Label_answer.config(text = "you need to ask a question!")
    else:
        if randomnumber == 1:
            Label_answer.config(text = "Yes - definitely.")
        elif randomnumber == 2:
            Label_answer.config(text = "It is decidedly so.")
        elif randomnumber == 3:
            Label_answer.config(text = "Without a doubt")
        elif randomnumber == 4:
            Label_answer.config(text = "Reply hazy, try again.")
        elif randomnumber == 5:
            Label_answer.config(text = "Ask again later.")
        elif randomnumber == 6:
            Label_answer.config(text = "Better not tell you now.")
        elif randomnumber == 7:
            Label_answer.config(text = "My sources say no")
        elif randomnumber == 8:
            Label_answer.config(text = "Outlook not so good.")
        elif randomnumber == 9:
            Label_answer.config(text = "Very doubtful.")

button = tk.Button(text='Send Message', command=answer_user_question)
canvas.create_window(250, 360, window=button)

root.mainloop()