# database\_commands

# Module Groups

-------------

# Group Description
Base class for mongodb commands. Has a big std::map with the keys of the command name and the  values as the Command itself. These are the commands that you run using  "db.$cmd.findOne({ "serverStatus" : true }).

## Files
- src/mongo/db/commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands.h   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
A bunch of commands for mongod. However, this ALSO has the definition of Command::execCommand for  mongod (the function that actually runs commands registered using the Command class, which gets  called whenever a query against the "$cmd" collection is made)

## Files
- src/mongo/db/dbcommands.cpp   (mongod, tools)

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
Commands (run using db.$cmd.findOne(...))

## Files
- src/mongo/db/commands/apply\_ops.cpp   (mongod, tools)
- src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp   (mongod, tools)
- src/mongo/db/commands/collection\_to\_capped.cpp   (mongod, tools)
- src/mongo/db/commands/compact.cpp   (mongod, tools)
- src/mongo/db/commands/connection\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/copydb.h   (mongod, tools, mongos)
- src/mongo/db/commands/copydb\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/create\_indexes.cpp   (mongod, tools)
- src/mongo/db/commands/dbhash.cpp   (mongod, tools)
- src/mongo/db/commands/dbhash.h   (mongod, tools)
- src/mongo/db/commands/distinct.cpp   (mongod, tools)
- src/mongo/db/commands/drop\_indexes.cpp   (mongod, tools)
- src/mongo/db/commands/fail\_point\_cmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/find\_and\_modify.cpp   (mongod, tools)
- src/mongo/db/commands/find\_and\_modify.h   (mongod, tools, mongos)
- src/mongo/db/commands/find\_and\_modify\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/geonear.cpp   (mongod, tools)
- src/mongo/db/commands/get\_last\_error.cpp   (mongod, tools)
- src/mongo/db/commands/group.cpp   (mongod, tools)
- src/mongo/db/commands/hashcmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/index\_filter\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/index\_filter\_commands.h   (mongod, tools)
- src/mongo/db/commands/index\_filter\_commands\_test.cpp   ()
- src/mongo/db/commands/index\_stats.cpp   (mongod, tools)
- src/mongo/db/commands/isself.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/mr.cpp   (mongod, tools)
- src/mongo/db/commands/mr.h   (mongod, tools, mongos)
- src/mongo/db/commands/mr\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/oplog\_note.cpp   (mongod, tools)
- src/mongo/db/commands/parallel\_collection\_scan.cpp   (mongod, tools)
- src/mongo/db/commands/parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/plan\_cache\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/plan\_cache\_commands.h   (mongod, tools)
- src/mongo/db/commands/plan\_cache\_commands\_test.cpp   ()
- src/mongo/db/commands/rename\_collection.cpp   (mongod, tools)
- src/mongo/db/commands/rename\_collection.h   (mongod, tools, mongos)
- src/mongo/db/commands/rename\_collection\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.h   (mongod, tools, mongos)
- src/mongo/db/commands/shutdown.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/shutdown.h   (mongod, tools, mongos)
- src/mongo/db/commands/storage\_details.cpp   (mongod, tools)
- src/mongo/db/commands/test\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/touch.cpp   (mongod)
- src/mongo/db/commands/validate.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_admin.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_generic.cpp   (mongod, tools, mongos)
- src/mongo/db/dbeval.cpp   (mongod, tools)
- src/mongo/db/driverHelpers.cpp   (mongod, tools)

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Commands + code for fsync of data files

## Files
- src/mongo/db/commands/fsync.cpp   (mongod, tools)
- src/mongo/db/commands/fsync.h   (mongod, tools)

## [Interface](interface/3)

## [Dependencies](dependencies/3)
