from tabulate import tabulate
data = [ ["Алиса", 24, "Инженер"], ["Боб", 32, "Доктор"], ["Чарли", 28, "Дизайнер"] ]
headers = ["Имя", "Возраст", "Профессия"]
print("Формат grid:")
print(tabulate(data, headers=headers, tablefmt="grid"))
print("\nФормат Markdown:")
print(tabulate(data, headers=headers, tablefmt="pipe"))
print("\nФормат HTML:")
print(tabulate(data, headers=headers, tablefmt="html"))
# ``` [1](https://codeforgeek.com/creating-tables-with-python-tabulate/)[2](https://www.pythoncentral.io/python-tabulate-creating-beautiful-tables-from-your-data/)
# * **Создание таблицы из списка словарей**. В этом примере Tabulate работает напрямую с списком словарей, используя ключи в качестве заголовков.
