from cryptography.fernet import Fernet

generate_key = Fernet.generate_key()
key = Fernet(generate_key)

msg = input("Enter Message: ")
print(f"Original Message: {msg}")
print("\n")

print("Start Encryption")
en_msg = key.encrypt(msg.encode())
print(f"Encrypted Message: {en_msg}")
print("\n")

print("Start Decryption")
de_msg = key.decrypt(en_msg.decode())
print(f"Decrypted Message: {de_msg}")
