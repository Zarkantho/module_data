
# Interface for Replica Set Sync and Initial Sync
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/rs\_sync.cpp

<div></div>

    mongo::replset::SyncTail::SyncTail(mongo::replset::BackgroundSyncInterface*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::replset::InitialSync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::InitialSync::InitialSync(mongo::replset::BackgroundSyncInterface*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::InitialSync::oplogApplication(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::multiInitialSyncApply(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::replset::SyncTail*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::InitialSync::~InitialSync()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::SyncTail::oplogApplication()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::SyncTail::syncApply(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

### src/mongo/db/repl/sync.cpp

<div></div>

    vtable for mongo::Sync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::Sync

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Sync::shouldRetry(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Sync::getMissingDoc(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
