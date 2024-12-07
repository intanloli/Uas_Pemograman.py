import time

# Daftar antrian pasien
queue = []
daftar_poli = ["Umum", "Anak", "Kandungan", "Gigi"]

def daftar_pasien(nama, poli, darurat, status='menunggu'):
    pasien = {
        'nama': nama,
        'darurat': darurat,
        'poli': poli,
        'status': status,
    }
    if darurat == 'y':
        queue.insert(0, pasien)
    else:
        queue.append(pasien)
    print(f"Pasien {nama} ditambahkan ke antrian di poli {poli}.")

def perkiraan_waktu_tunggu():
    waktu_tunggu = len(queue) * 15
    return waktu_tunggu

def kelola_pasien():
    if queue:
        pasien_sekarang = queue.pop(0)  # Mendahulukan pasien darurat
        pasien_sekarang['status'] = 'sedang dirawat'
        print(f"Mengerjakan pasien: {pasien_sekarang['nama']} di poli {pasien_sekarang['poli']}")
        time.sleep(1)  # Simulasi perawatan
        pasien_sekarang['status'] = 'selesai'
        print(f"Pasien {pasien_sekarang['nama']} telah selesai diobati.")
    else:
        print("Tidak ada pasien dalam antrian.")

def rekam_status_pasien():
    print("\nRekam status pasien:")
    for pasien in queue:
        print(f"Nama: {pasien['nama']}")
        print(f"Status: {pasien['status']}")
        print(f"Darurat: {pasien['darurat']}")
        print(f"Poli: {pasien['poli']}")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah pasien")
        print("2. Perkiraan waktu tunggu")
        print("3. Penanganan pasien")
        print("4. Rekam status pasien")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            darurat = input("Apakah pasien darurat? (y/n): ").lower()

            print("Pilih poli:")
            for i, poli in enumerate(daftar_poli, start=1):
                print(f"{i}. {poli}")
            try:
                poli_index = int(input("Masukkan nomor poli yang dipilih: "))
                if 1 <= poli_index <= len(daftar_poli):
                    poli = daftar_poli[poli_index - 1]
                    daftar_pasien(nama, poli, darurat)
                else:
                    print("Nomor poli tidak valid.")
            except ValueError:
                print("Input tidak valid. Masukkan nomor poli.")

        elif pilihan == '2':
            waktu_tunggu = perkiraan_waktu_tunggu()
            print(f"Perkiraan waktu tunggu: {waktu_tunggu} menit.")
        
        elif pilihan == '3':
            kelola_pasien()

        elif pilihan == '4':
            rekam_status_pasien()

        elif pilihan == '5':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
