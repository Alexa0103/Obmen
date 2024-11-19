import requests
import json
from tkinter import  *
from tkinter import  messagebox as mb
from tkinter import ttk

def exchange():
    #code = entry.get().upper() # из поля ввода энтри получаем код валюты, upper - преобразование букв в заглавные
    code = combobox.get()
    if code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/USD')
            response.raise_for_status() # если код 200 - все отлично
            data = response.json()

            if code in data['rates']: #смотрим, есть ли внутри раздела "rates" заданная валюта
                exchange_rate = data['rates'][code]

                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.2f} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")

    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты к доллару")
window.geometry("360x180")

Label(text="Выберите код валюты:").pack(padx=10, pady=10)

# Список 10 популярных валют
popular_currencies = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]
combobox = ttk.Combobox(values=popular_currencies)
combobox.pack(padx=10, pady=10)

#entry = Entry()
#entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()



