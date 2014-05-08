
# Interface for Shell Core
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/shell/dbshell.cpp

<div></div>

    mongo::Console::Console()

- Provided By:

    - [src/mongo/logger/console.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::dbexitCalled

- Provided By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::saslCommandPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ScriptEngine::_connectCallback

- Provided By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::isShell

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::saslCommandServiceHostnameFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Provided By:

    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    vtable for mongo::logger::MessageEventUnadornedEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Scope::invoke(char const*, mongo::BSONObj const*, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)

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

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    pcrecpp::RE::~RE()

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../../../../third\_party/pcrecpp)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Console::out()

- Provided By:

    - [src/mongo/logger/console.cpp](../../../../process\_management/logging\_system)

<div></div>

    pcrecpp::RE::no_arg

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../../../../third\_party/pcrecpp)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../../../../third\_party/pcrecpp)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::logger::LogManager::getNamedDomain(std::string const&)

- Provided By:

    - [src/mongo/logger/log\_manager.cpp](../../../../process\_management/logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::askPassword()

- Provided By:

    - [src/mongo/util/password.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    pcrecpp::RE::PartialMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../../../../third\_party/pcrecpp)

<div></div>

    mongo::ScriptEngine::setup()

- Provided By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::StartupTest::runTests()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../../../../utilities/utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

### src/mongo/shell/shell\_utils.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)

<div></div>

    mongo::isAnyIndexKeyTooLarge(mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index/external\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::validateKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/catalog/index\_key\_validate.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ScriptEngine::getInterpreterVersionString()

- Provided By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::ErrorCodes::errorString(mongo::ErrorCodes::Error)

- Provided By:

    - [build/darwin/ssl/mongo/base/error\_codes.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)

### src/mongo/shell/shell\_utils\_extended.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../../../../utilities/utilities)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::File::is_open() const

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::getHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::File::read(unsigned long long, char*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

### src/mongo/shell/shell\_utils\_launcher.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    mongo::dbexitCalled

- Provided By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Provided By:

    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::fassertFailed(int)

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

    boost::filesystem3::detail::initial_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::ProcessId::toString() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::ProcessId::asLongLong() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)
