#Поиск образца в тексте
#Найти все вхождения строки Pattern в строку Text.
#Вход. Строки Pattern и Text.
#Выход. Все индексы i строки Text, начиная с которых строка Pattern входит в Text: Text[i..i + |Pattern| − 1] = Pattern.

pattern = [ord(s) - 65 for s in input()]
text = [ord(s) - 65 for s in input()]

m, n = len(pattern), len(text)
x, p = 59, 67    #простые числа

x_pows = [1]    #степени x от 1 до m-1 по модулю p
for i in range(1, m):
    x_pows.append(x_pows[-1] * x % p)

pattern_hash = sum([pattern[i] * x_pows[m-i-1] for i in range(m)]) % p    #считаем хэш паттерна

last_odn = [text[i] * x_pows[-1] % p for i in range(n - m + 1)]    #последний одночлен в полиноме хеша: text[i] * x ^ (m-1)

cur_hash = (last_odn[0] + sum([text[i] * x_pows[m-i-1] for i in range(1, m)])) % p    #хеш первой подстроки

for i in range(n - m):
    if pattern_hash == cur_hash and pattern == text[i:(i+m)]:    #проверяем совпадение хеша паттерна и подстроки
        print(i, end = ' ')

    cur_hash = ((cur_hash - last_odn[i]) * x + text[i + m]) % p #пересчёт хэша подстроки

if pattern_hash == cur_hash and pattern == text[(n-m):]:    #проверяем совпадение хеша паттерна и последней подстроки
    print(n - m, end = ' ')