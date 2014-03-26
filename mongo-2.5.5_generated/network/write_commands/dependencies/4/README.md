
# Dependencies

### src/mongo/s/commands/cluster\_write\_cmd.cpp

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::ClusterWriterStats::hasShardStats() const

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::ClusterWriterStats::getShardStats() const

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::ClientInfo::exists()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientInfo::addHostOpTimes(std::map<mongo::ConnectionString, mongo::HostOpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::HostOpTime> > > const&)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::ClusterWriter::getStats()

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::ClusterWriter::ClusterWriter(bool, int)

- Provided By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

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

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../startup\_initialization)

### src/mongo/s/write\_ops/batch\_write\_exec.cpp

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::isErrInfoSet() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrInfo() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::BatchedCommandResponse::getLastOp() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::getElectionId() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../logging\_system)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isElectionIdSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isLastOpSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

### src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::cloneTo(mongo::BatchedCommandResponse*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

### src/mongo/s/write\_ops/batch\_write\_op.cpp

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setNModified(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setSession(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedRequestMetadata::BatchedRequestMetadata()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isOrderedSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setShardName(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getUpsertDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isUpsertDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::cloneTo(mongo::BatchedUpdateDocument*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::getErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::cloneTo(mongo::BatchedDeleteDocument*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setUpsertDetails(std::vector<mongo::BatchedUpsertDetail*, std::allocator<mongo::BatchedUpsertDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::cloneTo(mongo::WCErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setShardVersion(mongo::ChunkVersion const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::~WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::setMetadata(mongo::BatchedRequestMetadata*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getNModified() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::sizeUpsertDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getUpsertedID() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../write\_command\_schema)

### src/mongo/s/write\_ops/batch\_write\_op\_test.cpp

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::sizeErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

### src/mongo/s/write\_ops/write\_op.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

### src/mongo/s/write\_ops/write\_op\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrInfo() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)
