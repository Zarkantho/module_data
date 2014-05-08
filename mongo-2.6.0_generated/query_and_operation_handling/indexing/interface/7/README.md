
# Interface for Btree Indexes
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index/btree\_access\_method.cpp

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index/btree\_key\_generator.cpp

<div></div>

    mongo::BtreeKeyGeneratorV1::BtreeKeyGeneratorV1(std::vector<char const*, std::allocator<char const*> >, std::vector<mongo::BSONElement, std::allocator<mongo::BSONElement> >, bool)

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BtreeKeyGenerator::ParallelArraysCode

- Used By:

    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
