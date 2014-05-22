
# Interface for Replica Set Background Sync Threads
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/bgsync.cpp

<div></div>

    mongo::replset::BackgroundSync::get()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    vtable for mongo::replset::BackgroundSyncInterface

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::BackgroundSync::producerThread()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::BackgroundSync::stopReplicationAndFlushBuffer()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::BackgroundSync::shutdown()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::replset::BackgroundSyncInterface::~BackgroundSyncInterface()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::replset::BackgroundSync::notifierThread()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    typeinfo for mongo::replset::BackgroundSyncInterface

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
