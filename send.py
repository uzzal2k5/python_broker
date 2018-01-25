import pika

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               credentials=pika.PlainCredentials('uzzal', 'pass1234')
                                                               )
                                     )
channel = connection.channel()
channel.queue_declare(queue='shuni_tel_queue', durable=True)

channel.basic_publish(exchange='shuni_tel_ex',
                      routing_key='shuni_tel_queue',
                      body='Hello Shuni Tel World!')
print("[x] Sent 'Hello Shuni Tel World!'")
connection.close()
