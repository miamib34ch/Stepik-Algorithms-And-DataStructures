#Объединение таблиц
#Формат входа. Первая строка содержит числа n и m — число таблиц и число запросов, соответственно. Вторая строка содержит n целых чисел r1, ..., rn — размеры таблиц. Каждая из последующих m строк содержит два номера таблиц destinationi и sourcei, которые необходимо объединить.
#Формат выхода. Для каждого из m запросов выведите максимальный размер таблицы после соответствующего объединен

class Sets:
    def __init__(self, n):    #конструктор 
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.tables = [int(s) for s in input().split()]    #ввод размеров таблицы 
        self.max_rows = max(self.tables)

    def find_root(self, i):    #находит "адрес"
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):    #по методичке
        i_id = self.find_root(i)    #рассмотрим таблицу с номером destinationi. Пройдясь по цепочке символьных ссылок, найдём номер реальной таблицы, на которую ссылается эта таблица: пока таблица destinationi содержит символическую ссылку: destinationi ← symlink(destinationi)
        j_id = self.find_root(j)    # Сделаем то же самое с таблицей sourcei

        #Теперь таблицы destinationi и sourcei содержат реальные записи. Если destinationi != sourcei, скопируем все записи из таблицы sourcei в таблицу destinationi, очистим таблицу sourcei и пропишем в неё символическую ссылку на таблицу destinationi
        
        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.tables[i_id] += self.tables[j_id]
            self.tables[j_id] = 0
        else:
            self.parent[i_id] = j_id
            self.tables[j_id] += self.tables[i_id]
            self.tables[i_id] = 0
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        
        self.max_rows = max(self.max_rows, self.tables[i_id], self.tables[j_id])    # Выведем максимальный размер среди всех n таблиц. Размером таблицы называется число строк в ней. Если таблица содержит символическую ссылку, считаем её размер равным нулю.


def solve():
    n, m = [int(s) for s in input().split()]

    sets = Sets(n)

    for i in range(m):
        des, source = [int(s)-1 for s in input().split()]
        sets.union(des, source)
        print(sets.max_rows)


if __name__ == '__main__':
    solve()
