from transaksi.subtotal import hitung_subtotal
from transaksi.diskon import hitung_diskon
from transaksi.total_bayar import hitung_total_bayar
from transaksi.kembalian import hitung_kembalian
from database.database import ambil_barang, update_stok_barang

def proses_transaksi():
    while True:
        nama_barang = str(input("Masukkan nama barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

        barang = ambil_barang(nama_barang)

        harga_barang = barang[0]
        stok_barang = barang[1]

        print("Harga Barang: "+ str(harga_barang) + " " + "Stok Barang: " + str(stok_barang))

        total_harga = hitung_subtotal(harga_barang, jumlah_barang)
        print("Total Harga: " + str(total_harga))

        if total_harga > 100000 :
            diskon = hitung_diskon(total_harga)

            print (f"Diskon : 10%")
            total_diskon = total_harga - diskon
            print(f"Diskon (Rp) : {diskon}")
            print(f"Harga Setelah Diskon : {total_diskon}")

            total_harga == total_diskon

        pembayaran = (int(input("Masukan Jumlah Pembayaran :")))

        if pembayaran > 100000 :
            kembalian = pembayaran - total_diskon
            print (f"kembalian : {kembalian}")
        
        else :
            kembalian = pembayaran - total_harga
            print(f"Kembalian : {kembalian}")
        
        

        update_stok_barang(jumlah_barang, nama_barang)
    


         
        break




if __name__ == "__main__":
    proses_transaksi()
