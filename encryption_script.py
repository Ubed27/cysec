from cryptography.fernet import Fernet

def generate_key():
    """Menghasilkan kunci enkripsi baru dan menyimpannya ke file."""
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Kunci enkripsi berhasil dibuat dan disimpan di 'encryption_key.key'.")

def load_key():
    """Memuat kunci enkripsi dari file."""
    try:
        with open("encryption_key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Kunci enkripsi tidak ditemukan. Silakan buat kunci terlebih dahulu.")
        return None

def encrypt_message(message, key):
    """Mengenkripsi pesan menggunakan kunci."""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """Mendekripsi pesan menggunakan kunci."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    print("Pilih opsi:")
    print("1. Buat kunci enkripsi baru")
    print("2. Enkripsi pesan")
    print("3. Dekripsi pesan")
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        key = load_key()
        if key:
            message = input("Masukkan pesan yang akan dienkripsi: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Pesan terenkripsi: {encrypted_message.decode()}")
    elif choice == "3":
        key = load_key()
        if key:
            encrypted_message = input("Masukkan pesan terenkripsi: ").encode()
            try:
                decrypted_message = decrypt_message(encrypted_message, key)
                print(f"Pesan asli: {decrypted_message}")
            except Exception as e:
                print(f"Gagal mendekripsi pesan: {e}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
