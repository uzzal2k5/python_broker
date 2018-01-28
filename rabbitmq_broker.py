import pika
import sys
import time

VHOST_NMAE = '/'
RABBIT_SERVER = "172.17.0.4"
EXCHANGE_NAME = "test_exchange"
QUEUE_NAME = "test_queue"
USERNAME = "uzzal"
PASSWORD = "pass1234"
STOP_PROCESSING_MESSAGE = "QRT"


# FOLLOW_ME_MESSAGE = "Follow @uzzal2k5 on Twitter!"
class RabbitBroker:
    # Rabbit Connection
    def rabbit_conection(self):
        credentials = pika.PlainCredentials(USERNAME, PASSWORD)
        conn_params = pika.ConnectionParameters(host=RABBIT_SERVER,
                                                virtual_host=VHOST_NMAE,
                                                credentials=credentials)
        connection = pika.BlockingConnection(conn_params)
        self.channel = connection.channel()

    # Exchange Declaration
    def broker_exchange(self, exchange):
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type="fanout",
                                      passive=False,
                                      durable=False,
                                      auto_delete=False
                                      )

    # Queue Declaration
    def broker_queue(self, queue):
        self.channel.queue_declare(queue=queue,
                                   durable=True,
                                   auto_delete=False
                                   )

    # Binding Queue with Exchange
    def bind_queue(self, exchange, queue):
        self.channel.queue_bind(exchange=exchange,
                                queue=queue
                                )

    # Init Function to initialize
    def __init__(self):
        print("My Sample Rabbit Broker with Python ")
        self.rabbit_conection()

    # Sending Message
    def send_message(self, exchange, queue, message_body):
        message = message_body
        message_properties = pika.BasicProperties(delivery_mode=2,
                                                  content_type="text/plain"
                                                  )
        self.channel.basic_publish(body=message,
                                   exchange=exchange,
                                   properties=message_properties,
                                   routing_key=queue
                                   )
        print("Message Sent: ", message)

    def message_consume(self, queue):
        for method_frame, properties, body in self.channel.consume(queue=queue):
            #time.sleep(body.count(b'.'))
            self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            return body





    # Display Message
    def view(self):
        print("Message Viewer Mode")
        self.broker_queue()
        channel = self.channel
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.message_consume())

        channel.start_consuming()


# rb = RabbitBroker()
# rb.rabbit_conection()
# rb.send_message(FOLLOW_ME_MESSAGE)
# rb.message_consume()
# rb.view()
