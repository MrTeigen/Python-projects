import tkinter
import tkinter.font as font

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry("640x960")
mainWindow.minsize(320, 480)
if mainWindow.geometry == "320x480":
    mainWindow["padx"] = 10
#    mainWindow(padx=10)
else:
    mainWindow["padx"] = 20
mainWindow["pady"] = 10

myFont = tkinter.font.Font(size=35)

result = tkinter.Entry(mainWindow, font=myFont)
result.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="news")


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
# mainWindow.columnconfigure(4, weight=10)
mainWindow.rowconfigure(0, weight=2)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=10)
mainWindow.rowconfigure(3, weight=10)
mainWindow.rowconfigure(4, weight=10)
mainWindow.rowconfigure(5, weight=10)
# mainWindow.rowconfigure(6, weight=10)
# mainWindow.rowconfigure(7, weight=10)
# mainWindow.rowconfigure(8, weight=10)
# mainWindow.rowconfigure(9, weight=10)
# mainWindow.rowconfigure(10, weight=10)
length_result = 0
calculator_showing = ''
calculator_showing_2 = ''
operator = ''


def calc_shows(x):
    global calculator_showing
    calculator_showing = (str(x) + str(calculator_showing))

# function which


def button_click(x):
    global length_result, operator, calculator_showing, calculator_showing_2
    if x in range(10):
        length_result += 1
        result.insert(length_result, x)
        calc_shows(x)
    elif x == '*' or x == '+' or x == '-' or x == '/':
        operator = x
        calculator_showing_2 = result.get()
        calculator_showing = ''
        button_clear()
    else:
        if operator == '':
            button_clear()
            result.insert(0, 'Nope, no operator')
        else:
            calculator_showing = result.get()
            result.delete(0, len(result.get()))
            result.insert(0, eval('{}{}{}'.format(calculator_showing_2, operator, calculator_showing)))


# function for clearing the display

def button_clear():
    global length_result, calculator_showing
    length_result = 0
    result.delete(0, len(result.get()))
    calculator_showing = ''


# Making the buttons

cButton = tkinter.Button(mainWindow, text=" C ", font=myFont, command=button_clear)
ceButton = tkinter.Button(mainWindow, text="CE", font=myFont, command=button_clear)
zeroButton = tkinter.Button(mainWindow, text=" 0 ", font=myFont, command=lambda: button_click(0))
oneButton = tkinter.Button(mainWindow, text=" 1 ", font=myFont, command=lambda: button_click(1))
twoButton = tkinter.Button(mainWindow, text=" 2 ", font=myFont, command=lambda: button_click(2))
threeButton = tkinter.Button(mainWindow, text=" 3 ", font=myFont, command=lambda: button_click(3))
fourButton = tkinter.Button(mainWindow, text=" 4 ", font=myFont, command=lambda: button_click(4))
fiveButton = tkinter.Button(mainWindow, text=" 5 ", font=myFont, command=lambda: button_click(5))
sixButton = tkinter.Button(mainWindow, text=" 6 ", font=myFont, command=lambda: button_click(6))
sevenButton = tkinter.Button(mainWindow, text=" 7 ", font=myFont, command=lambda: button_click(7))
eightButton = tkinter.Button(mainWindow, text=" 8 ", font=myFont, command=lambda: button_click(8))
nineButton = tkinter.Button(mainWindow, text=" 9 ", font=myFont, command=lambda: button_click(9))
multiplicationButton = tkinter.Button(mainWindow, text=" x ", font=myFont, command=lambda: button_click('*'))
divideButton = tkinter.Button(mainWindow, text=" / ", font=myFont, command=lambda: button_click('/'))
addButton = tkinter.Button(mainWindow, text=" + ", font=myFont, command=lambda: button_click('+'))
subtractButton = tkinter.Button(mainWindow, text=" - ", font=myFont, command=lambda: button_click('-'))
equalButton = tkinter.Button(mainWindow, text=" = ", font=myFont, command=lambda: button_click('='))

# Placing the buttons

cButton.grid(row=1, column=0, sticky="wens")
ceButton.grid(row=1, column=1, sticky="wens")
sevenButton.grid(row=2, column=0, sticky="wens")
eightButton.grid(row=2, column=1, sticky="wens")
nineButton.grid(row=2, column=2, sticky="wens")
addButton.grid(row=2, column=3, sticky="wens")
fourButton.grid(row=3, column=0, sticky="wens")
fiveButton.grid(row=3, column=1, sticky="wens")
sixButton.grid(row=3, column=2, sticky="wens")
subtractButton.grid(row=3, column=3, sticky="wens")
oneButton.grid(row=4, column=0, sticky="wens")
twoButton.grid(row=4, column=1, sticky="wens")
threeButton.grid(row=4, column=2, sticky="wens")
multiplicationButton.grid(row=4, column=3, sticky="wens")
zeroButton.grid(row=5, column=0, sticky="wens")
equalButton.grid(row=5, column=1, columnspan=2, sticky="wens")
divideButton.grid(row=5, column=3, sticky="wens")


mainWindow.mainloop()
