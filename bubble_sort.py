
def sort():
    list = [7, 2, 4, 12, 2, 4]
    for i in range(0, (len(list) - 1)):
        for j in range(0, (len(list) - 1 - i)):
            if(list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list



result = sort()
print(result)