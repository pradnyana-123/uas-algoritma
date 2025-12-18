from database.database import cek_barang,main, simpan_barang, update_barang, delete_barang

def tambah_barang():
    connection = main()
    while True:
        print("\n----- MENU KERANJANG -----")
        print("1. Tambah")
        print("2. Update")
        print("3. Hapus Barang")
        print("4. Lihat Barang")
        print("5. Selesai")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            print("\n--- INPUT BARANG ---")
            nama = input("Masukkan nama barang  : ")
            harga = int(input("Masukkan harga barang : "))
            stock = int(input("Masukkan stock        : "))

            simpan_barang(connection, nama, harga, stock)
            print(f"Barang {nama} berhasil disimpan ke database.")

            data = cek_barang(connection)
            print("DEBUG isi database:", data)

        elif pilihan == '2':
            print("\n--- UPDATE BARANG ---")
            id = int(input("Masuk Id Barang Yang Ingin di Update : "))
            harga = int(input("Masuk Harga Barang : "))
            stock = int(input("Masukkan stock        : "))
            update_barang(connection, id, harga, stock)
            print(f"Harga, Stock barang berhasil diupdate ke database, Harga: {harga}, Stock: {stock}")

        elif pilihan == '3':
            print("\n--- HAPUS BARANG ---")
            id = input("Masukkan id barang yang ingin dihapus: ")
            delete_barang(connection, id)

        elif pilihan == '4':
            data = cek_barang(connection)

            print("\n--- DAFTAR BARANG ---")
            print("ID | Nama | Stock | Harga")
            print("-" * 40)
            if not data:
                print("Belum ada data barang.")
            else:
                 for item in data:
                    print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")
    
        elif pilihan == '5':
            break
        
        else:
            print("Pilihan tidak valid!")

    return connection

if __name__ == "__main__":
    tambah_barang()