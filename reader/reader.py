import pulsar
 
client = pulsar.Client('pulsar://localhost:6650')
 
reader = client.create_reader(
   'persistent://public/default/mytopic',
    pulsar.MessageId.earliest)
 
while True:
    msg = reader.read_next()
    print("Read message '%s' id='%s'", 
      msg.data().decode('utf-8'), msg.message_id())
        
 
client.close()