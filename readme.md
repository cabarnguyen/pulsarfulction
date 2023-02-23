- List all the clusters in the Pulsar instance.​

docker exec -it pulsar /pulsar/bin/pulsar-admin clusters list​

 -List all the tenants in the Pulsar instance.​

docker exec -it pulsar /pulsar/bin/pulsar-admin tenants list​

Create a new tenant named manning.​

docker exec -it pulsar /pulsar/bin/pulsar-admin tenants create manning​

Create a new namespace named resturant under the manning tenant​

docker exec -it pulsar /pulsar/bin/pulsar-admin namespaces create manning/resturant ​

List the namespaces under the manning tenant.​

docker exec -it pulsar /pulsar/bin/pulsar-admin namespaces list manning ​

Create a new topic.​

docker exec -it pulsar /pulsar/bin/pulsar-admin topics create persistent://manning/resturant /example-topic​

docker exec -it pulsar /pulsar/bin/pulsar-admin topics list manning/resturant 
