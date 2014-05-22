
# Interface for Index Legacy Exceptions
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index\_legacy.cpp

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::getMissingField(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
