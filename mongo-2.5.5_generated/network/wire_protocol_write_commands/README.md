# wire\_protocol\_write\_commands

# Module Groups

-------------

# Group Description
New write commands for new wire protocol. The new "write commands" are all actual Commands run  using "db.$cmd.findOne(...)". The reason for this is that the old wire protocol did not have  acknowledgements for anything BUT queries (which include commands), so everything is now a query  so we can get acknowledgements for writes (and not just for queries).
TODO: Split this up in more detail.  Note that this code is not for dealing with the wire protocol component, but is instead is the glue between the write command system and the new update system.

## Files
- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Core config server write management.  Sends a batch of the new write commands to the config servers.

## Files
- src/mongo/s/write\_ops/config\_coordinator.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator\_test.cpp   ()

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
New wire protocol writes (in mongos) TODO: Separate this into smaller groups and reorganize this section.  There are different parts to it.  The cluster\_write\_cmd file has the actual "Command" classes, the batch\_write\_exec files have the actually "runner" of the batch, while the batch\_write\_op and write\_op files are classes that are used to track the lifecycle of batch write and single write operations respectively

## Files
- src/mongo/s/commands/cluster\_write\_cmd.cpp   (mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op\_test.cpp   ()
- src/mongo/s/write\_ops/write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op\_test.cpp   ()

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Code to convert incoming writes on a mongos from a legacy client into a write command for talking to new mongods and convert write command responses into legacy getLastError responses.

## Files
- src/mongo/s/write\_ops/batch\_upconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert\_test.cpp   ()

## [Interface](interface/3)

## [Dependencies](dependencies/3)

-------------

# Group Description
Code to convert the new style write commands into legacy operations using getLastError, hidden behind the same interface.  This should all be removed in the next major release.

## Files
- src/mongo/s/write\_ops/batch\_downconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert\_test.cpp   ()
- src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/dbclient\_safe\_writer.h   (mongod, tools, mongos)

## [Interface](interface/4)

## [Dependencies](dependencies/4)

-------------

# Group Description
Header to enumerate the wire protocol version, along with the max and min supported versions.  The versions so far carry semantic information such as whether aggregation can return cursors or whether write commands are supported.

## Files
- src/mongo/db/wire\_version.h   (mongod, tools, mongos)

## [Interface](interface/5)

## [Dependencies](dependencies/5)
