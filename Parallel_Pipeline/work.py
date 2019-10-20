import zmq

context = zmq.Context()

recive = context.socket(zmq.PULL)
recive.connect('tcp://127.0.0.1:5557')

sender_1 = context.socket(zmq.PUSH)
sender_1.connect('tcp://127.0.0.1:5558')
sender_2 = context.socket(zmq.PUSH)
sender_2.connect('tcp://127.0.0.1:5559')
while True:
    data = recive.recv()
    print("正在转发...")
    sender_1.send(data)
    sender_2.send(data)
