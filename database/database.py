import sqlite3
DB_NAME = "kasir.db"

def main():
    connection = sqlite3.connect("app.db")   

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (id integer primary key, nama_produk varchar(100), jumlah_produk integer, harga integer)")

    connection.commit()
    return connection

def simpan_transaksi_ke_keranjang(nama_produk, harga_satuan, jumlah_barang_yang_dibeli, subtotal, diskon):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO cart (nama_produk, harga_satuan, jumlah_barang_yang_dibeli, subtotal, diskon) VALUES (?, ?, ?, ?, ?)", (nama_produk, harga_satuan, jumlah_barang_yang_dibeli, subtotal, diskon))
    conn.commit()

def ambil_transaksi_dari_keranjang(id_keranjang):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nama_produk, harga_satuan, jumlah_barang_yang_dibeli, subtotal, diskon FROM cart WHERE id = ?", (id_keranjang,))
    data = cursor.fetchone()
    conn.close()

    return data

def simpan_barang(connection, nama, harga, stock):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO products (nama_produk, jumlah_produk, harga)
        VALUES ( ?, ?, ?)
    """, (nama, stock, harga))
    connection.commit()

def update_stok_barang(jumlah_barang, nama_barang):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE products SET jumlah_produk = jumlah_produk - ? WHERE nama_produk = ?", (jumlah_barang, nama_barang))

    conn.commit()

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

def search_barang(connection, nama_produk):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM products
        WHERE nama_produk LIKE ?
    """, ('%' + nama_produk + '%',))
    
    data = cursor.fetchall()
    return data

def get_connection():
    return sqlite3.connect("app.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_produk TEXT,
            jumlah_produk INTEGER,
            harga INTEGER
        )
    """)
    conn.commit()
    conn.close()


def ambil_barang(nama_barang):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT harga, jumlah_produk FROM products WHERE nama_produk = ?",
        (nama_barang,)
    )
    data = cursor.fetchone()
    conn.close()
    return data
    
if __name__ == "__main__":
    main()