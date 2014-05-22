# Database Commands
In the base MongoDB wire protocol, each packet has an "opCode" field that specifies what kind of operation it is.  These are things like "OP\_GET\_MORE", "OP\_QUERY", "OP\_INSERT", etc.

However, there is no "OP\_COMMAND" or anything that looks like it.  What are "Commands" then? What happens when you run "db.serverStatus()"?

Well, it turns out that commands are simply queries against the special reserved "$cmd" collection.  What this means is that "db.serverStatus()" calls "db.runCommand({serverStatus:1})" which then calls "db.$cmd.findOne({serverStatus:1})".

See TODO: wiki on Commands for more details.


-------------

## Commands Registration Class
Base class for mongodb commands. Has a static global std::map of Command objects keyed by the command name.  The way the registration works is by inheritance, since the Constructor of this class "registers itself" in the global command map when it gets executed.

#### Files
- [src/mongo/db/commands.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## General Mongod Commands
A bunch of commands for mongod. However, this ALSO has the definition of Command::execCommand for  mongod (the function that actually runs commands registered using the Command class, which gets  called whenever a query against the "$cmd" collection is made)

#### Files
- [src/mongo/db/dbcommands.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbcommands.cpp)   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Uncategorized Commands
Commands (run using db.$cmd.findOne(...))

TODO: Categorize and document these separately

#### Files
- [src/mongo/db/commands/apply\_ops.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/apply_ops.cpp)   (mongod, tools)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/cleanup_orphaned_cmd.cpp)   (mongod, tools)
- [src/mongo/db/commands/collection\_to\_capped.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/collection_to_capped.cpp)   (mongod, tools)
- [src/mongo/db/commands/compact.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/compact.cpp)   (mongod, tools)
- [src/mongo/db/commands/connection\_status.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/connection_status.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/copydb.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/copydb.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/copydb\_common.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/copydb_common.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/create\_indexes.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/create_indexes.cpp)   (mongod, tools)
- [src/mongo/db/commands/dbhash.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/dbhash.cpp)   (mongod, tools)
- [src/mongo/db/commands/dbhash.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/dbhash.h)   (mongod, tools)
- [src/mongo/db/commands/distinct.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/distinct.cpp)   (mongod, tools)
- [src/mongo/db/commands/drop\_indexes.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/drop_indexes.cpp)   (mongod, tools)
- [src/mongo/db/commands/fail\_point\_cmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/fail_point_cmd.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/find\_and\_modify.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/find_and_modify.cpp)   (mongod, tools)
- [src/mongo/db/commands/find\_and\_modify.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/find_and_modify.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/find\_and\_modify\_common.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/find_and_modify_common.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/geonear.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/geonear.cpp)   (mongod, tools)
- [src/mongo/db/commands/get\_last\_error.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/get_last_error.cpp)   (mongod, tools)
- [src/mongo/db/commands/group.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/group.cpp)   (mongod, tools)
- [src/mongo/db/commands/hashcmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/hashcmd.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/index\_stats.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/index_stats.cpp)   (mongod, tools)
- [src/mongo/db/commands/isself.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/isself.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/mr.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/mr.cpp)   (mongod, tools)
- [src/mongo/db/commands/mr.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/mr.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/mr\_common.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/mr_common.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/oplog\_note.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/oplog_note.cpp)   (mongod, tools)
- [src/mongo/db/commands/parallel\_collection\_scan.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/parallel_collection_scan.cpp)   (mongod, tools)
- [src/mongo/db/commands/parameters.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/parameters.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/rename\_collection.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/rename_collection.cpp)   (mongod, tools)
- [src/mongo/db/commands/rename\_collection.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/rename_collection.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/rename\_collection\_common.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/rename_collection_common.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/server\_status.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/server_status.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/server\_status.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/server_status.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/shutdown.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/shutdown.cpp)   (mongod, tools, mongos)
- [src/mongo/db/commands/shutdown.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/shutdown.h)   (mongod, tools, mongos)
- [src/mongo/db/commands/storage\_details.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/storage_details.cpp)   (mongod, tools)
- [src/mongo/db/commands/test\_commands.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/test_commands.cpp)   (mongod, tools)
- [src/mongo/db/commands/touch.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/touch.cpp)   (mongod)
- [src/mongo/db/commands/validate.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/validate.cpp)   (mongod, tools)
- [src/mongo/db/dbcommands\_admin.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbcommands_admin.cpp)   (mongod, tools)
- [src/mongo/db/dbcommands\_generic.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbcommands_generic.cpp)   (mongod, tools, mongos)
- [src/mongo/db/dbeval.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbeval.cpp)   (mongod, tools)
- [src/mongo/db/driverHelpers.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/driverHelpers.cpp)   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Fsync Command
Commands + code for fsync of data files

#### Files
- [src/mongo/db/commands/fsync.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/fsync.cpp)   (mongod, tools)
- [src/mongo/db/commands/fsync.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/fsync.h)   (mongod, tools)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)
