from pprint import pprint

import re, locale
locale.setlocale(locale.LC_ALL,"Russian_Russia.1251")

from itertools import groupby

# читаем адресную книгу в формате CSV в список contacts_list
# lastname,firstname,surname,organization,position,phone,email
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
cor_contacts_list = []
for i in contacts_list:
    r =  " ".join(i[0:2]).split() + i[2:]
    cor_contacts_list.append([str(r[0]) + " " +str(r[1])] + r[1:])

# ключевая функция сортировки
keyfunc = lambda x:x[0]

# сортируем список по сочетанию фамилия имя 'x[0]'
identity = sorted(cor_contacts_list, key=keyfunc)

p_word = re.compile(r"\w+")
p_ext = re.compile(r"доб.")
p_tel = re.compile(r"[0-9]")
p_mail = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
record_contacts_list = [contacts_list[0]]

#функция нахождения цифр в поле телефонного номера
def num_s(str_e):
    return [s for s in str_e if p_tel.search(s)][1:]

for id, combination in groupby(identity , key=keyfunc):
    #сортировка по наличию отчества
    order_combination = sorted(combination, key=lambda x:x[2])
    #создание словаря сгруппированных данных
    fields = {}
    for example in order_combination:
        fields['lastname'] = example[0].split()[0]
        fields['firstname'] = example[1]
        fields['surname'] = example[2]

        for field in example[3:]:#выбор полей кроме фио
            if p_mail.search(field):
                fields['email'] = field
            else:
                if p_tel.search(field):
                    fields['phone'] = "+7({0}{1}{2}){3}{4}{5}-{6}{7}-{8}{9}".format(*num_s(field))
                    if p_ext.search(field):
                        fields['phone'] = "+7({0}{1}{2}){3}{4}{5}-{6}{7}-{8}{9} доб.{10}{11}{12}{13}".format(*num_s(field))
                if len(p_word.findall(field))>1 and not p_tel.search(field):
                    fields['position'] = field
                elif len(p_word.findall(field)) == 1:
                    fields['organization'] = field

    #формирование и добавление данных в список для записи из накопленной информации в словаре fields
    #по заголовкам исходной книги (нулевая строка contacts_list[0]
    record_contacts_list.append([fields[column] if column in fields else '' for column in contacts_list[0]])

pprint(record_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(record_contacts_list)