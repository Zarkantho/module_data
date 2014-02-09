# cpp\_client\_driver

# Module Groups

-------------

# Group Description
Code to manage and store the current state of a connection to a replica set.  It is designed to allow the state to be shared across multiple threads so that each thread in our connection pool does not need to make a network call to get the current replica set state

# Files
- src/mongo/client/replica\_set\_monitor\_internal.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.cpp   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor\_test.cpp   ()

# Interface

### src/mongo/client/replica\_set\_monitor.cpp

<div></div>

    mongo::ReplicaSetMonitor::contains(mongo::HostAndPort const&) const

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getName() const

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getServerAddress() const

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getMasterOrUassert()

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function<void (std::string const&, std::string const&)>)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ReplicaSetMonitor::remove(std::string const&, bool)

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::maxConsecutiveFailedChecks

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

# Dependencies

### src/mongo/client/replica\_set\_monitor.cpp

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BackgroundJob::running() const

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::wait(unsigned int)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::PseudoRandom::nextInt64()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::cancel()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    boost::thread::detach()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/client/replica\_set\_monitor\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Stubs so that the client driver can build alone since our deps are screwed up. We have symbols  that are required by shared code that are very internal to the server, so if we didn't have these  files we'd either need to include the whole server (which we want to avoid) or the build wouldn't  successfully link.

# Files
- src/mongo/client/clientAndShell.cpp   ()
- src/mongo/client/clientOnly-private.h   ()
- src/mongo/client/clientOnly.cpp   ()

# Interface

### src/mongo/client/clientAndShell.cpp

<div></div>

    mongo::dbexitCalled

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Shard::isAShardNode(std::string const&)

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../sharding)

<div></div>

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

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
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)

# Dependencies

### src/mongo/client/clientAndShell.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

-------------

# Group Description
Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

# Files
- src/mongo/client/init.cpp   ()
- src/mongo/client/init.h   ()

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
The Core C++ Client Driver Library   who uses these, and why? maybe this description should be broken up into   some components, e.g. what exactly is a 'dbclient', a 'dbclientcursor'   and a 'syncclusterconnection' ?

# Files
- src/mongo/client/connpool.cpp   (mongod, tools, mongos)
- src/mongo/client/connpool.h   (mongod, tools, mongos)
- src/mongo/client/constants.h   (mongod, tools, mongos)
- src/mongo/client/dbclient.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient.h   ()
- src/mongo/client/dbclient\_rs.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs.h   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs\_test.cpp   ()
- src/mongo/client/dbclientcursor.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclientcursor.h   (mongod, tools, mongos)
- src/mongo/client/dbclientinterface.h   (mongod, tools, mongos)
- src/mongo/client/dbclientmockcursor.h   (mongod, tools)
- src/mongo/client/scoped\_db\_conn\_test.cpp   ()
- src/mongo/client/syncclusterconnection.cpp   (mongod, tools, mongos)
- src/mongo/client/syncclusterconnection.h   (mongod, tools, mongos)

# Interface

### src/mongo/client/connpool.cpp

<div></div>

    vtable for mongo::ScopedDbConnection

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Used By:

    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::pool

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::flush()

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::DBConnectionPool::removeHost(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::isConnectionGood(std::string const&, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::onHandedOut(mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::~DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::serverNameCompare::operator()(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::clear()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::AScopedConnection::_numConnections

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBConnectionPool::DBConnectionPool()

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

### src/mongo/client/dbclient.cpp

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    vtable for mongo::DBClientBase

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
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
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
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

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::Query::toString() const

- Used By:

    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::setPostRunCommandHook(boost::function<void (mongo::BSONObj const&, std::string const&)>)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::ConnectionString::_connectHookMutex

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBClientWithCommands::getCollectionNames(std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getDatabaseNames()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::Query::ReadPrefField

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::getErrField(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Query::Query(char const*)

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientConnection::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::Query::isExplain() const

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::Query::getFilter() const

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBClientConnection::setSoTimeout(double)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
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
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::exists(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::assembleRequest(std::string const&, mongo::BSONObj, int, int, mongo::BSONObj const*, int, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
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
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
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

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::Query::hint(std::string const&)

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientInterface::findN(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../sharding)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::auth(std::string const&, std::string const&, std::string const&, std::string&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<div></div>

    mongo::ConnectionString::_finishInit()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::Query::explain()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/tools/restore.cpp](../tools)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientWithCommands

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::nsGetDB(std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<div></div>

    mongo::DBClientConnection::_checkConnection()

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)

<div></div>

    mongo::Query::hasReadPreference(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::Query::isComplex(bool*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<div></div>

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
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::Query::minKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::Query::hint(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::Query::Query(std::string const&)

- Used By:

    - [src/mongo/tools/export.cpp](../tools)

<div></div>

    mongo::Query::snapshot()

- Used By:

    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<div></div>

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
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientConnection::_lazyKillCursor

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBClientWithCommands::createPasswordDigest(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ConnectionString::_connectHook

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::Query::maxKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientConnection::checkResponse(char const*, int, bool*, std::string*)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

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
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::DBClientConnection::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientConnection::recv(mongo::Message&)

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    vtable for mongo::DBClientConnection

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::DBClientWithCommands::eval(std::string const&, std::string const&, mongo::BSONObj&, mongo::BSONElement&, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    typeinfo for mongo::DBClientBase

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::getPrevError()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/client/dbclient\_rs.cpp

<div></div>

    mongo::DBClientReplicaSet::slaveConn()

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)

<div></div>

    mongo::DBClientReplicaSet::masterConn()

- Used By:

    - [src/mongo/s/version\_manager.cpp](../sharding)

### src/mongo/client/dbclientcursor.cpp

<div></div>

    mongo::DBClientCursor::peek(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&, int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::DBClientCursor::more()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::initLazy(bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::next()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<div></div>

    mongo::DBClientCursor::peekFirst()

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::DBClientCursor::_finishConsInit()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<div></div>

    mongo::DBClientCursor::initLazyFinish(bool&)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<div></div>

    vtable for mongo::DBClientCursor

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DBClientCursor

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

<div></div>

    mongo::DBClientCursor::~DBClientCursor()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)

### src/mongo/client/scoped\_db\_conn\_test.cpp

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

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
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

### src/mongo/client/syncclusterconnection.cpp

<div></div>

    mongo::SyncClusterConnection::prepare(std::string&)

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../sharding)

<div></div>

    typeinfo for mongo::SyncClusterConnection

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../sharding)

# Dependencies

### src/mongo/client/connpool.cpp

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::PeriodicTask::~PeriodicTask()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::PeriodicTask::PeriodicTask()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    typeinfo for mongo::PeriodicTask

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

### src/mongo/client/dbclient.cpp

<div></div>

    mongo::Socket::connect(mongo::SockAddr&)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::MessagingPort::MessagingPort(double, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::MessagingPort::shutdown()

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sslGlobalParams

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Socket::isStillConnected()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/client/auth\_helpers.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::MessagingPort::recv(mongo::Message&)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Socket::secure(mongo::SSLManagerInterface*, std::string const&)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::SockAddr::getAddr() const

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::MessagingPort::say(mongo::Message&, int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::SockAddr::SockAddr(char const*, int)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Backoff::nextSleepMillis()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    vtable for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::MessagingPort::piggyBack(mongo::Message&, int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::MessagingPort::setSocketTimeout(double)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::MessagingPort::call(mongo::Message&, mongo::Message&)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

### src/mongo/client/dbclient\_rs.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/client/dbclient\_rs\_test.cpp

<div></div>

    mongo::MockReplicaSet::getReplConfig() const

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::MockRemoteDBServer::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::MockReplicaSet::MockReplicaSet(std::string const&, unsigned long)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::MockConnRegistry::getConnStrHook()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::MockReplicaSet::getSecondaries() const

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::setConfig(std::map<std::string, mongo::ReplSetConfig::MemberCfg, std::less<std::string>, std::allocator<std::pair<std::string const, mongo::ReplSetConfig::MemberCfg> > > const&)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::getSetName() const

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockConnRegistry::get()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::MockReplicaSet::getNode(std::string const&)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::getHosts() const

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::kill(std::string const&)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::getPrimary() const

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::MockReplicaSet::~MockReplicaSet()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)

### src/mongo/client/dbclientcursor.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/client/scoped\_db\_conn\_test.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    boost::thread::thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Listener::globalTicketHolder

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FailPoint::setMode(mongo::FailPoint::Mode, unsigned int, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ListeningSockets::get()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::thread::join()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::FailPointRegistry::getFailPoint(std::string const&) const

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../utilities)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Provided By:

    - [src/mongo/util/net/message\_server\_port.cpp](../network)

<div></div>

    mongo::UserException::appendPrefix(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/client/syncclusterconnection.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::UserException::appendPrefix(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Legacy wire protocol in the client driver   what is the new equivalent, and where?

# Files
- src/mongo/db/dbmessage.cpp   (mongod, tools, mongos)
- src/mongo/db/dbmessage.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/dbmessage.cpp

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, void*, int, int, int, long long)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Message::toString() const

- Used By:

    - [src/mongo/s/d\_logic.cpp](../sharding)

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/strategy.cpp](../sharding)

# Dependencies

### src/mongo/db/dbmessage.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Utilities for keeping track of the data needed for getLastError (part of legacy wire protocol).

# Files
- src/mongo/db/lasterror.cpp   (mongod, tools, mongos)
- src/mongo/db/lasterror.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/lasterror.cpp

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::isShell

- Used By:

    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Used By:

    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::disableForCommand()

- Used By:

    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)

<div></div>

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<div></div>

    mongo::lastError

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
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
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/tool.cpp](../tools)

<div></div>

    mongo::LastErrorHolder::release()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::LastError::noError

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<div></div>

    mongo::LastErrorHolder::initThread()

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::setLastError(int, char const*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/assert\_util.cpp](../utilities)

# Dependencies

### src/mongo/db/lasterror.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::prettyHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Examples of how to use the client driver that get built in the server

# Files
- src/mongo/client/examples/authTest.cpp   ()
- src/mongo/client/examples/clientTest.cpp   ()
- src/mongo/client/examples/first.cpp   ()
- src/mongo/client/examples/httpClientTest.cpp   ()
- src/mongo/client/examples/rs.cpp   ()
- src/mongo/client/examples/second.cpp   ()
- src/mongo/client/examples/tutorial.cpp   ()
- src/mongo/client/examples/whereExample.cpp   ()

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Old performance testing utility. Builds the "mongoperf" binary.

# Files
- src/mongo/client/examples/mongoperf.cpp   (tools)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/client/examples/mongoperf.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::LogFile::~LogFile()

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MemoryMappedFile::close()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmicros(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    vtable for mongo::MemoryMappedFile

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::LockMongoFilesShared::era

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::LogFile::readAt(unsigned long long, void*, unsigned long)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MemoryMappedFile::map(char const*)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

-------------

# Group Description
Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

# Files
- src/mongo/client/export\_macros.h   (mongod, tools, mongos)
- src/mongo/client/undef\_macros.h   (mongod, tools, mongos)
- src/mongo/client/redef\_macros.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

# Files
- src/mongo/server.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Gridfs wrapper around the client driver.

# Files
- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h   (tools)

# Interface

### src/mongo/client/gridfs.cpp

<div></div>

    mongo::GridFS::findFile(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFS::getChunkSize() const

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

<div></div>

    mongo::GridFS::setChunkSize(unsigned int)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)

<div></div>

    mongo::GridFS::storeFile(std::string const&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFS::list(mongo::BSONObj) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFile::write(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFS::~GridFS()

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFS::GridFS(mongo::DBClientBase&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    mongo::GridFS::removeFile(std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../tools)

# Dependencies

### src/mongo/client/gridfs.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

-------------

# Group Description
Cursor that represents a connection to a bunch of shards. You would think that this only makes  sense in mongos, but it turns out it's built into mongod for purposes of map reduce (the final  destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

# Files
- src/mongo/client/parallel.cpp   (mongod, tools, mongos)
- src/mongo/client/parallel.h   (mongod, tools, mongos)

# Interface

### src/mongo/client/parallel.cpp

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::getNS()

- Used By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::Future::CommandResult::join(int)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::init()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::more()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::isSharded()

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::explain(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::next()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getPrimary()

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

# Dependencies

### src/mongo/client/parallel.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LabeledLevel)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardConnection::kill()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::ChunkManager::compatibleWith(mongo::ChunkManager const&, mongo::Shard const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBConfig::reload()

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::causedBy(std::exception const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ChunkManager::getVersion() const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ShardConnection::_finishInit()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::LiteParsedQuery::isTextScoreMeta(mongo::BSONElement)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

-------------

# Group Description
Hookup of client to sasl authentication.  The real meat of built in when user passes --use-sasl-client.  TODO: regenerate this data with --use-sasl-client to show the rest of the sasl related client driver files

# Files
- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h   (mongod, tools, mongos)

# Interface

### src/mongo/client/sasl\_client\_authenticate.cpp

<div></div>

    mongo::saslCommandUserFieldName

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/tools/tool.cpp](../tools)

<div></div>

    mongo::saslCommandPasswordFieldName

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::saslCommandDigestPasswordFieldName

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::saslCommandMechanismFieldName

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::saslCommandUserDBFieldName

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

# Dependencies

### src/mongo/client/sasl\_client\_authenticate.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::base64::decode(std::string const&)

- Provided By:

    - [src/mongo/util/base64.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)
