
# Interface for Oplog
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/repl/oplog.cpp

<div></div>

    mongo::Helpers::findById(mongo::Collection*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::replOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

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

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Scope::storedFuncMod()

- Provided By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool, mongo::PregeneratedKeys const*)

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SpinLock::SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::OpTime::notifier

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::_runCommands(char const*, mongo::BSONObj&, mongo::_BufBuilder<mongo::TrivialAllocator>&, mongo::BSONObjBuilder&, bool, int)

- Provided By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::IndexBuilder::IndexBuilder(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::IndexCatalog::haveIdIndex() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

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

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logOpForDbHash(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::resetSlaveCache()

- Provided By:

    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::OpTime::m

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::Collection::isCapped() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

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

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::OpDebug::reset()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::SpinLock::~SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::logOpForSharding(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Collection::insertDocument(mongo::DocWriter const*, bool)

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::ensureHaveIdIndex()

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)

<div></div>

    mongo::OpTime::last

- Provided By:

    - [src/mongo/bson/optime.cpp](../../../../bson/bson)

<div></div>

    mongo::IndexBuilder::~IndexBuilder()

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::reverseNaturalObj

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ErrorMsg::ErrorMsg(char const*, char)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBuilder::build(mongo::Client::Context&) const

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
