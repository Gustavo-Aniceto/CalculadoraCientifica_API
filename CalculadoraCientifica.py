import requests
import tkinter as tk
from tkinter import ttk, messagebox

def get_api_result(expression):
    url = 'http://api.mathjs.org/v4/'
    params = {
        'expr': expression
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro na conexão com a API: {e}")
        return None

def basic_calculate(operation):
    expression = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, expression + operation)

def scientific_calculate(operation):
    expression = display.get()
    result = get_api_result(expression + operation)
    if result:
        display.delete(0, tk.END)
        display.insert(tk.END, result)

def clear_display():
    display.delete(0, tk.END)

def calculate_result():
    expression = display.get()
    result = get_api_result(expression)
    if result:
        display.delete(0, tk.END)
        display.insert(tk.END, result)

root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("400x500")

# Estilo para os botões
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 18),
                padding=10,
                background="black",  # Cor de fundo dos botões (tons de preto)
                foreground="black"        # Cor do texto dos botões (preto)
                )

# Seção de cálculos básicos
basic_buttons = [
    ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('/', 1, 3, 1, 1),
    ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('*', 2, 3, 1, 1),
    ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('-', 3, 3, 1, 1),
    ('0', 4, 0, 1, 1), ('.', 4, 1, 1, 1), ('C', 4, 2, 1, 1), ('+', 4, 3, 1, 1),
    ('=', 5, 0, 1, 2)
]

for button_text, row, col, rowspan, columnspan in basic_buttons:
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: basic_calculate(text))
    button.grid(row=row, column=col, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan, sticky="nsew")

# Seção de cálculos científicos
scientific_buttons = [
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('^', 4, 4),
    ('√', 1, 5), ('x²', 2, 5), ('x³', 3, 5), ('!', 4, 5)
]

for button_text, row, col in scientific_buttons:
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: scientific_calculate(text))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

clear_button = ttk.Button(root, text="C", command=clear_display)
clear_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

# Botão de igual (calcular o resultado)
result_button = ttk.Button(root, text="=", command=calculate_result)
result_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew", columnspan=2)

# Display
display = tk.Entry(root, font=("Arial", 24), justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# Ajusta o tamanho das colunas e linhas para preencher toda a janela
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
