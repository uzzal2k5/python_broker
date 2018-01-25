import sys
import pika

connection = pika.BlokingConnection('172.17.0.5:5672')
channel = connection.channel()
message = ''.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2
                      ))
print(" [x] Sent %r" % message)


