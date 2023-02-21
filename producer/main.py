'''
bin/pulsar-admin topics list public/default
docker exec -it pulsar /pulsar/bin/pulsar-client consume persistent://public/default/mytopic --num-messages 0 --subscription-name example-sub --subscription-type Exclusive
'''


import pulsar

serverUrl = "pulsar://localhost:6650"
topic =  'persistent://public/default/mytopic'

client = pulsar.Client(serverUrl)

producer = client.create_producer(
    topic,
    block_if_queue_full= True,
    batching_enabled= True,
    batching_max_publish_delay_ms= 10)

for i in range(10):
    producer.send(('Hello cabar 123-%d' % i).encode('utf-8'))
client.close()