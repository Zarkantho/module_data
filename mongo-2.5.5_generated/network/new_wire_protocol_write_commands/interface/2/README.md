
# Interface

### src/mongo/s/write\_ops/batched\_command\_request.cpp

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_command\_response.cpp

<div></div>

    mongo::BatchedCommandResponse::getErrDetails() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_delete\_document.cpp

<div></div>

    mongo::BatchedDeleteDocument::setLimit(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_delete\_request.cpp

<div></div>

    mongo::BatchedDeleteRequest::BatchedDeleteRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedDeleteRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_insert\_request.cpp

<div></div>

    mongo::BatchedInsertRequest::BatchedInsertRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_update\_document.cpp

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setUpdateExpr(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setUpsert(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateDocument::setMulti(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/batched\_update\_request.cpp

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateRequest::BatchedUpdateRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedUpdateRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/wc\_error\_detail.cpp

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

### src/mongo/s/write\_ops/write\_error\_detail.cpp

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
