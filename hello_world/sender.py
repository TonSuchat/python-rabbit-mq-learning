import pika

queueName = 'hello'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue
channel.queue_declare(queue=queueName)
# send message to queue
channel.basic_publish(exchange='', routing_key=queueName,
                      body='Hello World! from Python')

print(' [x] Sent Hello World! message')

# close connection
connection.close()
