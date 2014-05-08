# Chunk Management
Commands and utilities to manage chunks in a sharded cluster


-------------

## Mongod Migration Commands
Commands to move chunks between nodes in a cluster.  Has the command to signal to a mongod that it should move a chunk, and the command to tell a mongod that it should start receiving a chunk.

#### Files
- src/mongo/s/d\_migrate.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongod Split Commands
Commands to split chunks on mongod

#### Files
- src/mongo/s/d\_split.cpp   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Merge Chunks Command
Command to merge two chunks in a sharded cluster.  See https://jira.mongodb.org/browse/SERVER-8869

#### Files
- src/mongo/s/d\_merge.cpp   (mongod, tools)
- src/mongo/s/d\_merge.h   (mongod, tools)
- src/mongo/db/commands/merge\_chunks\_cmd.cpp   (mongod, tools)
- src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp   (mongos)
- src/mongo/dbtests/merge\_chunk\_tests.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

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

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Range Comparison
Utilities for comparing ranges. Useful because our sharding is range based.

#### Files
- src/mongo/s/range\_arithmetic.cpp   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic.h   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Chunk Management
Code for managing chunks.  Contains the ChunkManger, which is responsible for loading and storing chunk information on mongos, as well as a Chunk class, which is an abstraction for a chunk that is too smart for its own good, and knows how to do things like split itself.  All this code is older and should eventually be factored out.

#### Files
- src/mongo/s/chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)
