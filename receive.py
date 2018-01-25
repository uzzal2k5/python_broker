import pika

# import rabbit_connection as rc

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               credentials=pika.PlainCredentials('uzzal', 'pass1234'))
                                     )
channel = connection.channel()
channel.queue_declare(queue='shuni_tel_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

for method_frame, properties, body in channel.consume('shuni_tel_queue'):
    print(method_frame, properties, body)
    channel.basic_ack(method_frame.delivery_tag)
    if method_frame.delivery_tag == 10:
        break
requeued_messages = channel.cancel()
print('Requeued %i message' % requeued_messages)

# def callback(ch, method, header, body):
#     print(" [x] Received %r" % (body,))
#
#
# channel.basic_consume(callback,
#                          queue='shuni_tel_queue',
#                          no_ack=True)
# print(' [*] Waiting for message. To exit press CTRL+C')
connection.close()
