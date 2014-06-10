
# Dependencies for Mongos Request Handling Implementation
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/request.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::CursorCache::gotKillCursors(mongo::Message&)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ClientInfo::newPeerRequest(mongo::HostAndPort const&)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::AuthorizationSession::startRequest()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::OpCounters::gotOp(int, bool)

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CursorCache::getRef(long long) const

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ClientInfo::newRequest()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

### src/mongo/s/strategy.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ShardedClientCursor::accessed()

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/default\_version.cpp](../../../../sharding/metadata\_versioning)

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardedClientCursor::getId()

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ParallelSortClusteredCursor::explain(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CursorCache::getMaxTimeMS(long long) const

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/default\_version.cpp](../../../../sharding/metadata\_versioning)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::CursorCache::removeRef(long long)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ShardConnection::~ShardConnection()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ShardedClientCursor::sendNextBatch(mongo::Request&, int, mongo::_BufBuilder<mongo::TrivialAllocator>&, int&)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Provided By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ShardedClientCursor::getTotalSent() const

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ShardConnection::done()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ActionType::inprog

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Query::ReadPrefField

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Shard::reset(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ParallelSortClusteredCursor::isSharded()

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Query::isExplain() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Query::getFilter() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ActionType::killop

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::CursorCache::remove(long long)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Command::runAgainstRegistered(char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, int)

- Provided By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::CursorCache::store(boost::shared_ptr<mongo::ShardedClientCursor>, int)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientCursor::peekFirst()

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Provided By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ShardedClientCursor::ShardedClientCursor(mongo::QueryMessage&, mongo::ParallelSortClusteredCursor*)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::CursorCache::get(long long) const

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::audit::logQueryAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::audit::logInProgAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::ShardedClientCursor::INIT_REPLY_BUFFER_SIZE

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::CursorCache::updateMaxTimeMS(long long, int)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::CursorCache::getRef(long long) const

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ParallelSortClusteredCursor::init()

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::ShardConnection::_finishInit()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ParallelSortClusteredCursor::getPrimary()

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::audit::logGetMoreAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../../../../bson/bson)

<div></div>

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::audit::logKillOpAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::ShardConnection::checkMyConnectionVersions(std::string const&)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
