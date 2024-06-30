import tkinter as tk
def calculate():
    a = float(entry1.get())
    b = float(entry2.get())
    operation = operation_var.get()
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            result = "Error! Division by zero is UNDEFINED."
        else:
            result = a / b
    elif operation == "%":
        if b == 0:
            result = "Error! Modulo by zero is UNDEFINED."
        else:
            result = a % b
    if isinstance(result, float):
        result = round(result, 3)
    result_label.config(text="Result: " + str(result))
root = tk.Tk()
root.title("Simple Calculator")
entry1 = tk.Entry(root,width=20)
entry1.pack()

operation_var = tk.StringVar()
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/", "%")
operation_menu.pack()

entry2 = tk.Entry(root,width=20)
entry2.pack()

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

