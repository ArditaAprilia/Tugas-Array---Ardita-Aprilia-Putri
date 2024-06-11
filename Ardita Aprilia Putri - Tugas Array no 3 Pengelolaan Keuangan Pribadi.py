def input_transaksi():
    jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
    deskripsi = input("Masukkan deskripsi transaksi: ")
    jumlah = float(input("Masukkan jumlah transaksi: "))
    return {"jenis": jenis, "deskripsi": deskripsi, "jumlah": jumlah}

def tampilkan_transaksi(daftar_transaksi):
    if not daftar_transaksi:
        print("\nTidak ada transaksi.")
    else:
        print("\nData Transaksi Keuangan:")
        for transaksi in daftar_transaksi:
            print(f"Jenis: {transaksi['jenis']}, Deskripsi: {transaksi['deskripsi']}, Jumlah: {transaksi['jumlah']}")

def hitung_total_pemasukan(daftar_transaksi):
    total_pemasukan = sum(transaksi['jumlah'] for transaksi in daftar_transaksi if transaksi['jenis'] == 'pemasukan')
    print(f"\nTotal Pemasukan: {total_pemasukan:.2f}")
    return total_pemasukan

def hitung_total_pengeluaran(daftar_transaksi):
    total_pengeluaran = sum(transaksi['jumlah'] for transaksi in daftar_transaksi if transaksi['jenis'] == 'pengeluaran')
    print(f"\nTotal Pengeluaran: {total_pengeluaran:.2f}")
    return total_pengeluaran

def hitung_saldo_akhir(total_pemasukan, total_pengeluaran):
    saldo_akhir = total_pemasukan - total_pengeluaran
    print(f"\nSaldo Akhir: {saldo_akhir:.2f}")
    return saldo_akhir

daftar_transaksi = []

while True:
    print("===================================")
    print("  Pengelolaan Keuangan Pribadi")
    print("===================================")
    print("| 1. Tambah transaksi             |")
    print("| 2. Tampilkan semua transaksi    |")
    print("| 3. Hitung total pemasukan       |")
    print("| 4. Hitung total pengeluaran     |")
    print("| 5. Hitung saldo akhir           |")
    print("| 6. Keluar                       |")
    print("===================================")
    pilihan = input("Pilih menu (1/2/3/4/5/6): ")
    
    if pilihan == '1':
        transaksi = input_transaksi()
        daftar_transaksi.append(transaksi)
    elif pilihan == '2':
        tampilkan_transaksi(daftar_transaksi)
    elif pilihan == '3':
        total_pemasukan = hitung_total_pemasukan(daftar_transaksi)
    elif pilihan == '4':
        total_pengeluaran = hitung_total_pengeluaran(daftar_transaksi)
    elif pilihan == '5':
        total_pemasukan = hitung_total_pemasukan(daftar_transaksi)
        total_pengeluaran = hitung_total_pengeluaran(daftar_transaksi)
        hitung_saldo_akhir(total_pemasukan, total_pengeluaran)
    elif pilihan == '6':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")