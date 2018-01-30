import cron
import rabbitmq_broker as br_module
import tornado.ioloop
import tornado.web
import tornado.websocket
from threading import Thread
import logging

logging.basicConfig(level=logging.INFO)

QUEUE_NAME = 'subscription_queue'
EXCHANGE_NAME = 'subscription_exchange'
NOTIFICATION = 'subscribe me'

FILE_NAME = 'test.txt'

rb = br_module.RabbitBroker()

# Broker Exchange
rb.broker_exchange(EXCHANGE_NAME)


# Send Message
def send_message_queue():
    rb.broker_queue(QUEUE_NAME)
    rb.bind_queue(exchange="subscription_exchange", queue="subscription_queue")
    cron.write_data(FILE_NAME, NOTIFICATION)
    rb.send_message(EXCHANGE_NAME, QUEUE_NAME, message_body="Message from Apps!")


# # Receive Message
def receive_message_queue():
    rb.broker_queue(QUEUE_NAME)
    message = rb.message_consume(QUEUE_NAME)
    # print(message)
    return message


logging.basicConfig(level=logging.INFO)

# web Socket Clients Connected
clients = []


class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        logging.info('WebSocket opened')
        clients.append(self)

    def on_close(self):
        logging.info('WebSocket closed')
        clients.remove(self)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


application = tornado.web.Application([
    (r'/ws', SocketHandler),
    (r"/", MainHandler),
])


def start_tornado():
    application.listen(25672)
    tornado.ioloop.IOLoop.instance().start()


def stop_tornado():
    tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    logging.info('Starting thread RabbitMQ')
    threadRMQ = Thread(target=receive_message_queue)
    threadRMQ.start()
    logging.info('Starting thread Tornado')
    threadTornado = Thread(target=start_tornado)
    threadTornado.start()

    try:
        input("Server ready. Press enter to stop\n")
        # raw_input("Server ready. Press enter to stop\n")
    except SyntaxError:
        pass
    try:
        logging.info('Disconnecting from RabbitMQ..')
        rb.disconnect_to_rabbitmq()
    except Exception as e:
        pass

    stop_tornado();

    logging.info('See you...')
receive_message_queue()
# send_message_queue
