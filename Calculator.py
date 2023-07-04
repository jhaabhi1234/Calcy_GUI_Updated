import tkinter as tk

def calculate():
    choice = choice_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())

    if choice == "+":
        result = a + b
    elif choice == "-":
        result = a - b
    elif choice == "*":
        result = a * b
    elif choice == "/":
        result = a / b
    elif choice == "%":
        result = a % b
    else:
        result = "Invalid choice"

    result_label.configure(text="Result: " + str(result))

window = tk.Tk()
window.title("Calculator")

choice_label = tk.Label(window, text="Mathematical symbol (+, -, *, /, %):")
choice_label.pack()

choice_entry = tk.Entry(window)
choice_entry.pack()

a_label = tk.Label(window, text="First number:")
a_label.pack()

a_entry = tk.Entry(window)
a_entry.pack()

b_label = tk.Label(window, text="Second number:")
b_label.pack()

b_entry = tk.Entry(window)
b_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
