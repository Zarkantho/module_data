
# Interface for Hashed Indexes
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index/hash\_access\_method.cpp

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index/hash\_key\_generator.cpp

<div></div>

    mongo::HashKeyGenerator::HashKeyGenerator(std::string const&, int, int, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::HashKeyGenerator::makeSingleHashKey(mongo::BSONElement const&, int, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::HashKeyGenerator::getKeys(mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*) const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::HashKeyGenerator

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
