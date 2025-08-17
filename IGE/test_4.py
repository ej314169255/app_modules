import types


def flat_generator(list_of_lists):
    result = []
    for el in iterate_nested_list(list_of_lists, result):
        yield el

def iterate_nested_list(a, result):
    for e in a:
        # Проверить, является ли элемент списком
        if isinstance(e, list):
            # Повторить для внутреннего списка
            iterate_nested_list(e, result)
        else:
            result.append(e)
    return result


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
