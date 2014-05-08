# Replica Set Configuration
Persistent configuration of a replica set.


-------------

## Replica Set Initiate
rs.initiate() (replSetInitiate) command

#### Files
- src/mongo/db/repl/rs\_initiate.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Replica Set Config
Class that manages the configuration of a replica set.  This is the static configuration in which changes are only really triggered by the user.  See the output of rs.conf(), which queries the current replica set configuration from the local database.

#### Files
- src/mongo/db/repl/rs\_config.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_config.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Replication Command Line Options
Global configuration options for replication from the command line.

#### Files
- src/mongo/db/repl/replication\_server\_status.h   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
