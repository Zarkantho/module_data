# tools

# Module Groups

-------------

# Group Description
Tools and tool options. For most tools, just prepend "mongo" to get the name of the tool the file  is for. For example, "bridge.cpp" is the main for "mongobridge".

# Files
- src/mongo/tools/bridge.cpp   (tools)
- src/mongo/tools/bsondump.cpp   (tools)
- src/mongo/tools/bsondump\_options.cpp   (tools)
- src/mongo/tools/bsondump\_options.h   (tools)
- src/mongo/tools/bsondump\_options\_init.cpp   (tools)
- src/mongo/tools/bsondump\_options\_test.cpp   ()
- src/mongo/tools/dump.cpp   (tools)
- src/mongo/tools/export.cpp   (tools)
- src/mongo/tools/files.cpp   (tools)
- src/mongo/tools/import.cpp   (tools)
- src/mongo/tools/mongobridge\_options.cpp   (tools)
- src/mongo/tools/mongobridge\_options.h   (tools)
- src/mongo/tools/mongobridge\_options\_init.cpp   (tools)
- src/mongo/tools/mongobridge\_options\_test.cpp   ()
- src/mongo/tools/mongodump\_options.cpp   (tools)
- src/mongo/tools/mongodump\_options.h   (tools)
- src/mongo/tools/mongodump\_options\_init.cpp   (tools)
- src/mongo/tools/mongodump\_options\_test.cpp   ()
- src/mongo/tools/mongoexport\_options.cpp   (tools)
- src/mongo/tools/mongoexport\_options.h   (tools)
- src/mongo/tools/mongoexport\_options\_init.cpp   (tools)
- src/mongo/tools/mongoexport\_options\_test.cpp   ()
- src/mongo/tools/mongofiles\_options.cpp   (tools)
- src/mongo/tools/mongofiles\_options.h   (tools)
- src/mongo/tools/mongofiles\_options\_init.cpp   (tools)
- src/mongo/tools/mongofiles\_options\_test.cpp   ()
- src/mongo/tools/mongoimport\_options.cpp   (tools)
- src/mongo/tools/mongoimport\_options.h   (tools)
- src/mongo/tools/mongoimport\_options\_init.cpp   (tools)
- src/mongo/tools/mongoimport\_options\_test.cpp   ()
- src/mongo/tools/mongooplog\_options.cpp   (tools)
- src/mongo/tools/mongooplog\_options.h   (tools)
- src/mongo/tools/mongooplog\_options\_init.cpp   (tools)
- src/mongo/tools/mongooplog\_options\_test.cpp   ()
- src/mongo/tools/mongorestore\_options.cpp   (tools)
- src/mongo/tools/mongorestore\_options.h   (tools)
- src/mongo/tools/mongorestore\_options\_init.cpp   (tools)
- src/mongo/tools/mongorestore\_options\_test.cpp   ()
- src/mongo/tools/mongostat\_options.cpp   (tools)
- src/mongo/tools/mongostat\_options.h   (tools)
- src/mongo/tools/mongostat\_options\_init.cpp   (tools)
- src/mongo/tools/mongostat\_options\_test.cpp   ()
- src/mongo/tools/mongotop\_options.cpp   (tools)
- src/mongo/tools/mongotop\_options.h   (tools)
- src/mongo/tools/mongotop\_options\_init.cpp   (tools)
- src/mongo/tools/mongotop\_options\_test.cpp   ()
- src/mongo/tools/oplog.cpp   (tools)
- src/mongo/tools/restore.cpp   (tools)
- src/mongo/tools/sniffer.cpp   (tools)
- src/mongo/tools/stat.cpp   (tools)
- src/mongo/tools/stat\_util.cpp   (tools)
- src/mongo/tools/stat\_util.h   (tools)
- src/mongo/tools/tool.cpp   (tools)
- src/mongo/tools/tool.h   (tools)
- src/mongo/tools/tool\_logger.cpp   (tools)
- src/mongo/tools/tool\_logger.h   (tools)
- src/mongo/tools/tool\_options.cpp   (tools)
- src/mongo/tools/tool\_options.h   (tools)
- src/mongo/tools/top.cpp   (tools)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/tools/bridge.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Listener::Listener(std::string const&, std::string const&, int, bool)

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::recv(mongo::Message&)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::MessagingPort::shutdown()

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Listener::accepted(boost::shared_ptr<mongo::Socket>, long long)

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::MessagingPort::say(mongo::Message&, int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::Listener::~Listener()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::SockAddr::toString(bool) const

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::ListeningSockets::get()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Listener::initAndListen()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Listener::setupSockets()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

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

    typeinfo for mongo::Listener

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::MessagingPort::call(mongo::Message&, mongo::Message&)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/tools/bsondump.cpp

<div></div>

    mongo::isValidUTF8(char const*)

- Provided By:

    - [src/mongo/util/text.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

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

### src/mongo/tools/bsondump\_options.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/tools/bsondump\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/bsondump\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/dump.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

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

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::LogIndentLevel::~LogIndentLevel()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Query::snapshot()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::LogIndentLevel::LogIndentLevel()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::errnoWithPrefix(char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logContext(char const*)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    typeinfo for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

### src/mongo/tools/export.cpp

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Query::snapshot()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Query::Query(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/tools/files.cpp

<div></div>

    mongo::GridFS::findFile(std::string const&) const

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    pcrecpp::RE::QuoteMeta(pcrecpp::StringPiece const&)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::GridFS::~GridFS()

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

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

    mongo::GridFS::storeFile(std::string const&, std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::GridFS::list(mongo::BSONObj) const

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::GridFile::write(std::string const&) const

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::GridFS::GridFS(mongo::DBClientBase&, std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::GridFS::removeFile(std::string const&)

- Provided By:

    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

### src/mongo/tools/import.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    mongo::isValidUTF8(char const*)

- Provided By:

    - [src/mongo/util/text.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

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

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

### src/mongo/tools/mongobridge\_options.cpp

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongobridge\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongobridge\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongodump\_options.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionDescription::requires(std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/tools/mongodump\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongodump\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongoexport\_options.cpp

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

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

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/tools/mongoexport\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongoexport\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongofiles\_options.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

### src/mongo/tools/mongofiles\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongofiles\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

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

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongoimport\_options.cpp

<div></div>

    mongo::StringSplitter::split(std::vector<std::string, std::allocator<std::string> >&)

- Provided By:

    - [src/mongo/util/text.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

### src/mongo/tools/mongoimport\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongoimport\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongooplog\_options.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/tools/mongooplog\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongooplog\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongorestore\_options.cpp

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

### src/mongo/tools/mongorestore\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongorestore\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongostat\_options.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/tools/mongostat\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongostat\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/mongotop\_options.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/tools/mongotop\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/mongotop\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::isEmpty() const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::getAllOptions(std::vector<mongo::optionenvironment::OptionDescription, std::allocator<mongo::optionenvironment::OptionDescription> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

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

    mongo::optionenvironment::Value::equal(mongo::optionenvironment::Value const&) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/oplog.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::OplogReader::OplogReader()

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::OplogReader::tailingQueryGTE(char const*, mongo::OpTime, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::OplogReader::connect(std::string const&)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/tools/restore.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    boost::filesystem3::path::parent_path() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

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

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::DBClientWithCommands::getLastError(std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/tools/sniffer.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MemoryMappedFile::close()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MemoryMappedFile

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LockMongoFilesShared::era

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::get_tss_data(void const*)

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

    mongo::MessagingPort::say(mongo::Message&, int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::MessagingPort::call(mongo::Message&, mongo::Message&)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::UserException::appendPrefix(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/stat.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBClientConnection::_checkConnection()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::saslCommandUserDBFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::StringSplitter::next()

- Provided By:

    - [src/mongo/util/text.cpp](../utilities)

<div></div>

    mongo::HttpClient::get(std::string const&, mongo::HttpClient::Result*)

- Provided By:

    - [src/mongo/util/net/httpclient.cpp](../network)

<div></div>

    mongo::saslCommandMechanismFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/tools/stat\_util.cpp

<div></div>

    mongo::time_t_to_Struct(long, tm*, bool)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

### src/mongo/tools/tool.cpp

<div></div>

    mongo::DBClientReplicaSet::slaveConn()

- Provided By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthzManagerExternalStateMock::AuthzManagerExternalStateMock()

- Provided By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::Query::Query(char const*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::FileAllocator::start()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::dur::startup()

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::acquirePathLock(bool)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::saslCommandUserDBFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::saslCommandMechanismFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/tools/tool\_logger.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Console::out()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::clearAppenders()

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../logging\_system)

<div></div>

    vtable for mongo::logger::MessageEventUnadornedEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::setRawOutToStderr()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../logging\_system)

<div></div>

    mongo::Console::Console()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    vtable for mongo::logger::MessageEventDetailsEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogManager::getNamedDomain(std::string const&)

- Provided By:

    - [src/mongo/logger/log\_manager.cpp](../logging\_system)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/tools/tool\_options.cpp

<div></div>

    pcrecpp::Arg::parse_string(char const*, int, void*)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::enableIPv6(bool)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    pcrecpp::RE::no_arg

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../utilities)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::addSSLClientOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::storeSSLClientOptions(mongo::optionenvironment::Environment const&)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::gitVersion()

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp](../build\_generated\_files)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/client\_build/mongo/buildinfo.cpp](../build\_generated\_files)

<div></div>

    mongo::askPassword()

- Provided By:

    - [src/mongo/util/password.cpp](../startup\_initialization)

<div></div>

    pcrecpp::RE::~RE()

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    pcrecpp::RE::Consume(pcrecpp::StringPiece*, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/tools/top.cpp

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::terseCurrentTime(bool)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)
