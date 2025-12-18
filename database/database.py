import sqlite3

def main():
    connection = sqlite3.connect("app.db")   

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (id integer primary key, nama_produk varchar(100), jumlah_produk integer, harga integer)")

    connection.commit()
    return connection 

def simpan_barang(connection, nama, harga, stock):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO products (nama_produk, jumlah_produk, harga)
        VALUES ( ?, ?, ?)
    """, (nama, stock, harga))
    connection.commit()

def update_barang(connection, id, harga, stock):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE products
        SET harga = ?, jumlah_produk = ?
        WHERE id = ?
    """, (harga, stock, id))
    connection.commit()

def delete_barang(connection, id):
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM products
        WHERE id = ?
    """,(id,))
    connection.commit()

def cek_barang(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return data
    
if __name__ == "__main__":
    main()