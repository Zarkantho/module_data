
# Interface for Mongos Specific Client State
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/s\_only.cpp

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, bool, std::string const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/cpp\_client\_driver)

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

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

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

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::AuthzSessionExternalStateMongos::AuthzSessionExternalStateMongos(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authz\_session\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    mongo::Command::_checkAuthorization(mongo::Command*, mongo::ClientBasic*, std::string const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LastErrorHolder::initThread()

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/cpp\_client\_driver)
