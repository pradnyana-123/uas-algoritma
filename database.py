import sqlite3

def main():
    connection = sqlite3.connect("app.db")   

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (id integer primary key, nama_produk varchar(100), jumlah_produk integer, harga integer)")

    return connection 

if __name__ == "__main__":
    main()