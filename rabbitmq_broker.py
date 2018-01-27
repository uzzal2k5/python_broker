import pika
import  sys

RABBIT_SERVER = "172.17.0.4"
EXCHANGE_NAME = "my_exchange"
VHOST_NMAE = '/'
QUEUE_NAME = "my_queue"
USERNAME = "uzzal"
PASSWORD = "pass1234"
STOP_PROCESSING_MESSAGE = "QRT"
FOLLOW_ME_MESSAGE = "Follow @uzzal2k5 on Twitter!"


class rabbit_broker:
    def rabbit_conection(self):
        credentials = pika.PlainCredentials(USERNAME, PASSWORD)
        conn_params = pika.ConnectionParameters(host=RABBIT_SERVER,
                                                virtual_host=VHOST_NMAE,
                                                credentials=credentials)
        connection = pika.BlockingConnection(conn_params)
        self.channel = connection.channel()

    def broker_exchange(self):
        self.channel.exchange_declare(exchange=EXCHANGE_NAME,
                                      exchange_type="fanout",
                                      passive=False,
                                      durable=False,
                                      auto_delete=False
                                      )

    def broker_queue(self):
        self.channel.queue_declare(queue='my_queue',
                                   durable=False,
                                   auto_delete=False
                                   )

    def __init__(self):
        print("My Sample Rabbit Broker with Python ")
        self.rabbit_conection()
        self.broker_exchange()
        self.broker_queue()

    def sendMessage(self, message):
        my_message = message
        message_propertise = pika.BasicProperties(delivery_mode=2,
                                                  content_type="text/plain"
                                                  )
        self.channel.basic_publish(body=my_message,
                                   exchange=EXCHANGE_NAME,
                                   properties=message_propertise,
                                   routing_key='my_queue'
                                   )
        print("Message Sent: ", my_message)

    def message_consume(channel, method_frame, properties, body):
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        print(channel, method_frame, properties, body)
        if body == STOP_PROCESSING_MESSAGE:
            channel.basic_cancel(consumer_tag="MY_APPS")
            channel.stop_consuming()

    def view(self):
        print("Message Viewer Mode")
        self.broker_queue()
        chan = self.channel
        chan.queue_bind(exchange=EXCHANGE_NAME,
                        queue=QUEUE_NAME
                        )
        chan.basic_qos(prefetch_count=1)
        chan.basic_consume(self.message_consume())

        chan.start_consuming()


def main():
    if len(sys.argv[1])>1:
        if sys.argv[1] == "send":
            rb = rabbit_broker()
            rb.sendMessage("Hello")
            rb.sendMessage(FOLLOW_ME_MESSAGE)
            rb.sendMessage(STOP_PROCESSING_MESSAGE)
        else:
            brViewer = rabbit_broker()
            brViewer.view()


main()
