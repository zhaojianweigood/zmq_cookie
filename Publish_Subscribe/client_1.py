import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, "".encode())
while True:
    response = socket.recv()
    print("response: %s" % response.decode('utf-8'))
