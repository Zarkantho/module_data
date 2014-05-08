
# Interface for Document Iterators
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/matcher/path.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    typeinfo for mongo::ElementIterator

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::ElementPath::init(mongo::StringData const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
