
# Dependencies for Mongos Write Commands Lifecycle Tracking
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/write\_ops/batch\_write\_op.cpp

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setNModified(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setSession(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedRequestMetadata::BatchedRequestMetadata()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isOrderedSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setShardName(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getUpsertDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isUpsertDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::cloneTo(mongo::BatchedUpdateDocument*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::getErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::cloneTo(mongo::BatchedDeleteDocument*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setUpsertDetails(std::vector<mongo::BatchedUpsertDetail*, std::allocator<mongo::BatchedUpsertDetail*> > const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::cloneTo(mongo::WCErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedRequestMetadata::setShardVersion(mongo::ChunkVersion const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::~WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandRequest::setMetadata(mongo::BatchedRequestMetadata*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getNModified() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::sizeUpsertDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpsertDetail::getUpsertedID() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

### src/mongo/s/write\_ops/batch\_write\_op\_test.cpp

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::setLimit(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::sizeErrDetails() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MINKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::MAXKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrDetailsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

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

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::setMulti(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

### src/mongo/s/write\_ops/write\_op.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)

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

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

### src/mongo/s/write\_ops/write\_op\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::LT

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MINKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)

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

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::MAXKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::rangeOverlaps(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../../network/write\_command\_schema)
