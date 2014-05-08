
# Interface for Collection Metadata
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/collection\_metadata.cpp

<div></div>

    mongo::CollectionMetadata::getNextChunk(mongo::BSONObj const&, mongo::ChunkType*) const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CollectionMetadata::getMinKey() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::CollectionMetadata::keyIsPending(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
