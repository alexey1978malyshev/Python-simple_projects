from PyPDF2 import PdfWriter, PdfReader
import sys


def encrypt_file():
    file_path = input("[+] Enter file path:")
    password = input("[+] Enter password:")
    encrypted_file_name = input("[+] Enter a name for the encrypted file:")

    file_writer = PdfWriter()
    try:
        file_reader = PdfReader(file_path)
    except FileNotFoundError:
        print(f"[INFO] No file with path: {file_path}")
        sys.exit()

    for page in range(len(file_reader.pages)):
        file_writer.add_page(file_reader._get_page(page))
    
    file_writer.encrypt(password)

    with open(encrypted_file_name, "wb") as file: #'wb' flag for write in binary format
        file_writer.write(file)

    print(f"[+] Creted - {encrypted_file_name}")


def decrypt_file():
    file_path = input("[+] Enter file path:")
    password = input("[+] Enter password:")
    decrypted_file_name = input("[+] Enter a name for the decrypted file:")

    file_writer = PdfWriter()
    try:
        file_reader = PdfReader(file_path)
    except FileNotFoundError:
        print(f"[INFO] No file with path: {file_path}")
        sys.exit()

    if file_reader.is_encrypted:
        file_reader.decrypt(password)

    for page in range(len(file_reader.pages)):
        file_writer.add_page(file_reader._get_page(page))
    
    

    with open(decrypted_file_name, "wb") as file: #'wb' flag for write in binary format
        file_writer.write(file)

    print(f"[+] Creted - {decrypted_file_name}")

def main():
    choose = input("[+] Enter 0 for encrypt the file or 1 for to decript...")

    encrypt_file() if choose == "0" else decrypt_file()

if __name__ == main():
    main()