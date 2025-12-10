# products.py
def tambah_barang():
    print("-----INPUT BARANG-----")
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))


    keranjang = {
        "A001": {"nama": "Air Mineral", "harga": 5000},
        "A002": {"nama": "Roti Coklat", "harga": 6000},
        "A003": {"nama": "Mie Instan", "harga": 3500},
        "A004": {"nama": "Kopi Botol", "harga": 12000},
        "A005": {"nama": "Coklat Batang", "harga": 10000}
    }

    keranjang[kode] = {"nama": nama, "harga": harga}

    return keranjang


if __name__ == "__main__":
    data = tambah_barang()
