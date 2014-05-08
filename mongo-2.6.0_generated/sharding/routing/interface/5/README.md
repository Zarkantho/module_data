
# Interface for Shard Key Management
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/shard\_key\_pattern.cpp

<div></div>

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

### src/mongo/s/shardkey.cpp

<div></div>

    mongo::ShardKeyPattern::toString() const

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardKeyPattern::hasShardKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardKeyPattern::isUniqueIndexCompatible(mongo::KeyPattern const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
