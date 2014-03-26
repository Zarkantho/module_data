
# Interface

### src/mongo/client/connpool.cpp

<div></div>

    vtable for mongo::ScopedDbConnection

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::pool

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::flush()

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::DBConnectionPool::removeHost(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::isConnectionGood(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::onHandedOut(mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::~DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::serverNameCompare::operator()(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBConnectionPool::clear()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::AScopedConnection::_numConnections

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBConnectionPool::DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)

### src/mongo/client/dbclient.cpp

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/tools/top.cpp](../../../tools)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    vtable for mongo::DBClientBase

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::toString() const

- Used By:

    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::setPostRunCommandHook(boost::function<void (mongo::BSONObj const&, std::string const&)>)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::ConnectionString::_connectHookMutex

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBClientWithCommands::getCollectionNames(std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getDatabaseNames()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::ReadPrefField

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::getErrField(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Query::Query(char const*)

- Used By:

    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientConnection::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::isExplain() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../sharding)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)
    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::Query::getFilter() const

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::DBClientConnection::setSoTimeout(double)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::exists(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::assembleRequest(std::string const&, mongo::BSONObj, int, int, mongo::BSONObj const*, int, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/tools/files.cpp](../../../tools)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/tools/import.cpp](../../../tools)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::hint(std::string const&)

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientInterface::findN(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::auth(std::string const&, std::string const&, std::string const&, std::string&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)

<div></div>

    mongo::ConnectionString::_finishInit()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::explain()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::nsGetDB(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Used By:

    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../tools)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientConnection::_checkConnection()

- Used By:

    - [src/mongo/tools/stat.cpp](../../../tools)

<div></div>

    mongo::Query::hasReadPreference(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::Query::isComplex(bool*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)

<div></div>

    mongo::DBClientConnection::_numConnections

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::minKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::hint(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::Query(std::string const&)

- Used By:

    - [src/mongo/tools/export.cpp](../../../tools)

<div></div>

    mongo::Query::snapshot()

- Used By:

    - [src/mongo/tools/export.cpp](../../../tools)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientConnection::_lazyKillCursor

- Used By:

    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBClientWithCommands::createPasswordDigest(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ConnectionString::_connectHook

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::Query::maxKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/tools/export.cpp](../../../tools)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    mongo::DBClientConnection::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)

<div></div>

    vtable for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&, mongo::BSONObj&, mongo::BSONElement&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)

<div></div>

    typeinfo for mongo::DBClientBase

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getPrevError()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

### src/mongo/client/dbclient\_rs.cpp

<div></div>

    mongo::DBClientReplicaSet::slaveConn()

- Used By:

    - [src/mongo/tools/tool.cpp](../../../tools)

<div></div>

    mongo::DBClientReplicaSet::masterConn()

- Used By:

    - [src/mongo/s/version\_manager.cpp](../../../sharding)

### src/mongo/client/dbclientcursor.cpp

<div></div>

    mongo::DBClientCursor::peek(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)

<div></div>

    mongo::DBClientCursor::more()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::initLazy(bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::next()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::peekFirst()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::DBClientCursor::_finishConsInit()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientCursor::initLazyFinish(bool&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)

<div></div>

    vtable for mongo::DBClientCursor

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientCursor

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../unit\_tests)

<div></div>

    mongo::DBClientCursor::~DBClientCursor()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../unit\_tests)

### src/mongo/client/scoped\_db\_conn\_test.cpp

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network\_core)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/util/net/listen.cpp](../../../network\_core)
    - [src/mongo/util/assert\_util.cpp](../../../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/util/concurrency/task.cpp](../../../utilities)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network\_core)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
