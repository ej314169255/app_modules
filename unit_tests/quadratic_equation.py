def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return (b**2-4*a*c)

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    #x1 = (-b + d ** 0.5)/(2 * a) и x2 = (-b - d ** 0.5) / (2 * a)
    d = discriminant(a,b,c)
    if d < 0:
        print("корней нет")
    elif d == 0:
        print((-b)/(2 * a))
    else:
        print(f"{(-b + d ** 0.5)/(2 * a)} {(-b - d ** 0.5)/(2 * a)}")
    return True

if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)