menu_pilihan = input("Silahkan masukkan angka:")

if (not(menu_pilihan is int)):
    print("masukan tidak valid")
elif (int(menu_pilihan) < 10):
    print("Angka kurang dari 10")
elif (int(menu_pilihan) == 10):
    print("Angka sama dengan 10")
elif (int(menu_pilihan) > 10):
    print("Angka lebih dari 10")

