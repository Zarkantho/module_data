# Routing
Code to deal with routing operations in a sharded cluster


-------------

## Operation Targeter
Classes to facilitate finding the target shard or shards for an operation.  Currently only used for write operations.  Built on the ChunkManager

#### Files
- [src/mongo/dbtests/chunk\_manager\_targeter\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/dbtests/chunk_manager_targeter_test.cpp)   ()
- [src/mongo/s/chunk\_manager\_targeter.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/chunk_manager_targeter.cpp)   (mongod, tools, mongos)
- [src/mongo/s/chunk\_manager\_targeter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/chunk_manager_targeter.h)   (mongod, tools, mongos)
- [src/mongo/s/ns\_targeter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/ns_targeter.h)   (mongod, tools, mongos)
- [src/mongo/s/mock\_ns\_targeter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/mock_ns_targeter.h)   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Shard Host Resolver
Class that allows conversion from a shard name to an actual connection object for the shard

#### Files
- [src/mongo/s/dbclient\_shard\_resolver.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/dbclient_shard_resolver.cpp)   (mongod, tools, mongos)
- [src/mongo/s/dbclient\_shard\_resolver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/dbclient_shard_resolver.h)   (mongod, tools, mongos)
- [src/mongo/s/mock\_shard\_resolver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/mock_shard_resolver.h)   ()
- [src/mongo/s/shard\_resolver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/shard_resolver.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Cluster Write
Top level entry point for doing any kind of write to a sharded cluster.  Writes against "admin" and "config" databases will be sent to the config servers, while Writes against any other database will go through the targeting and batch write command execution process.

#### Files
- [src/mongo/s/cluster\_write.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cluster_write.cpp)   (mongod, tools, mongos)
- [src/mongo/s/cluster\_write.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cluster_write.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Sharded Cursor
Client cursor for the results of a query on a sharded cluster. Built on top of ParallelSortClusteredCursor which keeps track of the cursors on the shards.  Currently only used for queries and getMore operations.

#### Files
- [src/mongo/s/cursors.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cursors.cpp)   (mongos)
- [src/mongo/s/cursors.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cursors.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Parallel Cursor
Cursor that represents a connection to a bunch of shards.  You would think that this only makes sense in mongos, but it turns out it is built into mongod for purposes of map reduce (the final destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

#### Files
- [src/mongo/client/parallel.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/client/parallel.cpp)   (mongod, tools, mongos)
- [src/mongo/client/parallel.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/client/parallel.h)   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Shard Key Management
Helpers for managing and storing shard keys.  Does things like checking if a shard key is compatible with a particular unique index and checking if a document contains the shard key.

#### Files
- [src/mongo/s/shard\_key\_pattern.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/shard_key_pattern.cpp)   (mongod, tools, mongos)
- [src/mongo/s/shard\_key\_pattern.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/shard_key_pattern.h)   (mongod, tools, mongos)
- [src/mongo/s/shardkey.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/shardkey.cpp)   (mongod, tools, mongos)
- [src/mongo/s/shardkey.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/shardkey.h)   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)
