# unit\_tests

# Module Groups

-------------

# Group Description
Unittest framework (for both old style dbtests and new style tests)

# Files
- src/mongo/unittest/crutch.cpp   ()
- src/mongo/unittest/fixture\_test.cpp   ()
- src/mongo/unittest/temp\_dir.cpp   ()
- src/mongo/unittest/temp\_dir.h
- src/mongo/unittest/temp\_dir\_test.cpp   ()
- src/mongo/unittest/unittest-inl.h
- src/mongo/unittest/unittest.cpp   ()
- src/mongo/unittest/unittest.h
- src/mongo/unittest/unittest\_main.cpp   ()
- src/mongo/unittest/unittest\_test.cpp   ()

# Interface

### src/mongo/unittest/crutch.cpp

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/stats/snapshots.cpp](../utilities)
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

### src/mongo/unittest/unittest.cpp

    mongo::unittest::Test::Test()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Suite::getSuite(std::string const&)

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    typeinfo for mongo::unittest::Test

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Used By:

    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Test::run()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Test::setUp()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Test::tearDown()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::Test::~Test()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

    mongo::unittest::TestAssertion::~TestAssertion()

- Used By:

    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/config\_server\_tests.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

-------------

# Group Description
Old style unittests ("test" binary)

# Files
- src/mongo/dbtests/accumulatortests.cpp   ()
- src/mongo/dbtests/basictests.cpp   ()
- src/mongo/dbtests/btreebuildertests.cpp   ()
- src/mongo/dbtests/btreetests.cpp   ()
- src/mongo/dbtests/btreetests.inl
- src/mongo/dbtests/chunk\_manager\_targeter\_test.cpp   ()
- src/mongo/dbtests/chunktests.cpp   ()
- src/mongo/dbtests/clienttests.cpp   ()
- src/mongo/dbtests/commandtests.cpp   ()
- src/mongo/dbtests/config\_server\_fixture.cpp   ()
- src/mongo/dbtests/config\_server\_fixture.h
- src/mongo/dbtests/config\_upgrade\_tests.cpp   ()
- src/mongo/dbtests/counttests.cpp   ()
- src/mongo/dbtests/dbclient\_multi\_command\_test.cpp   ()
- src/mongo/dbtests/dbhelper\_tests.cpp   ()
- src/mongo/dbtests/dbtests.cpp   ()
- src/mongo/dbtests/dbtests.h
- src/mongo/dbtests/directclienttests.cpp   ()
- src/mongo/dbtests/documentsourcetests.cpp   ()
- src/mongo/dbtests/documenttests.cpp   ()
- src/mongo/dbtests/expressiontests.cpp   ()
- src/mongo/dbtests/extsorttests.cpp   ()
- src/mongo/dbtests/framework.cpp   ()
- src/mongo/dbtests/framework.h
- src/mongo/dbtests/framework\_options.cpp   ()
- src/mongo/dbtests/framework\_options.h
- src/mongo/dbtests/framework\_options\_init.cpp   ()
- src/mongo/dbtests/framework\_options\_test.cpp   ()
- src/mongo/dbtests/gle\_test.cpp   ()
- src/mongo/dbtests/gridfstest.cpp   ()
- src/mongo/dbtests/indexcatalogtests.cpp   ()
- src/mongo/dbtests/indexupdatetests.cpp   ()
- src/mongo/dbtests/jsobjtests.cpp   ()
- src/mongo/dbtests/jsontests.cpp   ()
- src/mongo/dbtests/jstests.cpp   ()
- src/mongo/dbtests/keypatterntests.cpp   ()
- src/mongo/dbtests/macrotests.cpp   ()
- src/mongo/dbtests/matchertests.cpp   ()
- src/mongo/dbtests/merge\_chunk\_tests.cpp   ()
- src/mongo/dbtests/mmaptests.cpp   ()
- src/mongo/dbtests/mock/mock\_conn\_registry.cpp   ()
- src/mongo/dbtests/mock/mock\_conn\_registry.h
- src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp   ()
- src/mongo/dbtests/mock/mock\_dbclient\_connection.h
- src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp   ()
- src/mongo/dbtests/mock/mock\_dbclient\_cursor.h
- src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp   ()
- src/mongo/dbtests/mock/mock\_remote\_db\_server.h
- src/mongo/dbtests/mock/mock\_replica\_set.cpp   ()
- src/mongo/dbtests/mock/mock\_replica\_set.h
- src/mongo/dbtests/mock\_dbclient\_conn\_test.cpp   ()
- src/mongo/dbtests/mock\_replica\_set\_test.cpp   ()
- src/mongo/dbtests/namespacetests.cpp   ()
- src/mongo/dbtests/oplogstarttests.cpp   ()
- src/mongo/dbtests/pdfiletests.cpp   ()
- src/mongo/dbtests/perf/perftest.cpp   ()
- src/mongo/dbtests/perftests.cpp   ()
- src/mongo/dbtests/pipelinetests.cpp   ()
- src/mongo/dbtests/profile\_test.cpp   ()
- src/mongo/dbtests/query\_multi\_plan\_runner.cpp   ()
- src/mongo/dbtests/query\_single\_solution\_runner.cpp   ()
- src/mongo/dbtests/query\_stage\_and.cpp   ()
- src/mongo/dbtests/query\_stage\_collscan.cpp   ()
- src/mongo/dbtests/query\_stage\_fetch.cpp   ()
- src/mongo/dbtests/query\_stage\_limit\_skip.cpp   ()
- src/mongo/dbtests/query\_stage\_merge\_sort.cpp   ()
- src/mongo/dbtests/query\_stage\_sort.cpp   ()
- src/mongo/dbtests/query\_stage\_tests.cpp   ()
- src/mongo/dbtests/querytests.cpp   ()
- src/mongo/dbtests/queryutiltests.cpp   ()
- src/mongo/dbtests/replica\_set\_monitor\_test.cpp   ()
- src/mongo/dbtests/replsettests.cpp   ()
- src/mongo/dbtests/repltests.cpp   ()
- src/mongo/dbtests/runner\_registry.cpp   ()
- src/mongo/dbtests/sharding.cpp   ()
- src/mongo/dbtests/socktests.cpp   ()
- src/mongo/dbtests/stacktests.cpp   ()
- src/mongo/dbtests/threadedtests.cpp   ()
- src/mongo/dbtests/updatetests.cpp   ()

# Interface
(not used outside this module)
