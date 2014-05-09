# Metadata Versioniong
Since a sharded cluster is distributed, mongos and mongod both have to cache metadata from the config servers.  Because of this, there is a need to keep track of metadata version information and make decisions based on the last version that was seen.


-------------

## Chunk Diff
Helper class that takes the current state of the configuration matadata for the chunks in a cluster and uses that to determine what query should be used to get only what has changed rather than releading all the chunk data.

It does this by using the latest version that has been seen and makes a query that does not return anything lower than that version.

#### Files
- src/mongo/s/chunk\_diff-inl.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Chunk Version
Class that represents a version.  Used to version shards as well as chunks.

#### Files
- src/mongo/s/chunk\_version.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_version\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Stale Config Exeptions
Definitions of the exceptions that get thrown when a mongos tries to write to a mongod, but the mongos has an outdated config metadata version and should refresh.

#### Files
- src/mongo/s/stale\_exception.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Shard Version Manager
Code for managing shard versions on a mongos.  This is the code that throws the stale config exceptions if the mongos metadata is out of date.

#### Files
- src/mongo/s/version\_manager.cpp   (mongos)
- src/mongo/s/version\_manager.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Shard Version Stubs
Stubs for code shared between mongos and mongod that references functions to set the shard version of connections.  You should not have to care about this unless you are fixing build dependencies.

#### Files
- src/mongo/s/default\_version.cpp   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)
