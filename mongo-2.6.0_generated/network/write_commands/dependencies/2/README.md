
# Interface for Batch Executor
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/commands/write\_commands/batch\_executor.cpp

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::BatchedCommandResponse::setNModified(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::anyReplEnabled()

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::UpdateExecutor::execute()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, mongo::CollectionOptions const&, bool, bool)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DeleteExecutor::execute()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::ShardingState::inCriticalMigrateSection()

- Provided By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::UpdateExecutor::~UpdateExecutor()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::BatchedCommandRequest::getIndexKeyPattern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ErrorCodes::isInterruption(mongo::ErrorCodes::Error)

- Provided By:

    - [build/darwin/ssl/mongo/base/error\_codes.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::UpdateExecutor::UpdateExecutor(mongo::UpdateRequest const*, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::WriteErrorDetail::isErrInfoSet() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::GeneratorHolder::getInstance()

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::UpdateExecutor::prepare()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::sleepmicros(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::DeleteExecutor::~DeleteExecutor()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool, mongo::PregeneratedKeys const*)

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::WCErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)

<div></div>

    mongo::BatchedRequestMetadata::getShardVersion() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandRequest::getMetadata() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteConcernOptions::Acknowledged

- Provided By:

    - [src/mongo/db/write\_concern\_options.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ShardingState::waitTillNotInCriticalSection(int)

- Provided By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedRequestMetadata::isShardVersionSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrInfo() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/write\_concern\_options.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedCommandResponse::setElectionId(mongo::OID const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::setUpsertDetails(std::vector<mongo::BatchedUpsertDetail*, std::allocator<mongo::BatchedUpsertDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setLastOp(mongo::OpTime)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Lock::ScopedLock::recordTime()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::GeneratorHolder::prepare(mongo::StringData const&, mongo::BSONObj const&, mongo::PregeneratedKeys*)

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::setErrDetails(std::vector<mongo::WriteErrorDetail*, std::allocator<mongo::WriteErrorDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::DeleteExecutor::prepare()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::DeleteExecutor::DeleteExecutor(mongo::DeleteRequest const*)

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::validateWriteConcern(mongo::WriteConcernOptions const&)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::BatchedCommandRequest::isMetadataSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::kMaxWriteBatchSize

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::getShardName() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isUniqueIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::CurOp::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::ScopedLock::resetTime()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::ShardingState::setShardName(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CurOp::enter(mongo::Client::Context*)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BatchedCommandRequest::isValidIndexRequest(std::string*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
