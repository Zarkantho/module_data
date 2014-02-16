
# Interface

### src/mongo/unittest/crutch.cpp

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../../../network)
    - [src/mongo/util/assert\_util.cpp](../../../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/util/concurrency/task.cpp](../../../utilities)
    - [src/mongo/s/writeback\_listener.cpp](../../../sharding)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

### src/mongo/unittest/unittest.cpp

<div></div>

    mongo::unittest::Test::Test()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Suite::Suite(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)

<div></div>

    typeinfo for mongo::unittest::Suite

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    typeinfo for mongo::unittest::Test

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../bson)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../bson)
    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::run()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::setUp()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::tearDown()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Test::~Test()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../bson)
    - [src/mongo/s/config\_server\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)

<div></div>

    mongo::unittest::Suite::~Suite()

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
