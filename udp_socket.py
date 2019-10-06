#coding=utf-8

import socket

def main():
    #  创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #  绑定本地的相关信息，如果一个网络程序不绑定，测系统会随机分配
    local_addr = ("127.0.0.1",8000)  #  IP地址和端口号，ip一般不写，表示本机的任何一个ip
    udp_socket.bind(local_addr)

    #  等待接收对方发送的数据
    recv_data = udp_socket.recvfrom(1024)  # 表示接收最大字节

    #  recv_data这个变量中存储的是一个元组（接收到的数据，（发送方的ip，端口号））
    recv_msg = recv_data[0] # 存储接收数据
    send_addr = recv_data[1]  #  存储发送方的ip 及端口

    #  显示接收到的数据
    #print(recv_data)
    # print(recv_data[0].decode('gbk'))

    while True:
        #  从键盘获取数据
        send_data = input("请输入要发送的数据：")
        #  如果输入的数据是exit，那么久退出程序：
        if send_data == "exit":
            break
        #  ...这里是使用套接字的功能。。。
        #  udp_socket.sendto(b"hahahah---",("192.168.1.10",8000))
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8000))
        #  不用的时候，关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()