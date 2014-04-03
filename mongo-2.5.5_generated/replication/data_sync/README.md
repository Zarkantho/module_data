# Data Sync
This module contains the code that replica sets use to keep the data synced between nodes.  Note that there are multiple phases.  The first stage is the initial sync, where all the data must be copied over, and the second is the stage where the node syncing the data reads the oplog and applies all operations to its local copy of the data.


-------------

## resync Command
Implementation of "resync" command

#### Files
- src/mongo/db/repl/resync.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Replica Set Sync and Initial Sync
Code to do sync and inital sync.  Note that this is a complex class heirarchy, and the files do not map one to one with class definitions and implementation.  The sync thread is started and run in "rs\_sync.cpp".  It handles doing the initial sync if applicable, then tailing the oplog.

#### Files
- src/mongo/db/repl/rs\_initialsync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.h   (mongod, tools, mongos)
- src/mongo/db/repl/sync.cpp   (mongod, tools)
- src/mongo/db/repl/sync.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Replica Set Background Sync Threads
Threads that actually handle syncing the oplog from the sync source. This includes the thread that actually reads the data from the source as well as the thread that notifies the source of how far it read

#### Files
- src/mongo/db/repl/bgsync.cpp   (mongod, tools)
- src/mongo/db/repl/bgsync.h   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Sync Source Feedback
Code to tell the sync source how far we have progressed in the oplog.  For new versions this is the "replSetUpdatePosition command, but for old versions this was a "ghost cursor" which would only be advanced when the batch had been processed

#### Files
- src/mongo/db/repl/sync\_source\_feedback.cpp   (mongod, tools)
- src/mongo/db/repl/sync\_source\_feedback.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Oplog Reader
Class to handle the details of how we are querying the oplog.  The interface is something like the interface for a cursor.

#### Files
- src/mongo/db/repl/oplogreader.cpp   (mongod, tools)
- src/mongo/db/repl/oplogreader.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Oplog
Free helper functions to create the oplog, log operations into the oplog and apply operations from the oplog.

#### Files
- src/mongo/db/repl/oplog.cpp   (mongod, tools)
- src/mongo/db/repl/oplog.h   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Replica Set Rollback
Code to handle rollbacks when two nodes got different writes (in the case where two nodes thought they were primary for some period of time).

#### Files
- src/mongo/db/repl/rs\_rollback.cpp   (mongod, tools)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)
