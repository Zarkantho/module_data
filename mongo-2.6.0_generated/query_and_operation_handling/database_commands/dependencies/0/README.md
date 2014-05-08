
# Interface for Commands Registration Class
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/commands.cpp

<div></div>

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::audit::logCommandAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::mutablebson::Document const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../../../../security/authorization)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::AuthorizationSession::getAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::ActionType::connPoolSync

- Provided By:

    - [build/darwin/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

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

    mongo::AuthorizationManager::isAuthEnabled() const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)

<div></div>

    mongo::DBConnectionPool::flush()

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ActionType::connPoolStats

- Provided By:

    - [build/darwin/ssl/mongo/db/auth/action\_type.cpp](../../../../security/authorization)

<div></div>

    mongo::shardConnectionPool

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)
