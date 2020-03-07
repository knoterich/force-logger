import queue
from threading import Thread, Lock

en_log = False
en_blink = False

STATUS_NEW = 0
STATUS_TAR = 1
STATUS_READY = 2

list_scale_id = [False, False, False, False, False, False]
list_client_ip = ["NC", "NC", "NC", "NC", "NC", "NC"]
list_cell_units = ["", "", "", "", "", ""]
list_scale_mom = ["", "", "", "", "", ""]
list_scale_status = [STATUS_NEW, STATUS_NEW, STATUS_NEW, STATUS_NEW, STATUS_NEW, STATUS_NEW]
list_mes_file = ["", "", "", "", "", ""]
list_blk_file = ["", "", "", "", "", ""]

port_server = 4242
rec_dir = "./rec/"

queues_recv = []
for i in range(6):
    queues_recv.append(queue.Queue())

queues_send = []
for i in range(6):
    queues_send.append(queue.Queue())

queues_ack = []
for i in range(6):
    queues_ack.append(queue.Queue())

queues_mes = []
for i in range(6):
    queues_mes.append(queue.LifoQueue())
