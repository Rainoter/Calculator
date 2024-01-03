import tkinter as tk

def on_button_click(key):
    current = display_var.get()
    if key == 'C':
        display_var.set('')
    elif key == '=':
        try:
            result = str(eval(current))
            display_var.set(result)
        except:
            display_var.set("Error")
    else:
        display_var.set(current + key)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Frame to contain the calculator with a blue shadow effect
frame = tk.Frame(root, bd=10, relief=tk.RIDGE, highlightbackground='blue', highlightthickness=5)
frame.grid(row=0, column=0)

# Variable to store the display value
display_var = tk.StringVar()

# Entry widget to display the input and result
display = tk.Entry(frame, textvariable=display_var, font=('Arial', 18), bd=10, insertwidth=4, width=15, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button labels
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '', '', '')
]

# Create and place buttons with a blue shadow effect
for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        if label != '':
            button = tk.Button(frame, text=label, padx=20, pady=20, font=('Arial', 14), command=lambda key=label: on_button_click(key))
            button.grid(row=i + 1, column=j, padx=5, pady=5)

# Run the main loop
root.mainloop()
