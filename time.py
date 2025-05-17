import timeit


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
        return mid
    elif n == arr[mid]:
        return mid
    else:
        return -1
arr = [34, 41, 41, 42, 57, 62, 67, 84, 98, 116, 122, 135, 139, 147, 151, 159, 160, 163, 171, 173, 185, 186, 208, 239, 277, 278, 287, 294, 295, 332, 333, 337, 353, 360, 378, 393, 397, 402, 430, 432, 437, 441, 485, 503, 507, 515, 541, 554, 559, 563, 577, 593, 609, 610, 619, 621, 645, 650, 661, 664, 670, 685, 689, 691, 697, 711, 712, 713, 716, 725, 729, 753, 759, 761, 765, 766, 770, 771, 778, 807, 822, 823, 831, 833, 838, 851, 855, 856, 881, 888, 891, 896, 897, 937, 945, 961, 965, 977, 979, 987]
print(search(arr, 881))

def tsearch():

    search(arr, 881)

print(timeit.timeit(stmt = "tsearch()", globals=globals(), number = 100000))

# время 1 - 0,061
# время 25 - 0,04
# время 50 - 0,03
# время 75 - 0,04
# время 100 - 0,067

def search(arr, n):
    ind = 0
    for i in arr:
        if i == n:
            return ind
        ind += 1
    return -1

print(timeit.timeit(stmt = "tsearch()", globals=globals(), number = 100000))

# время 1 - 0,006
# время 25 - 0,055
# время 50 - 0,1
# время 75 - 0,15
# время 100 - 0,2

