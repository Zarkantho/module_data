
# Interface for Lock State
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/lockstate.cpp

<div></div>

    mongo::LockState::LockState()

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Acquiring::~Acquiring()

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LockState::hasAnyReadLock() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LockState::reportState(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Acquiring::Acquiring(mongo::Lock::ScopedLock*, mongo::LockState&)

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LockState::Dump()

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)

<div></div>

    mongo::LockState::hasAnyWriteLock() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LockState::reportState()

- Used By:

    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
