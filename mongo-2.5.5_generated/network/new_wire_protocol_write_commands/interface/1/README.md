
# Interface

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::BatchSafeWriter::safeWriteBatch(mongo::DBClientBase*, mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::enforceLegacyWriteConcern(mongo::MultiCommandDispatch*, mongo::StringData const&, mongo::BSONObj const&, std::map<mongo::ConnectionString, mongo::HostOpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::HostOpTime> > > const&, std::vector<mongo::LegacyWCResponse, std::allocator<mongo::LegacyWCResponse> >*)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_upconvert.cpp

<div></div>

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

### src/mongo/s/write\_ops/batch\_write\_exec.cpp

<div></div>

    mongo::BatchWriteExec::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchWriteExec::BatchWriteExec(mongo::NSTargeter*, mongo::ShardResolver*, mongo::MultiCommandDispatch*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::BatchWriteExec::releaseStats()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/config\_coordinator.cpp

<div></div>

    mongo::ConfigCoordinator::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*, bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

<div></div>

    mongo::ConfigCoordinator::ConfigCoordinator(mongo::MultiCommandDispatch*, std::vector<mongo::ConnectionString, std::allocator<mongo::ConnectionString> > const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../sharding)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

<div></div>

    vtable for mongo::DBClientSafeWriter

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
