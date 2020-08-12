import pika
import sys

exchangeName = 'topic_logs'
routingKey = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create exchange
channel.exchange_declare(exchange=exchangeName, exchange_type='topic')
# publish message
channel.basic_publish(exchange=exchangeName,
                      routing_key=routingKey, body=message)

print(' [x] Sent {}:{}'.format(routingKey, message))

# close connection
connection.close()
