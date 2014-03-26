
# Interface

### src/mongo/s/write\_ops/batched\_command\_request.cpp

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::containsUpserts(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::cloneTo(mongo::BatchedCommandRequest*) const

- Used By:

    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::isMetadataSet() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isOrderedSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getMetadata() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getIndexKeyPattern() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isValid(std::string*) const

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::setMetadata(mongo::BatchedRequestMetadata*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::BatchedCommandRequest::getIndexedNS(mongo::BSONObj const&, std::string*, std::string*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isUniqueIndexRequest() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
