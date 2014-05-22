
# Interface for Write Commands Upconvert
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batch\_upconvert.cpp

<div></div>

    mongo::batchErrorToLastError(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse const&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::msgToBatchRequests(mongo::Message const&, std::vector<mongo::BatchedCommandRequest*, std::allocator<mongo::BatchedCommandRequest*> >*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
