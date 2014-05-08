
# Interface for BSON Element Hasher
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/hasher.cpp

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/hashcmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/hash\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
