
# Interface for Write Commands Response Schema
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batched\_command\_response.cpp

<div></div>

    mongo::BatchedCommandResponse::setWriteConcernError(mongo::WCErrorDetail*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getUpsertDetails() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getErrDetails() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BatchedCommandResponse::setElectionId(mongo::OID const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::isErrDetailsSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setErrDetails(std::vector<mongo::WriteErrorDetail*, std::allocator<mongo::WriteErrorDetail*> > const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setN(long long)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::sizeUpsertDetails() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::isLastOpSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setOk(int)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setErrCode(int)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::addToErrDetails(mongo::WriteErrorDetail*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getN() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getErrCode() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BatchedCommandResponse::isWriteConcernErrorSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BatchedCommandResponse::sizeErrDetails() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::addToUpsertDetails(mongo::BatchedUpsertDetail*)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getErrMessage() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BatchedCommandResponse::setUpsertDetails(std::vector<mongo::BatchedUpsertDetail*, std::allocator<mongo::BatchedUpsertDetail*> > const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getLastOp() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::BatchedCommandResponse::getElectionId() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::isElectionIdSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getWriteConcernError() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BatchedCommandResponse::setNModified(long long)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::isUpsertDetailsSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::cloneTo(mongo::BatchedCommandResponse*) const

- Used By:

    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::setLastOp(mongo::OpTime)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedCommandResponse::getNModified() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
