"""_summary_
"""
import logging
import pika
from pika.exceptions import AMQPError
from src.settings import QUEUE


class QueueRabbitmq():
    """_summary_
    """

    def __init__(self, queue_name: str):
        """_summary_
        """
        self.__connection = None
        self.__channel = None
        self.__queue_name = queue_name

    def __create_connection(self):
        """_summary_
        """
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=QUEUE["QUEUE_HOST"],
                port=QUEUE["QUEUE_PORT"]
            ))
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue=self.__queue_name)

    def send_message(self, message: str):
        """_summary_
        """
        try:
            self.__create_connection()
            self.__channel.basic_publish(
                exchange='', routing_key=self.__queue_name, body=message)
            self.__connection.close()
        except AMQPError as ex:
            logging.error(ex.args)

    def receive_message(self):
        """_summary_
        """
        self.__create_connection()
        method_frame, header_frame, body = self.__channel.basic_get(
            self.__queue_name
        )

        if method_frame:
            self.__channel.basic_ack(method_frame.delivery_tag)

        self.__connection.close()
        return method_frame, body

    def queue_purge(self):
        """_summary_
        """
        self.__create_connection()
        self.__channel.queue_purge(self.__queue_name)
