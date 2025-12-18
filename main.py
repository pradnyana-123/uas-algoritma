import sys
from login import auth
import products
def TampilanMenu ():
    print("==================================================")
    print("================= SISTEM KASIR ===================")
    print("==================================================")
    print("     1. Input Data Barang ")
    print("     2. Transaksi ")
    print("     3. Cetak Struk ")
    print("     4. Keluar ")
 
def main():
    if not auth.login_admin():
        sys.exit()
    while True:
        TampilanMenu ()
        pilihan = input ("Masuk Menu yang Ingin di Akses : ")

        match pilihan:
            case "1":
                print ("Fitur Input Barang")
                products.tambah_barang()
            case "2" :
                print ("Fitur Transaksi")
            case "3" :
                print ("Fitur Cetak Struk")
            case "4" :
                print ("Keluar Dari Sistem")
                sys.exit()
            case _: 
                print ("Pilihan Invalid")
                
if __name__ == "__main__":
    main()
