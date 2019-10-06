#coding=utf-8
import socket
import os


def send_msg(udp_socket):
    """发送信息"""
    # 获取发送的内容
    # dest_ip = input("请输入对方的ip：")
    dest_ip = str('192.168.1.10')
    # dest_port = int(input("请输入对方的port："))
    dest_port = int(8000)
    send_data = input("请输入要发送的信息：")
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gdk'))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("",8080))

    # 循环进行处理事件
    while True:
        # 发送
        send_msg(udp_socket)

        # 接收并显示
        recv_msg(udp_socket)

if __name__ == "__main__":
    main()