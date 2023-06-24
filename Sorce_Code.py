from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

       
        self.master.config(bg="black")
        self.display_font = ("Arial", 20, "bold")
        self.button_font = ("Arial", 14, "bold")
        self.button_bg = "#555555"
        self.button_fg = "#ee82ee"

        
        self.display = Entry(master, width=30, justify=RIGHT, font=self.display_font, bg="black", fg="#ee82ee")
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

       
        digits = "789456123"
        self.buttons = []
        for i, digit in enumerate(digits):
            button = Button(master, text=digit, width=5, height=2, font=self.button_font,
                            bg=self.button_bg, fg=self.button_fg,
                            command=lambda x=digit: self.append_digit(x))
            row = 1 + i // 3
            col = i % 3
            button.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(button)

        self.button0 = Button(master, text="0", width=12, height=2, font=self.button_font,
                              bg=self.button_bg, fg=self.button_fg,
                              command=lambda x='0': self.append_digit(x))
        self.button0.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

        self.button_decimal = Button(master, text=".", width=5, height=2, font=self.button_font,
                                      bg=self.button_bg, fg=self.button_fg,
                                      command=lambda x='.': self.append_digit(x))
        self.button_decimal.grid(row=4, column=2, padx=2, pady=2)

        self.button_clear = Button(master, text="C", width=5, height=2, font=self.button_font,
                                    bg=self.button_bg, fg=self.button_fg,
                                    command=self.clear_display)
        self.button_clear.grid(row=1, column=3, padx=2, pady=2)

        self.button_plus = Button(master, text="+", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='+': self.append_digit(x))
        self.button_plus.grid(row=2, column=3, padx=2, pady=2)

        self.button_minus = Button(master, text="-", width=5, height=2, font=self.button_font,
                                   bg=self.button_bg, fg=self.button_fg,
                                   command=lambda x='-': self.append_digit(x))
        self.button_minus.grid(row=3, column=3, padx=2, pady=2)

        self.button_multiply = Button(master, text="*", width=5, height=2, font=self.button_font,
                                       bg=self.button_bg, fg=self.button_fg,
                                       command=lambda x='*': self.append_digit(x))
        self.button_multiply.grid(row=4, column=3, padx=2, pady=2)

        self.button_divide = Button(master, text="/", width=5, height=2, font=self.button_font,
                                     bg=self.button_bg, fg=self.button_fg,
                                     command=lambda x='/': self.append_digit(x))
        self.button_divide.grid(row=5, column=3, padx=2, pady=2)

        self.button_equals = Button(master, text="=", width=5, height=2, font=self.button_font,
                                     bg=self.button_bg, fg=self.button_fg,
                                     command=self.calculate)
        self.button_equals.grid(row=5, column=4, padx=2, pady=2)

        self.button_sqrt = Button(master, text="√", width=5, height=2, font=self.button_font,
                                   bg=self.button_bg, fg=self.button_fg,
                                   command=self.calculate_sqrt)
        self.button_sqrt.grid(row=1, column=4, padx=2, pady=2)

        self.button_sin = Button(master, text="sin", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='sin': self.append_function(x))
        self.button_sin.grid(row=2, column=4, padx=2, pady=2)

        self.button_cos = Button(master, text="cos", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='cos': self.append_function(x))
        self.button_cos.grid(row=3, column=4, padx=2, pady=2)

        self.button_tan = Button(master, text="tan", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='tan': self.append_function(x))
        self.button_tan.grid(row=4, column=4, padx=2, pady=2)

        self.button_log = Button(master, text="log", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='log': self.append_function(x))
        self.button_log.grid(row=5, column=0, padx=2, pady=2)

        self.button_pi = Button(master, text="π", width=5, height=2, font=self.button_font,
                                 bg=self.button_bg, fg=self.button_fg,
                                 command=lambda x='π': self.append_function(x))
        self.button_pi.grid(row=1, column=0, padx=2, pady=2)

        self.button_e = Button(master, text="e", width=5, height=2, font=self.button_font,
                                bg=self.button_bg, fg=self.button_fg,
                                command=lambda x='e': self.append_function(x))
        self.button_e.grid(row=1, column=1, padx=2, pady=2)

        self.button_pow = Button(master, text="x^y", width=5, height=2, font=self.button_font,
                                  bg=self.button_bg, fg=self.button_fg,
                                  command=lambda x='^': self.append_digit(x))
        self.button_pow.grid(row=1, column=2, padx=2, pady=2)

        
        self.clear_display()

    def append_digit(self, digit):
        self.display.insert(END, digit)

    def append_function(self, function):
        self.display.insert(END, function + "(")

    def clear_display(self):
        self.display.delete(0, END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.display.insert(0, result)
        except:
            self.clear_display()
            self.display.insert(0, "Error")

    def calculate_sqrt(self):
        try:
            num = float(self.display.get())
            result = math.sqrt(num)
            self.clear_display()
            self.display.insert(0, result)
        except:
            self.clear_display()
            self.display.insert(0, "Error")

root = Tk()
calc = Calculator(root)
root.mainloop()