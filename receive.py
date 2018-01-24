import  pika
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

connection = pika.BlokingConnection('192.168.122.1')
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, propertise, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()