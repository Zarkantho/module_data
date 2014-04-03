
# Interface for Unittest Framework
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/unittest/crutch.cpp

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/util/concurrency/task.cpp](../../../../utilities/utilities)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

### src/mongo/unittest/unittest.cpp

<div></div>

    mongo::unittest::Test::Test()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Suite::Suite(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)

<div></div>

    typeinfo for mongo::unittest::Suite

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    typeinfo for mongo::unittest::Test

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::run()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::setUp()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::tearDown()

- Used By:

    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Test::~Test()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/config\_server\_tests.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::unittest::Suite::~Suite()

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
