import pika
import rabbitmq_broker as br_module
import logging
logging.basicConfig()

NOTIFY_QUEUE = 'notification_queue'
NOTIFY_EXCHANGE = 'notification_exchange'
NOTIFY_MESSAGE = 'Notification From Notification Queue! UZZAL'


SUBSCRIBE_QUEUE = 'subscription_queue'
SUBSCRIBE_EXCHANGE = 'subscription_exchange'
SUBSCRIBE_MESSAGE = 'Subscription Message from Subscription Queue!uuuuuu'

br = br_module.RabbitBroker()


def send_notification():
    br.broker_exchange(NOTIFY_EXCHANGE)
    br.broker_queue(NOTIFY_QUEUE)
    br.bind_queue(exchange="notification_exchange", queue="notification_queue")
    br.send_message(NOTIFY_EXCHANGE, NOTIFY_QUEUE, message_body=NOTIFY_MESSAGE)
    # Close Rabbit Connection
    #br.connection.close()


def send_subscription():
    br.broker_exchange(SUBSCRIBE_EXCHANGE)
    br.broker_queue(SUBSCRIBE_QUEUE)
    br.bind_queue(exchange="subscription_exchange", queue="subscription_queue")
    br.send_message(SUBSCRIBE_EXCHANGE, SUBSCRIBE_QUEUE, message_body=SUBSCRIBE_MESSAGE)
    # Close Rabbit Connection
    #br.connection.close()


# Send Notification from APP
send_notification()

# Send Subscription Request From Web
#send_subscription()
