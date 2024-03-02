import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create input box
        self.input_text = tk.StringVar()
        self.input_box = tk.Entry(master, textvariable=self.input_text, width=25, font=("Arial", 16))
        self.input_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create number buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("0", 4, 0)

        # create operation buttons
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button("C", 4, 1)
        self.create_button("=", 4, 2)

        # create square root button
        self.create_button("sqrt", 5, 0, columnspan=2)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 14), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.clear()
        elif text == "=":
            self.calculate()
        elif text == "sqrt":
            self.input_text.set(str(math.sqrt(float(self.input_text.get()))))
        else:
            self.input_text.set(self.input_text.get() + text)

    def clear(self):
        self.input_text.set("")

    def calculate(self):
        try:
            self.input_text.set(str(eval(self.input_text.get())))
        except:
            self.input_text.set("ERROR")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
