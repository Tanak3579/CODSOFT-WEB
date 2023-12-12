import tkinter as tk

def clear():
    display_var.set("")

def calculate():
    try:
        expression = display_var.get().replace("%", "/100")
        result = eval(expression)
        display_var.set(str(result))
    except:
        display_var.set("Error")

def add_to_display(value):
    display_var.set(display_var.get() + str(value))

def undo():
    current_value = display_var.get()
    if current_value != "Error":
        display_var.set(current_value[:-1])

root = tk.Tk()
root.title("Wow Calculator")

root.configure(bg='#333333')
root.geometry("300x400")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, bg='#666666', fg='white', justify='right')
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", "8", "9", "/", "Undo"),
    ("4", "5", "6", "*", "%"),
    ("1", "2", "3", "-", "C"),
    ("0", ".", "=", "+")
]

for i, row in enumerate(buttons):
    for j, button_value in enumerate(row):
        if button_value == "=":
            button = tk.Button(root, text=button_value, width=4, height=2, bg='#FF6347', fg='white', font=('Arial', 15, 'bold'), command=calculate)
        elif button_value in ["C", "Undo"]:
            button = tk.Button(root, text=button_value, width=4, height=2, bg='#FF6347', fg='white', font=('Arial', 15), command=clear if button_value == "C" else undo)
        else:
            button = tk.Button(root, text=button_value, width=4 if button_value != "%" else 8, height=2, bg='#333333', fg='white', font=('Arial', 15), command=lambda val=button_value: add_to_display(val))
        button.grid(row=i + 1, column=j, padx=2, pady=2, sticky="nsew")
        root.grid_columnconfigure(j, weight=1)  # Setting column weights

root.grid_rowconfigure(0, weight=1)

root.mainloop()
