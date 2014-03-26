
# Interface

### src/mongo/util/net/ssl\_manager.cpp

<div></div>

    mongo::sslGlobalParams

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)
    - [src/mongo/util/net/message\_port.cpp](../../../network\_core)

<div></div>

    mongo::isSSLServer

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::getSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../../../utilities)

<div></div>

    mongo::getSSLManager()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/util/net/listen.cpp](../../../network\_core)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/util/net/httpclient.cpp](../../../rest\_client)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network\_core)
    - [src/mongo/util/background.cpp](../../../utilities)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)

<div></div>

    mongo::SSLConnection::~SSLConnection()

- Used By:

    - [src/mongo/util/net/sock.cpp](../../../network\_core)
