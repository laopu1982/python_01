#coding=utf-8
import  socket,os


server = socket.socket()
server.bind(("192.168.1.10",8080))
server.listen(5)
while True:
    conn,addr = server.accept()
    print("new addr:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read()
        print("before send:",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output...."
        conn.send(str(len(cmd_res.encode())).encode())
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
    server.close()


