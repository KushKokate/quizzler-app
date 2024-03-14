from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzApp:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text = "Score : 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)
        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width = 280,
                                                     text ="some question text",
                                                     fill=THEME_COLOR,
                                                     font = ("Arial", 20, "italic"))
        self.canvas.grid(row = 1, column =0, columnspan = 2, pady =50)
        trueimage = PhotoImage(file = "images/true.png")
        falseimage = PhotoImage(file = "images/false.png")
        self.button = Button(self.window, image=trueimage)
        self.button.grid(row = 2, column =0)
        self.button = Button(self.window, image=falseimage)
        self.button.grid(row=2, column =1)
        self.gen_next_question()
        self.window.mainloop()

    def gen_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
