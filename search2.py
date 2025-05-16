#Линейный поиск и сложности алгоритмов

def search(arr, n):
    arr.sort()
    first = 0
    mid = len(arr) // 2                     #3
    last = len(arr) - 1                     #5
    while arr[mid] != n and first <= last:
        if n > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if first == mid:
        print("Число нашлось, под индексом:")
        return mid
    elif n == arr[mid]:
        print("Число нашлось, под индексом:")
        return mid
    else:
        print("Пойми брат, нет такого числа!")
        return -1
arr = [5, 1, 15, 30, 50, 150]
print(search(arr, 5))

from random import randint

arr = []
for i in range(100):
    arr.append(randint(1, 1000))
arr.sort()
print(arr)
print(search(arr, int(input('Введите число для поиска индекса: '))))

