
# Interface for Action Types
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/action\_set.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
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
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionSet::removeAllActions()

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)

### build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getShardVersion

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::addShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::update

- Used By:

    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ActionType::collStats

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::insert

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ActionType::planCacheRead

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::logRotate

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::netstat

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::removeShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::indexStats

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::dbStats

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::getParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::connPoolSync

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::hostInfo

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::validate

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::resync

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)

<div></div>

    mongo::ActionType::planCacheIndexFilter

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::planCacheWrite

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::dropDatabase

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::repairDatabase

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::splitChunk

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::getLog

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::internal

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::touch

- Used By:

    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::inprog

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ActionType::listDatabases

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::unlock

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ActionType::replSetStateChange

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)

<div></div>

    mongo::ActionType::shardingState

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::flushRouterConfig

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::cleanupOrphaned

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::createIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ActionType::killop

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ActionType::storageDetails

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::replSetConfigure

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)

<div></div>

    mongo::ActionType::collMod

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::fsync

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::remove

- Used By:

    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ActionType::enableSharding

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::moveChunk

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::listShards

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::enableProfiler

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::connPoolStats

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::appendOplogNote

- Used By:

    - [src/mongo/db/commands/oplog\_note.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::splitVector

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::setParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::dbHash

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::serverStatus

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::renameCollectionSameDB

- Used By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::convertToCapped

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::cursorInfo

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/cursors.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::getShardMap

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::reIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::find

- Used By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::dropIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::top

- Used By:

    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ActionType::diagLogging

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::closeAllDatabases

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::killCursors

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../../../../sharding/sharding)

<div></div>

    mongo::ActionType::compact

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::replSetGetStatus

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)

<div></div>

    mongo::ActionType::createCollection

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::shutdown

- Used By:

    - [src/mongo/db/commands/shutdown.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::dropCollection

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ActionType::getCmdLineOpts

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
