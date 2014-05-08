
# Interface for Find and getMore Entry Point
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/query/new\_find.cpp

<div></div>

    mongo::TypeExplain::getScanAndOrder() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::SingleSolutionRunner::SingleSolutionRunner(mongo::Collection const*, mongo::CanonicalQuery*, mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::ClientCursor::updateSlaveLocation(mongo::CurOp&)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::isScanAndOrderSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::setMaxTimeMicros(unsigned long long)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WorkingSetCommon::toStatusString(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/exec/working\_set\_common.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::TypeExplain::isNScannedObjectsSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CanonicalQuery::toString() const

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CanonicalQuery::canonicalize(mongo::QueryMessage const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::TypeExplain::isIDHackSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::CanonicalQuery::toStringShort() const

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::_runCommands(char const*, mongo::BSONObj&, mongo::_BufBuilder<mongo::TrivialAllocator>&, mongo::BSONObjBuilder&, bool, int)

- Provided By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::OplogStart::OplogStart(std::string const&, mongo::MatchExpression*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

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

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(mongo::Collection const*, long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ScopedRunnerRegistration::~ScopedRunnerRegistration()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ShardingState::getVersion(std::string const&) const

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::setMillis(long long)

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ScopedRunnerRegistration::ScopedRunnerRegistration(mongo::Runner*)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::replVerifyReadsOk(mongo::LiteParsedQuery const*)

- Provided By:

    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::CurOp::getRemainingMaxTimeMicros() const

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::TypeExplain::getIDHack() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::getHostNameCached()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ClientCursorPin::c() const

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::TypeExplain::setServer(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::verboseQueryLogging

- Provided By:

    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Collection const*, mongo::Runner*, int, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::setN(long long)

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ShardingState::needCollectionMetadata(std::string const&) const

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::isNScannedSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ClientCursor::setIdleTime(unsigned int)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
