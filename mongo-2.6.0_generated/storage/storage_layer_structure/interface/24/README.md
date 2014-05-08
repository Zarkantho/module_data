
# Interface for Legacy Instance File
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/instance.cpp

<div></div>

    typeinfo for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::exitCleanly(mongo::ExitCode)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/util/signal\_handlers.cpp](../../../../utilities/utilities)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBDirectClient::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::lockFile

- Used By:

    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::_diaglog

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::mongoAbort(char const*)

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DiagLog::flush()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

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

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

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
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::DiagLog::setLevel(int)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBDirectClient::killCursor(long long)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dbExecCommand

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::acquirePathLock(bool)

- Used By:

    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::replHasDatabases()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::killCurrentOp

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/interrupt\_status\_mongod.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
