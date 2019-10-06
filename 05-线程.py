#coding = utf-8
import time
import threading


def saySorry():
    print("亲爱的，我错了！！！")
    # time.sleep(5)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()