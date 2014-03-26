
# Interface

### src/mongo/s/write\_ops/batch\_upconvert.cpp

<div></div>

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
