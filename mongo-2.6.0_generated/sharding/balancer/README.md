# Balancer
The balancer is a background job that runs on each mongos and is responsible for ensuring that the data is evenly distributed in a sharded cluster.  The balancer operates in "balancing rounds" during which it must take out a distributed lock on the config servers.


-------------

## Balancer Job
Job that runs in the background on mongos and calls "moveChunk" to move data between shards if an imbalance is detected.

#### Files
- [src/mongo/s/balance.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/balance.cpp)   (mongos)
- [src/mongo/s/balance.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/balance.h)   (mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Balancer Policy
Logic to determine how the balancer should balance data.  Takes into account things like whether a shard is draining, shard tags for tag aware sharding, and how overloaded the shards are.

#### Files
- [src/mongo/s/balancer\_policy.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/balancer_policy.cpp)   (mongos)
- [src/mongo/s/balancer\_policy.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/balancer_policy.h)   (mongos)
- [src/mongo/s/balancer\_policy\_tests.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/balancer_policy_tests.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
