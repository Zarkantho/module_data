# Shard Abstraction
Classes abstracting the idea of a shard in a sharded cluster


-------------

## Shard Connection
Abstraction around a connection to a shard.  Uses its own private connection pool that is independent of the one in the C++ client driver.

#### Files
- src/mongo/s/shardconnection.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_conn\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Shard Configuration
Abstraction around a shard.  Contains all the information needed to connect to the shard as well as helpers to run commands.  Also stores the shard tags.

#### Files
- src/mongo/s/shard.cpp   (mongod, tools, mongos)
- src/mongo/s/shard.h   (mongod, tools, mongos)
- src/mongo/s/shard\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
