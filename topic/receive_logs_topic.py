import pika
import sys

exchangeName = 'topic_logs'
bindingKeys = sys.argv[1:]

if not bindingKeys:
    sys.stderr.write(
        "Usage: {} [binding_key]...\n".format(sys.argv[0]))
    sys.exit(1)


def callback(ch, method, properties, body):
    print(' [x] {}:{}'.format(method.routing_key, body))


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create exchange
channel.exchange_declare(exchange=exchangeName, exchange_type='topic')
# create queue
result = channel.queue_declare(queue='', exclusive=True)
# get queue name
queueName = result.method.queue
# bind queue with routing key
print(bindingKeys)
for bindingKey in bindingKeys:
    channel.queue_bind(exchange=exchangeName,
                       queue=queueName, routing_key=bindingKey)
# binding with callback
channel.basic_consume(
    queue=queueName, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.start_consuming()
