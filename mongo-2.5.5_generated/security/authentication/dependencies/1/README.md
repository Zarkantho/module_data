
# Interface for Authentication Commands
This dependency information represents symbolsthat are used in this group but defined in other modules.  Does not includesymbols used in this group that are defined inside this module.

### src/mongo/db/commands/authentication\_commands.cpp

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../security/authorization)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../security/authorization)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../utilities/utilities)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::mutablebson::Element::rightSibling(unsigned long) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::User::getCredentials() const

- Provided By:

    - [src/mongo/db/auth/user.cpp](../../../security/authorization)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::AuthorizationSession::logoutDatabase(std::string const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../security/authorization)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities/utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::mutablebson::Element::findElementNamed(mongo::StringData const&) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::internalSecurity

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../security/authorization)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../network/ssl)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::User::getName() const

- Provided By:

    - [src/mongo/db/auth/user.cpp](../../../security/authorization)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../queries/client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../security/authorization)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../../../utilities/utilities)

<div></div>

    mongo::SecureRandom::create()

- Provided By:

    - [src/mongo/platform/random.cpp](../../../utilities/utilities)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../../../network/cpp\_client\_driver)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../security/authorization)

<div></div>

    mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::findFirstChildNamed(mongo::StringData const&) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../bson/mutable\_bson)

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/auth/user\_name.cpp](../../../security/authorization)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../../../utilities/base\_utilites)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../process\_management/startup\_initialization)

<div></div>

    mongo::audit::logAuthentication(mongo::ClientBasic*, mongo::StringData const&, mongo::UserName const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../security/auditing)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../utilities/base\_utilites)
