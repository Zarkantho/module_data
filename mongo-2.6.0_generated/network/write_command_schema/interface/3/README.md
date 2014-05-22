
# Interface for Write Commands Operation Metadata
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batched\_request\_metadata.cpp

<div></div>

    mongo::BatchedRequestMetadata::BatchedRequestMetadata()

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::setShardVersion(mongo::ChunkVersion const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::isShardVersionSet() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::getShardName() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::getShardVersion() const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::setShardName(mongo::StringData const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)

<div></div>

    mongo::BatchedRequestMetadata::setSession(long long)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
