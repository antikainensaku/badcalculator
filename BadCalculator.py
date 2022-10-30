from tkinter import *
import random


class Calculator:
    def __init__(self):
        self.text = ""
        self.text_box = None
        self.gui = None
        self.equation = None

        # gui related variables
        self.height = 1
        self.width = 6
        self.font_color = 'black'
        self.bg_color = 'grey'
        self.font = 'Arial 18'

        # buttons
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.button5 = None
        self.button6 = None
        self.button7 = None
        self.button8 = None
        self.button9 = None
        self.button0 = None
        self.minus = None
        self.plus = None
        self.divide = None
        self.multiply = None
        self.equal = None
        self.clear = None
        self.decimal = None

    def start(self):
        self.init_gui()
        self.init_buttons()

    def init_gui(self):
        self.gui = Tk()
        self.gui.configure(background="#363636")
        self.gui.title("Bad Calculator")
        self.equation = StringVar()
        self.text_box = Entry(
            self.gui, textvariable=self.equation, font=self.font)
        self.text_box.grid(columnspan=4)

    def button_press(self, num):
        self.text += str(num)
        self.equation.set(self.text)

    def equal_press(self):
        try:
            total = str(eval(self.text) + random.randrange(0,
                        int(eval(self.text))+3))
            self.equation.set(total)
            self.text = ""
        except:
            self.equation.set(" undefined ")
            self.text = ""

    def clear_press(self):
        self.text = ""
        self.equation.set("")

    def init_buttons(self):
        self.button1 = Button(self.gui, text=' 1 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(1), height=self.height, width=self.width, font=self.font)
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.gui, text=' 2 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(2), height=self.height, width=self.width, font=self.font)
        self.button2.grid(row=2, column=1)

        self.button3 = Button(self.gui, text=' 3 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(3), height=self.height, width=self.width, font=self.font)
        self.button3.grid(row=2, column=2)

        self.button4 = Button(self.gui, text=' 4 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(4), height=self.height, width=self.width, font=self.font)
        self.button4.grid(row=3, column=0)

        self.button5 = Button(self.gui, text=' 5 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(5), height=self.height, width=self.width, font=self.font)
        self.button5.grid(row=3, column=1)

        self.button6 = Button(self.gui, text=' 6 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(6), height=self.height, width=self.width, font=self.font)
        self.button6.grid(row=3, column=2)

        self.button7 = Button(self.gui, text=' 7 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(7), height=self.height, width=self.width, font=self.font)
        self.button7.grid(row=4, column=0)

        self.button8 = Button(self.gui, text=' 8 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(8), height=self.height, width=self.width, font=self.font)
        self.button8.grid(row=4, column=1)

        self.button9 = Button(self.gui, text=' 9 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(9), height=self.height, width=self.width, font=self.font)
        self.button9.grid(row=4, column=2)

        self.button0 = Button(self.gui, text=' 0 ', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press(0), height=self.height, width=self.width, font=self.font)
        self.button0.grid(row=5, column=0)

        self.plus = Button(self.gui, text=' + ', fg=self.font_color, bg=self.bg_color,
                           command=lambda: self.button_press("+"), height=self.height, width=self.width, font=self.font)
        self.plus.grid(row=2, column=3)

        self.minus = Button(self.gui, text=' - ', fg=self.font_color, bg=self.bg_color,
                            command=lambda: self.button_press("-"), height=self.height, width=self.width, font=self.font)
        self.minus.grid(row=3, column=3)

        self.multiply = Button(self.gui, text=' * ', fg=self.font_color, bg=self.bg_color,
                               command=lambda: self.button_press("*"), height=self.height, width=self.width, font=self.font)
        self.multiply.grid(row=4, column=3)

        self.divide = Button(self.gui, text=' / ', fg=self.font_color, bg=self.bg_color,
                             command=lambda: self.button_press("/"), height=self.height, width=self.width, font=self.font)
        self.divide.grid(row=5, column=3)

        self.equal = Button(self.gui, text=' = ', fg=self.font_color, bg=self.bg_color,
                            command=self.equal_press, height=self.height, width=self.width, font=self.font)
        self.equal.grid(row=5, column=2)

        self.clear = Button(self.gui, text='Clear', fg=self.font_color, bg=self.bg_color,
                            command=self.clear_press, height=self.height, width=self.width, font=self.font)
        self.clear.grid(row=6, column=0)

        self.decimal = Button(self.gui, text='.', fg=self.font_color, bg=self.bg_color,
                              command=lambda: self.button_press('.'), height=self.height, width=self.width, font=self.font)
        self.decimal.grid(row=5, column=1)
        # start the GUI
        self.gui.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.start()
