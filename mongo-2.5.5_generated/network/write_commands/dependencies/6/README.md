
# Interface for Write Commands Downconvert
This dependency information represents symbolsthat are used in this group but defined in other modules.  Does not includesymbols used in this group that are defined inside this module.

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::sizeErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::WCErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedCommandResponse::addToUpsertDetails(mongo::BatchedUpsertDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setLastOp(mongo::OpTime)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../utilities/utilities)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson/bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

### src/mongo/s/write\_ops/batch\_downconvert\_test.cpp

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::sizeErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::getUpsertDetailsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::isUpsertDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedInsertRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrDetailsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getLastOp() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::getErrInfo() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../../../bson/bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getUpsertedID() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../network/write\_command\_schema)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../../../sharding/sharding)
    - [src/mongo/s/default\_version.cpp](../../../sharding/sharding)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../../../sharding/sharding)
    - [src/mongo/s/default\_version.cpp](../../../sharding/sharding)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities/utilities)
