# Write Commands
New write commands for new wire protocol. The new "write commands" are all implemented as server Commands run using "db.$cmd.findOne(...)".  The legacy write operations did not recieve responses, but commands do recieve responses, so sending writes as "commands" ensures that all writes get a response.  Note that this means the "write commands" are layered on top of the legacy wire protocol, rather than replacing it.


-------------

## Multi Command Dispatcher
The classes that actually handle the networking component of dispatching commands to multiple shards in parallel.

#### Files
- src/mongo/s/dbclient\_multi\_command.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_multi\_command.h   (mongod, tools, mongos)
- src/mongo/s/mock\_multi\_write\_command.h   ()
- src/mongo/s/multi\_command\_dispatch.h   (mongod, tools, mongos)
- src/mongo/dbtests/dbclient\_multi\_command\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Write Commands Declarations
Classes registering the write commands into the command system. When a write command is recieved by a mongod, this is the entry point.

#### Files
- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Batch Executor
Class that actually does the work of executing a batch of writes on a mongod.

#### Files
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Write Commands Utilities
Common utilities that are shared by the write commands, such as authorization checks.

#### Files
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Config Coordinator
Core config server write management.  Sends a batch of the new write commands to the config servers.

#### Files
- src/mongo/s/write\_ops/config\_coordinator.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Mongos Write Commands Entry Point
Command definition for the write commands.  The bulk of the work is done elsewhere, but this is where execution of the write commands begins.

#### Files
- src/mongo/s/commands/cluster\_write\_cmd.cpp   (mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Mongos Write Commands Runner
Entry point to the actual write command execution.  This is the top level class that the mongos calls to run the write commands and aggregate the results for returning to the client.  It is responsible for moving write command execution forward.

#### Files
- src/mongo/s/write\_ops/batch\_write\_exec.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Mongos Write Commands Lifecycle Tracking
Code to track the life cycle of a single write operation or batch of operations that are being dispatched by a mongos.  The batched life cycle tracking is built on top of the single operation lifecycle tracking.

#### Files
- src/mongo/s/write\_ops/batch\_write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op\_test.cpp   ()
- src/mongo/s/write\_ops/write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op\_test.cpp   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Write Commands Upconvert
Code to convert incoming writes on a mongos from a legacy client into a write command for talking to new mongods and convert write command responses into legacy getLastError responses.

#### Files
- src/mongo/s/write\_ops/batch\_upconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert\_test.cpp   ()

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Write Commands Downconvert
Code to convert the new style write commands into legacy operations using getLastError, hidden behind the same interface.  This should all be removed in the next major release.

#### Files
- src/mongo/s/write\_ops/batch\_downconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert\_test.cpp   ()
- src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/dbclient\_safe\_writer.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Wire Version
Header to enumerate the wire protocol version, along with the max and min supported versions.  The versions so far carry semantic information such as whether aggregation can return cursors or whether write commands are supported.

#### Files
- src/mongo/db/wire\_version.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
