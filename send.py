#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=6666))
channel = connection.channel()

channel.queue_declare(queue='github')

channel.basic_publish(exchange='', routing_key='github', body='Hello World!')
print(" [x] Sent 'Hello World!'")

a, b, body = channel.basic_get(queue='github')

print(" [x] Received %r" % body)

connection.close()