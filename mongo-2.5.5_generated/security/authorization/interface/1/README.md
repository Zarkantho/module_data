
# Interface

### src/mongo/db/auth/privilege.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../../../replication)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../write\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/stats/top.cpp](../../../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/db/commands/shutdown.cpp](../../../database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../write\_commands)
