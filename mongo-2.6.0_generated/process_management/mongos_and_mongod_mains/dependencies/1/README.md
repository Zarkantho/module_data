
# Interface for Mongos Main
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/server.cpp

<div></div>

    mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    vtable for mongo::UserCacheInvalidator

- Provided By:

    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)

<div></div>

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function<void (std::string const&, std::string const&)>)

- Provided By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::addHook(mongo::DBConnectionHook*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for mongo::SocketException

- Provided By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::VersionType::VersionType()

- Provided By:

    - [src/mongo/s/type\_config\_version.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::DBClientConnection::_lazyKillCursor

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

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

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ConfigServer::ok(bool)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    vtable for mongo::ShardingConnectionHook

- Provided By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Provided By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)

<div></div>

    mongo::initializeServerGlobalState()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::signalForkSuccess()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::isSSLServer

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)

<div></div>

    mongo::VersionType::~VersionType()

- Provided By:

    - [src/mongo/s/type\_config\_version.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Provided By:

    - [src/mongo/util/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CursorCache::startTimeoutThread()

- Provided By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::startConfigServerChecker()

- Provided By:

    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::AuthorizationManager::initialize()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::balancer

- Provided By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)

- Provided By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ClientInfo::create(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardConnection::releaseMyConnections()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ConfigServer::reloadSettings()

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Request::process(int)

- Provided By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::AuthzManagerExternalStateMongos::AuthzManagerExternalStateMongos()

- Provided By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::shardConnectionPool

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::setupSignalHandlers()

- Provided By:

    - [src/mongo/util/signal\_handlers.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Request::init()

- Provided By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)

<div></div>

    mongo::webServerThread(mongo::AdminAccess const*)

- Provided By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Grid::setAllowLocalHost(bool)

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ConfigServer::replicaSetChange(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::serverID

- Provided By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::forkServerOrDie()

- Provided By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::cmdline_utils::censorArgvArray(int, char**)

- Provided By:

    - [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Grid::allowLocalHost() const

- Provided By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::runGlobalInitializers(int, char const* const*, char const* const*)

- Provided By:

    - [src/mongo/base/initializer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::mongosGlobalParams

- Provided By:

    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::printShardingVersionInfo(bool)

- Provided By:

    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::startSignalProcessingThread()

- Provided By:

    - [src/mongo/util/signal\_handlers.cpp](../../../../utilities/utilities)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbmessage.cpp](../../../../network/network\_core)
