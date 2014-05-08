
# Interface for Legacy Instance File
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/instance.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::_unlockFsync()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::UpdateExecutor::execute()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::Client::clients

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::audit::logInsertAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::UpdateExecutor::~UpdateExecutor()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::UpdateExecutor::UpdateExecutor(mongo::UpdateRequest const*, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::GeneratorHolder::getInstance()

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::UpdateExecutor::prepare()

- Provided By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::DeleteExecutor::~DeleteExecutor()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DeleteExecutor::DeleteExecutor(mongo::DeleteRequest const*)

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::AuthorizationSession::startRequest()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::nsGetDB(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ExceptionInfo::append(mongo::BSONObjBuilder&, char const*, char const*) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::oplogCheckCloseDatabase(mongo::Database*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)

<div></div>

    mongo::audit::logKillOpAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::lockedForWriting()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ActionType::inprog

- Provided By:

    - [build/darwin/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::dur::haveJournalFiles(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::ActionType::unlock

- Provided By:

    - [build/darwin/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../../../../utilities/utilities)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/dbmessage.cpp](../../../../network/network\_core)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CurOp::info()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::audit::logUpdateAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::setPostRunCommandHook(boost::function<void (mongo::BSONObj const&, std::string const&)>)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::ActionType::killop

- Provided By:

    - [build/darwin/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::MessagingPort::closeAllSockets(unsigned int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../../../../network/network\_core)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../../../../bson/bson)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ListeningSockets::get()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::KillCurrentOp::killAll()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::dur::journalCleanup(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::dur::commitJob

- Provided By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DeleteExecutor::execute()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::ReplSet::shutdown()

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::GeneratorHolder::prepare(mongo::StringData const&, mongo::BSONObj const&, mongo::PregeneratedKeys*)

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::audit::logQueryAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::OpTime::m

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::audit::logInProgAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::runCount(std::string const&, mongo::BSONObj const&, std::string&, int&)

- Provided By:

    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::OpDebug::reset()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::directDBClient

- Provided By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../../../../tests/fail\_points)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::DeleteExecutor::prepare()

- Provided By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Provided By:

    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::audit::logDeleteAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::readlocktry::~readlocktry()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::audit::logFsyncUnlockAuthzCheck(mongo::ClientBasic*, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Lock::isReadLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    typeinfo for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../../../../third\_party/boost\_filesystem)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)

- Provided By:

    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::audit::logGetMoreAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Client::clientsMutex

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
