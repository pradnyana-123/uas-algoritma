from datetime import datetime

keranjang = [
    ("Susu", 10000, 2, 20000),
    ("Roti", 10000, 1, 10000)
]

total = sum(item[3] for item in keranjang)
bayar = 50000
kembali = bayar - total

tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

with open("struk.txt", "w") as f:
    f.write("TOKO MAJU JAYA\n")
    f.write("Jl. Merdeka No. 12\n")
    f.write("----------------------------\n")
    f.write(f"Tanggal : {tanggal}\n")
    f.write("Kasir   : Admin\n")
    f.write("----------------------------\n")

    for nama, harga, qty, subtotal in keranjang:
        f.write(f"{nama:10} {qty} x {harga} = {subtotal}\n")

    f.write("----------------------------\n")
    f.write(f"TOTAL    : {total}\n")
    f.write(f"BAYAR    : {bayar}\n")
    f.write(f"KEMBALI  : {kembali}\n")
    f.write("----------------------------\n")
    f.write("Terima kasih telah berbelanja\n")
