# utilities

# Module Groups

-------------

# Group Description
Code to manage paths to files.  Conversion from relative to full path within database directory as  well as code to get the current partition (for readahead checks).

# Files
- src/mongo/util/paths.cpp   (mongod, tools, mongos)
- src/mongo/util/paths.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/paths.cpp

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/util/logfile.cpp](../journaling)

# Dependencies

### src/mongo/util/paths.cpp

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

-------------

# Group Description
Classes to help in tracking statistics

# Files
- src/mongo/db/stats/counters.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/counters.h   (mongod, tools, mongos)
- src/mongo/db/stats/snapshots.cpp   (mongod, tools)
- src/mongo/db/stats/snapshots.h   (mongod, tools, mongos)
- src/mongo/db/stats/snapshots\_webplugins.cpp   (mongod)
- src/mongo/db/stats/timer\_stats.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/timer\_stats.h   (mongod, tools, mongos)
- src/mongo/db/stats/top.cpp   (mongod, tools)
- src/mongo/db/stats/top.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/stats/counters.cpp

<div></div>

    mongo::replOpCounters

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::OpCounters::gotOp(int, bool)

- Used By:

    - [src/mongo/s/request.cpp](../sharding)

<div></div>

    mongo::OpCounters::getObj() const

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::NetworkCounter::hit(long long, long long)

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../network)

<div></div>

    mongo::globalOpCounters

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::networkCounter

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::NetworkCounter::append(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

### src/mongo/db/stats/snapshots.cpp

<div></div>

    mongo::snapshotThread

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/stats/timer\_stats.cpp

<div></div>

    mongo::TimerStats::getReport() const

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::TimerHolder::TimerHolder(mongo::TimerStats*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::TimerHolder::~TimerHolder()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::TimerHolder::recordMillis()

- Used By:

    - [src/mongo/db/write\_concern.cpp](../replication)

### src/mongo/db/stats/top.cpp

<div></div>

    mongo::Top::global

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Top::record(mongo::StringData const&, int, int, long long, bool)

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Top::collectionDropped(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

# Dependencies

### src/mongo/db/stats/counters.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::SpinLock::SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::SpinLock::~SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

### src/mongo/db/stats/snapshots.cpp

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/db/stats/snapshots\_webplugins.cpp

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::WebStatusPlugin::WebStatusPlugin(std::string const&, double, std::string const&)

- Provided By:

    - [src/mongo/db/dbwebserver.cpp](../web\_server)

### src/mongo/db/stats/top.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::top

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

-------------

# Group Description
Utilities to hash BSON elements. Used in hashed shard keys and hashed indexes.

# Files
- src/mongo/db/hasher.cpp   (mongod, tools, mongos)
- src/mongo/db/hasher.h   (mongod, tools, mongos)
- src/mongo/db/hasher\_test.cpp   ()

# Interface

### src/mongo/db/hasher.cpp

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Used By:

    - [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

# Dependencies

### src/mongo/db/hasher\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::OID::init(std::string const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Helpers to track in progress operations.  This works by inheriting from it when you make a class that represents an operation that should be tracked. The constructor registers itself in an "in progress" map, and the destructor removes it.

# Files
- src/mongo/db/background.cpp   (mongod, tools)
- src/mongo/db/background.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/background.cpp

<div></div>

    mongo::BackgroundOperation::dump(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/restapi.cpp](../web\_server)

<div></div>

    mongo::BackgroundOperation::BackgroundOperation(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForDb(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Utility to check whether a certain time interval has elapsed. Currently only used in  d\_migrate.cpp to check if we should yield.

# Files
- src/mongo/util/elapsed\_tracker.cpp   (mongod, tools)
- src/mongo/util/elapsed\_tracker.h   (mongod, tools)

# Interface

### src/mongo/util/elapsed\_tracker.cpp

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

# Dependencies

### src/mongo/util/elapsed\_tracker.cpp

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

-------------

# Group Description
Helper classes to accumulate and log progress in a nice format using the logging system (so the logging system is only dependency)

# Files
- src/mongo/util/progress\_meter.cpp   (mongod, tools, mongos)
- src/mongo/util/progress\_meter.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/progress\_meter.cpp

<div></div>

    mongo::ProgressMeter::hit(int)

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ProgressMeter::toString() const

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)

# Dependencies

### src/mongo/util/progress\_meter.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

-------------

# Group Description
Debug macros and gdb server helpers

# Files
- src/mongo/util/debug\_util.cpp   (mongod, tools, mongos)
- src/mongo/util/debug\_util.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/debug\_util.cpp

<div></div>

    mongo::setupSIGTRAPforGDB()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Library to get and set the name of the current thread. Just uses a boost::thread\_specific\_ptr.

# Files
- src/mongo/util/concurrency/thread\_name.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_name.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/concurrency/thread\_name.cpp

<div></div>

    mongo::setThreadName(mongo::StringData)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/query/plan\_enumerator.cpp](../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/tests.cpp](../dead\_code)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/third\_party/s2/base/logging.cc](../s2)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/query/plan\_ranker.cpp](../core\_query\_system)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/util/log.cpp](../logging\_system)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/third\_party/s2/s2polyline.cc](../s2)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/db/exec/projection.cpp](../core\_query\_system)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/repl\_start.cpp](../replication)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/util/file.cpp](../file\_interface)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)

# Dependencies

### src/mongo/util/concurrency/thread\_name.cpp

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

-------------

# Group Description
Utility library to manipulate hex strings

# Files
- src/mongo/util/hex.cpp   (mongod, tools, mongos)
- src/mongo/util/hex.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/hex.cpp

<div></div>

    std::string mongo::integerToHex<unsigned int>(unsigned int)

- Used By:

    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Utilities to run jobs (threads) in the "background".  You can use this to run tasks periodically.  Note that there are two different classes here. One is a Task and one is a BackgroundJob.  They are both used in the code in various places.  Task is just a wrapper around BackgroundJob with a slightly simpler interface.  They both effectively serve the same purpose.

# Files
- src/mongo/util/background.cpp   (mongod, tools, mongos)
- src/mongo/util/background.h   (mongod, tools, mongos)
- src/mongo/util/background\_job\_test.cpp   ()
- src/mongo/util/concurrency/task.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/task.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/background.cpp

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    typeinfo for mongo::PeriodicTask

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::running() const

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::cancel()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::PeriodicTask::~PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::go()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::BackgroundJob::wait(unsigned int)

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::PeriodicTask::PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::BackgroundJob

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Used By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/d\_globals.cpp](../legacy\_code)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

### src/mongo/util/concurrency/task.cpp

<div></div>

    vtable for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    typeinfo for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::task::Server::send(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    vtable for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::task::Task::run()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::task::Task::Task()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::task::Task::setUp()

- Used By:

    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::task::repeat(mongo::task::Task*, unsigned int)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::task::Task::halt()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

<div></div>

    mongo::task::Server::doWork()

- Used By:

    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    typeinfo for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::task::fork(mongo::task::Task*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

# Dependencies

### src/mongo/util/background.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/util/background\_job\_test.cpp

<div></div>

    mongo::Notification::notifyOne()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Notification::waitToBeNotified()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Notification::Notification()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/concurrency/task.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

-------------

# Group Description
Wrapper around a background task that creates an object with a "server" interface.  What this means is that "messages" (in the form of lambdas) can be registered with this class to be called sometime in the future by the event loop in this task.  Some functions just register the function and return, and others will block until the function is executed.

# Files
- src/mongo/util/concurrency/msg.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
mapFindWithDefault - looks something up in a map with a default value.

# Files
- src/mongo/util/map\_util.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
I still do not know what this was originally for, but I know we are slowly getting rid of it.

# Files
- src/mongo/pch.cpp   (mongod, tools, mongos)
- src/mongo/pch.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Assertion library.

# Files
- src/mongo/util/assert\_util.cpp   (mongod, tools, mongos)
- src/mongo/util/assert\_util.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/assert\_util.cpp

<div></div>

    mongo::causedBy(mongo::Status const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExceptionInfo::append(mongo::BSONObjBuilder&, char const*, char const*) const

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::traceExceptions

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/util/alignedbuilder.cpp](../journaling)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/field\_path.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../aggregation\_framework)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../replication)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::fassertFailedNoTrace(int)

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/or.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/exec/keep\_mutations.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/index\_names.cpp](../indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../core\_query\_system)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/util/file.cpp](../file\_interface)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/exec/keep\_mutations.cpp](../core\_query\_system)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/plan\_ranker.cpp](../core\_query\_system)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/util/alignedbuilder.cpp](../journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::causedBy(std::string const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgassertedNoTrace(int, char const*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::msgasserted(int, char const*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/third\_party/s2/base/logging.cc](../s2)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/db/field\_ref\_set.cpp](../update\_system)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/plan\_ranker.cpp](../core\_query\_system)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.cpp](../full\_text\_search\_module)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../sharding)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/exec/keep\_mutations.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/exec/or.cpp](../core\_query\_system)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/ops/field\_checker.cpp](../update\_system)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/field\_path.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/bson/oid.cpp](../bson)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../aggregation\_framework)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/db/query/plan\_enumerator.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../core\_query\_system)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/driverHelpers.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/index\_tag.cpp](../core\_query\_system)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/index\_names.cpp](../indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/util/fail\_point\_registry.cpp](../fail\_points)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/db/fts/stop\_words.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index\_set.cpp](../indexing)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/matcher/matcher.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/role\_graph.cpp](../authentication)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../aggregation\_framework)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../core\_query\_system)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
    - [src/mongo/db/auth/action\_set.cpp](../authentication)
    - [src/mongo/db/matcher/expression\_text.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/db/pipeline/accumulator\_sum.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/socktests.cpp](../unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/util/file.cpp](../file\_interface)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    typeinfo for mongo::DBException

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/base/initializer.cpp](../startup\_initialization)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/base/initializer.cpp](../startup\_initialization)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    vtable for mongo::UserException

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::MsgAssertionException

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::assertionCount

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/matcher/match\_details.cpp](../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/logger/ramlog.cpp](../logging\_system)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/third\_party/s2/base/logging.cc](../s2)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/util/alignedbuilder.cpp](../journaling)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp](../aggregation\_framework)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/tools/admin.cpp](../tools)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/plan\_ranker.cpp](../core\_query\_system)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.cpp](../full\_text\_search\_module)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../sharding)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/db/exec/keep\_mutations.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/exec/or.cpp](../core\_query\_system)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/structure/collection\_iterator.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/field\_path.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/accumulator\_min\_max.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/db/query/plan\_enumerator.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/index\_tag.cpp](../core\_query\_system)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/index\_names.cpp](../indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/bson/oid.cpp](../bson)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/db/fts/stop\_words.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/db/pipeline/accumulator\_avg.cpp](../aggregation\_framework)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/query/single\_solution\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/2d.cpp](../core\_query\_system)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../replication)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../core\_query\_system)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
    - [src/mongo/db/pipeline/accumulator\_push.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/db/pipeline/accumulator\_sum.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/stats/service\_stats.cpp](../dead\_code)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../sharding)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/util/file.cpp](../file\_interface)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::fassertFailed(int)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/driverHelpers.cpp](../database\_commands)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/auth/role\_graph.cpp](../authentication)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/third\_party/s2/base/logging.cc](../s2)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_documents\_update\_guard.cpp](../authentication)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../sharding)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, std::string const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/interval.cpp](../core\_query\_system)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/write\_concern\_options.cpp](../replication)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_changelog.cpp](../sharding)
    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/db/matcher/expression\_where.cpp](../core\_query\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/matcher/expression\_array.cpp](../core\_query\_system)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../full\_text\_search\_module)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/s/type\_lockpings.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/query/parsed\_projection.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/type\_collection.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_element\_iterator.cpp](../full\_text\_search\_module)
    - [src/mongo/db/field\_parser.cpp](../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/lockstat.cpp](../concurrency)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/matcher/expression\_parser\_tree.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/exec/and\_hash.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/tools/stat\_util.cpp](../tools)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/exec/merge\_sort.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/db/matcher/expression\_parser.cpp](../core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../core\_query\_system)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../bson)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/query/explain\_plan.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/version.cpp](../build\_information)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../aggregation\_framework)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)
    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/query/query\_solution.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/type\_locks.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/projection.cpp](../core\_query\_system)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/query/planner\_ixselect.cpp](../core\_query\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../concurrency)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_dbclient\_cursor.cpp](../unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/s/type\_database.cpp](../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/scripting/bson\_template\_evaluator.cpp](../javascript\_libraries)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/exec/projection\_exec.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_geo.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/exec/and\_sorted.cpp](../core\_query\_system)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/matcher/matcher.cpp](../core\_query\_system)
    - [src/mongo/bson/bson\_validate.cpp](../bson)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/db/matcher/path\_internal.cpp](../core\_query\_system)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_stats.cpp](../sharding)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../aggregation\_framework)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../bson)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/type\_explain.cpp](../core\_query\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/path.cpp](../core\_query\_system)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/s/type\_config\_version.cpp](../sharding)
    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/query/index\_bounds.cpp](../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/bson/mutable/document.cpp](../bson)
    - [src/mongo/s/type\_shard.cpp](../sharding)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/pipeline/dependencies.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/util/net/miniwebserver.cpp](../web\_server)
    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::DBException

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::UserException

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    mongo::causedBy(std::exception const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::DBException::toString() const

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    mongo::causedBy(char const*)

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::fassertFailedWithStatus(int, mongo::Status const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/role\_graph.cpp](../authentication)

<div></div>

    mongo::errnoWithPrefix(char const*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::causedBy(std::string const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::ErrorMsg::ErrorMsg(char const*, char)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::demangleName(std::type_info const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/socktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ExceptionInfo::toString() const

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::UserException::appendPrefix(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

# Dependencies

### src/mongo/util/assert\_util.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logContext(char const*)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::setLastError(int, char const*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

-------------

# Group Description
Helper library that you inherit from to make a class "reference counted"

# Files
- src/mongo/util/intrusive\_counter.cpp   (mongod, tools, mongos)
- src/mongo/util/intrusive\_counter.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/intrusive\_counter.cpp

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)

<div></div>

    mongo::RCString::create(mongo::StringData)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
md5 hash library

# Files
- src/mongo/util/md5.cpp   (mongod, tools, mongos)
- src/mongo/util/md5.h   (mongod, tools, mongos)
- src/mongo/util/md5.hpp   (mongod, tools, mongos)
- src/mongo/util/md5\_test.cpp   ()
- src/mongo/util/md5main.cpp   ()

# Interface

### src/mongo/util/md5.cpp

<div></div>

    _md5_finish

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    _md5_init

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    _md5_append

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

# Dependencies

### src/mongo/util/md5\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Windows service

# Files
- src/mongo/util/ntservice.cpp   (mongod, mongos)
- src/mongo/util/ntservice.h   (mongod, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Utilities to hash a username + password

# Files
- src/mongo/client/auth\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/client/auth\_helpers.h   (mongod, tools, mongos)

# Interface

### src/mongo/client/auth\_helpers.cpp

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::auth::getRemoteStoredAuthorizationVersion(mongo::DBClientBase*, int*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/tools/restore.cpp](../tools)

<div></div>

    mongo::auth::schemaVersionServerParameter

- Used By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::auth::getUpdateToUpgradeUser(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

# Dependencies

### src/mongo/client/auth\_helpers.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
Giant list of utilities that I haven't gotten to yet. TODO: document what these are for and why  you would use them.

# Files
- src/mongo/util/queue.h   (mongod, tools)
- src/mongo/util/ramlog.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num-inl.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num.cpp   (mongod, tools, mongos)
- src/mongo/util/safe\_num.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num\_test.cpp   ()
- src/mongo/util/scopeguard.h   (mongod, tools, mongos)
- src/mongo/util/sequence\_util.h   (mongod, tools, mongos)
- src/mongo/util/signal\_handlers.cpp   (mongod, tools, mongos)
- src/mongo/util/signal\_handlers.h   (mongod, tools, mongos)
- src/mongo/util/signal\_win32.cpp   (mongod, tools, mongos)
- src/mongo/util/signal\_win32.h   (mongod, mongos)
- src/mongo/util/stack\_introspect.cpp   (mongod, tools, mongos)
- src/mongo/util/stack\_introspect.h   (mongod, tools, mongos)
- src/mongo/util/stacktrace.cpp   (mongod, tools, mongos)
- src/mongo/util/stacktrace.h   (mongod, tools, mongos)
- src/mongo/util/startup\_test.cpp   (mongod, tools, mongos)
- src/mongo/util/startup\_test.h   (mongod, tools, mongos)
- src/mongo/util/string\_map.h   (mongod, tools, mongos)
- src/mongo/util/string\_map\_test.cpp   ()
- src/mongo/util/stringutils.cpp   (mongod, tools, mongos)
- src/mongo/util/stringutils.h   (mongod, tools, mongos)
- src/mongo/util/stringutils\_test.cpp   ()
- src/mongo/util/tcmalloc\_server\_status\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/text.cpp   (mongod, tools, mongos)
- src/mongo/util/text.h   (mongod, tools, mongos)
- src/mongo/util/text\_startuptest.cpp   (mongod, tools, mongos)
- src/mongo/util/text\_test.cpp   ()
- src/mongo/util/time\_support.cpp   (mongod, tools, mongos)
- src/mongo/util/time\_support.h   (mongod, tools, mongos)
- src/mongo/util/time\_support\_test.cpp   ()
- src/mongo/util/timer-generic-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-posixclock-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-win32-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer.cpp   (mongod, tools, mongos)
- src/mongo/util/timer.h   (mongod, tools, mongos)
- src/mongo/util/touch\_pages.cpp   (mongod, tools)
- src/mongo/util/touch\_pages.h   (mongod, tools)
- src/mongo/util/trace.h   (mongod, tools, mongos)
- src/mongo/util/unordered\_fast\_key\_table.h   (mongod, tools, mongos)
- src/mongo/util/unordered\_fast\_key\_table\_internal.h   (mongod, tools, mongos)
- src/mongo/util/util.cpp   (mongod, tools, mongos)
- src/mongo/util/version\_reporting.cpp   (mongod, tools, mongos)
- src/mongo/util/version\_reporting.h   (mongod, tools, mongos)
- src/mongo/util/version\_test.cpp   ()
- src/mongo/util/winutil.h   (mongod, mongos)
- src/mongo/util/admin\_access.h   (mongod, tools, mongos)
- src/mongo/util/allocator.h   (mongod, tools, mongos)
- src/mongo/util/array.h   ()
- src/mongo/util/base64.cpp   (mongod, tools, mongos)
- src/mongo/util/base64.h   (mongod, tools, mongos)
- src/mongo/util/bson\_util.h   (mongod, tools)
- src/mongo/util/bufreader.h   (mongod, tools, mongos)
- src/mongo/util/checksum.h   (mongod, tools)
- src/mongo/util/compress.cpp   (mongod, tools)
- src/mongo/util/compress.h   (mongod, tools)
- src/mongo/util/concurrency/list.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mapsf.h   (mongod, tools)
- src/mongo/util/concurrency/mutex.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mutexdebugger.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/mutexdebugger.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mvar.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/qlock.h   (mongod, tools)
- src/mongo/util/concurrency/race.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/shared\_mutex\_win.hpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/simplerwlock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_pool.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_pool.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/threadlocal.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/ticketholder.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/value.h   (mongod, tools, mongos)
- src/mongo/util/descriptive\_stats-inl.h   (mongod, tools)
- src/mongo/util/descriptive\_stats.h   (mongod, tools)
- src/mongo/util/descriptive\_stats\_test.cpp   ()
- src/mongo/util/embedded\_builder.h   (mongod, tools, mongos)
- src/mongo/util/exception\_filter\_win32.cpp   (mongod, tools, mongos)
- src/mongo/util/exception\_filter\_win32.h   (mongod, tools, mongos)
- src/mongo/util/exit\_code.h   (mongod, tools, mongos)
- src/mongo/util/gcov.h   (mongod, tools, mongos)
- src/mongo/util/goodies.h   (mongod, tools, mongos)
- src/mongo/util/heapcheck.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/safe\_num.cpp

<div></div>

    mongo::SafeNum::isIdentical(mongo::SafeNum const&) const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::orInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::xorInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::andInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::debugString() const

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::mulInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::SafeNum(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::addInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

### src/mongo/util/signal\_handlers.cpp

<div></div>

    mongo::printStackAndExit(int)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/util/stack\_introspect.cpp

<div></div>

    mongo::inConstructorChainSupported()

- Used By:

    - [src/mongo/dbtests/stacktests.cpp](../unit\_tests)

### src/mongo/util/stacktrace.cpp

<div></div>

    mongo::printStackTrace(std::ostream&)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/db/tests.cpp](../dead\_code)
    - [src/mongo/util/log.cpp](../logging\_system)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/s/shardconnection.cpp](../sharding)

### src/mongo/util/startup\_test.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::StartupTest::StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::StartupTest::runTests()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    typeinfo for mongo::StartupTest

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

### src/mongo/util/stringutils.cpp

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Used By:

    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/tools/restore.cpp](../tools)

<div></div>

    mongo::joinStringDelim(std::vector<std::string, std::allocator<std::string> > const&, std::string*, char)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::LexNumCmp::operator()(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::LexNumCmp::cmp(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::LexNumCmp::LexNumCmp(bool)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

### src/mongo/util/text.cpp

<div></div>

    mongo::parseLL(char const*)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::isValidUTF8(char const*)

- Used By:

    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::StringSplitter::split(std::vector<std::string, std::allocator<std::string> >&)

- Used By:

    - [src/mongo/tools/mongoimport\_options.cpp](../tools)

<div></div>

    mongo::StringSplitter::next()

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)

<div></div>

    mongo::StringSplitter::join(std::vector<std::string, std::allocator<std::string> > const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::StringSplitter::split(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

### src/mongo/util/time\_support.cpp

<div></div>

    mongo::Date_t::toString() const

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::jsTime()

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::sleepmillis(long long)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::Date_t::toTimeT() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::Backoff::getNextSleepMillis(int, unsigned long long, unsigned long long) const

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::time_t_to_Struct(long, tm*, bool)

- Used By:

    - [src/mongo/tools/stat\_util.cpp](../tools)

<div></div>

    mongo::currentDate()

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::dateFromISOString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::sleepmicros(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::toPointInTime(std::string const&, boost::posix_time::ptime*)

- Used By:

    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::getJSTimeVirtualThreadSkew()

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/tools/export.cpp](../tools)

<div></div>

    mongo::Backoff::nextSleepMillis()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::time_t_to_String_short(long)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/oplog.cpp](../tools)

<div></div>

    mongo::curTimeMicros64()

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::terseCurrentTime(bool)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::sleepsecs(int)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)

<div></div>

    mongo::jsTimeVirtualThreadSkew(long long)

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMicros()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMillis64()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/util/timer.cpp

<div></div>

    mongo::Timer::_countsPerSecond

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)

### src/mongo/util/touch\_pages.cpp

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

### src/mongo/util/util.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/util/fail\_point\_service.cpp](../fail\_points)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ThreadSafeString const&)

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::hexdump(char const*, unsigned int)

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../journaling)

### src/mongo/util/version\_reporting.cpp

<div></div>

    mongo::printSysInfo()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::openSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/version\_mongos.cpp](../sharding)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::printAllocator()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::printGitVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::printOpenSSLVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/util/base64.cpp

<div></div>

    mongo::base64::chars

- Used By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::base64::encode(std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::encode(char const*, int)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::decode(std::string const&)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::encode(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&, char const*, int)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

### src/mongo/util/compress.cpp

<div></div>

    mongo::maxCompressedLength(unsigned long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::compress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    mongo::rawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

### src/mongo/util/concurrency/thread\_pool.cpp

<div></div>

    mongo::threadpool::ThreadPool::ThreadPool(int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::~ThreadPool()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::schedule(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::join()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

### src/mongo/util/exception\_filter\_win32.cpp

<div></div>

    mongo::setWindowsUnhandledExceptionFilter()

- Used By:

    - [src/mongo/unittest/unittest\_main.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)

# Dependencies

### src/mongo/util/safe\_num\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/stacktrace.cpp

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/util/string\_map\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/stringutils\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/tcmalloc\_server\_status\_section.cpp

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    MallocExtension::instance()

- Provided By:

    - [src/third\_party/gperftools-2.0/src/malloc\_extension.cc](../gperftools)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/util/text\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/time\_support.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/time\_support\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/touch\_pages.cpp

<div></div>

    mongo::g_minOSPageSizeBytes

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

### src/mongo/util/util.cpp

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/util/version\_reporting.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::gitVersion()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../build\_information)

<div></div>

    mongo::allocator()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::compiledJSEngine()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::getSSLVersion(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::versionArray

- Provided By:

    - [src/mongo/util/version.cpp](../build\_information)

<div></div>

    mongo::loaderFlags()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

<div></div>

    mongo::sysInfo()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

<div></div>

    mongo::compilerFlags()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_information)

### src/mongo/util/version\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::toVersionArray(char const*)

- Provided By:

    - [src/mongo/util/version.cpp](../build\_information)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/compress.cpp

<div></div>

    snappy::Uncompress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    snappy::MaxCompressedLength(unsigned long)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    snappy::RawCompress(char const*, unsigned long, char*, unsigned long*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

### src/mongo/util/concurrency/thread\_pool.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::thread::join()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/util/descriptive\_stats\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Platform specific code? TODO: Verify this and document what they are for.

# Files
- src/mongo/platform/atomic\_intrinsics.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_gcc\_generic.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_gcc\_intel.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_win32.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_word.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_word\_test.cpp   ()
- src/mongo/platform/backtrace.cpp   (mongod, tools, mongos)
- src/mongo/platform/backtrace.h   (mongod, tools, mongos)
- src/mongo/platform/basic.h   (mongod, tools, mongos)
- src/mongo/platform/bits.h   (mongod, tools)
- src/mongo/platform/bits\_test.cpp   ()
- src/mongo/platform/compiler.h   (mongod, tools, mongos)
- src/mongo/platform/compiler\_gcc.h   (mongod, tools, mongos)
- src/mongo/platform/compiler\_msvc.h   (mongod, tools, mongos)
- src/mongo/platform/cstdint.h   (mongod, tools, mongos)
- src/mongo/platform/float\_utils.h   (mongod, tools, mongos)
- src/mongo/platform/hash\_namespace.h   (mongod, tools, mongos)
- src/mongo/platform/posix\_fadvise.cpp   (mongod, tools, mongos)
- src/mongo/platform/posix\_fadvise.h   (mongod, tools, mongos)
- src/mongo/platform/process\_id.cpp   (mongod, tools, mongos)
- src/mongo/platform/process\_id.h   (mongod, tools, mongos)
- src/mongo/platform/process\_id\_test.cpp   ()
- src/mongo/platform/random.cpp   (mongod, tools, mongos)
- src/mongo/platform/random.h   (mongod, tools, mongos)
- src/mongo/platform/random\_test.cpp   ()
- src/mongo/platform/strcasestr.cpp   (mongod, tools, mongos)
- src/mongo/platform/strcasestr.h   (mongod, tools, mongos)
- src/mongo/platform/strtoll.h   (mongod, tools, mongos)
- src/mongo/platform/unordered\_map.h   (mongod, tools, mongos)
- src/mongo/platform/unordered\_set.h   (mongod, tools, mongos)
- src/mongo/platform/windows\_basic.h   (mongod, tools, mongos)
- src/mongo/util/platform\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo.h   (mongod, tools, mongos)
- src/mongo/util/processinfo\_darwin.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo\_test.cpp   ()
- src/mongo/util/mongoutils/checksum.h   (mongod, tools)
- src/mongo/util/mongoutils/hash.h   (mongod, tools)
- src/mongo/util/mongoutils/html.h   (mongod, tools, mongos)
- src/mongo/util/mongoutils/str.h   (mongod, tools, mongos)

# Interface

### src/mongo/platform/process\_id.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Used By:

    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProcessId::getCurrent()

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/bson/oid.cpp](../bson)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ProcessId::toString() const

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ProcessId::asLongLong() const

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

### src/mongo/platform/random.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(unsigned int)

- Used By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

<div></div>

    mongo::SecureRandom::create()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

<div></div>

    mongo::PseudoRandom::nextInt64()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

### src/mongo/util/processinfo.cpp

<div></div>

    mongo::ProcessInfo::systemInfo

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<div></div>

    mongo::writePidFile(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

### src/mongo/util/processinfo\_darwin.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::blockInMemory(void const*)

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProcessInfo::getExtraInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)

<div></div>

    mongo::ProcessInfo::pagesInMemory(void const*, unsigned long, std::vector<char, std::allocator<char> >*)

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

# Dependencies

### src/mongo/platform/atomic\_word\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/platform/bits\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/platform/process\_id\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/platform/random\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/util/processinfo.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/util/processinfo\_darwin.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/util/processinfo\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

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

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
