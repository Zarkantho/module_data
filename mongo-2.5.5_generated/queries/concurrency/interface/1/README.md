
# Interface for Spin Locks
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/concurrency/spin\_lock.cpp

<div></div>

    mongo::SpinLock::SpinLock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/s/client\_info.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/stats/service\_stats.cpp](../../../../dead\_code/dead\_code)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)

<div></div>

    mongo::SpinLock::~SpinLock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/s/client\_info.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/stats/service\_stats.cpp](../../../../dead\_code/dead\_code)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)
