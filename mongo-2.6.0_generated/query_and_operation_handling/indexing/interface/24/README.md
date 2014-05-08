
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/keypattern.cpp

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KeyPattern::keyBounds(mongo::FieldRangeSet const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::extendRangeBound(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyPattern::isSpecial() const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
