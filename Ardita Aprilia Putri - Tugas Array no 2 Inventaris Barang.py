def input_data():
    nama = input("Masukkan nama barang: ")
    kode = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    return {"nama": nama, "kode": kode, "jumlah": jumlah}

def tampilkan_barang(daftar_barang):
    if not daftar_barang:
        print("\nTidak ada barang di inventaris.")
    else:
        print("\nData Barang pada Inventaris:")
        for barang in daftar_barang:
            print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")

def cari_berdasarkan_kode(daftar_barang, kode):
    for barang in daftar_barang:
        if barang['kode'] == kode:
            return barang
    return None

def hapus_berdasarkan_kode(daftar_barang, kode):
    for barang in daftar_barang:
        if barang['kode'] == kode:
            daftar_barang.remove(barang)
            return True
    return False

daftar_barang = []

while True:
    print("========================================")
    print("           Inventaris Barang       ")
    print("========================================")
    print("| 1. Tambah barang                     |")
    print("| 2. Tampilkan semua barang            |")
    print("| 3. Cari barang berdasarkan kode      |")
    print("| 4. Hapus barang berdasarkan kode     |")
    print("| 5. Keluar                            |")
    print("========================================")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == '1':
        barang = input_data()
        daftar_barang.append(barang)
    elif pilihan == '2':
        tampilkan_barang(daftar_barang)
    elif pilihan == '3':
        kode = input("Masukkan kode barang yang dicari: ")
        barang = cari_berdasarkan_kode(daftar_barang, kode)
        if barang:
            print(f"\n Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")
        else:
            print("\nBarang tidak ada.")
    elif pilihan == '4':
        kode = input("Masukkan kode barang yang akan dihapus: ")
        if hapus_berdasarkan_kode(daftar_barang, kode):
            print("\nBarang telah dihapus.")
        else:
            print("\nBarang tidak ada.")
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")