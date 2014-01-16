# new\_wire\_protocol\_write\_commands

# Module Groups

-------------

# Group Description
New write commands for new wire protocol. The new "write commands" are all actual Commands run  using "db.$cmd.findOne(...)". The reason for this is that the old wire protocol didn't have  acknowledgements for anything BUT queries (which include commands), so everything is now a query  so we can get acknowledgements for writes (and not just for queries).

# Files
- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h

# Interface
(not used outside this module)

-------------

# Group Description
New wire protocol writes (in mongos)

# Files
- src/mongo/s/commands/cluster\_write\_cmd.cpp   (mongos)
- src/mongo/s/write\_ops/batch\_downconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_downconvert.h
- src/mongo/s/write\_ops/batch\_downconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_upconvert.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_upconvert.h
- src/mongo/s/write\_ops/batch\_upconvert\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_exec.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_exec.h
- src/mongo/s/write\_ops/batch\_write\_exec\_test.cpp   ()
- src/mongo/s/write\_ops/batch\_write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batch\_write\_op.h
- src/mongo/s/write\_ops/batch\_write\_op\_test.cpp   ()
- src/mongo/s/write\_ops/config\_coordinator.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/config\_coordinator.h
- src/mongo/s/write\_ops/config\_coordinator\_test.cpp   ()
- src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/dbclient\_safe\_writer.h
- src/mongo/s/write\_ops/write\_op.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_op.h
- src/mongo/s/write\_ops/write\_op\_test.cpp   ()

# Interface

### src/mongo/s/write\_ops/batch\_downconvert.cpp

    mongo::BatchSafeWriter::safeWriteBatch(mongo::DBClientBase*, mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_upconvert.cpp

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_write\_exec.cpp

    mongo::BatchWriteExec::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchWriteExec::BatchWriteExec(mongo::NSTargeter*, mongo::ShardResolver*, mongo::MultiCommandDispatch*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchWriteExec::releaseStats()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/config\_coordinator.cpp

    mongo::ConfigCoordinator::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*, bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::ConfigCoordinator::ConfigCoordinator(mongo::MultiCommandDispatch*, std::vector<mongo::ConnectionString, std::allocator<mongo::ConnectionString> > const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

    vtable for mongo::DBClientSafeWriter

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

-------------

# Group Description
New wire protocol writes (in mongod)   why are these in s/ ?

# Files
- src/mongo/s/write\_ops/batched\_command\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_request.h
- src/mongo/s/write\_ops/batched\_command\_response.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_response.h
- src/mongo/s/write\_ops/batched\_command\_response\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_delete\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_document.h
- src/mongo/s/write\_ops/batched\_delete\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request.h
- src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_insert\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_insert\_request.h
- src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_request\_metadata.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_request\_metadata.h
- src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_update\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_document.h
- src/mongo/s/write\_ops/batched\_update\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request.h
- src/mongo/s/write\_ops/batched\_update\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_upsert\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_upsert\_detail.h
- src/mongo/s/write\_ops/wc\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/wc\_error\_detail.h
- src/mongo/s/write\_ops/write\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_error\_detail.h

# Interface

### src/mongo/s/write\_ops/batched\_command\_request.cpp

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandRequest::getNS() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandRequest::getTargetingNS() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandRequest::isWriteConcernSet() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    vtable for mongo::BatchedCommandRequest

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandRequest::isInsertIndexRequest() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandRequest::sizeWriteOps() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandRequest::getOrdered() const

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandRequest::isVerboseWC() const

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_command\_response.cpp

    mongo::BatchedCommandResponse::setN(long long)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandResponse::setOk(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandResponse::setErrCode(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::BatchedCommandResponse::getN() const

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedCommandResponse::toBSON() const

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_delete\_document.cpp

    mongo::BatchedDeleteDocument::setLimit(int)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedDeleteDocument::getLimit() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

    mongo::BatchedDeleteDocument::BatchedDeleteDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedDeleteDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_delete\_request.cpp

    mongo::BatchedDeleteRequest::BatchedDeleteRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedDeleteRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_insert\_request.cpp

    mongo::BatchedInsertRequest::BatchedInsertRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_update\_document.cpp

    mongo::BatchedUpdateDocument::getUpdateExpr() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

    mongo::BatchedUpdateDocument::BatchedUpdateDocument()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateDocument::getMulti() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

    mongo::BatchedUpdateDocument::setUpdateExpr(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateDocument::setUpsert(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateDocument::getUpsert() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

    mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateDocument::getQuery() const

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

    mongo::BatchedUpdateDocument::setMulti(bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/batched\_update\_request.cpp

    mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateRequest::BatchedUpdateRequest()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

    mongo::BatchedUpdateRequest::setWriteConcern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

-------------

# Group Description
Header to enumerate the wire protocol version, along with the max and min supported versions   can you say a bit about who exactly cares (which components) about wire protocol version?

# Files
- src/mongo/db/wire\_version.h

# Interface
(not used outside this module)
