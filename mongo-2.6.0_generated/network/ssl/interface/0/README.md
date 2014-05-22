
# Interface for SSL Manager
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/ssl\_manager.cpp

<div></div>

    mongo::getSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SSLConnection::~SSLConnection()

- Used By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::isSSLServer

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::getSSLManager()

- Used By:

    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/util/background.cpp](../../../../utilities/utilities)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::sslGlobalParams

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/net/message\_port.cpp](../../../../network/network\_core)
