def tambah_barang():
    keranjang = {
        "M001": {"nama": "Teh Botol", "harga": 5000, "stock": 2},
        "M002": {"nama": "Tisu", "harga": 3000, "stock": 5},
    }

    while True:
        print("\n----- MENU KERANJANG -----")
        print("1. Tambah/Update Barang")
        print("2. Hapus Barang")
        print("3. Selesai")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            print("\n--- INPUT BARANG ---")
            kode = input("Masukkan kode barang  : ")
            nama = input("Masukkan nama barang  : ")
            harga = int(input("Masukkan harga barang : "))
            stock = int(input("Masukkan stock        : "))

            data_baru = {"nama": nama, "harga": harga, "stock": stock}
            keranjang[kode] = data_baru
            print(f"Barang {nama} berhasil disimpan.")

        elif pilihan == '2':
            print("\n--- HAPUS BARANG ---")
            kode_hapus = input("Masukkan kode barang yang ingin dihapus: ")
            
            if kode_hapus in keranjang:
                nama_terhapus = keranjang[kode_hapus]['nama']
                del keranjang[kode_hapus]
                print(f"Barang '{nama_terhapus}' (Kode: {kode_hapus}) telah dihapus.")
            else:
                print("Error: Kode barang tidak ditemukan!")

        elif pilihan == '3':
            break
        
        else:
            print("Pilihan tidak valid!")

    return keranjang

if __name__ == "__main__":
    tambah_barang()