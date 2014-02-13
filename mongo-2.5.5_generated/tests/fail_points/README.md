# fail\_points

# Module Groups

-------------

# Group Description
Library for adding fail points into the code for testing purposes

# Files
- src/mongo/util/fail\_point.cpp   (mongod, tools, mongos)
- src/mongo/util/fail\_point.h   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_registry.cpp   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_registry.h   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_service.cpp   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_service.h   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_test.cpp   ()

# Interface

### src/mongo/util/fail\_point.cpp

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::ScopedFailPoint::getData() const

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ScopedFailPoint::ScopedFailPoint(mongo::FailPoint*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ScopedFailPoint::~ScopedFailPoint()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::FailPoint::toBSON() const

- Used By:

    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)

<div></div>

    mongo::FailPoint::FailPoint()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::FailPoint::setMode(mongo::FailPoint::Mode, unsigned int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

### src/mongo/util/fail\_point\_registry.cpp

<div></div>

    mongo::FailPointRegistry::getFailPoint(std::string const&) const

- Used By:

    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/util/fail\_point\_service.cpp

<div></div>

    mongo::getGlobalFailPointRegistry()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

# Dependencies

### src/mongo/util/fail\_point.cpp

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

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

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

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

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/util/fail\_point\_registry.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/fail\_point\_service.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/util/fail\_point\_test.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

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

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::thread::interrupt()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::join()

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

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)
