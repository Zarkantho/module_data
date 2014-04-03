# Mongod Commands
Core sharding commands on mongod


-------------

## Migration Commands
Commands to move chunks between nodes in a cluster.  Has the command to signal to a mongod that it should move a chunk, and the command to tell a mongod that it should start receiving a chunk.

#### Files
- src/mongo/s/d\_migrate.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Split Commands
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
