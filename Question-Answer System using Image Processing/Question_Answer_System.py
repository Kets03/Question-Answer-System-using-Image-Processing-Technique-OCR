import tkinter as tk
from Question_Bank import question_database
import random,re
from tkinter import filedialog
from img_processing import * 

# Initialize variables
#random.shuffle(question_database)
current_question_index = -1  # Start with -1 to indicate no question displayed
score = 0
num=0
def alpha(no):
    global num
    num = no
    next_question()
    root.mainloop()

file_path=""
user_input=""
def get_image_path():
    global file_path, user_input
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
    user_input =img_to_string(file_path)
    browse.config(state="disabled")
    submit_button.config(state="active")

# Function to start a new question
def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < num:
        question, _ = question_database[current_question_index]
        question_label.config(text=question)
        browse.config(state="active")
        submit_button.config(state="active")
        next_button.config(state="disabled")
    else:
        question_label.config(text="No more questions.")
        submit_button.config(state="disabled")
        next_button.config(state="disabled")

# Function to check the answer
def check_answer():
    global score
    user_answer = re.sub(r'\s', '', user_input)

    _, correct_answer = question_database[current_question_index]
    
    if user_answer.lower() ==correct_answer.lower():
        score += 1
    feedback_label.config(text=f"Your score: {score}")
    submit_button.config(state="disabled")
    next_button.config(state="active")

# Create the main window
root = tk.Tk()
root.title("Advanced Question-Answer System")
root.geometry("760x200")

root.configure(bg='lightblue') 

# Create labels and input field
question_label = tk.Label(root, text="",font=('Arial Black', 10),bg="lightblue")
browse = tk.Button(root,font=('Arial Black', 10))
feedback_label = tk.Label(root, text="Your score: 0", font=('Arial Black', 12),bg="lightblue")

# Create "Submit" and "Next" buttons
browse = tk.Button(root,text="Browse",command=get_image_path,font=('Arial Black', 10),state="active")
submit_button = tk.Button(root, text="Submit", command=check_answer, font=('Arial Black', 10), state="disabled")
next_button = tk.Button(root, text="Next Question", command=next_question, font=('Arial Black', 10), state="active")

# Layout the widgets using the grid layout manager
#background.grid(row=0, column=0, rowspan=3, columnspan=2)
question_label.place(x=10,y=10)
browse.place(x=10,y=40)
submit_button.place(x=220,y=40)
feedback_label.place(x=150,y=90)
next_button.place(x=10,y=130)
