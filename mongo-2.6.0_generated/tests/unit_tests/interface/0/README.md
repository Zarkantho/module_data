
# Interface for Unittest Framework
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/unittest/crutch.cpp

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/concurrency/task.cpp](../../../../utilities/utilities)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

### src/mongo/unittest/unittest.cpp

<div></div>

    mongo::unittest::Test::Test()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    typeinfo for mongo::unittest::Test

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::run()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::setUp()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::tearDown()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::~Test()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
