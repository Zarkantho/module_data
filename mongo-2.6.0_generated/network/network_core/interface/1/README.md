
# Interface for Socket
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/sock.cpp

<div></div>

    mongo::hostbyname(char const*)

- Used By:

    - [src/mongo/dbtests/socktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Socket::unsafe_recv(char*, int)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    typeinfo for mongo::SocketException

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::portRecvFlags

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)

<div></div>

    mongo::prettyHostName()

- Used By:

    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Socket::send(char const*, int, char const*)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::Socket::~Socket()

- Used By:

    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::Socket::isStillConnected()

- Used By:

    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::unknownAddress

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::portSendFlags

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)

<div></div>

    mongo::Socket::Socket(double, mongo::logger::LogSeverity)

- Used By:

    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::SockAddr::isLocalHost() const

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Socket::setTimeout(double)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Socket::connect(mongo::SockAddr&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::getHostNameCached()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::enableIPv6(bool)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::Socket::secure(mongo::SSLManagerInterface*, std::string const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    mongo::SockAddr::getAddr() const

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::SockAddr::toString(bool) const

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::IPv6Enabled()

- Used By:

    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::SockAddr::SockAddr(char const*, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../../../../network/rest\_client)

<div></div>

    vtable for mongo::SocketException

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Socket::handleSendError(int, char const*)

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)

<div></div>

    mongo::Socket::handleRecvError(int, int)

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)

<div></div>

    mongo::Socket::close()

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::getHostName()

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Socket::doSSLHandshake(char const*, int)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
