
# Interface

### src/mongo/db/auth/action\_set.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../sharding)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../../../replication)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../new\_wire\_protocol\_write\_commands)
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
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::ActionSet::removeAllActions()

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)

### build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getShardVersion

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::addShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::update

- Used By:

    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ActionType::collStats

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::insert

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ActionType::planCacheRead

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../sharding)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::revokeRole

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::logRotate

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::viewRole

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::netstat

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::removeShard

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::indexStats

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dbStats

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::getParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::connPoolSync

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::hostInfo

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::invalidateUserCache

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::validate

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::resync

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../replication)

<div></div>

    mongo::ActionType::planCacheIndexFilter

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../sharding)

<div></div>

    mongo::ActionType::dropRole

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::planCacheWrite

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../sharding)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dropDatabase

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::repairDatabase

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::splitChunk

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)

<div></div>

    mongo::ActionType::getLog

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::internal

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/d\_writeback.cpp](../../../sharding)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::ActionType::touch

- Used By:

    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::createRole

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dropUser

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::inprog

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ActionType::listDatabases

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::unlock

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ActionType::replSetStateChange

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)

<div></div>

    mongo::ActionType::authSchemaUpgrade

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::shardingState

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)

<div></div>

    mongo::ActionType::flushRouterConfig

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::cleanupOrphaned

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::createIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ActionType::killop

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ActionType::storageDetails

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::replSetConfigure

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)

<div></div>

    mongo::ActionType::collMod

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::fsync

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::remove

- Used By:

    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ActionType::enableSharding

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::moveChunk

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::ActionType::listShards

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ActionType::changeCustomData

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::enableProfiler

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::connPoolStats

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::ActionType::viewUser

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::appendOplogNote

- Used By:

    - [src/mongo/db/commands/oplog\_note.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::changePassword

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::splitVector

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)

<div></div>

    mongo::ActionType::setParameter

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dbHash

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::serverStatus

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::createUser

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::renameCollectionSameDB

- Used By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::convertToCapped

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::cursorInfo

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::ActionType::getShardMap

- Used By:

    - [src/mongo/s/shard.cpp](../../../sharding)

<div></div>

    mongo::ActionType::reIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::find

- Used By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/commands/mr\_common.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dropIndex

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::top

- Used By:

    - [src/mongo/db/stats/top.cpp](../../../utilities)

<div></div>

    mongo::ActionType::diagLogging

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::closeAllDatabases

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::killCursors

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::ActionType::compact

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::replSetGetStatus

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)

<div></div>

    mongo::ActionType::createCollection

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::shutdown

- Used By:

    - [src/mongo/db/commands/shutdown.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::dropCollection

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)

<div></div>

    mongo::ActionType::getCmdLineOpts

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
