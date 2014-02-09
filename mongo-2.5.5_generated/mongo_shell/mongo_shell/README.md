# mongo\_shell

# Module Groups

-------------

# Group Description
C++ files that are automatically generated from the Javascript source files. This means that certain Javascript files work in the shell because they are actually compiled in, which means that sometimes the server needs to be recompiled to see changes in Javascript files

# Files
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/shell/mongo-server.cpp   ()
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/shell/mongo.cpp   (mongod, tools, mongos)

# Interface

### build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/shell/mongo.cpp

<div></div>

    mongo::JSFiles::utils

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::batch_api

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::mongo

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::query

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::collection

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::utils_sh

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::assert

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::db

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::types

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

<div></div>

    mongo::JSFiles::mr

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Javascript files that get wrapped in strings and put in cpp files. See the "env.JSHeader" calls  in src/mongo/SConscript and shell/createCPPfromJavaScriptFiles.js

# Files
- src/mongo/shell/assert.js   (mongod, tools, mongos)
- src/mongo/shell/batch\_api.js   (mongod, tools, mongos)
- src/mongo/shell/collection.js   (mongod, tools, mongos)
- src/mongo/shell/db.js   (mongod, tools, mongos)
- src/mongo/shell/mongo.js   (mongod, tools, mongos)
- src/mongo/shell/mr.js   (mongod, tools, mongos)
- src/mongo/shell/query.js   (mongod, tools, mongos)
- src/mongo/shell/replsetbridge.js   ()
- src/mongo/shell/replsettest.js   ()
- src/mongo/shell/servers.js   ()
- src/mongo/shell/servers\_misc.js   ()
- src/mongo/shell/shardingtest.js   ()
- src/mongo/shell/types.js   (mongod, tools, mongos)
- src/mongo/shell/utils.js   (mongod, tools, mongos)
- src/mongo/shell/utils\_sh.js   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Files only built into the mongo shell

# Files
- src/mongo/shell/dbshell.cpp   ()
- src/mongo/shell/linenoise.cpp   ()
- src/mongo/shell/linenoise.h   ()
- src/mongo/shell/linenoise\_utf8.cpp   ()
- src/mongo/shell/linenoise\_utf8.h   ()
- src/mongo/shell/mk\_wcwidth.cpp   ()
- src/mongo/shell/mk\_wcwidth.h   ()
- src/mongo/shell/shell\_utils.cpp   ()
- src/mongo/shell/shell\_utils.h   ()
- src/mongo/shell/shell\_utils\_extended.cpp   ()
- src/mongo/shell/shell\_utils\_extended.h   ()
- src/mongo/shell/shell\_utils\_launcher.cpp   ()
- src/mongo/shell/shell\_utils\_launcher.h   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/shell/dbshell.cpp

<div></div>

    mongo::Console::Console()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    mongo::dbexitCalled

- Provided By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::ScriptEngine::_connectCallback

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::isShell

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

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

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Provided By:

    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    vtable for mongo::logger::MessageEventUnadornedEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::Scope::invoke(char const*, mongo::BSONObj const*, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../logging\_system)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

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

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    pcrecpp::RE::~RE()

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Console::out()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    pcrecpp::RE::no_arg

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../build\_information)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogManager::getNamedDomain(std::string const&)

- Provided By:

    - [src/mongo/logger/log\_manager.cpp](../logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::askPassword()

- Provided By:

    - [src/mongo/util/password.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    pcrecpp::RE::PartialMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::ScriptEngine::setup()

- Provided By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

<div></div>

    mongo::StartupTest::runTests()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/shell/shell\_utils.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ScriptEngine::getInterpreterVersionString()

- Provided By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

### src/mongo/shell/shell\_utils\_extended.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

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

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::is_open() const

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::getHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::File::read(unsigned long long, char*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/shell/shell\_utils\_launcher.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::dbexitCalled

- Provided By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

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

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Provided By:

    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    boost::filesystem3::detail::initial_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ProcessId::toString() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

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

    mongo::ProcessId::asLongLong() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

-------------

# Group Description
Shell command line options

# Files
- src/mongo/shell/shell\_options.cpp   ()
- src/mongo/shell/shell\_options.h   ()
- src/mongo/shell/shell\_options\_init.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/shell/shell\_options.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

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

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

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

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../build\_information)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

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

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/shell/shell\_options\_init.cpp

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
