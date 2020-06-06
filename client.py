import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()


def DecryptMessage(data):
    encrypted_data = data
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted_data)
    return decrypted
    
def EncryptMessage(message):
    binary_data= ''.join(format(ord(i), 'b') for i in message) 
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(binary_data)
    return encrypted

def client_program():
    host = '127.0.0.1'
    port = 6000
    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("->")
    while message.lower().strip() != 'bye':
        EncryptedData = EncryptMessage(message)
        client_socket.send(EncryptedData)
        data = client_socket.recv(1024).decode()
        new_data = DecryptMessage(data)
        print("Received From Server: " + new_data.decode())
        message = input("->")
    client_socket.close()

if __name__ == '__main__':
    client_program()