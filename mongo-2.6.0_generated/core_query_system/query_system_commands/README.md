# Query System Commands
Database commands specifically for interacting with the query system.


-------------

## Mongod Query System Commands
Query system commands for mongod.  They allow for some runtime configuration of the query system.

#### Files
- [src/mongo/db/commands/index\_filter\_commands.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/index_filter_commands.cpp)   (mongod, tools)
- [src/mongo/db/commands/index\_filter\_commands.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/index_filter_commands.h)   (mongod, tools)
- [src/mongo/db/commands/index\_filter\_commands\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/index_filter_commands_test.cpp)   ()
- [src/mongo/db/commands/plan\_cache\_commands.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/plan_cache_commands.cpp)   (mongod, tools)
- [src/mongo/db/commands/plan\_cache\_commands.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/plan_cache_commands.h)   (mongod, tools)
- [src/mongo/db/commands/plan\_cache\_commands\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/plan_cache_commands_test.cpp)   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongos Query System Commands
Query system commands for mongos.  These just pass the operations through to the shards and aggregate the results.

#### Files
- [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/commands/cluster_index_filter_cmd.cpp)   (mongos)
- [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/commands/cluster_plan_cache_cmd.cpp)   (mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
