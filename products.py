# products.py
def tambah_barang():
    keranjang = {
       "M001": {"nama": "Nasi Goreng", "harga": 15000},
        "M002": {"nama": "Mie Ayam", "harga": 12000},
        "M003": {"nama": "Bakso", "harga": 13000},
        "M004": {"nama": "Sate Ayam", "harga": 20000},
        "M005": {"nama": "Gado-gado", "harga": 10000},
        "M006": {"nama": "Ayam Penyet", "harga": 18000},
        "M007": {"nama": "Rendang", "harga": 25000}
    }
    while True:
        print("-----INPUT BARANG-----")
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))

        keranjang[kode] = {"nama": nama, "harga": harga}
        lanjut = input("tambah barang lagi? (y/n): ")
        if lanjut != 'y':
            break
    return keranjang

if __name__ == "__main__":
    tambah_barang()