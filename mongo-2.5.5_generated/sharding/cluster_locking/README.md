# Cluster Locking
Locking that is specific to a sharded cluster


-------------

## Distributed Lock
A distributed locking mechanism to allow nodes to correctly and safely take a lock on a specific resource in the entire cluster.  For example, a mongos could take a "balancer" lock, or a mongod could take out a lock for a specific chunk

#### Files
- src/mongo/s/distlock.cpp   (mongod, tools, mongos)
- src/mongo/s/distlock.h   (mongod, tools, mongos)
- src/mongo/s/distlock\_test.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
