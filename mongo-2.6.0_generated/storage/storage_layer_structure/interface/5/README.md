
# Interface for Namespace Details
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/structure/catalog/namespace\_details.cpp

<div></div>

    mongo::bucketSizes

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceDetails::quantizeAllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::idx(int, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::writingWithExtra()

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceDetails::getRecordAllocationSize(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::NamespaceDetails::setPaddingFactor(double)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceDetails::clearUserFlag(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceDetails::setIndexIsMultikey(int, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceDetails::alloc(mongo::Collection*, mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
