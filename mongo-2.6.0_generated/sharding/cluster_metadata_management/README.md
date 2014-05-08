# Cluster Metadata Management
Helpers and wrappers to manage cluster metadata.  These exist so that operations requiring cluster metadata do not have to have code to directly query the config servers.


-------------

## Top Level Cluster Configuration
Global class that is a point of contact for top level cluster configurations and config server interaction.  For example, has helpers to get the configuration of a database and its classes, add shards, and enable sharding on databases and collections.

#### Files
- src/mongo/s/grid.cpp   (mongod, tools, mongos)
- src/mongo/s/grid.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Database And Collection Configuration
Contains the sharded configuration of a database and its collections, such as whether sharding is enabled and what the shard key is
This file also has a class for interacting with the config servers, which bizarrely inherits from the class that stores all the metadata for a database.  I am not sure why the inheritance works this way, but it seems like a mistake, especially since the config server connection string gets stored in "\_primary", which is an instance of the "Shard" class.  The separation of work between this class and other classes that interact with the config server does not seem well defined, but the difference between this and the database class is that it manipulates metadata that is relevant to the cluster rather than database specific metadata.

#### Files
- src/mongo/s/config.cpp   (mongod, tools, mongos)
- src/mongo/s/config.h   (mongod, tools, mongos)
- src/mongo/s/config\_server\_tests.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Config Server Consistency Check Job
Thread periodically checks to make sure the config servers are in sync.

#### Files
- src/mongo/s/config\_server\_checker\_service.cpp   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
