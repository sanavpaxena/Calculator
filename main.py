import tkinter
import math

root = tkinter.Tk()
root.title("Calculator")

expression = ""


def add(value):
    global expression
    expression += value
    label_result.config(text = expression)

def clear():
    global expression
    expression = ""
    label_result.config(text = expression)
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)            
        except:
            result = "Error"
            expression = ""
    expression =str(result) 
    label_result.config(text = result)

label_result = tkinter.Label(root, text = "")
label_result.grid(row = 0, column = 0, columnspan = 4)

button1 = tkinter.Button(root, text = "1", command =lambda: add("1"), padx = 7.5)
button1.grid(row = 1, column = 0)

button2 = tkinter.Button(root, text = "2", command = lambda:add("2"), padx = 7.5)
button2.grid(row = 1, column = 1)

button3 = tkinter.Button(root, text = "3", command =lambda: add("3"), padx = 7.5)
button3.grid(row = 1, column = 2)

buttondiv = tkinter.Button(root, text = "/", command =lambda: add("/"), padx = 7.5)
buttondiv.grid(row = 1, column = 3)

button4 = tkinter.Button(root, text = "4", command = lambda:add("4"), padx = 7.5)
button4.grid(row = 2, column = 0)

button5 = tkinter.Button(root, text = "5", command =lambda: add("5"), padx = 7.5)
button5.grid(row = 2, column = 1)

button6 = tkinter.Button(root, text = "6", command =lambda: add("6"), padx = 7.5)
button6.grid(row = 2, column = 2)

buttonmulti = tkinter.Button(root, text = "*", command =lambda: add("*"), padx = 7.5)
buttonmulti.grid(row = 2, column = 3)

button7 = tkinter.Button(root, text = "7", command = lambda:add("7"), padx = 7.5)
button7.grid(row = 3, column = 0)

button8 = tkinter.Button(root, text = "8", command = lambda:add("8"), padx = 7.5)
button8.grid(row = 3, column = 1)

button9 = tkinter.Button(root, text = "9", command = lambda:add("9"), padx = 7.5)
button9.grid(row = 3, column = 2)

buttonsub = tkinter.Button(root, text = "-", command = lambda:add("-"), padx = 7.5)
buttonsub.grid(row = 3, column = 3)

buttonC = tkinter.Button(root, text = "C", command = lambda:clear(), padx = 7.5)
buttonC.grid(row = 4, column = 0)

button0 = tkinter.Button(root, text = "0", command = lambda:add("0"), padx = 7.5)
button0.grid(row = 4, column = 1)

buttondec = tkinter.Button(root, text = ".",width = 1, command =lambda: add("."), padx = 7.5)
buttondec.grid(row = 4, column = 2)

buttonplus = tkinter.Button(root, text = "+", width = 1,command = lambda:add("+"), padx = 7.5)
buttonplus.grid(row = 4, column = 3)

buttonEq = tkinter.Button(root, text = "=",width = 8,command = lambda:calculate(), padx = 1)
buttonEq.grid(row = 5, column = 1, columnspan = 10)

root.mainloop()