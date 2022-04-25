
from src.service.queue.rabbitmq.queue_rabbitmq import QueueRabbitmq


class Queue():

    def __init__(self, queue_name):
        self.__queue = QueueRabbitmq(queue_name)

    def send_message(self, message):
        self.__queue.send_message( message)

    def receive_message(self):
        return self.__queue.receive_message()

    def queue_purge(self):
        return self.__queue.queue_purge()
        