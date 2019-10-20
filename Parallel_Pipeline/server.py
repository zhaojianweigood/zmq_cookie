import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5557")

while True:
    socket.send("测试消息".encode())
    print('已发送')
    time.sleep(1)
