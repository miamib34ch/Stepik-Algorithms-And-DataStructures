#Множество с запросами суммы на отрезке
#Реализуйте структуру данных для хранения множества целых чисел, поддерживающую запросы добавления, удаления, поиска, а также суммы на отрезке. На вход в данной задаче будет дана последовательность таких запросов. Чтобы гарантировать, что ваша программа обрабатывает каждый запрос по мере поступления (то есть онлайн), каждый запрос будет зависеть от результата выполнения одного из предыдущих запросов. Если бы такой зависимости не было, задачу можно было бы решить оффлайн: сначала прочитать весь вход и сохранить все запросы в каком-нибудь виде, а потом прочитать вход ещё раз, параллельно отвечая на запросы.
#Формат входа. Изначально множество пусто. Первая строка содержит число запросов n. Каждая из n следующих строк содержит запрос в одном из следующих четырёх форматов: 
    #• + i: добавить число f(i) в множество (если оно уже есть, проигнорировать запрос);
    #• - i: удалить число f(i) из множества (если его нет, проигнорировать запрос);
    #• ? i: проверить принадлежность числа f(i) множеству;
    #• s l r: посчитать сумму всех элементов множества, попадающих в отрезок [f(l), f(r)].
#Функция f определяется следующим образом. Пусть s — результат последнего запроса суммы на отрезке (если таких запросов ещё не было, то s = 0). Тогда f(x) = (x + s) mod 1 000 000 001.
#Формат выхода. Для каждого запроса типа ? i выведите «Found» или «Not found». Для каждого запроса суммы выведите сумму всех элементов множества, попадающих в отрезок [f(l), f(r)]. Гарантируется, что во всех тестах f(l) ≤ f(r).

from sys import setrecursionlimit, stdin

def f(x, f_sum):    #по условию
    return (x + f_sum) % p

def get_height(t):    #получает высоту дерева
    return t.height if t else 0

def get_sum(t):    #получает сумму дерева
    return t.s if t else 0

def fix_height(t):    #меняем высоту
    h_l = get_height(t.left)
    h_r = get_height(t.right)
    t.height = max(h_l, h_r)+1

def fix_sum(t):    #меняем сумму
    t.s = t.key + get_sum(t.left) + get_sum(t.right)

def b_factor(t):    #фактор баланса
    return get_height(t.right)-get_height(t.left)

def rotate_right(t):    #вращение правой ветви    
    q = t.left
    t.left = q.right
    q.right = t
    fix_height(t)
    fix_height(q)
    fix_sum(t)
    fix_sum(q)
    return q

def rotate_left(t):    #вращение левой ветви
    q = t.right
    t.right = q.left
    q.left = t
    fix_height(t)
    fix_height(q)
    fix_sum(t)
    fix_sum(q)
    return q

def balance(t):    #балансировка дерева
    fix_height(t)
    if b_factor(t) == 2:
        if b_factor(t.right) < 0:
            t.right = rotate_right(t.right)
        return rotate_left(t)
    if b_factor(t) == -2:
        if b_factor(t.left) > 0:
            t.left = rotate_left(t.left)
        return rotate_right(t)
    fix_sum(t)
    return t

def insert(t, k):    #добавить в дерево, команда +
    if not t:
        return Tree(k)
    if k < t.key:
        t.left = insert(t.left, k)
    elif k > t.key:
        t.right = insert(t.right, k)
    return balance(t)

def find_min(t):    #находит минимальный
    while t.left:
        t = t.left
    return t

def remove_min(t):    #удалить минимальный
    if not t.left:
        return t.right
    t.left = remove_min(t.left)
    return balance(t)

def remove(t, k):    #удалить из дерева, команда -
    if not t:
        return
    if k < t.key:
        t.left = remove(t.left, k)
    elif k > t.key:
        t.right = remove(t.right, k)
    else:
        l = t.left
        r = t.right
        del t
        if not r:
            return l
        m = find_min(r)
        m.right = remove_min(r)
        m.left = l
        return balance(m)
    return balance(t)

def find(t, k):    #поиск по дереву, команда ?
    while t and k != t.key:
        if k < t.key:
            t = t.left
        else:
            t = t.right
    return t

def sum_range(t, key):    #сумма на отрезке
    found = False
    less_sum = 0
    greater_sum = 0
    while t:
        if key < t.key:
            if t.right:
                greater_sum += get_sum(t.right)
            greater_sum += t.key
            t = t.left
        elif key > t.key:
            if t.left:
                less_sum += get_sum(t.left)
            less_sum += t.key
            t = t.right
        else:
            found = True
            break
    if found:
        if t.left:
            less_sum += get_sum(t.left)
        if t.right:
            greater_sum += get_sum(t.right)

    return less_sum, greater_sum

class Tree:
    def __init__(self, k):    #конструктор
        self.left = None
        self.right = None
        self.key = k
        self.height = 1
        self.s = k

def solve():
    setrecursionlimit(100001)    #увеличивает размер стэка (нужно для рекурсии)
    n = int(input())
    f_sum = 0
    tree = None
    for i in range(n):
        command = stdin.readline()
        if command[0] == '+':
            i = int(command.split()[-1])
            tree = insert(tree, f(i, f_sum))
        elif command[0] == '-':
            i = int(command.split()[-1])
            tree = remove(tree, f(i, f_sum))
        elif command[0] == '?':
            i = int(command.split()[-1])
            if find(tree, f(i, f_sum)):
                print('Found')
            else:
                print('Not found')
        elif command[0] == 's':
            l, r = int(command.split()[-2]), int(command.split()[-1])
            if f(l, f_sum) <= f(r, f_sum):
                f_sum = get_sum(tree) - sum_range(tree, f(l, f_sum))[0] - sum_range(tree, f(r, f_sum))[1]
            else:
                f_sum = 0
            print(f_sum)

if __name__ == '__main__':
    p = 1000000001
    solve()
