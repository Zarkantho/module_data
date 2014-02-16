
# Interface

### src/mongo/db/structure/catalog/namespace\_details.cpp

<div></div>

    mongo::bucketSizes

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::quantizeAllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::getRecordAllocationSize(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::idx(int, bool)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::writingWithExtra()

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::alloc(mongo::Collection*, mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::setPaddingFactor(double)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::clearUserFlag(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::setIndexIsMultikey(int, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
