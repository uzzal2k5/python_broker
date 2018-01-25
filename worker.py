import pika
import time

# import rabbitmq_connection as rc
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
connection = pika.BlokingConnection('localhost')
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, propertise, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
