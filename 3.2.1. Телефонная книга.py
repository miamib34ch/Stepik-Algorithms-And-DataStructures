#Телефонная книга
#Реализовать структуру данных, эффективно обрабатывающую запросы вида add number name, del number и find number.
#Вход. Последовательность запросов вида add number name, del number и find number, где number — телефонный номер, содержащий не более семи знаков, а name — короткая строка.
#Выход. Для каждого запроса find number выведите соответствующее имя или сообщите, что такой записи нет.

def solve():
    n = int(input())
    d = {}

    for i in range(n):
        s = input()
        if s.startswith('add'):    #если запрос add
            s, number, name = s.split()    #выбираем из строки номер и имя контакта
            d[number] = name    #номер контакта - ключ словаря, имя значение по ключу
        elif s.startswith('find'):    #если запрос find
            s, number = s.split()
            print(d.get(number, 'not found'))    #если в словаре нет указанного номера, то возвращаем not found
        elif s.startswith('del'):    #если запрос del
            s, number = s.split()
            d.pop(number, None)    #удаляем номер из словаря, если данного номера нет, то возвращаем ничего 


if __name__ == '__main__':
    solve()
