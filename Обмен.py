import requests
import json
from tkinter import  *
from tkinter import  messagebox as mb
from tkinter import ttk


def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    # Получаем полное название валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)#метка с названием валюты под комбобоксом

def exchange():
    #code = entry.get().upper() # из поля ввода энтри получаем код валюты, upper - преобразование букв в заглавные
    #code = combobox.get()
    target_code = target_combobox.get() # Целевая валюта
    base_code = base_combobox.get() # базовая валюта

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка!", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка!", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")

# Словарь кодов валют и их полных названий
currencies = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахский тенге",
    "UZS": "Узбекский сум",
    "AED": "Дирхам ОАЭ",
    "AMD": "Армянский драм",
    "USD": "Американский доллар"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x200")

'''Label(text="Выберите код валюты:").pack(padx=10, pady=10)

# Список 10 популярных валют
popular_currencies = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]
combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)'''

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



