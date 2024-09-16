import tkinter as tk
from tkinter import simpledialog
from Question_Answer_System import *

# Function to get the number of questions
def get_num_questions():
    num = simpledialog.askinteger("Number of Questions", "How many questions do you want to answer?")
    return num

# Create the main window
root = tk.Toplevel()
root.title("Question-Answer System")
root.geometry("300x150")
root.configure(bg='pink') 

# Function to start the main interface
def start_quiz():
    num_questions = get_num_questions()
    if num_questions is not None:
        root.destroy()  # Close the initial window
        start_question_interface(num_questions)

# Create a label and a button in the initial window
intro_label = tk.Label(root, text="Welcome to the \nQuestion-Answer System",padx=30, pady=20, font=('Algerian', 12),bg="pink")
start_button = tk.Button(root, text="Start Quiz",font=('Arial Black', 10),border=5, command=start_quiz)

# Layout the widgets
intro_label.place(x=10,y=10)
start_button.place(x=100,y=100)

# Function to start the main question interface
def start_question_interface(num_questions):
    alpha(num_questions)

# Start the GUI event loop for the initial window
root.mainloop()
