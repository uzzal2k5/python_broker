import pika
import cron
import rabbitmq_broker as br_module

FILE_NAME = 'test.txt'
EXCHANGE_NAME = "apps_exchange"
APPS_QUEUE = "apps_queue"
WEB_QUEUE = "web_queue"
FOLLOW_ME_MESSAGE = "Follow @uzzal2k5 on Apps!"

rb = br_module.RabbitBroker()

# Broker Exchange
rb.broker_exchange(EXCHANGE_NAME)


# Send Message
def send_message_queue():
    rb.broker_queue(APPS_QUEUE)
    rb.bind_queue(exchange="apps_exchange", queue="apps_queue")
    cron.write_data(FILE_NAME, FOLLOW_ME_MESSAGE)
    rb.send_message(EXCHANGE_NAME, APPS_QUEUE, message_body="Message from Apps!")


# # Receive Message
def receive_message_queue():
    rb.broker_queue(WEB_QUEUE)
    message = rb.message_consume(WEB_QUEUE)
    #print(message)
    return message

# if receive_from_queue() != '':
#     cron.read_data(FILE_NAME)
# else:
#     print("No Instruction Found into Message")
send_message_queue()
receive_message_queue()
