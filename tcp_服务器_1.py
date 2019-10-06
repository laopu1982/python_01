import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    tcp_server_socket.bind(("",8888))
    tcp_server_socket.listen(128)
    print("_____1____")
    new_client_socket,client_addr = tcp_server_socket.accept()
    print("_____2____")
    print(client_addr)
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    new_client_socket.send("ok".encode("gbk"))
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()