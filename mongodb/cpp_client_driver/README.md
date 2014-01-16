# cpp\_client\_driver

# Module Groups

-------------

# Group Description
Stubs so that the client driver can build alone since our deps are screwed up. We have symbols  that are required by shared code that are very internal to the server, so if we didn't have these  files we'd either need to include the whole server (which we want to avoid) or the build wouldn't  successfully link.

# Files
- src/mongo/client/clientAndShell.cpp   (cppclientdriver)
- src/mongo/client/clientOnly-private.h
- src/mongo/client/clientOnly.cpp   (cppclientdriver)

# Interface

### src/mongo/client/clientAndShell.cpp

    mongo::dbexitCalled

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

    mongo::shell_utils::mongoProgramOutputMutex

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::Shard::isAShardNode(std::string const&)

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../sharding)

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::inShutdown()

- Used By:

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

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

### src/mongo/client/clientOnly.cpp

    mongo::StartupTest::~StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/util/text\_startuptest.cpp](../utilities)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/hasher.cpp](../utilities)
    - [src/mongo/db/memconcept.cpp](../utilities)

    mongo::StartupTest::StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/util/text\_startuptest.cpp](../utilities)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/hasher.cpp](../utilities)
    - [src/mongo/db/memconcept.cpp](../utilities)

    typeinfo for mongo::StartupTest

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/util.cpp](../utilities)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/util/text\_startuptest.cpp](../utilities)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/hasher.cpp](../utilities)
    - [src/mongo/db/memconcept.cpp](../utilities)

-------------

# Group Description
Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

# Files
- src/mongo/client/init.cpp   (cppclientdriver)
- src/mongo/client/init.h

# Interface
(not used outside this module)

-------------

# Group Description
The Core C++ Client Driver Library   who uses these, and why? maybe this description should be broken up into   some components, e.g. what exactly is a 'dbclient', a 'dbclientcursor'   and a 'syncclusterconnection' ?

# Files
- src/mongo/client/connpool.cpp   (cppclientdriver)
- src/mongo/client/connpool.h
- src/mongo/client/constants.h
- src/mongo/client/dbclient.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient.h
- src/mongo/client/dbclient\_rs.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs.h
- src/mongo/client/dbclient\_rs\_test.cpp   ()
- src/mongo/client/dbclientcursor.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclientcursor.h
- src/mongo/client/dbclientinterface.h
- src/mongo/client/dbclientmockcursor.h
- src/mongo/client/scoped\_db\_conn\_test.cpp   ()
- src/mongo/client/syncclusterconnection.cpp   (cppclientdriver)
- src/mongo/client/syncclusterconnection.h

# Interface

### src/mongo/client/connpool.cpp

    vtable for mongo::ScopedDbConnection

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Used By:

    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::pool

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBConnectionPool::clear()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

    mongo::DBConnectionPool::flush()

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)

    mongo::DBConnectionPool::removeHost(std::string const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ScopedDbConnection::_setSocketTimeout()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

    mongo::DBConnectionPool::isConnectionGood(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBConnectionPool::get(std::string const&, double)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBConnectionPool::onHandedOut(mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBConnectionPool::~DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBConnectionPool::serverNameCompare::operator()(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::AScopedConnection::_numConnections

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBConnectionPool::DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

### src/mongo/client/dbclient.cpp

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Used By:

    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    vtable for mongo::DBClientBase

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

    mongo::Query::toString() const

- Used By:

    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::Query::Query(std::string const&)

- Used By:

    - [src/mongo/tools/export.cpp](../tools)

    mongo::ConnectionString::_connectHookMutex

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::getCollectionNames(std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::getDatabaseNames()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

    mongo::Query::ReadPrefField

- Used By:

    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

    mongo::getErrField(mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::Query::Query(char const*)

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

    mongo::Query::hasReadPreference(mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::DBClientWithCommands::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::Query::explain()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

    mongo::DBClientConnection::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    mongo::Query::isExplain() const

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

    mongo::Query::getFilter() const

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

    mongo::DBClientConnection::setSoTimeout(double)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    vtable for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

    mongo::ConnectionString::typeToString(mongo::ConnectionString::ConnectionType)

- Used By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::exists(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::DBClientConnection::setReplSetClientCallback(mongo::DBClientReplicaSet*)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

    mongo::assembleRequest(std::string const&, mongo::BSONObj, int, int, mongo::BSONObj const*, int, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::ConnectionIdSequence

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&, mongo::BSONObj&, mongo::BSONElement&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

    mongo::Query::hint(std::string const&)

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

    mongo::DBClientInterface::findN(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)

    mongo::nsGetCollection(std::string const&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::isOk(mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/chunk.cpp](../sharding)

    non-virtual thunk to mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    mongo::DBClientWithCommands::auth(std::string const&, std::string const&, std::string const&, std::string&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

    mongo::ConnectionString::_finishInit()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Used By:

    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::ConnectionString::_fillServers(std::string)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/tools/restore.cpp](../tools)

    mongo::DBClientWithCommands::resetIndexCache()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::Query::ReadPrefTagsField

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

    typeinfo for mongo::DBClientConnection

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/tools/dump.cpp](../tools)

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::isNotMasterErrorString(mongo::BSONElement const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

    typeinfo for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

    mongo::nsGetDB(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientConnection::_checkConnection()

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)

    mongo::Query::isComplex(bool*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

    mongo::DBClientConnection::_numConnections

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::Query::minKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

    mongo::Query::hint(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

    mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::Query::snapshot()

- Used By:

    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

    mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

    mongo::DBClientConnection::_lazyKillCursor

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::createPasswordDigest(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::ConnectionString::_connectHook

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::Query::maxKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

    mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    mongo::Query::ReadPrefModeField

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/stat.cpp](../tools)

    mongo::Query::sort(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

    mongo::DBClientConnection::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    non-virtual thunk to mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

    mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

    vtable for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::ConnectionString::connect(std::string&, double) const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

    typeinfo for mongo::DBClientBase

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

    mongo::hasErrField(mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::DBClientWithCommands::getPrevError()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/client/dbclient\_rs.cpp

    mongo::DBClientReplicaSet::slaveConn()

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)

    mongo::ReplicaSetMonitor::_maxFailedChecks

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

    mongo::ReplicaSetMonitor::remove(std::string const&, bool)

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ReplicaSetMonitor::getServerAddress() const

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)

    mongo::ReplicaSetMonitor::getAllTrackedSets(std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

    mongo::DBClientReplicaSet::connect()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    mongo::ReplicaSetMonitor::getMaster()

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function1<void, mongo::ReplicaSetMonitor const*>)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

    mongo::DBClientReplicaSet::isntMaster()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    mongo::ReplicaSetMonitor::contains(std::string const&) const

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)

    mongo::DBClientReplicaSet::masterConn()

- Used By:

    - [src/mongo/s/version\_manager.cpp](../sharding)

    mongo::DBClientReplicaSet::DBClientReplicaSet(std::string const&, std::vector<mongo::HostAndPort, std::allocator<mongo::HostAndPort> > const&, double)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/client/dbclientcursor.cpp

    mongo::DBClientCursor::peekError(mongo::BSONObj*)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    mongo::DBClientCursor::init()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    mongo::DBClientCursor::peek(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

    mongo::DBClientCursor::more()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

    mongo::DBClientCursor::initLazy(bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

    mongo::DBClientCursor::next()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

    mongo::DBClientCursor::peekFirst()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::DBClientCursor::_finishConsInit()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

    mongo::DBClientCursor::initLazyFinish(bool&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

    vtable for mongo::DBClientCursor

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

    typeinfo for mongo::DBClientCursor

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

    mongo::DBClientCursor::exhaustReceiveMore()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    mongo::DBClientCursor::~DBClientCursor()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

### src/mongo/client/scoped\_db\_conn\_test.cpp

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::inShutdown()

- Used By:

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

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

### src/mongo/client/syncclusterconnection.cpp

    mongo::SyncClusterConnection::prepare(std::string&)

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../sharding)

    mongo::SyncClusterConnection::SyncClusterConnection(std::list<mongo::HostAndPort, std::allocator<mongo::HostAndPort> > const&, double)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

    typeinfo for mongo::SyncClusterConnection

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../sharding)

    mongo::SyncClusterConnection::setAllSoTimeouts(double)

- Used By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

-------------

# Group Description
Legacy wire protocol in the client driver   what is the new equivalent, and where?

# Files
- src/mongo/db/dbmessage.cpp   (cppclientdriver)
- src/mongo/db/dbmessage.h

# Interface

### src/mongo/db/dbmessage.cpp

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, void*, int, int, int, long long)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

    mongo::Message::toString() const

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/d\_logic.cpp](../sharding)

    mongo::replyToQuery(int, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

-------------

# Group Description
Utilities for keeping track of the data needed for getLastError (part of legacy wire protocol).

# Files
- src/mongo/db/lasterror.cpp   (cppclientdriver)
- src/mongo/db/lasterror.h

# Interface

### src/mongo/db/lasterror.cpp

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

    mongo::LastErrorHolder::get(bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/s/shardconnection.cpp](../sharding)

    mongo::isShell

- Used By:

    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Used By:

    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

    mongo::LastErrorHolder::disableForCommand()

- Used By:

    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

    mongo::lastError

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/tools/tool.cpp](../tools)

    mongo::LastErrorHolder::release()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::LastError::noError

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

    mongo::LastErrorHolder::initThread()

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

    mongo::LastErrorHolder::_get(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

    mongo::setLastError(int, char const*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Examples of how to use the client driver that get built in the server

# Files
- src/mongo/client/examples/authTest.cpp   (cppclientdriver)
- src/mongo/client/examples/clientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/first.cpp   (cppclientdriver)
- src/mongo/client/examples/httpClientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/rs.cpp   (cppclientdriver)
- src/mongo/client/examples/second.cpp   (cppclientdriver)
- src/mongo/client/examples/tutorial.cpp   (cppclientdriver)
- src/mongo/client/examples/whereExample.cpp   (cppclientdriver)

# Interface
(not used outside this module)

-------------

# Group Description
Old performance testing utility. Builds the "mongoperf" binary.

# Files
- src/mongo/client/examples/mongoperf.cpp   (tools)

# Interface
(not used outside this module)

-------------

# Group Description
Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

# Files
- src/mongo/client/export\_macros.h
- src/mongo/client/undef\_macros.h
- src/mongo/client/redef\_macros.h

# Interface
(not used outside this module)

-------------

# Group Description
More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

# Files
- src/mongo/server.h

# Interface
(not used outside this module)

-------------

# Group Description
Gridfs wrapper around the client driver.

# Files
- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h

# Interface

### src/mongo/client/gridfs.cpp

    mongo::GridFS::findFile(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFS::getChunkSize() const

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

    mongo::GridFS::setChunkSize(unsigned int)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

    mongo::GridFS::storeFile(std::string const&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFS::list(mongo::BSONObj) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFile::write(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFS::~GridFS()

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFS::GridFS(mongo::DBClientBase&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)

    mongo::GridFS::removeFile(std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

-------------

# Group Description
Cursor that represents a connection to a bunch of shards. You would think that this only makes  sense in mongos, but it turns out it's built into mongod for purposes of map reduce (the final  destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

# Files
- src/mongo/client/parallel.cpp   (mongod, tools, mongos)
- src/mongo/client/parallel.h

# Interface

### src/mongo/client/parallel.cpp

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::Future::CommandResult::join(int)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::ParallelSortClusteredCursor::next()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ParallelSortClusteredCursor::more()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::ParallelSortClusteredCursor::isSharded()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::ClusteredCursor::init()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

    mongo::ParallelSortClusteredCursor::getPrimary()

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

-------------

# Group Description
Hookup of client to sasl authentication. Only built in when user passes --use-sasl-client

# Files
- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h

# Interface

### src/mongo/client/sasl\_client\_authenticate.cpp

    mongo::saslCommandErrmsgFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandUserFieldName

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/tool.cpp](../tools)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

    mongo::saslCommandPasswordFieldName

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/tool.cpp](../tools)

    mongo::saslCommandDigestPasswordFieldName

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandUserDBFieldName

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/tool.cpp](../tools)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

    mongo::saslCommandServiceHostnameFieldName

- Used By:

    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandServiceNameFieldName

- Used By:

    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandDoneFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandAutoAuthorizeFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

    mongo::saslDefaultDBName

- Used By:

    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslStartCommandName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandPayloadFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslExtractPayload(mongo::BSONObj const&, std::string*, mongo::BSONType*)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandMechanismListFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

    mongo::saslClientAuthenticate

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandConversationIdFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslContinueCommandName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslDefaultServiceName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

    mongo::saslCommandMechanismFieldName

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/tools/tool.cpp](../tools)

    mongo::saslCommandCodeFieldName

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
