# Sharding Uncategorized
TODO: Uncategorized sharding code TODO: Figure out what should go here and what should go in the write commands network section


-------------

## Mongod Sharding Globals
Declarations for a bunch of globals used in sharding.  The actual definitions are unfortunately scatterned between d\_logic.cpp, d\_state.cpp, and others.

#### Files
- src/mongo/s/d\_logic.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Range Deleter
Helper classes to delete a range of documents. This is used for example in chunk migrations when we are cleaning up an old chunk.

#### Files
- src/mongo/db/range\_deleter.cpp   (mongod, tools)
- src/mongo/db/range\_deleter.h   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.h   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.h   (mongod, tools)
- src/mongo/db/range\_deleter\_service.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_service.h   (mongod, tools)
- src/mongo/db/range\_deleter\_stat\_test.cpp   ()
- src/mongo/db/range\_deleter\_stats.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_stats.h   (mongod, tools)
- src/mongo/db/range\_deleter\_test.cpp   ()
- src/mongo/db/range\_preserver.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Range Comparison
Utilities for comparing ranges. Useful because our sharding is range based.

#### Files
- src/mongo/s/range\_arithmetic.cpp   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic.h   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Config Upgrade
Code to upgrade config server metadata

#### Files
- src/mongo/s/config\_upgrade.cpp   (mongos)
- src/mongo/s/config\_upgrade.h   (mongos)
- src/mongo/s/config\_upgrade\_helpers.cpp   (mongos)
- src/mongo/s/config\_upgrade\_helpers.h   (mongos)
- src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp   (mongos)
- src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp   (mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Distributed Lock
Distributed lock (lock on the config servers from mongos, i.e. "balancer lock")

#### Files
- src/mongo/s/distlock.cpp   (mongod, tools, mongos)
- src/mongo/s/distlock.h   (mongod, tools, mongos)
- src/mongo/s/distlock\_test.cpp   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Chunk Diff
Helper class that takes the current state of the configuration matadata for the chunks in a cluster and uses that to determine what query should be used to get only what has changed rather than releading all the chunk data.
It does this by using the latest version that has been seen and makes a query that does not return anything lower than that version.

#### Files
- src/mongo/s/chunk\_diff-inl.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff\_test.cpp   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Top Level Cluster Configuration
Global class that is a point of contact for top level cluster configurations and config server interaction.  For example, has helpers to get the configuration of a database and its classes, add shards, and enable sharding on databases and collections.

#### Files
- src/mongo/s/grid.cpp   (mongod, tools, mongos)
- src/mongo/s/grid.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Database And Collection Configuration
Contains the sharded configuration of a database and its collections, such as whether sharding is enabled and what the shard key is
This file also has a class for interacting with the config servers, which bizarrely inherits from the class that stores all the metadata for a database.  I am not sure why the inheritance works this way, but it seems like a mistake, especially since the config server connection string gets stored in "\_primary", which is an instance of the "Shard" class.  The separation of work between this class and other classes that interact with the config server does not seem well defined, but the difference between this and the database class is that it manipulates metadata that is relevant to the cluster rather than database specific metadata.
TODO: Clean up this description.  The basic idea behind this is that there is one global ConfigServer object that has things to interact with the changelog and the settings collections, while the DBConfig class has things to interact with collections that have database specific information.

#### Files
- src/mongo/s/config.cpp   (mongod, tools, mongos)
- src/mongo/s/config.h   (mongod, tools, mongos)
- src/mongo/s/config\_server\_tests.cpp   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Chunk Version
Class that represents a version.  Used to version shards as well as chunks.

#### Files
- src/mongo/s/chunk\_version.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_version\_test.cpp   ()

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Storage Layer Stubs
Some code that is shared between mongos and mongod references symbols in the storage layer, which should not be built into mongos.  You should not care about this file unless you are trying to fix our build dependencies.

#### Files
- src/mongo/s/mongos\_persistence\_stubs.cpp   (mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Operation Targeter
Classes to facilitate finding the target shard or shards for an operation.  Currently only used for write operations.  Built on the ChunkManager

#### Files
- src/mongo/dbtests/chunk\_manager\_targeter\_test.cpp   ()
- src/mongo/s/chunk\_manager\_targeter.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_manager\_targeter.h   (mongod, tools, mongos)
- src/mongo/s/ns\_targeter.h   (mongod, tools, mongos)
- src/mongo/s/mock\_ns\_targeter.h   ()

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Shard Host Resolver
Class that allows conversion from a shard name to an actual connection object for the shard

#### Files
- src/mongo/s/dbclient\_shard\_resolver.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_shard\_resolver.h   (mongod, tools, mongos)
- src/mongo/s/mock\_shard\_resolver.h   ()
- src/mongo/s/shard\_resolver.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## Cluster Write
Top level entry point for doing any kind of write to a sharded cluster.  Writes against "admin" and "config" databases will be sent to the config servers, while Writes against any other database will go through the targeting and batch write command execution process.

#### Files
- src/mongo/s/cluster\_write.cpp   (mongod, tools, mongos)
- src/mongo/s/cluster\_write.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Chunk Management
Code for managing chunks.  Contains the ChunkManger, which is responsible for loading and storing chunk information on mongos, as well as a Chunk class, which is an abstraction for a chunk that is too smart for its own good, and knows how to do things like split itself.  All this code is older and should eventually be factored out.

#### Files
- src/mongo/s/chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk.h   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Cluster Management Utilities
Helpers for accessing the current state of a cluster.  Has helpers to get config metadata as well as helpers to check the versions of all nodes in the cluster.  Used by the config metadata upgrade system as well as the auth schema upgrade system.

#### Files
- src/mongo/s/cluster\_client\_internal.cpp   (mongos)
- src/mongo/s/cluster\_client\_internal.h   (mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

## Config Server Consistency Check Job
Thread periodically checks to make sure the config servers are in sync.

#### Files
- src/mongo/s/config\_server\_checker\_service.cpp   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.h   (mongod, tools, mongos)

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)

-------------

## Stale Config Exeptions
Definitions of the exceptions that get thrown when a mongos tries to write to a mongod, but the mongos has an outdated config metadata version and should refresh.

#### Files
- src/mongo/s/stale\_exception.h   (mongod, tools, mongos)

#### [Interface](interface/16)

#### [Dependencies](dependencies/16)

-------------

## Sharded Cursor
Client cursor for the results of a query on a sharded cluster. Built on top of ParallelSortClusteredCursor which keeps track of the cursors on the shards.  Currently only used for queries and getMore operations.

#### Files
- src/mongo/s/cursors.cpp   (mongos)
- src/mongo/s/cursors.h   (mongod, tools, mongos)

#### [Interface](interface/17)

#### [Dependencies](dependencies/17)

-------------

## Mongos Admin Commands
Mongos commands that can only be run against the admin database.

#### Files
- src/mongo/s/commands\_admin.cpp   (mongos)

#### [Interface](interface/18)

#### [Dependencies](dependencies/18)

-------------

## Mongos Public Commands
Assorted mongos commands that do not need to be run against the admin database.  Many commands just pass through to the shards or config servers.

#### Files
- src/mongo/s/commands\_public.cpp   (mongos)

#### [Interface](interface/19)

#### [Dependencies](dependencies/19)

-------------

## Version Validity Checker
Helpers to check whether a version is within a range of versions. It is used by the config metadata upgrade system to determine if the version being upgraded to is in an invalid range.

#### Files
- src/mongo/s/mongo\_version\_range.cpp   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range.h   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range\_test.cpp   ()

#### [Interface](interface/20)

#### [Dependencies](dependencies/20)

-------------

## Shard Version Manager
Code for managing shard versions from mongos.  This is the code that throws the stale config exceptions if the mongos metadata is out of date.

#### Files
- src/mongo/s/version\_manager.cpp   (mongos)
- src/mongo/s/version\_manager.h   (mongod, tools, mongos)

#### [Interface](interface/21)

#### [Dependencies](dependencies/21)

-------------

## Shard Connection
Abstraction around a connection to a shard.  Uses its own private connection pool that is independent of the one in the C++ client driver.

#### Files
- src/mongo/s/shardconnection.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_conn\_test.cpp   ()

#### [Interface](interface/22)

#### [Dependencies](dependencies/22)

-------------

## Shard Configuration
Abstraction around a shard.  Contains all the information needed to connect to the shard as well as helpers to run commands.  Also stores the shard tags.

#### Files
- src/mongo/s/shard.cpp   (mongod, tools, mongos)
- src/mongo/s/shard.h   (mongod, tools, mongos)
- src/mongo/s/shard\_test.cpp   ()

#### [Interface](interface/23)

#### [Dependencies](dependencies/23)

-------------

## Print Mongos Version
Helper to print version information about the running mongos

#### Files
- src/mongo/s/version\_mongos.cpp   (mongos)
- src/mongo/s/version\_mongos.h   (mongos)

#### [Interface](interface/24)

#### [Dependencies](dependencies/24)

-------------

## Shard Version Stubs
Stubs for code shared between mongos and mongod that references functions to set the shard version of connections.  You should not have to care about this unless you are fixing build dependencies.

#### Files
- src/mongo/s/default\_version.cpp   (mongod, tools)

#### [Interface](interface/25)

#### [Dependencies](dependencies/25)

-------------

## Shard Key Management
Helpers for managing and storing shard keys.  Does things like checking if a shard key is compatible with a particular unique index and checking if a document contains the shard key.

#### Files
- src/mongo/s/shard\_key\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_key\_pattern.h   (mongod, tools, mongos)
- src/mongo/s/shardkey.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.h   (mongod, tools, mongos)

#### [Interface](interface/26)

#### [Dependencies](dependencies/26)
