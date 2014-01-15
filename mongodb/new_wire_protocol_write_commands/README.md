# new\_wire\_protocol\_write\_commands

# Module Groups

-------------

New write commands for new wire protocol. The new "write commands" are all actual Commands run  using "db.$cmd.findOne(...)". The reason for this is that the old wire protocol didn't have  acknowledgements for anything BUT queries (which include commands), so everything is now a query  so we can get acknowledgements for writes (and not just for queries).

- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h

-------------

New wire protocol writes (in mongos)

- src/mongo/s/commands/cluster\_write\_cmd.cpp   (mongos)
- src/mongo/s/write\_ops/batch\_downconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert.h
- src/mongo/s/write\_ops/batch\_downconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_upconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert.h
- src/mongo/s/write\_ops/batch\_upconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_exec.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.h
- src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op.h
- src/mongo/s/write\_ops/batch\_write\_op\_test.cpp   ()
- src/mongo/s/write\_ops/config\_coordinator.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator.h
- src/mongo/s/write\_ops/config\_coordinator\_test.cpp   ()
- src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/dbclient\_safe\_writer.h
- src/mongo/s/write\_ops/write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op.h
- src/mongo/s/write\_ops/write\_op\_test.cpp   ()

-------------

New wire protocol writes (in mongod)   why are these in s/ ?

- src/mongo/s/write\_ops/batched\_command\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_request.h
- src/mongo/s/write\_ops/batched\_command\_response.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_response.h
- src/mongo/s/write\_ops/batched\_command\_response\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_delete\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_document.h
- src/mongo/s/write\_ops/batched\_delete\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request.h
- src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_insert\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_insert\_request.h
- src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_request\_metadata.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_request\_metadata.h
- src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_update\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_document.h
- src/mongo/s/write\_ops/batched\_update\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request.h
- src/mongo/s/write\_ops/batched\_update\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_upsert\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_upsert\_detail.h
- src/mongo/s/write\_ops/wc\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/wc\_error\_detail.h
- src/mongo/s/write\_ops/write\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_error\_detail.h

-------------

Header to enumerate the wire protocol version, along with the max and min supported versions   can you say a bit about who exactly cares (which components) about wire protocol version?

- src/mongo/db/wire\_version.h
