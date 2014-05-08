
# Interface for Chunk Management
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/chunk.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Provided By:

    - [src/mongo/platform/random.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::clusterDelete(std::string const&, mongo::BSONObj const&, int, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::FieldRangeSet::universalRange() const

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChunkType::max

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ChunkType::min

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChunkType::jumbo

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::OrRangeGenerator::popOrClauseSingleKey()

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Shard::pick(mongo::Shard const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::Query::toString() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::KeyPattern::keyBounds(mongo::FieldRangeSet const&) const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)

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

    mongo::ChunkType::name

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CollectionType::DEPRECATED_lastmod

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::keyPattern

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ShardConnection::sync()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::serverID

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Provided By:

    - [src/mongo/platform/random.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::CollectionType::unique

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::Grid::shouldBalance(std::string const&, mongo::BSONObj*) const

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::WriteConcernOptions::AllConfigs

- Provided By:

    - [src/mongo/db/write\_concern\_options.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::ConfigServer::logChange(std::string const&, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ShardKeyPattern::toString() const

- Provided By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Shard::reloadShardInfo()

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::Shard::reset(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)

<div></div>

    mongo::Shard::_setAddr(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::KeyPattern::isSpecial() const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::CollectionType::ns

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::FieldRange::universal() const

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::ConfigServer::allUp()

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChunkType::DEPRECATED_lastmod

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::isConfigServerConsistent()

- Provided By:

    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::ChunkType::ns

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChunkType::shard

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

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

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Provided By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::FieldRangeSetPair::operator&=(mongo::FieldRangeSetPair const&)

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::OrRangeGenerator::OrRangeGenerator(char const*, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::SettingsType::chunksize

- Provided By:

    - [src/mongo/s/type\_settings.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardKeyPattern::hasShardKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)

<div></div>

    mongo::clusterUpdate(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::Grid::getConfigSetting(std::string const&) const

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ChunkType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::FieldRangeSet::getSpecial() const

- Provided By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
