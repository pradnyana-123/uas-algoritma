from database.database import cek_barang,main, simpan_barang, update_barang, delete_barang, search_barang

def tambah_barang():
    connection = main()

    while True:
        print("\n----- MENU KERANJANG -----")
        print("1. Tambah")
        print("2. Update")
        print("3. Hapus Barang")
        print("4. Lihat Barang")
        print("5. Search")
        print("6. Selesai")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            print("\n--- INPUT BARANG ---")
            nama = input("Masukkan nama barang  : ")
            harga = int(input("Masukkan harga barang : "))
            stock = int(input("Masukkan stock        : "))

            simpan_barang(connection, nama, harga, stock)
            print(f"Barang {nama} berhasil disimpan ke database.")

        elif pilihan == '2':
            print("\n--- UPDATE BARANG ---")
            id = int(input("Masuk Id Barang Yang Ingin di Update : "))
            harga = int(input("Masuk Harga Barang : "))
            stock = int(input("Masukkan stock     : "))
            update_barang(connection, id, harga, stock)
            print("Barang berhasil diupdate.")

        elif pilihan == '3':
            print("\n--- HAPUS BARANG ---")
            id = int(input("Masukkan id barang yang ingin dihapus: "))
            delete_barang(connection, id)
            print("Barang berhasil dihapus.")

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
            print("\n--- SEARCH BARANG ---")
            nama = input("Masukan item yang akan dicari: ")
            hasil_search = search_barang(connection, nama)

            if not hasil_search:
                print("Barang tidak ditemukan.")
            else:
                print("ID | Nama | Stock | Harga")
                print("-" * 40)
                for item in hasil_search:
                    print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif pilihan == '6':
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


    return connection

if __name__ == "__main__":
    tambah_barang()