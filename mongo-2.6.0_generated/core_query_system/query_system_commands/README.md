# Query System Commands
Database commands specifically for interacting with the query system.


-------------

## Mongod Query System Commands
Query system commands for mongod.  They allow for some runtime configuration of the query system.

#### Files
- src/mongo/db/commands/index\_filter\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/index\_filter\_commands.h   (mongod, tools)
- src/mongo/db/commands/index\_filter\_commands\_test.cpp   ()
- src/mongo/db/commands/plan\_cache\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/plan\_cache\_commands.h   (mongod, tools)
- src/mongo/db/commands/plan\_cache\_commands\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongos Query System Commands
Query system commands for mongos.  These just pass the operations through to the shards and aggregate the results.

#### Files
- src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp   (mongos)
- src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp   (mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
