
# Interface for Collection Metadata
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/collection\_metadata.cpp

<div></div>

    mongo::CollectionMetadata::getMinKey() const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::CollectionMetadata::keyIsPending(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
