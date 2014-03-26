
# Interface for Privileges
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/privilege.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/s/shard.cpp](../../../../sharding/sharding)
    - [src/mongo/s/cursors.cpp](../../../../sharding/sharding)
    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/shutdown.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
