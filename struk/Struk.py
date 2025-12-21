from datetime import datetime
from database.operations import ambil_transaksi_dari_keranjang

def cetak_struk():
    id_keranjang = int(input("Masukkan id keranjang: "))
    keranjang = ambil_transaksi_dari_keranjang(id_keranjang) 

    total = sum(item[3] for item in keranjang)
    bayar = keranjang[0][4] 
    kembali = bayar - total

    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

    with open("struk.txt", "w") as f:
        f.write("TOKO MAJU JAYA\n")
        f.write("Jl. Merdeka No. 12\n")
        f.write("----------------------------\n")
        f.write(f"Tanggal : {tanggal}\n")
        f.write("Kasir   : Admin\n")
        f.write("----------------------------\n")

        for nama, harga, qty, subtotal, _, diskon in keranjang:
            f.write(f"{nama:10} {qty} x {harga} = {subtotal}\n")

        f.write("----------------------------\n")
        f.write(f"TOTAL    : {subtotal}\n")
        f.write(f"BAYAR    : {bayar}\n")
        f.write(f"KEMBALI  : {kembali}\n")
        f.write(f"DISKON   : {diskon}\n")
        f.write("----------------------------\n")
        f.write("Terima kasih telah berbelanja\n")