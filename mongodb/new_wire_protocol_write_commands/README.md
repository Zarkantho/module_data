# new\_wire\_protocol\_write\_commands

# Module Groups

-------------

New write commands for new wire protocol. The new "write commands" are all actual Commands run  using "db.$cmd.findOne(...)". The reason for this is that the old wire protocol didn't have  acknowledgements for anything BUT queries (which include commands), so everything is now a query  so we can get acknowledgements for writes (and not just for queries).

- src/mongo/db/commands/write\_commands/write\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/write\_commands.h
- src/mongo/db/commands/write\_commands/batch\_executor.cpp   (mongod, tools)
- src/mongo/db/commands/write\_commands/batch\_executor.h
- src/mongo/db/commands/write\_commands/write\_commands\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/write\_commands/write\_commands\_common.h

## Interface

-------------

New wire protocol writes (in mongos)

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

## Interface
### src/mongo/s/write\_ops/batch\_downconvert.cpp
<pre>mongo::BatchSafeWriter::safeWriteBatch(mongo::DBClientBase*, mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)</pre>
#### Used By:
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
### src/mongo/s/write\_ops/batch\_upconvert.cpp
<pre>mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)
### src/mongo/s/write\_ops/batch\_write\_exec.cpp
<pre>mongo::BatchWriteExec::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchWriteExec::BatchWriteExec(mongo::NSTargeter*, mongo::ShardResolver*, mongo::MultiCommandDispatch*)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchWriteExec::releaseStats()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/config\_coordinator.cpp
<pre>mongo::ConfigCoordinator::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*, bool)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::ConfigCoordinator::ConfigCoordinator(mongo::MultiCommandDispatch*, std::vector<mongo::ConnectionString, std::allocator<mongo::ConnectionString> > const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp
<pre>vtable for mongo::DBClientSafeWriter</pre>
#### Used By:
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

-------------

New wire protocol writes (in mongod)   why are these in s/ ?

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

## Interface
### src/mongo/s/write\_ops/batched\_command\_request.cpp
<pre>mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)</pre>
#### Used By:
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)</pre>
#### Used By:
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::setWriteConcern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::getNS() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::getTargetingNS() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::isWriteConcernSet() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>vtable for mongo::BatchedCommandRequest</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::isInsertIndexRequest() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::sizeWriteOps() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::getOrdered() const</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::setNS(mongo::StringData const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandRequest::isVerboseWC() const</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_command\_response.cpp
<pre>mongo::BatchedCommandResponse::setN(long long)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::setOk(int)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::BatchedCommandResponse()</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::setErrCode(int)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::~BatchedCommandResponse()</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::getN() const</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::parseBSON(mongo::BSONObj const&, std::string*)</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::setErrMessage(mongo::StringData const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedCommandResponse::toBSON() const</pre>
#### Used By:
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_delete\_document.cpp
<pre>mongo::BatchedDeleteDocument::setLimit(int)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedDeleteDocument::getLimit() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<pre>mongo::BatchedDeleteDocument::BatchedDeleteDocument()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedDeleteDocument::setQuery(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedDeleteDocument::getQuery() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_delete\_request.cpp
<pre>mongo::BatchedDeleteRequest::BatchedDeleteRequest()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedDeleteRequest::addToDeletes(mongo::BatchedDeleteDocument*)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedDeleteRequest::setWriteConcern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_insert\_request.cpp
<pre>mongo::BatchedInsertRequest::BatchedInsertRequest()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedInsertRequest::addToDocuments(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_update\_document.cpp
<pre>mongo::BatchedUpdateDocument::getUpdateExpr() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::BatchedUpdateDocument()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::getMulti() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::setUpdateExpr(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::setUpsert(bool)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::getUpsert() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::setQuery(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::getQuery() const</pre>
#### Used By:
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<pre>mongo::BatchedUpdateDocument::setMulti(bool)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)
### src/mongo/s/write\_ops/batched\_update\_request.cpp
<pre>mongo::BatchedUpdateRequest::addToUpdates(mongo::BatchedUpdateDocument*)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateRequest::BatchedUpdateRequest()</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

<pre>mongo::BatchedUpdateRequest::setWriteConcern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/cluster\_write.cpp](../sharding)

-------------

Header to enumerate the wire protocol version, along with the max and min supported versions   can you say a bit about who exactly cares (which components) about wire protocol version?

- src/mongo/db/wire\_version.h

## Interface
