import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5558")

while True:
    response = socket.recv()
    print("response: %s" % response.decode('utf-8'))
