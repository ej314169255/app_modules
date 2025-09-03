documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    # your code
    res = []
    for str_val in documents:
        if doc_number == str_val.get('number'):
            res = res.append(str_val.get('name'))
            break
    # if not res:
    #     return 'Документ не найден'
    return res


def get_directory(doc_number):
    result = []  # создание списка результатов поиска
    for key, val in directories.items():
        if doc_number in val:
            result.append([key, val])
    # if result:
        # sh = result[0][0]
    # else:
    #     return 'Полки с таким документом не найдено'
    return result


def add(document_type, number, name, shelf_number):
    # your code
    if number not in directories.values():
        directories.update({str(shelf_number): [number]})
        documents.append({'type': document_type, 'number': number, 'name': name})


if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))