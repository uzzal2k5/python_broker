import pika

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
def rabbit_connection():
    connection = pika.BlokingConnection('172.17.0.5:5672')
    channel = connection.channel()
