import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe(
   'persistent://public/default/mytopic',
   'my-subscription',
   consumer_type= pulsar.ConsumerType.Exclusive,
   initial_position= pulsar.InitialPosition.Latest,
   message_listener= None,
   negative_ack_redelivery_delay_ms= 60000 
)

while True:
    msg = consumer.receive()
    try:
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except Exception:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()