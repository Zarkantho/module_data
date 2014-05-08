
# Interface for Index Names
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index\_names.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::IndexNames::existedBefore24(std::string const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/haystack.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_2D

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::IndexNames::TEXT

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::isKnownName(std::string const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::nameToType(std::string const&)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexNames::HASHED

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::IndexNames::BTREE

- Used By:

    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
