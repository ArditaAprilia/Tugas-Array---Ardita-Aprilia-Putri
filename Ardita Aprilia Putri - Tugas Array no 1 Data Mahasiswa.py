def input_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return {"nama": nama, "nim": nim, "prodi": prodi, "nilai": nilai}

def tampilkan_data(daftar_mahasiswa):
    print("\nData Mahasiswa:")
    for x in daftar_mahasiswa:
        print(f"Nama: {x['nama']}, NIM: {x['nim']}, Prodi: {x['prodi']}, Nilai: {x['nilai']}")

def hitung_rata_nilai(daftar_mahasiswa):
    total_nilai = sum(x['nilai'] for x in daftar_mahasiswa)
    rata_rata = total_nilai / len(daftar_mahasiswa)
    print(f"\nRata-rata nilai mahasiswa: {rata_rata:.2f}")

def cari_nilai(daftar_mahasiswa):
    tertinggi = max(daftar_mahasiswa, key=lambda x: x['nilai'])
    terendah = min(daftar_mahasiswa, key=lambda x: x['nilai'])
    print(f"\nMahasiswa dengan nilai tertinggi adalah {tertinggi['nama']} dengan nilai {tertinggi['nilai']}")
    print(f"Mahasiswa dengan nilai terendah adalah {terendah['nama']} dengan nilai {terendah['nilai']}")

daftar_mahasiswa = []

while True:
    print("========================================")
    print("              Data Mahasiswa            ")
    print("========================================")
    print("| 1. Input data mahasiswa              |")
    print("| 2. Tampilkan data mahasiswa          |")
    print("| 3. Hitung rata-rata nilai mahasiswa  |")
    print("| 4. Cari nilai tertinggi dan terendah |")
    print("| 5. Keluar                            |")
    print("========================================")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == '1':
        mahasiswa = input_data()
        daftar_mahasiswa.append(mahasiswa)
    elif pilihan == '2':
        tampilkan_data(daftar_mahasiswa)
    elif pilihan == '3':
        hitung_rata_nilai(daftar_mahasiswa)
    elif pilihan == '4':
        cari_nilai(daftar_mahasiswa)
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
        