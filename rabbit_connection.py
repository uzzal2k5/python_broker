import pika
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

connection = pika.BlokingConnection('192.168.122.1')
channel = connection.channel()