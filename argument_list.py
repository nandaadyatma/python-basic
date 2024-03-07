
def jumlahkan(*list_angka):
    result = 0
    for i in list_angka:
        result = result + i
    return result

print(jumlahkan(3, 5, 6, 23, 23, 1))