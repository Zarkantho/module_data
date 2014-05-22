
# Interface for Write Commands Request Schema Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batched\_command\_request.cpp

<div></div>

    mongo::BatchedCommandRequest::isVerboseWC() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isMetadataSet() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isValid(std::string*) const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getBatchType() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::toString() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::getUpdateRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::kMaxWriteBatchSize

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::containsUpserts(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getDeleteRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::setMetadata(mongo::BatchedRequestMetadata*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getIndexKeyPattern() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::setOrdered(bool)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getIndexedNS(mongo::BSONObj const&, std::string*, std::string*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isUniqueIndexRequest() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::cloneTo(mongo::BatchedCommandRequest*) const

- Used By:

    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::isValidIndexRequest(std::string*) const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::isOrderedSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getInsertRequest() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getWriteConcern() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getTargetingNS() const

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)

<div></div>

    mongo::BatchedCommandRequest::getMetadata() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandRequest::getOrdered() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
