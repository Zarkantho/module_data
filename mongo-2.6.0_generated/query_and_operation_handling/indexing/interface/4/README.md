
# Interface for Btree Index Cursor
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index/btree\_index\_cursor.cpp

<div></div>

    mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::BtreeIndexCursor::seek(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/count.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::BtreeIndexCursor::pointsAt(mongo::BtreeIndexCursor const&)

- Used By:

    - [src/mongo/db/exec/count.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../core\_query\_system/query\_execution)
