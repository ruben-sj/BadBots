import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))

print("\n = = = WELCOME TO CHATROOM = = = ")

try:
    while True:
        userInput=input('\nYou: ')
        client_socket.send(userInput.encode('utf-8'))
        data=client_socket.recv(1024)
        if userInput != 'exit':
            print("%s"%data.decode('utf-8'))
        else:
            break
except KeyboardInterrupt:
    print("Exited by use")
client_socket.close()