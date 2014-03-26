
# Interface

### src/mongo/s/collection\_metadata.cpp

<div></div>

    mongo::CollectionMetadata::getMinKey() const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../core\_query\_system)

<div></div>

    mongo::CollectionMetadata::keyIsPending(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
