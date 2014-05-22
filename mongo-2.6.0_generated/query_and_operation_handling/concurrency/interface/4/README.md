
# Interface for Spin Locks
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/concurrency/spin\_lock.cpp

<div></div>

    mongo::SpinLock::SpinLock()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/stats/service\_stats.cpp](../../../../dead\_code/dead\_code)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::SpinLock::~SpinLock()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/stats/service\_stats.cpp](../../../../dead\_code/dead\_code)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
