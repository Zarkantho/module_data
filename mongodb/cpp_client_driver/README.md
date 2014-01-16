# cpp\_client\_driver

# Module Groups

-------------

Stubs so that the client driver can build alone since our deps are screwed up. We have symbols  that are required by shared code that are very internal to the server, so if we didn't have these  files we'd either need to include the whole server (which we want to avoid) or the build wouldn't  successfully link.

- src/mongo/client/clientAndShell.cpp   (cppclientdriver)
- src/mongo/client/clientOnly-private.h
- src/mongo/client/clientOnly.cpp   (cppclientdriver)

## Interface


### src/mongo/client/clientAndShell.cpp

<pre>mongo::dbexitCalled</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::shell_utils::mongoProgramOutputMutex</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::haveLocalShardingInfo(std::string const&)</pre>

#### Used By:

- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<pre>mongo::createDirectClient()</pre>

#### Used By:

- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<pre>mongo::dbexit(mongo::ExitCode, char const*)</pre>

#### Used By:

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

<pre>mongo::Shard::isAShardNode(std::string const&)</pre>

#### Used By:

- [src/mongo/s/writeback\_listener.cpp](../sharding)

<pre>mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)</pre>

#### Used By:

- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/s/strategy.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::inShutdown()</pre>

#### Used By:

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

<pre>mongo::ClientBasic::getCurrent()</pre>

#### Used By:

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

<pre>mongo::StartupTest::~StartupTest()</pre>

#### Used By:

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

<pre>mongo::StartupTest::StartupTest()</pre>

#### Used By:

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

<pre>typeinfo for mongo::StartupTest</pre>

#### Used By:

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

Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

- src/mongo/client/init.cpp   (cppclientdriver)
- src/mongo/client/init.h

## Interface

(not used outside this module)

-------------

The Core C++ Client Driver Library   who uses these, and why? maybe this description should be broken up into   some components, e.g. what exactly is a 'dbclient', a 'dbclientcursor'   and a 'syncclusterconnection' ?

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

## Interface


### src/mongo/client/connpool.cpp

<pre>vtable for mongo::ScopedDbConnection</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)</pre>

#### Used By:

- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::pool</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::clear()</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<pre>mongo::DBConnectionPool::flush()</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)

<pre>mongo::DBConnectionPool::removeHost(std::string const&)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::ScopedDbConnection::_setSocketTimeout()</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::isConnectionGood(std::string const&, mongo::DBClientBase*)</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::DBConnectionPool::get(std::string const&, double)</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::onHandedOut(mongo::DBClientBase*)</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::DBConnectionPool::~DBConnectionPool()</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::DBConnectionPool::serverNameCompare::operator()(std::string const&, std::string const&) const</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::AScopedConnection::_numConnections</pre>

#### Used By:

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

<pre>mongo::DBConnectionPool::DBConnectionPool()</pre>

#### Used By:

- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::ScopedDbConnection::~ScopedDbConnection()</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)</pre>

#### Used By:

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

<pre>vtable for mongo::DBClientBase</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::reIndex(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<pre>mongo::Query::toString() const</pre>

#### Used By:

- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientBase::INVALID_SOCK_CREATION_TIME</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::Query::Query(std::string const&)</pre>

#### Used By:

- [src/mongo/tools/export.cpp](../tools)

<pre>mongo::ConnectionString::_connectHookMutex</pre>

#### Used By:

- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::getCollectionNames(std::string const&)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::getDatabaseNames()</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)</pre>

#### Used By:

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

<pre>mongo::Query::ReadPrefField</pre>

#### Used By:

- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<pre>mongo::getErrField(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<pre>mongo::Query::Query(char const*)</pre>

#### Used By:

- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::Query::hasReadPreference(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::DBClientWithCommands::count(std::string const&, mongo::BSONObj const&, int, int, int)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::Query::explain()</pre>

#### Used By:

- [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<pre>mongo::DBClientConnection::_auth(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>mongo::Query::isExplain() const</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::ConnectionString::parse(std::string const&, std::string&)</pre>

#### Used By:

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

<pre>mongo::Query::getFilter() const</pre>

#### Used By:

- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<pre>mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)

<pre>mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::DBClientConnection::setSoTimeout(double)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>vtable for mongo::DBClientWithCommands</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::getIndexes(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)</pre>

#### Used By:

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

<pre>mongo::ConnectionString::typeToString(mongo::ConnectionString::ConnectionType)</pre>

#### Used By:

- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientWithCommands::exists(std::string const&)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::DBClientConnection::setReplSetClientCallback(mongo::DBClientReplicaSet*)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<pre>mongo::assembleRequest(std::string const&, mongo::BSONObj, int, int, mongo::BSONObj const*, int, mongo::Message&)</pre>

#### Used By:

- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientBase::ConnectionIdSequence</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::getLastError(bool, bool, int, int)</pre>

#### Used By:

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

<pre>mongo::DBClientBase::remove(std::string const&, mongo::Query, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::eval(std::string const&, std::string const&, mongo::BSONObj&, mongo::BSONElement&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::Query::hint(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<pre>mongo::DBClientInterface::findN(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int)</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/d\_merge.cpp](../sharding)

<pre>mongo::nsGetCollection(std::string const&)</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::isOk(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/s/chunk.cpp](../sharding)

<pre>non-virtual thunk to mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::auth(std::string const&, std::string const&, std::string const&, std::string&, bool)</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<pre>mongo::ConnectionString::_finishInit()</pre>

#### Used By:

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

<pre>mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)</pre>

#### Used By:

- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/tools/stat.cpp](../tools)

<pre>mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::ConnectionString::_fillServers(std::string)</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::auth(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientBase::getMore(std::string const&, long long, int, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)</pre>

#### Used By:

- [src/mongo/tools/restore.cpp](../tools)

<pre>mongo::DBClientWithCommands::resetIndexCache()</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::Query::ReadPrefTagsField</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<pre>typeinfo for mongo::DBClientConnection</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::isNotMasterErrorString(mongo::BSONElement const&)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<pre>typeinfo for mongo::DBClientWithCommands</pre>

#### Used By:

- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<pre>mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)</pre>

#### Used By:

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

<pre>mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::nsGetDB(std::string const&)</pre>

#### Used By:

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

<pre>mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)</pre>

#### Used By:

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

<pre>mongo::DBClientConnection::_checkConnection()</pre>

#### Used By:

- [src/mongo/tools/stat.cpp](../tools)

<pre>mongo::Query::isComplex(bool*) const</pre>

#### Used By:

- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<pre>mongo::DBClientConnection::_numConnections</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::Query::minKey(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<pre>mongo::Query::hint(mongo::BSONObj)</pre>

#### Used By:

- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

<pre>mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)</pre>

#### Used By:

- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<pre>mongo::Query::snapshot()</pre>

#### Used By:

- [src/mongo/tools/export.cpp](../tools)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<pre>mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)</pre>

#### Used By:

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

<pre>mongo::DBClientConnection::_lazyKillCursor</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientWithCommands::createPasswordDigest(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/db/auth/security\_key.cpp](../authentication)

<pre>mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientWithCommands::dropIndexes(std::string const&)</pre>

#### Used By:

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

<pre>mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)</pre>

#### Used By:

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

<pre>mongo::DBClientWithCommands::_lookupAvailableOptions()</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::ConnectionString::_connectHook</pre>

#### Used By:

- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::Query::maxKey(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<pre>mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>mongo::Query::ReadPrefModeField</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/tools/stat.cpp](../tools)

<pre>mongo::Query::sort(mongo::BSONObj const&)</pre>

#### Used By:

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

<pre>mongo::DBClientConnection::logout(std::string const&, mongo::BSONObj&)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>non-virtual thunk to mongo::DBClientConnection::recv(mongo::Message&)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::eval(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::DBClientConnection::recv(mongo::Message&)</pre>

#### Used By:

- [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<pre>vtable for mongo::DBClientConnection</pre>

#### Used By:

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

<pre>mongo::ConnectionString::connect(std::string&, double) const</pre>

#### Used By:

- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<pre>typeinfo for mongo::DBClientBase</pre>

#### Used By:

- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<pre>mongo::hasErrField(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientWithCommands::getPrevError()</pre>

#### Used By:

- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<pre>mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/client/dbclient\_rs.cpp

<pre>mongo::DBClientReplicaSet::slaveConn()</pre>

#### Used By:

- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::ReplicaSetMonitor::_maxFailedChecks</pre>

#### Used By:

- [src/mongo/db/commands/parameters.cpp](../database\_commands)

<pre>mongo::ReplicaSetMonitor::remove(std::string const&, bool)</pre>

#### Used By:

- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::ReplicaSetMonitor::getServerAddress() const</pre>

#### Used By:

- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/grid.cpp](../sharding)

<pre>mongo::ReplicaSetMonitor::getAllTrackedSets(std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)</pre>

#### Used By:

- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientReplicaSet::connect()</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>mongo::ReplicaSetMonitor::getMaster()</pre>

#### Used By:

- [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

<pre>mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const</pre>

#### Used By:

- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<pre>mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function1<void, mongo::ReplicaSetMonitor const*>)</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::ReplicaSetMonitor::get(std::string const&, bool)</pre>

#### Used By:

- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<pre>mongo::DBClientReplicaSet::isntMaster()</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>mongo::ReplicaSetMonitor::contains(std::string const&) const</pre>

#### Used By:

- [src/mongo/s/shard.cpp](../sharding)

<pre>mongo::DBClientReplicaSet::masterConn()</pre>

#### Used By:

- [src/mongo/s/version\_manager.cpp](../sharding)

<pre>mongo::DBClientReplicaSet::DBClientReplicaSet(std::string const&, std::vector<mongo::HostAndPort, std::allocator<mongo::HostAndPort> > const&, double)</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/client/dbclientcursor.cpp

<pre>mongo::DBClientCursor::peekError(mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientCursor::init()</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientCursor::peek(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, int)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)

<pre>mongo::DBClientCursor::more()</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<pre>mongo::DBClientCursor::initLazy(bool)</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<pre>mongo::DBClientCursor::next()</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<pre>mongo::DBClientCursor::peekFirst()</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::DBClientCursor::_finishConsInit()</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
- [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<pre>mongo::DBClientCursor::initLazyFinish(bool&)</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<pre>vtable for mongo::DBClientCursor</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
- [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<pre>typeinfo for mongo::DBClientCursor</pre>

#### Used By:

- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<pre>mongo::DBClientCursor::exhaustReceiveMore()</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>mongo::DBClientCursor::~DBClientCursor()</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
- [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

### src/mongo/client/scoped\_db\_conn\_test.cpp

<pre>mongo::createDirectClient()</pre>

#### Used By:

- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<pre>mongo::dbexit(mongo::ExitCode, char const*)</pre>

#### Used By:

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

<pre>mongo::inShutdown()</pre>

#### Used By:

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

<pre>mongo::haveLocalShardingInfo(std::string const&)</pre>

#### Used By:

- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

### src/mongo/client/syncclusterconnection.cpp

<pre>mongo::SyncClusterConnection::prepare(std::string&)</pre>

#### Used By:

- [src/mongo/s/config\_upgrade.cpp](../sharding)

<pre>mongo::SyncClusterConnection::SyncClusterConnection(std::list<mongo::HostAndPort, std::allocator<mongo::HostAndPort> > const&, double)</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<pre>typeinfo for mongo::SyncClusterConnection</pre>

#### Used By:

- [src/mongo/s/config\_upgrade.cpp](../sharding)

<pre>mongo::SyncClusterConnection::setAllSoTimeouts(double)</pre>

#### Used By:

- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

-------------

Legacy wire protocol in the client driver   what is the new equivalent, and where?

- src/mongo/db/dbmessage.cpp   (cppclientdriver)
- src/mongo/db/dbmessage.h

## Interface


### src/mongo/db/dbmessage.cpp

<pre>mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, void*, int, int, int, long long)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/cursors.cpp](../sharding)

<pre>mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Message::toString() const</pre>

#### Used By:

- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/s/d\_logic.cpp](../sharding)

<pre>mongo::replyToQuery(int, mongo::Message&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<pre>mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

-------------

Utilities for keeping track of the data needed for getLastError (part of legacy wire protocol).

- src/mongo/db/lasterror.cpp   (cppclientdriver)
- src/mongo/db/lasterror.h

## Interface


### src/mongo/db/lasterror.cpp

<pre>mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::LastErrorHolder::get(bool)</pre>

#### Used By:

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

<pre>mongo::isShell</pre>

#### Used By:

- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::LastErrorHolder::reset(mongo::LastError*)</pre>

#### Used By:

- [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LastErrorHolder::disableForCommand()</pre>

#### Used By:

- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)

<pre>mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)</pre>

#### Used By:

- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<pre>mongo::lastError</pre>

#### Used By:

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

<pre>mongo::LastErrorHolder::release()</pre>

#### Used By:

- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<pre>mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)</pre>

#### Used By:

- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::LastError::noError</pre>

#### Used By:

- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<pre>mongo::LastErrorHolder::initThread()</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LastErrorHolder::_get(bool)</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::setLastError(int, char const*)</pre>

#### Used By:

- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/util/assert\_util.cpp](../utilities)

-------------

Examples of how to use the client driver that get built in the server

- src/mongo/client/examples/authTest.cpp   (cppclientdriver)
- src/mongo/client/examples/clientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/first.cpp   (cppclientdriver)
- src/mongo/client/examples/httpClientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/rs.cpp   (cppclientdriver)
- src/mongo/client/examples/second.cpp   (cppclientdriver)
- src/mongo/client/examples/tutorial.cpp   (cppclientdriver)
- src/mongo/client/examples/whereExample.cpp   (cppclientdriver)

## Interface

(not used outside this module)

-------------

Old performance testing utility. Builds the "mongoperf" binary.

- src/mongo/client/examples/mongoperf.cpp   (tools)

## Interface

(not used outside this module)

-------------

Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

- src/mongo/client/export\_macros.h
- src/mongo/client/undef\_macros.h
- src/mongo/client/redef\_macros.h

## Interface

(not used outside this module)

-------------

More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

- src/mongo/server.h

## Interface

(not used outside this module)

-------------

Gridfs wrapper around the client driver.

- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h

## Interface


### src/mongo/client/gridfs.cpp

<pre>mongo::GridFS::findFile(std::string const&) const</pre>

#### Used By:

- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFS::getChunkSize() const</pre>

#### Used By:

- [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

<pre>mongo::GridFS::setChunkSize(unsigned int)</pre>

#### Used By:

- [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

<pre>mongo::GridFS::storeFile(std::string const&, std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFS::list(mongo::BSONObj) const</pre>

#### Used By:

- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFile::write(std::string const&) const</pre>

#### Used By:

- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFS::~GridFS()</pre>

#### Used By:

- [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFS::GridFS(mongo::DBClientBase&, std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
- [src/mongo/tools/files.cpp](../tools)

<pre>mongo::GridFS::removeFile(std::string const&)</pre>

#### Used By:

- [src/mongo/tools/files.cpp](../tools)

-------------

Cursor that represents a connection to a bunch of shards. You would think that this only makes  sense in mongos, but it turns out it's built into mongod for purposes of map reduce (the final  destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

- src/mongo/client/parallel.cpp   (mongod, tools, mongos)
- src/mongo/client/parallel.h

## Interface


### src/mongo/client/parallel.cpp

<pre>mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Future::CommandResult::join(int)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::ParallelSortClusteredCursor::next()</pre>

#### Used By:

- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::ParallelSortClusteredCursor::more()</pre>

#### Used By:

- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::ParallelSortClusteredCursor::isSharded()</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::ClusteredCursor::init()</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

<pre>mongo::ParallelSortClusteredCursor::getPrimary()</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)

-------------

Hookup of client to sasl authentication. Only built in when user passes --use-sasl-client

- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h

## Interface


### src/mongo/client/sasl\_client\_authenticate.cpp

<pre>mongo::saslCommandErrmsgFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandUserFieldName</pre>

#### Used By:

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

<pre>mongo::saslCommandPasswordFieldName</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::saslCommandDigestPasswordFieldName</pre>

#### Used By:

- [src/mongo/db/auth/security\_key.cpp](../authentication)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandUserDBFieldName</pre>

#### Used By:

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

<pre>mongo::saslCommandServiceHostnameFieldName</pre>

#### Used By:

- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandServiceNameFieldName</pre>

#### Used By:

- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandDoneFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandAutoAuthorizeFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

<pre>mongo::saslDefaultDBName</pre>

#### Used By:

- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslStartCommandName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandPayloadFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslExtractPayload(mongo::BSONObj const&, std::string*, mongo::BSONType*)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandMechanismListFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

<pre>mongo::saslClientAuthenticate</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandConversationIdFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslContinueCommandName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslDefaultServiceName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::saslCommandMechanismFieldName</pre>

#### Used By:

- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::saslCommandCodeFieldName</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
