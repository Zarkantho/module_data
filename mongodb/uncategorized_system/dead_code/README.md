# dead\_code

# Module Groups

-------------

# Group Description


# Files
- src/mongo/util/trace.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/db/tests.cpp   (mongod, tools)
- src/mongo/db/stats/service\_stats.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/service\_stats.h   (mongod, tools, mongos)
- src/mongo/util/histogram.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/histogram.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/dbtests/histogram\_test.cpp   ()
- src/mongo/util/lruishmap.h   (mongod, tools, mongos)
- src/mongo/db/taskqueue.h   (mongod, tools)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/util/trace.cpp

<div></div>

    mongo::SimpleRWLock::lock_shared()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::unlock()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::unlock_shared()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::lock()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::SimpleRWLock(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::lock_shared()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::unlock()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::unlock_shared()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::lock()

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

<div></div>

    mongo::SimpleRWLock::SimpleRWLock(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/concurrency/rwlockimpl.cpp](../concurrency)

### src/mongo/db/tests.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

### src/mongo/db/stats/service\_stats.cpp

<div></div>

    mongo::SpinLock::SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

<div></div>

    mongo::SpinLock::~SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/dbtests/histogram\_test.cpp

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::Suite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::demangleName(std::type_info const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Suite

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::unittest::Suite::~Suite()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)
