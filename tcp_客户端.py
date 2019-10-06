from socket import *


def main():
    # 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_DGRAM)
    # 链接服务器
    tcp_socket.connect(("192.168.1.7",7777))
    """
    server_ip = input("输入ip:")
    server_port = int(input("输入port:"))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    """
    # 发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("gbk"))
    recvData = tcp_socket.recv(1024)
    print("接收到的数据：",recvData.decode("gbk"))
    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()