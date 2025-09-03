def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return (b**2-4*a*c)

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a,b,c)
    if d < 0:
        result_function = dict({'description': "корней нет", 'value': False})
    elif d == 0:
        result_function = dict({'description': "один корень", 'value': ((-b)/(2 * a))})
    else:
        result_function = dict({'description': "два корня",
                                'value': ((-b + d ** 0.5)/(2 * a), (-b - d ** 0.5)/(2 * a))})
    return result_function

if __name__ == '__main__':
    print(solution(1, 8, 15))
#     solution(1, -13, 12)
#     solution(-4, 28, -49)
#     solution(1, 1, 1)