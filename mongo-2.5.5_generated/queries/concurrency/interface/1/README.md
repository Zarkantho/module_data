
# Interface

### src/mongo/util/concurrency/spin\_lock.cpp

<div></div>

    mongo::SpinLock::SpinLock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/stats/service\_stats.cpp](../dead\_code)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/stats/counters.cpp](../utilities)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::SpinLock::~SpinLock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/stats/service\_stats.cpp](../dead\_code)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/stats/counters.cpp](../utilities)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/s/shardconnection.cpp](../sharding)
