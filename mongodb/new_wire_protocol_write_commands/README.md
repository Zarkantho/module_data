# new\_wire\_protocol\_write\_commands

# Module Groups

-------------

# Group Description
New write commands for new wire protocol. The new "write commands" are all actual Commands run  using "db.$cmd.findOne(...)". The reason for this is that the old wire protocol didn't have  acknowledgements for anything BUT queries (which include commands), so everything is now a query  so we can get acknowledgements for writes (and not just for queries).

# Files
- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/commands/write\_commands/write\_commands.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::getLastErrorDefault

- Provided By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::CurOp::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::setLastError(int, char const*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

### src/mongo/db/commands/write\_commands/batch\_executor.cpp

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::anyReplEnabled()

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../sharding)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ShardingState::setShardName(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../query\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/write\_commands/write\_commands\_common.cpp

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

-------------

# Group Description
New wire protocol writes (in mongos)

# Files
- src/mongo/s/commands/cluster\_write\_cmd.cpp   (mongos)
- src/mongo/s/write\_ops/batch\_downconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert.h
- src/mongo/s/write\_ops/batch\_downconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_upconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert.h
- src/mongo/s/write\_ops/batch\_upconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_exec.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.h
- src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op.h
- src/mongo/s/write\_ops/batch\_write\_op\_test.cpp   ()
- src/mongo/s/write\_ops/config\_coordinator.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator.h
- src/mongo/s/write\_ops/config\_coordinator\_test.cpp   ()
- src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/dbclient\_safe\_writer.h
- src/mongo/s/write\_ops/write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op.h
- src/mongo/s/write\_ops/write\_op\_test.cpp   ()

# Interface

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::BatchSafeWriter::safeWriteBatch(mongo::DBClientBase*, mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_upconvert.cpp

<div></div>

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_write\_exec.cpp

<div></div>

    mongo::BatchWriteExec::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchWriteExec::BatchWriteExec(mongo::NSTargeter*, mongo::ShardResolver*, mongo::MultiCommandDispatch*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchWriteExec::releaseStats()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/config\_coordinator.cpp

<div></div>

    mongo::ConfigCoordinator::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*, bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ConfigCoordinator::ConfigCoordinator(mongo::MultiCommandDispatch*, std::vector<mongo::ConnectionString, std::allocator<mongo::ConnectionString> > const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

<div></div>

    vtable for mongo::DBClientSafeWriter

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

# Dependencies

### src/mongo/s/commands/cluster\_write\_cmd.cpp

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ClusterWriterStats::hasShardStats() const

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ClusterWriterStats::getShardStats() const

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ClientInfo::exists()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ClusterWriter::getStats()

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ClusterWriter::ClusterWriter(bool, int)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ClientInfo::addHostOpTimes(std::map<mongo::ConnectionString, mongo::OpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::OpTime> > > const&)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batch\_downconvert\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/s/write\_ops/batch\_upconvert.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/s/write\_ops/batch\_upconvert\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batch\_write\_exec.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

### src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/s/write\_ops/batch\_write\_op.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

### src/mongo/s/write\_ops/batch\_write\_op\_test.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/s/write\_ops/config\_coordinator.cpp

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/config\_coordinator\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/s/write\_ops/write\_op.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/write\_op\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../sharding)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
New wire protocol writes (in mongod)   why are these in s/ ?

# Files
- src/mongo/s/write\_ops/batched\_command\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_request.h
- src/mongo/s/write\_ops/batched\_command\_response.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_response.h
- src/mongo/s/write\_ops/batched\_command\_response\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_delete\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_document.h
- src/mongo/s/write\_ops/batched\_delete\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request.h
- src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_insert\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_insert\_request.h
- src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_request\_metadata.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_request\_metadata.h
- src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_update\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_document.h
- src/mongo/s/write\_ops/batched\_update\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request.h
- src/mongo/s/write\_ops/batched\_update\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_upsert\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_upsert\_detail.h
- src/mongo/s/write\_ops/wc\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/wc\_error\_detail.h
- src/mongo/s/write\_ops/write\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_error\_detail.h

# Interface

### src/mongo/s/write\_ops/batched\_command\_request.cpp

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_command\_response.cpp

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_delete\_document.cpp

<div></div>

    mongo::BatchedDeleteDocument::setLimit(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_delete\_request.cpp

<div></div>

    mongo::BatchedDeleteRequest::BatchedDeleteRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedDeleteRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_insert\_request.cpp

<div></div>

    mongo::BatchedInsertRequest::BatchedInsertRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_update\_document.cpp

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setUpdateExpr(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setUpsert(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setMulti(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_update\_request.cpp

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateRequest::BatchedUpdateRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchedUpdateRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

# Dependencies

### src/mongo/s/write\_ops/batched\_command\_request.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_command\_response.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OpTime> const&, mongo::OpTime*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_command\_response\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_delete\_document.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_delete\_request.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_insert\_request.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_request\_metadata.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_update\_document.cpp

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_update\_request.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_update\_request\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/batched\_upsert\_detail.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extractID(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/wc\_error\_detail.cpp

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/s/write\_ops/write\_error\_detail.cpp

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Header to enumerate the wire protocol version, along with the max and min supported versions   can you say a bit about who exactly cares (which components) about wire protocol version?

# Files
- src/mongo/db/wire\_version.h

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)
