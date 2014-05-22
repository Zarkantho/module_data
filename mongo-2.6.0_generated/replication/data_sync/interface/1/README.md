
# Interface for Replica Set Sync and Initial Sync
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/rs\_sync.cpp

<div></div>

    mongo::GhostSync::associateSlave(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetImpl::blockSync(bool)

- Used By:

    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::InitialSync::InitialSync(mongo::replset::BackgroundSyncInterface*)

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

    mongo::ReplSetImpl::forceSyncFrom(std::string const&, std::string&, mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::GhostSync::updateSlave(mongo::OID const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::startSyncThread()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::SyncTail::oplogApplication()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::SyncTail::syncApply(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::GhostSync::clearCache()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::SyncTail::SyncTail(mongo::replset::BackgroundSyncInterface*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::InitialSync::oplogApplication(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::replset::InitialSync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::GhostSync

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

### src/mongo/db/repl/sync.cpp

<div></div>

    mongo::Sync::getMissingDoc(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::Sync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::Sync

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Sync::shouldRetry(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
