
# Interface for Heath Status Helpers
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/repl/health.cpp

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Consensus::aMajoritySeemsToBeUp() const

- Provided By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::OplogReader::connect(std::string const&)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::replSetBlind

- Provided By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::RamLog::get(std::string const&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::RamLog::toHTML(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::OplogReader::OplogReader()

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::readlocktry::~readlocktry()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::replset::BackgroundSync::get()

- Provided By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::OplogReader::query(char const*, mongo::Query, int, int, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)
