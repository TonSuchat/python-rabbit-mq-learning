import pika
import sys

exchangeName = "logs"
message = ' '.join(sys.argv[1:]) or 'info: Hello World!'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create exchange
channel.exchange_declare(exchange=exchangeName, exchange_type="fanout")
# publish message
channel.basic_publish(exchange=exchangeName, routing_key='', body=message)

print(' [x] Sent {}'.format(message))

# close connection
connection.close()
