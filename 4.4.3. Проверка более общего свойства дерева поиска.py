#Проверка более общего свойства дерева поиска
#Данная задача полностью аналогична предыдущей, но проверять теперь нужно более общее свойство. Дереву разрешается содержать равные ключи, но они всегда должны находиться в правом поддереве. Формально, двоичное дерево называется деревом поиска, если для любой вершины её ключ больше всех ключей из её левого поддерева и не меньше всех ключей из правого поддерева

from sys import setrecursionlimit

class Tree:

    def __init__(self, n):    #конструктор 
        self.tree = []
        for i in range(n):
            self.tree.append([int(s) for s in input().split()])

    def run_in_order(self, v, t_min, t_max):    #проверка правильности порядка, параметры: вершина, максимум и минимум дерева
        if v == -1:    #база рекурсии 
            return True
        if self.tree[v][0] < t_min or self.tree[v][0] > t_max:    #сравниваем вершины с переданными параметрами
            return False
        return self.run_in_order(self.tree[v][1], t_min, self.tree[v][0]-1) and self.run_in_order(self.tree[v][2], self.tree[v][0], t_max)    #рекурсия 

    def check(self):
        return self.run_in_order(0, float('-inf'), float('inf'))


def solve():
    n = int(input())
    setrecursionlimit(100001)    #расширяет стэк (нужно для рекурсии)

    t = Tree(n)

    print('CORRECT' if not n or t.check() else 'INCORRECT')


if __name__ == '__main__':
    solve()
