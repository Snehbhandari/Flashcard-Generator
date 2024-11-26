from tkinter import *
import random 



q_a = [("Q1", "A1"), 
    ("Q2", "A2"),
    ("Q3", "A3"),
    ("Q4", "A4"),
    ("Q5", "A5"),
    ("Q6", "A6"),
    ("Q7", "A7"),
    ("Q8", "A8")
    ]

def reveal_answer():
    answer_label.config(text=current_card[1])
    next_button.pack()

# def next_card():

def flashcards_():
    window = Tk()
    window.title("Flashcard App")
    window.geometry("500x300")
    
    # UI 
    question_label = Label(window, text = "Question") # create question label 
    question_label.pack(pady=20) # add padding around question 
    answer_label = Label(window, text = "Answer")
    answer_label.pack(pady=20) # add padding to answer as well 

    # shuffle 
    random.shuffle(q_a) 

    current_card = q_a.pop(0)
    question_label.config(text = current_card[0])
    reveal_button = Button(window, text = "Reveal Answer", command = reveal_answer)
    next_button = Button(window, text = "Next")
    reveal_button.pack() # place the button on the window




    window.mainloop()