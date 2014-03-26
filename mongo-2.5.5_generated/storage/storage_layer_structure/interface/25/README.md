
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/instance.cpp

<div></div>

    typeinfo for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::exitCleanly(mongo::ExitCode)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBDirectClient::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::lockFile

- Used By:

    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::_diaglog

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::mongoAbort(char const*)

- Used By:

    - [src/mongo/db/dur.cpp](../../../storage/journaling)

<div></div>

    mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    vtable for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/perftests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/directclienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../security/authorization)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/dbtests/commandtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../queries/database\_commands)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::DiagLog::flush()

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../../../network/network\_core)
    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../security/authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication/replication)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding/sharding)
    - [src/mongo/db/dur\_journal.cpp](../../../storage/journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../storage/journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities/utilities)
    - [src/mongo/util/concurrency/task.cpp](../../../utilities/utilities)
    - [src/mongo/s/writeback\_listener.cpp](../../../sharding/writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../sharding/sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding/sharding)
    - [src/mongo/db/dur.cpp](../../../storage/journaling)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/client.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network/network\_core)
    - [src/mongo/s/distlock.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../sharding/sharding)
    - [src/mongo/db/storage/data\_file.cpp](../../../storage/mmap\_file\_interface)

<div></div>

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network/network\_core)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)

<div></div>

    mongo::DiagLog::setLevel(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBDirectClient::killCursor(long long)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::dbExecCommand

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::acquirePathLock(bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::replHasDatabases()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication/replication)

<div></div>

    mongo::killCurrentOp

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../queries/database\_commands)
    - [src/mongo/db/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/extsort.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dur\_recover.cpp](../../../storage/journaling)
    - [src/mongo/db/clientcursor.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/interrupt\_status\_mongod.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/storage\_details.cpp](../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)

<div></div>

    mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../security/authorization)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
