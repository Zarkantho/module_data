
# Interface for Mongod Client State Implementation
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/client.cpp

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::FileAllocator::hasFailed() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../../security/authorization)

<div></div>

    mongo::LockState::LockState()

- Provided By:

    - [src/mongo/db/lockstate.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::AuthzSessionExternalStateMongod::AuthzSessionExternalStateMongod(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

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

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::dbHolderUnchecked()

- Provided By:

    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::LockState::hasAnyReadLock() const

- Provided By:

    - [src/mongo/db/lockstate.cpp](../../../../queries/concurrency)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../../../../security/authorization)

<div></div>

    mongo::ExceptionInfo::append(mongo::BSONObjBuilder&, char const*, char const*) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::Lock::atLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::ReplSetImpl::registerSlave(mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::LastErrorHolder::initThread()

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::LockStat::report(mongo::StringBuilderImpl<mongo::TrivialAllocator>&) const

- Provided By:

    - [src/mongo/db/lockstat.cpp](../../../../queries/concurrency)

<div></div>

    mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)

- Provided By:

    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::LockState::hasAnyWriteLock() const

- Provided By:

    - [src/mongo/db/lockstate.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::LockStat::report() const

- Provided By:

    - [src/mongo/db/lockstat.cpp](../../../../queries/concurrency)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    mongo::shardVersionOk(std::string const&, std::string&, mongo::ChunkVersion&, mongo::ChunkVersion&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ActionType::internal

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
