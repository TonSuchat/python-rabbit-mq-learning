import pika
import sys

exchangeName = 'direct_logs'
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create exchange
channel.exchange_declare(exchange=exchangeName, exchange_type='direct')
# publish message
channel.basic_publish(exchange=exchangeName,
                      routing_key=severity, body=message)

print(' [x] Sent {}:{}'.format(severity, message))

# close connection
connection.close()
