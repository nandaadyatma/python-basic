banyak = int(input("Masukkan angka jumlah data yang akan dimasukkan:"))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke-{i+1}")
    input_nama = input("Masukkan nama:")
    input_umur = int(input("Masukkan umur:"))

    nama.append(input_nama)
    umur.append(input_umur)

print(nama)
print(umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")


