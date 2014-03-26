
# Interface for BSON Element Hasher
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/hasher.cpp

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Used By:

    - [src/mongo/db/commands/hashcmd.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/keypattern.cpp](../../../queries/indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../queries/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
