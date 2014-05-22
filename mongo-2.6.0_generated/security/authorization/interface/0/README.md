
# Interface for Action Types
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/action\_set.cpp

<div></div>

    mongo::ActionSet::removeAllActions()

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/shutdown.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/geo/haystack.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

### build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getShardVersion

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::addShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::collStats

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::insert

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::planCacheRead

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::ActionType::netstat

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::removeShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::indexStats

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::dbStats

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::getParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::closeAllDatabases

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::hostInfo

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::validate

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::getShardMap

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ActionType::resync

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ActionType::planCacheIndexFilter

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::ActionType::planCacheWrite

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::ActionType::dropDatabase

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::repairDatabase

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::splitChunk

- Used By:

    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ActionType::connPoolSync

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::getLog

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::internal

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::ActionType::appendOplogNote

- Used By:

    - [src/mongo/db/commands/oplog\_note.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::touch

- Used By:

    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::update

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::inprog

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ActionType::listDatabases

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::replSetStateChange

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ActionType::shardingState

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::ActionType::flushRouterConfig

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::getCmdLineOpts

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::unlock

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ActionType::logRotate

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::createIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::killop

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ActionType::storageDetails

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::replSetConfigure

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ActionType::collMod

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::fsync

- Used By:

    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::remove

- Used By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::enableSharding

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::cleanupOrphaned

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::listShards

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::enableProfiler

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::connPoolStats

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ActionType::splitVector

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ActionType::setParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::dbHash

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::serverStatus

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::renameCollectionSameDB

- Used By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::convertToCapped

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::cursorInfo

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ActionType::reIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::find

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/geo/haystack.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/fts/fts\_command.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::dropCollection

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::dropIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::top

- Used By:

    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ActionType::diagLogging

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::moveChunk

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::killCursors

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ActionType::compact

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::replSetGetStatus

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ActionType::createCollection

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ActionType::shutdown

- Used By:

    - [src/mongo/db/commands/shutdown.cpp](../../../../query\_and\_operation\_handling/database\_commands)
