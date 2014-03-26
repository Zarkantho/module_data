
# Interface for Statistics Tracking
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/stats/counters.cpp

<div></div>

    mongo::replOpCounters

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)

<div></div>

    mongo::OpCounters::gotOp(int, bool)

- Used By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::OpCounters::getObj() const

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::NetworkCounter::hit(long long, long long)

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)

<div></div>

    mongo::globalOpCounters

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)

<div></div>

    mongo::networkCounter

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::NetworkCounter::append(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

### src/mongo/db/stats/snapshots.cpp

<div></div>

    mongo::snapshotThread

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/db/stats/timer\_stats.cpp

<div></div>

    mongo::TimerStats::getReport() const

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/s/client\_info.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)

<div></div>

    mongo::TimerHolder::TimerHolder(mongo::TimerStats*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)

<div></div>

    mongo::TimerHolder::~TimerHolder()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)

<div></div>

    mongo::TimerHolder::recordMillis()

- Used By:

    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)

### src/mongo/db/stats/top.cpp

<div></div>

    mongo::Top::global

- Used By:

    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Top::record(mongo::StringData const&, int, int, long long, bool)

- Used By:

    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::Top::collectionDropped(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
