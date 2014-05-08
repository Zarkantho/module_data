
# Interface for Cluster Management Utilities
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/cluster\_client\_internal.cpp

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::clusterInsert(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::CollectionType::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ShardType::~ShardType()

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChangelogType::~ChangelogType()

- Provided By:

    - [src/mongo/s/type\_changelog.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChangelogType::ChangelogType()

- Provided By:

    - [src/mongo/s/type\_changelog.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ShardType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ShardType::ShardType()

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteConcernOptions::AllConfigs

- Provided By:

    - [src/mongo/db/write\_concern\_options.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::ChangelogType::toBSON() const

- Provided By:

    - [src/mongo/s/type\_changelog.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MongosType::mongoVersion

- Provided By:

    - [src/mongo/s/type\_mongos.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChangelogType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_changelog.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::terseCurrentTime(bool)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ShardType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ShardType::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::~ChunkType()

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

    mongo::ChunkType::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::ns

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::MongosType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_mongos.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::ChunkType()

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::MongosType::~MongosType()

- Provided By:

    - [src/mongo/s/type\_mongos.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::getHostNameCached()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::CollectionType::dropped

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::CollectionType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MongosType::MongosType()

- Provided By:

    - [src/mongo/s/type\_mongos.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::MongosType::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/type\_mongos.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::CollectionType::~CollectionType()

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::CollectionType::CollectionType()

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)
