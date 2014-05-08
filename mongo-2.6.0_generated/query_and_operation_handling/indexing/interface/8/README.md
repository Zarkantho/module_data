
# Interface for 2d Indexes
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index/2d\_access\_method.cpp

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::TwoDAccessMethod::getKeys(mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
