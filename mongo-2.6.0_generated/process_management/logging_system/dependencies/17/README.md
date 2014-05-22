
# Interface for Extra Log Context
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/server\_extra\_log\_context.cpp

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNames()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../../../../security/authorization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ClientBasic::hasAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
