
ADMIN = {
    "username": "admin",
    "password": "admin123"
}

def login_admin():
    percobaan = 3

    while percobaan > 0:
        print("\n=== LOGIN ADMIN ===")
        username = input("Username : ")
        password = input("Password : ")

        if username == ADMIN["username"] and password == ADMIN["password"]:
            print("Login berhasil. Selamat datang Admin!\n")
            return True
        else:
            percobaan -= 1
            print(f"Login gagal. Sisa percobaan: {percobaan}")

    print("Akses ditolak. Terlalu banyak percobaan.")
    return False
