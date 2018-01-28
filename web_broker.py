import pika
import cron
import rabbitmq_broker as br_module

FILE_NAME = 'web_file.txt'
EXCHANGE_NAME = "web_exchange"
APPS_QUEUE = "apps_queue"
WEB_QUEUE = "web_queue"
FOLLOW_ME_MESSAGE = "Subscribe to get Message From Apps"

# Call RabbitBroker Class Module
rbw = br_module.RabbitBroker()
# Broker Exchange
rbw.broker_exchange(EXCHANGE_NAME)


# Send Message
def send_message_queue():
    rbw.broker_queue(WEB_QUEUE)
    rbw.bind_queue(exchange="web_exchange", queue="web_queue")
    cron.write_data(FILE_NAME, FOLLOW_ME_MESSAGE)
    rbw.send_message(EXCHANGE_NAME, WEB_QUEUE, message_body="Message from Web!")


# Receive Message
def receive_message_queue():
    rbw.broker_queue(APPS_QUEUE)
    message = rbw.message_consume(APPS_QUEUE)
    # print(message)
    return message


#
#
# if receive_from_queue != '':
#     cron.read_data(FILE_NAME)
# else:
#     print("No Instruction Found into Message")

# if receive_message_queue() == "b'Message from Web!'":
#     print("Well done!")
mes = receive_message_queue()
print(mes)

send_message_queue()
