
# Interface for Cpp Driver Core
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/client/connpool.cpp

<div></div>

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::onHandedOut(mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DBConnectionPool::~DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DBConnectionPool::DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    vtable for mongo::ScopedDbConnection

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::flush()

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBConnectionPool::removeHost(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::serverNameCompare::operator()(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::pool

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::DBConnectionPool::clear()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DBConnectionPool::isConnectionGood(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::AScopedConnection::_numConnections

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

### src/mongo/client/dbclient.cpp

<div></div>

    mongo::DBClientConnection::_numConnections

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)

<div></div>

    vtable for mongo::DBClientInterface

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::minKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::Query(std::string const&)

- Used By:

    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientWithCommands::getDatabaseNames()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::getErrField(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBClientConnection::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::auth(std::string const&, std::string const&, std::string const&, std::string&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBClientInterface::findN(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Query::hasReadPreference(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Query::isExplain() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::explain()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::DBClientBase

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientConnection::_checkConnection()

- Used By:

    - [src/mongo/tools/stat.cpp](../../../../tools/tools)

<div></div>

    mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::DBClientConnection::_lazyKillCursor

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Query::Query(char const*)

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::DBClientBase

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::DBClientWithCommands::getPrevError()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Used By:

    - [src/mongo/tools/top.cpp](../../../../tools/tools)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::setPostRunCommandHook(boost::function<void (mongo::BSONObj const&, std::string const&)>)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ConnectionString::_connectHookMutex

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientConnection::setSoTimeout(double)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    vtable for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&, mongo::BSONObj&, mongo::BSONElement&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::Query::getSort() const

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ConnectionString::_finishInit()

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Used By:

    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::isComplex(bool*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ConnectionString::_connectHook

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBClientWithCommands::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::toString() const

- Used By:

    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBClientWithCommands::getCollectionNames(std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Query::hint(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::snapshot()

- Used By:

    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    vtable for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Used By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    mongo::Query::ReadPrefField

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::getFilter() const

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::assembleRequest(std::string const&, mongo::BSONObj, int, int, mongo::BSONObj const*, int, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Query::hint(std::string const&)

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::exists(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::nsGetDB(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    typeinfo for mongo::DBClientConnection

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Query::maxKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientConnection::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

### src/mongo/client/dbclient\_rs.cpp

<div></div>

    mongo::DBClientReplicaSet::isSecondaryQuery(std::string const&, mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientReplicaSet::slaveConn()

- Used By:

    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    typeinfo for mongo::DBClientReplicaSet

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientReplicaSet::masterConn()

- Used By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)

### src/mongo/client/dbclientcursor.cpp

<div></div>

    mongo::DBClientCursor::init()

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientCursor::peek(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientCursor::_finishConsInit()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBClientCursor::initLazyFinish(bool&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientCursor::initLazy(bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::DBClientCursor::peekFirst()

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::DBClientCursor::initCommand()

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    typeinfo for mongo::DBClientCursor

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBClientCursor::~DBClientCursor()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DBClientCursor::more()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::DBClientCursor::peekError(mongo::BSONObj*)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    vtable for mongo::DBClientCursor

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::DBClientCursor::attach(mongo::AScopedConnection*)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

### src/mongo/client/scoped\_db\_conn\_test.cpp

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)
    - [src/mongo/util/concurrency/task.cpp](../../../../utilities/utilities)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
