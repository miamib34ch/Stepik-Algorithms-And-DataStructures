#Максимум в скользящем окне
#Найти максимум в каждом окне размера m данного массива чисел A[1 . . . n].
#Вход. Массив чисел A[1 . . . n] и число 1 ≤ m ≤ n.
#Выход. Максимум подмассива A[i . . . i + m − 1] для всех 1 ≤ i ≤ n − m + 1.

def solve():
    n = int(input())
    mas = [int(s) for s in input().split()]
    m = int(input())

    window = []
    s = []

    for i in range(m):    #первое окно
        window.append(mas[i]) 
        while len(s) and mas[i] > s[-1]: #максимум окна в s
            s.pop()
        s.append(mas[i])

    print(s[0], end=' ')
    for i in range(m, n):
        if window[i % m] == s[0]:    #остаток от деления "задаёт окно"
            s.pop(0)    #если старый максимум прошёл, удаляем его
        window[i % m] = mas[i]    #двигаем окно
        while len(s) and mas[i] > s[-1]:    #новый максимум окна
            s.pop()
        s.append(mas[i])
        print(s[0], end=' ')


if __name__ == '__main__':
    solve()