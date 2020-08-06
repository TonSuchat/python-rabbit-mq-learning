import sys
import pika

queueName = 'hello'

message = ' '.join(sys.argv[1:]) or 'Hello World'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue
channel.queue_declare(queue=queueName, durable=True)
# send message to queue
channel.basic_publish(exchange='',
                      routing_key=queueName,
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2  # make message persistent
                                                      ))

print(' [x] Sent {}'.format(message))

# close connection
connection.close()
