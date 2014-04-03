
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/keypattern.cpp

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KeyPattern::keyBounds(mongo::FieldRangeSet const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::extendRangeBound(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::isSpecial() const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/exec/shard\_filter.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
