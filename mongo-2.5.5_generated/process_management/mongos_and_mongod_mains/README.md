# mongos\_and\_mongod\_mains

# Module Groups

-------------

# Group Description
Main for mongod

# Files
- src/mongo/db/db.cpp   (mongod)
- src/mongo/db/db.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/db.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::rotateLogs()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::getDeleter()

- Provided By:

    - [src/mongo/db/range\_deleter\_service.cpp](../sharding)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ProcessId::asLongLong() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ScriptEngine::_getCurrentOpIdCallback

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Database::_initExtentFreeList()

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::_diaglog

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ScriptEngine::_checkInterruptCallback

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::startupWarningsLog

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logStartupWarnings()

- Provided By:

    - [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::sleepmicros(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::initializeServerGlobalState()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::startReplication()

- Provided By:

    - [src/mongo/db/repl/repl\_start.cpp](../replication)

<div></div>

    mongo::DiagLog::flush()

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dur::startup()

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::curTimeMicros()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

    mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::RangeDeleter::startWorkers()

- Provided By:

    - [src/mongo/db/range\_deleter.cpp](../sharding)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::dbExecCommand

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::snapshotThread

- Provided By:

    - [src/mongo/db/stats/snapshots.cpp](../utilities)

<div></div>

    mongo::d

- Provided By:

    - [src/mongo/db/d\_globals.cpp](../legacy\_code)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::AuthorizationManager::initialize()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::isSSLServer

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexNames::HASHED

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::FileAllocator::start()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::getCollectionNames(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::startTTLBackgroundJob()

- Provided By:

    - [src/mongo/db/ttl.cpp](../indexing)

<div></div>

    mongo::Database::clearTmpCollections()

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logProcessDetails()

- Provided By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::indexRebuilder

- Provided By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    vtable for mongo::RestAdminAccess

- Provided By:

    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<div></div>

    mongo::setupSIGTRAPforGDB()

- Provided By:

    - [src/mongo/util/debug\_util.cpp](../utilities)

<div></div>

    mongo::ExtentManager::getFile(int, int, bool)

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

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

    mongo::DBClientWithCommands::createCollection(std::string const&, long long, bool, int, mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessId::toString() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::webServerThread(mongo::AdminAccess const*)

- Provided By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::getHostNameCached()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Client::recommendedYieldMicros(int*, int*, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::AuthzManagerExternalStateMongod::AuthzManagerExternalStateMongod()

- Provided By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::forkServerOrDie()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::acquirePathLock(bool)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::cmdline_utils::censorArgvArray(int, char**)

- Provided By:

    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::runGlobalInitializers(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::findIdIndex() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceIndex::_init()

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_2D

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Provided By:

    - [src/mongo/util/net/message\_server\_port.cpp](../network)

<div></div>

    mongo::MongoFile::totalMappedLength()

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::ScriptEngine::setup()

- Provided By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

<div></div>

    mongo::signalForkSuccess()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::StartupTest::runTests()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::setupCoreSignals()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::logProcessDetailsForLogRotate()

- Provided By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Mongod command line options

# Files
- src/mongo/db/mongod\_options.cpp   (mongod)
- src/mongo/db/mongod\_options.h   (mongod, tools)
- src/mongo/db/mongod\_options\_init.cpp   (mongod)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/mongod\_options.cpp

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::_diaglog

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiagLog::setLevel(int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::startupWarningsLog

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

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

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::enableIPv6(bool)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::mongodVersion()

- Provided By:

    - [src/mongo/util/version.cpp](../utilities)

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

    mongo::optionenvironment::Value::get(unsigned int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::optionenvironment::Value::get(double*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(long*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

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

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::printGitVersion()

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::printOpenSSLVersion()

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/mongod\_options\_init.cpp

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

-------------

# Group Description
Main for mongos

# Files
- src/mongo/s/server.cpp   (mongos)
- src/mongo/s/server.h   (mongod, tools, mongos)

# Interface

### src/mongo/s/server.cpp

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
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
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::dbexitCalled

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

# Dependencies

### src/mongo/s/server.cpp

<div></div>

    mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    vtable for mongo::UserCacheInvalidator

- Provided By:

    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::printStackAndExit(int)

- Provided By:

    - [src/mongo/util/signal\_handlers.cpp](../utilities)

<div></div>

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function<void (std::string const&, std::string const&)>)

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::rotateLogs()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::VersionType::VersionType()

- Provided By:

    - [src/mongo/s/type\_config\_version.cpp](../sharding)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientConnection::_lazyKillCursor

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::setWindowsUnhandledExceptionFilter()

- Provided By:

    - [src/mongo/util/exception\_filter\_win32.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

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

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ConfigServer::ok(bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    vtable for mongo::ShardingConnectionHook

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::initializeServerGlobalState()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::signalForkSuccess()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::setupSIGTRAPforGDB()

- Provided By:

    - [src/mongo/util/debug\_util.cpp](../utilities)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::VersionType::~VersionType()

- Provided By:

    - [src/mongo/s/type\_config\_version.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::CursorCache::startTimeoutThread()

- Provided By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::startConfigServerChecker()

- Provided By:

    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)

<div></div>

    mongo::AuthorizationManager::initialize()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::isSSLServer

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

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

    mongo::balancer

- Provided By:

    - [src/mongo/s/balance.cpp](../sharding)

<div></div>

    mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)

- Provided By:

    - [src/mongo/s/config\_upgrade.cpp](../sharding)

<div></div>

    mongo::ClientInfo::create(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::releaseMyConnections()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ConfigServer::reloadSettings()

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::Request::process(int)

- Provided By:

    - [src/mongo/s/request.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::AuthzManagerExternalStateMongos::AuthzManagerExternalStateMongos()

- Provided By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::shardConnectionPool

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::Request::init()

- Provided By:

    - [src/mongo/s/request.cpp](../sharding)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::webServerThread(mongo::AdminAccess const*)

- Provided By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Grid::setAllowLocalHost(bool)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ConfigServer::replicaSetChange(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::serverID

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::forkServerOrDie()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::cmdline_utils::censorArgvArray(int, char**)

- Provided By:

    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../startup\_initialization)

<div></div>

    mongo::Grid::allowLocalHost() const

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::runGlobalInitializers(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::printShardingVersionInfo(bool)

- Provided By:

    - [src/mongo/s/version\_mongos.cpp](../sharding)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/request.cpp](../sharding)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Provided By:

    - [src/mongo/util/net/message\_server\_port.cpp](../network)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::setupCoreSignals()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::logProcessDetailsForLogRotate()

- Provided By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

-------------

# Group Description
Mongos command line options

# Files
- src/mongo/s/mongos\_options.cpp   (mongos)
- src/mongo/s/mongos\_options.h   (mongod, tools, mongos)
- src/mongo/s/mongos\_options\_init.cpp   (mongos)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/s/mongos\_options.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::printShardingVersionInfo(bool)

- Provided By:

    - [src/mongo/s/version\_mongos.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Chunk::ShouldAutoSplit

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::enableIPv6(bool)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../startup\_initialization)

<div></div>

    mongo::StartupTest::runTests()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

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

    mongo::Chunk::setMaxChunkSizeSizeMB(int)

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

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

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/mongo/s/mongos\_options\_init.cpp

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
