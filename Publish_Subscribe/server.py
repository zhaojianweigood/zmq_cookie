import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    print('发送消息')
    socket.send("消息群发".encode())
    time.sleep(1)
