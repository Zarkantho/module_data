
# Interface

### src/mongo/s/balance.cpp

<div></div>

    mongo::balancer

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/chunk.cpp

<div></div>

    mongo::ChunkManager::loadExistingRanges(std::string const&)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::createFirstChunks(std::string const&, mongo::Shard const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const*, std::vector<mongo::Shard, std::allocator<mongo::Shard> > const*)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::ChunkManager(std::string const&, mongo::ShardKeyPattern const&, bool)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::compatibleWith(mongo::ChunkManager const&, mongo::Shard const&) const

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Chunk::ShouldAutoSplit

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ChunkRangeManager::reloadAll(std::map<mongo::BSONObj, boost::shared_ptr<mongo::Chunk const>, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, boost::shared_ptr<mongo::Chunk const> > > > const&)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::ChunkManager(boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::ChunkManager()

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

<div></div>

    mongo::Chunk::Chunk(mongo::ChunkManager const*, mongo::BSONObj const&, mongo::BSONObj const&, mongo::Shard const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

<div></div>

    mongo::Chunk::setMaxChunkSizeSizeMB(int)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Chunk::genID(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

<div></div>

    mongo::ChunkManager::getVersion() const

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

### src/mongo/s/cluster\_client\_internal.cpp

<div></div>

    mongo::checkClusterMongoVersions(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/cluster\_write.cpp

<div></div>

    mongo::clusterDelete(std::string const&, mongo::BSONObj const&, int, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::ClusterWriterStats::hasShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClusterWriterStats::getShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::clusterCreateIndex(std::string const&, mongo::BSONObj, bool, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::ClusterWriter::ClusterWriter(bool, int)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClusterWriter::getStats()

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::clusterInsert(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::clusterUpdate(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

### src/mongo/s/commands\_admin.cpp

<div></div>

    mongo::CmdShutdown::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/db/commands/shutdown.cpp](../database\_commands)

<div></div>

    mongo::CmdShutdown::run(std::string const&, mongo::BSONObj&, int, std::string&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/commands/shutdown.cpp](../database\_commands)

### src/mongo/s/config.cpp

<div></div>

    mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::configServer

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::serverID

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ConfigServer::reloadSettings()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBConfig::getShard(std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ConfigServer::init(std::string const&)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ConfigServer::ok(bool)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBConfig::reload()

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ConfigServer::replicaSetChange(std::string const&, std::string const&)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/config\_server\_checker\_service.cpp

<div></div>

    mongo::startConfigServerChecker()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/cursors.cpp

<div></div>

    mongo::cursorCache

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::CursorCache::startTimeoutThread()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/d\_logic.cpp

<div></div>

    mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/s/d\_merge.cpp

<div></div>

    mongo::mergeChunks(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

### src/mongo/s/d\_migrate.cpp

<div></div>

    mongo::ShardingState::inCriticalMigrateSection()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ShardingState::waitTillNotInCriticalSection(int)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::logOpForSharding(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/s/d\_state.cpp

<div></div>

    mongo::ShardedConnectionInfo::addHook()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

<div></div>

    mongo::ShardingState::gotShardName(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

<div></div>

    mongo::shardingState

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ShardingState::resetMetadata(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::ShardingState::initialize(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

<div></div>

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ShardingState::setShardName(std::string const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ShardingState::needCollectionMetadata(std::string const&) const

- Used By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)

<div></div>

    mongo::ShardingState::getVersion(std::string const&) const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)

<div></div>

    mongo::ShardedConnectionInfo::get(bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ShardingState::refreshMetadataNow(std::string const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::shardVersionOk(std::string const&, std::string&, mongo::ChunkVersion&, mongo::ChunkVersion&)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ShardingState::resetShardingState()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/s/default\_version.cpp

<div></div>

    mongo::versionManager

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/grid.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Grid::setAllowLocalHost(bool)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::grid

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Grid::allowLocalHost() const

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/mongos\_persistence\_stubs.cpp

<div></div>

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/s/request.cpp

<div></div>

    mongo::Request::process(int)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Request::init()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/shard.cpp

<div></div>

    mongo::Shard::setAddress(mongo::ConnectionString const&)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ShardingConnectionHook

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Shard::_setAddr(std::string const&)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

### src/mongo/s/shard\_key\_pattern.cpp

<div></div>

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

### src/mongo/s/shardconnection.cpp

<div></div>

    mongo::ShardConnection::forgetNS(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ShardConnection::releaseMyConnections()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ShardConnection::_finishInit()

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::kill()

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::shardConnectionPool

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/shardkey.cpp

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

### src/mongo/s/strategy.cpp

<div></div>

    mongo::Strategy::commandOp(std::string const&, mongo::BSONObj const&, int, std::string const&, mongo::BSONObj const&, std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> >*)

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)

<div></div>

    mongo::STRATEGY

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)

### src/mongo/s/version\_manager.cpp

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::versionManager

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/version\_mongos.cpp

<div></div>

    mongo::printShardingVersionInfo(bool)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
