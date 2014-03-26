
# Interface for Write Commands Request Schema
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batched\_delete\_document.cpp

<div></div>

    mongo::BatchedDeleteDocument::setLimit(int)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedDeleteDocument::getLimit() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedDeleteDocument::cloneTo(mongo::BatchedDeleteDocument*) const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedDeleteDocument::getQuery() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)

### src/mongo/s/write\_ops/batched\_delete\_request.cpp

<div></div>

    mongo::BatchedDeleteRequest::BatchedDeleteRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedDeleteRequest::getDeletesAt(unsigned long) const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedDeleteRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

### src/mongo/s/write\_ops/batched\_insert\_request.cpp

<div></div>

    mongo::BatchedInsertRequest::BatchedInsertRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedInsertRequest::getDocumentsAt(unsigned long) const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

### src/mongo/s/write\_ops/batched\_update\_document.cpp

<div></div>

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateDocument::cloneTo(mongo::BatchedUpdateDocument*) const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpdateDocument::getMulti() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpdateDocument::setUpdateExpr(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateDocument::setUpsert(bool)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateDocument::getUpsert() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateDocument::getQuery() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateDocument::setMulti(bool)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

### src/mongo/s/write\_ops/batched\_update\_request.cpp

<div></div>

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateRequest::getUpdatesAt(unsigned long) const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpdateRequest::BatchedUpdateRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

<div></div>

    mongo::BatchedUpdateRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding)

### src/mongo/s/write\_ops/batched\_upsert\_detail.cpp

<div></div>

    mongo::BatchedUpsertDetail::getIndex() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpsertDetail::setIndex(int)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpsertDetail::getUpsertedID() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpsertDetail::setUpsertedID(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedUpsertDetail::BatchedUpsertDetail()

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
