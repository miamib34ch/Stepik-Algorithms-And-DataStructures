#Хеширование цепочками
#Формат входа. Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n. Каждая из последующих n строк содержит запрос одного из перечисленных выше четырёх типов.
#Формат выхода. Для каждого из запросов типа find и check выведите результат в отдельной строке.

d = [[] for _ in range(int(input()))]    #таблица с заданным размером
for _ in range(int(input())):    #для каждого запроса
    cmd, v = input().split()    #в cmd идёт команда, в v идёт значение 
    if cmd == 'check': print(*d[int(v)]) #если команда check, то выводим список под индексом v
    else: 
        h = sum([ord(s)*263**i for i, s in enumerate(v)]) % 1000000007 % len(d) #по формуле данной в методичке, ord() - получает ASCII-код i-го символа
        if cmd == 'add' and not v in d[h]:  d[h].insert(0,v)    #если add И значения нет в таблице, то добавляем  
        elif cmd == 'find': print('yes' if v in d[h] else 'no')    #если find, то выводим соотвествующие ответы по наличие в таблице  
        elif cmd == 'del' and v in d[h]: d[h].remove(v)    #если del, то удаляем 