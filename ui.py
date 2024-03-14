from tkinter import *
from quiz_brain import QuizBrain
import time

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
        self.button = Button(self.window, image=trueimage, command =self.true_pressed)
        self.button.grid(row = 2, column =0)
        self.button = Button(self.window, image=falseimage, command = self.false_pressed)
        self.button.grid(row=2, column =1)
        self.gen_next_question()
        self.window.mainloop()

    def gen_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You've reached end of the Quiz Bro !")
            self.true_pressed.config(state = "disabled")
            self.false_pressed.config(state = "disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.gen_next_question)


