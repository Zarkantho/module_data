
# Interface for Btree Datastructure
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/structure/btree/btree.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::asVersion(mongo::Record*)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::asVersion(mongo::Record*)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)

### src/mongo/db/structure/btree/btreebuilder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

### src/mongo/db/structure/btree/key.cpp

<div></div>

    mongo::KeyV1::dataSize() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::woEqual(mongo::KeyV1 const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::toBson() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
