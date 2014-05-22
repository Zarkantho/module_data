
# Interface for Btree Datastructure
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/structure/btree/key.cpp

<div></div>

    mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::woEqual(mongo::KeyV1 const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::dataSize() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KeyV1::toBson() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
