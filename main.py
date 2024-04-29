import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        root.title("General Knowledge Quiz")
        
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
            {"question": "Who invented the Python programming language?", "options": ["Tim Berners-Lee", "Guido van Rossum", "Dennis Ritchie", "James Gosling"], "answer": "Guido van Rossum"},
            {"question": "What year was the World Wide Web invented?", "options": ["1985", "1989", "1991", "1993"], "answer": "1989"},
            {"question": "What does 'www' stand for in a website browser?", "options": ["World Wide Web", "Wide World Web", "Web World Wide", "None of the above"], "answer": "World Wide Web"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
            {"question": "Who wrote the novel 'Pride and Prejudice'?", "options": ["Jane Austen", "Emily Bronte", "Virginia Woolf", "Mary Shelley"], "answer": "Jane Austen"},
            {"question": "What gas do living creatures breathe in that is necessary for survival?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Oxygen"},
            {"question": "Which element has the chemical symbol 'O'?", "options": ["Gold", "Oxygen", "Silver", "Zinc"], "answer": "Oxygen"},
            {"question": "In what year did the Titanic sink?", "options": ["1912", "1905", "1898", "1923"], "answer": "1912"},
            {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent Van Gogh", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"}
        ]
        self.question_index = 0
        self.score = 0
        
        self.question_var = tk.StringVar()
        self.question_var.set(self.questions[self.question_index]["question"])
        
        self.question_label = tk.Label(root, textvariable=self.question_var, font=("Helvetica", 16))
        self.question_label.pack(pady=(20, 10))
        
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=(0, 20))
        
        self.option_vars = []
        self.radio_buttons = []
        self.selected_answer = tk.StringVar()
        
        for option in self.questions[self.question_index]["options"]:
            option_var = tk.StringVar(value=option)
            self.option_vars.append(option_var)
            rb = tk.Radiobutton(self.options_frame, textvariable=option_var, variable=self.selected_answer, value=option, font=("Helvetica", 14))
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack(pady=(10, 20))
        
    def check_answer(self):
        if self.selected_answer.get() == self.questions[self.question_index]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Correct answer!")
        else:
            messagebox.showerror("Incorrect", f"Incorrect! The correct answer was {self.questions[self.question_index]['answer']}.")
        
        self.question_index += 1
        if self.question_index == len(self.questions):
            messagebox.showinfo("Quiz Complete", f"You scored {self.score}/{len(self.questions)}!")
            self.root.destroy()
        else:
            self.next_question()
    
    def next_question(self):
        self.question_var.set(self.questions[self.question_index]["question"])
        self.selected_answer.set(None)
        
        for i, option in enumerate(self.questions[self.question_index]["options"]):
            self.option_vars[i].set(option)
            self.radio_buttons[i]['value'] = option

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
