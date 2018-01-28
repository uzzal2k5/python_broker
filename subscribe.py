import rabbitmq_broker as br_module
QUEUE_NAME = 'subscription_queue'
EXCHANGE_NAME = 'subscription_exchange'
SUBSCRIBE_ME_MESSAGE = 'subscribe me'

br = br_module.RabbitBroker()
br.broker_exchange(EXCHANGE_NAME)


def send_message_queue():
    br.broker_queue(QUEUE_NAME)
    br.bind_queue(exchange="subscription_exchange", queue="subscription_queue")
    br.send_message(EXCHANGE_NAME, QUEUE_NAME, message_body=SUBSCRIBE_ME_MESSAGE)

send_message_queue()

