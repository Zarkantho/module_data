
# Interface

### src/mongo/util/fail\_point.cpp

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/exec/fetch.cpp](../../../core\_query\_system)
    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::ScopedFailPoint::getData() const

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ScopedFailPoint::ScopedFailPoint(mongo::FailPoint*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ScopedFailPoint::~ScopedFailPoint()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/exec/fetch.cpp](../../../core\_query\_system)
    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::FailPoint::toBSON() const

- Used By:

    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::FailPoint::FailPoint()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/exec/fetch.cpp](../../../core\_query\_system)
    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::FailPoint::setMode(mongo::FailPoint::Mode, unsigned int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)

### src/mongo/util/fail\_point\_registry.cpp

<div></div>

    mongo::FailPointRegistry::getFailPoint(std::string const&) const

- Used By:

    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/exec/fetch.cpp](../../../core\_query\_system)
    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

### src/mongo/util/fail\_point\_service.cpp

<div></div>

    mongo::getGlobalFailPointRegistry()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/exec/fetch.cpp](../../../core\_query\_system)
    - [src/mongo/db/curop.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
