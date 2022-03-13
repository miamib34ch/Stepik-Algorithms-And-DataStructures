#Построение кучи
#Переставить элементы заданного массива чисел так, чтобы он удовлетворял свойству мин-кучи.
#Вход. Массив чисел A[0 . . . n − 1].
#Выход. Переставить элементы массива так, чтобы выполнялись неравенства A[i] ≤ A[2i + 1] и A[i] ≤ A[2i + 2] для всех i.

size, heap = int(input()), [int(i) for i in input().split()]
steps = []
for i in range(size // 2, -1, -1):
  while i < size:
    m, left, right = i, 2 * i + 1, 2 * i + 2
    if left < size and heap[left] < heap[m]: m = left    #по условиям
    if right < size and heap[right] < heap[m]: m = right    #по условиям
    if m == i: break
    steps += [[i, m]]    #добавляем в ответ перестановку
    heap[i], heap[m], i = heap[m], heap[i], m    #переставляем 
print(len(steps))
for step in steps: print(*step)
