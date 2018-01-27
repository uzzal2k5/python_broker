import pika
#http://www.codeghar.com/blog/install-latest-python-on-centos-7.html
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html


my_message= "My Message to subscriber "

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.1',
                                                               credentials=pika.PlainCredentials('uzzal', 'pass1234')
                                                               )
                                     )
channel = connection.channel()

channel.queue_declare(queue='my_queue', durable=True)
channel.exchange_declare(exchange='my_exchange', exchange_type='fanout')
channel.queue_bind(exchange='my_exchange',
                   queue='my_queue')

channel.basic_publish(exchange='my_exchange',
                      routing_key='my_queue',
                      body=my_message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make the message persistent
                      ))
print("[x] Sent %r" % my_message )
connection.close()
