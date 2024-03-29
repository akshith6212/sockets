import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(">>> ")  # take input

    while message.lower().strip() != 'bye':	#for ending the conversation!
        client_socket.send(message.encode())  # sends the message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(">>> ")  # again take input

    client_socket.close()  # close the connection


client_program()
