import pika
import time

# import rabbit_connection as rc

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.1',
                                                               credentials=pika.PlainCredentials('uzzal', 'pass1234'))
                                     )
channel = connection.channel()

#generate_consumer_tag(name = "my_apps")
channel.queue_declare(queue='my_queue', durable=True)

for method_frame, properties, body in channel.consume('my_queue'):
    print(method_frame, properties, body)
    print(time.sleep(body.count(b'.')))
    channel.basic_ack(method_frame.delivery_tag)
    if method_frame.delivery_tag == 10:
        break

requeued_messages = channel.cancel()
print('Requeued %i message' % requeued_messages)

# channel.basic_consume(exchange='my_exchange',
#                           queue='my_queue',
#                           no_ack=True)


channel.start_consuming()
connection.close()
