import tkinter as tk

window = tk.Tk()
window.title('calculate')
window.geometry("500x550")
window.resizable(False, False)
window.configure(bg='black')


# Функция высчитывания операций
def calculate(operation):
    global formula

    if operation == "C":
        formula = ""
    elif operation == "del":
        formula = formula[0:-1]
    elif operation == "X^2":
        formula = str((eval(formula)) ** 2)
    elif operation == "=":
        formula = str(eval(formula))
    elif operation == "%":
        if '+' in formula:
            num_1 = formula.split('+')
            print(num_1)
        elif '-' in formula:
            num_2 = formula.split('-')
            print(num_2)

    else:
        if formula == "0":
            formula = ""
        formula += operation
    label_text.configure(text=formula)

# Создание вывода информации о вычислениях
formula = "0"
label_text = tk.Label(text=formula, font=("Roboto", 30, "bold"), bg="black", foreground="white")
label_text.place(x=11, y=50)

# Создание кнопок
buttons = ['C', 'del', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+','7','8','9','-','+/-','0','%', 'X^2']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg="orange", font=("Roboto", 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 100
    if x > 400:
        x = 18
        y += 81







window.mainloop()
