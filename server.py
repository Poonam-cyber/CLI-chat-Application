import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()


def EncryptMessage(data):
    binary_data= ''.join(format(ord(i), 'b') for i in data) 
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(binary_data)
    return encrypted
def DecryptMessage():
    encrypted_data = data
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted_data)
    return decrypted
    
def server_program():
    host = '127.0.0.1'
    port = 6000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    conn, address = server_socket.accept()
    print("Connection From: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        new_data = DecryptMessage(data)
        if not data:
            break
        print("demo" + data)
        print("From Connected User: " + new_data)
        data = input('->')
        EncryptedData = EncryptMessage(data)
        conn.send(EncryptedData.encode())
    conn.close()

if __name__ == '__main__':
    server_program()