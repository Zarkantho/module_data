
# Interface for Mongos Public Commands
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/commands\_public.cpp

<div></div>

    mongo::ActionType::collStats

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    typeinfo for mongo::DocumentSource

- Provided By:

    - [src/mongo/db/pipeline/document\_source.cpp](../../../../core\_query\_system/aggregation\_framework)

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

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ActionType::dropDatabase

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../../security/authorization)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::ValueStorage::putDocument(mongo::Document const&)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ActionType::reIndex

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Future::CommandResult::join(int)

- Provided By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::Command::parseNsFullyQualified(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, bool, std::string const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/default\_version.cpp](../../../../sharding/metadata\_versioning)

<div></div>

    mongo::ShardConnection::~ShardConnection()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DocumentStorage::clone() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

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

    mongo::Pipeline::canRunInMongos() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::find_and_modify::addPrivilegesRequiredForFindAndModify(mongo::Command*, std::string const&, mongo::BSONObj const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ShardConnection::done()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../../security/authorization)

<div></div>

    mongo::Value::Value(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::DBConfig::getShard(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Command::parseResourcePattern(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::STRATEGY

- Provided By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::ActionType::repairDatabase

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Command::execCommandClientBasic(mongo::Command*, mongo::ClientBasic&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Provided By:

    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../../../../security/authorization)

<div></div>

    mongo::DBConfig::load()

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DocumentStorage::findField(mongo::StringData) const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ActionType::validate

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::Document::toBson() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::Chunk::MaxChunkSize

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Grid::removeDBIfExists(mongo::DBConfig const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::mr::addPrivilegesRequiredForMapReduce(mongo::Command*, std::string const&, mongo::BSONObj const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/commands/mr\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBConfig::removeSharding(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ActionType::createCollection

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::ActionType::dropCollection

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Pipeline::getInitialQuery() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::Shard::_setAddr(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ActionType::enableProfiler

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Pipeline::commandName

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ActionType::collMod

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    vtable for mongo::DocumentStorage

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::causedBy(std::exception const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Pipeline::serialize() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ActionType::splitVector

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Pipeline::splitForSharded()

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ValueStorage::putVector(mongo::RCVector const*)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ActionType::convertToCapped

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Command::stopIndexBuilds(mongo::Database*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ChunkManager::drop(boost::shared_ptr<mongo::ChunkManager const>) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBConfig::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ActionType::find

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Strategy::commandOp(std::string const&, mongo::BSONObj const&, int, std::string const&, mongo::BSONObj const&, std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> >*)

- Provided By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::DBConfig::dropDatabase(std::string&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ActionType::dropIndex

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::Chunk::splitIfShould(long) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Command::findCommand(std::string const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::_finishInit()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ActionType::dbStats

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::DBConfig::enableSharding(bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::InterruptStatusMongos::status

- Provided By:

    - [src/mongo/s/interrupt\_status\_mongos.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../../../../security/authorization)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DocumentStorage::appendField(mongo::StringData)

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::rename_collection::checkAuthForRenameCollectionCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::Chunk::ShouldAutoSplit

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    typeinfo for mongo::DocumentSourceOut

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::ChunkManager::getShardsForRange(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ActionType::compact

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::ChunkManager::hasShardKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Pipeline::stitch()

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
