
# Dependencies

### src/mongo/db/commands/write\_commands/write\_commands.cpp

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../startup\_initialization)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../utilities)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::getLastErrorDefault

- Provided By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::setLastError(int, char const*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

### src/mongo/db/commands/write\_commands/batch\_executor.cpp

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)

<div></div>

    mongo::BatchedCommandResponse::setNModified(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::anyReplEnabled()

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)

<div></div>

    mongo::ShardingState::inCriticalMigrateSection()

- Provided By:

    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getIndexKeyPattern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::isErrInfoSet() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../../../logging\_system)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../../../journaling)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../../../replication)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)

<div></div>

    mongo::BatchedRequestMetadata::getShardVersion() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandRequest::getMetadata() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::ShardingState::waitTillNotInCriticalSection(int)

- Provided By:

    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedRequestMetadata::isShardVersionSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrInfo() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/write\_concern\_options.cpp](../../../replication)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedCommandResponse::setElectionId(mongo::OID const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::setUpsertDetails(std::vector<mongo::BatchedUpsertDetail*, std::allocator<mongo::BatchedUpsertDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)

<div></div>

    mongo::BatchedCommandResponse::setLastOp(mongo::OpTime)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::setErrDetails(std::vector<mongo::WriteErrorDetail*, std::allocator<mongo::WriteErrorDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::validateWriteConcern(mongo::WriteConcernOptions const&)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../../../replication)

<div></div>

    mongo::BatchedCommandRequest::isMetadataSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ShardingState::setShardName(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)

<div></div>

    mongo::BatchedRequestMetadata::getShardName() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isUniqueIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::CurOp::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../startup\_initialization)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)

### src/mongo/db/commands/write\_commands/write\_commands\_common.cpp

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../../../authorization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedCommandRequest::containsUpserts(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ActionType::update

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../../../authorization)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../../../authorization)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../../../authorization)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../authorization)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../authorization)

<div></div>

    mongo::BatchedCommandRequest::getIndexedNS(mongo::BSONObj const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../wire\_protocol\_write\_command\_schema)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../../../authorization)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../authorization)
