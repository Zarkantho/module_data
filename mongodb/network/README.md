# network

# Module Groups

-------------

# Group Description
Network library   can you say a few words about:   - what this does   - who uses it   - how to use it?

# Files
- src/mongo/util/net/listen.cpp   (mongod, tools, mongos)
- src/mongo/util/net/listen.h
- src/mongo/util/net/hostandport.h
- src/mongo/util/net/message.cpp   (cppclientdriver)
- src/mongo/util/net/message.h
- src/mongo/util/net/message\_port.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message\_port.h
- src/mongo/util/net/httpclient.cpp   (cppclientdriver)
- src/mongo/util/net/httpclient.h
- src/mongo/util/net/sock.cpp   (mongod, tools, mongos)
- src/mongo/util/net/sock.h
- src/mongo/util/net/sock\_test.cpp   ()
- src/mongo/util/net/socket\_poll.cpp   (cppclientdriver)
- src/mongo/util/net/socket\_poll.h
- src/mongo/util/net/ssl\_manager.cpp   (cppclientdriver)
- src/mongo/util/net/ssl\_manager.h
- src/mongo/util/net/ssl\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_options.h

# Interface

### src/mongo/util/net/listen.cpp

<div></div>

    mongo::Listener::globalConnectionNumber

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::Listener::setupSockets()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::Listener::globalTicketHolder

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::Listener::Listener(std::string const&, std::string const&, int, bool)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::Listener::accepted(boost::shared_ptr<mongo::Socket>, long long)

- Used By:

    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::Listener::~Listener()

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::ListeningSockets::get()

- Used By:

    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Listener::_timeTracker

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    mongo::Listener::acceptedMP(mongo::MessagingPort*)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Listener::initAndListen()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    typeinfo for mongo::Listener

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

### src/mongo/util/net/message.cpp

<div></div>

    mongo::Message::send(mongo::MessagingPort&, char const*)

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::nextMessageId()

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::doesOpGetAResponse(int)

- Used By:

    - [src/mongo/s/d\_logic.cpp](../sharding)

### src/mongo/util/net/message\_port.cpp

<div></div>

    mongo::MessagingPort::MessagingPort(double, mongo::logger::LogSeverity)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::say(mongo::Message&, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::MessagingPort::recv(mongo::Message&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::MessagingPort::shutdown()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::MessagingPort::closeAllSockets(unsigned int)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::MessagingPort::piggyBack(mongo::Message&, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::MessagingPort(boost::shared_ptr<mongo::Socket>)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::MessagingPort::setSocketTimeout(double)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::call(mongo::Message&, mongo::Message&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

<div></div>

    mongo::AbstractMessagingPort::setConnectionId(long long)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/util/net/httpclient.cpp

<div></div>

    mongo::HttpClient::get(std::string const&, mongo::HttpClient::Result*)

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/client/examples/httpClientTest.cpp](../cpp\_client\_driver)

### src/mongo/util/net/sock.cpp

<div></div>

    mongo::hostbyname(char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/dbtests/socktests.cpp](../unit\_tests)

<div></div>

    mongo::Socket::unsafe_recv(char*, int)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/httpclient.cpp](../network)

<div></div>

    typeinfo for mongo::SocketException

- Used By:

    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Socket::send(std::vector<std::pair<char*, int>, std::allocator<std::pair<char*, int> > > const&, char const*)

- Used By:

    - [src/mongo/util/net/message.cpp](../network)

<div></div>

    mongo::portRecvFlags

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::prettyHostName()

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Socket::send(char const*, int, char const*)

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/net/message.cpp](../network)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Socket::~Socket()

- Used By:

    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::Socket::isStillConnected()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

<div></div>

    mongo::Socket::recv(char*, int)

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::unknownAddress

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::portSendFlags

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::SockAddr::getPort() const

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp

<div></div>

    mongo::Socket::Socket(double, mongo::logger::LogSeverity)

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/httpclient.cpp](../network)

<div></div>

    mongo::SockAddr::isLocalHost() const

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Socket::setTimeout(double)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::Socket::connect(mongo::SockAddr&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)

<div></div>

    mongo::getHostNameCached()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)

<div></div>

    mongo::enableIPv6(bool)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Socket::secure(mongo::SSLManagerInterface*, std::string const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)

<div></div>

    mongo::SockAddr::getAddr() const

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::SockAddr::toString(bool) const

- Used By:

    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::IPv6Enabled()

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)

<div></div>

    mongo::Socket::secureAccepted(mongo::SSLManagerInterface*)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::SockAddr::SockAddr(char const*, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::disableNagle(int)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    vtable for mongo::SocketException

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Socket::handleRecvError(int, int)

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::makeUnixSockPath(int)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::Socket::close()

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::getHostName()

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::Socket::doSSLHandshake(char const*, int)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::Socket::Socket(int, mongo::SockAddr const&)

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    mongo::Socket::handleSendError(int, char const*)

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::SockAddr::getType() const

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/util/net/socket\_poll.cpp

<div></div>

    mongo::socketPoll(pollfd*, unsigned long, int)

- Used By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::isPollSupported()

- Used By:

    - [src/mongo/util/net/sock.cpp](../network)

### src/mongo/util/net/ssl\_manager.cpp

<div></div>

    mongo::sslGlobalParams

- Used By:

    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/examples/httpClientTest.cpp](../cpp\_client\_driver)

<div></div>

    mongo::isSSLServer

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::getSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::getSSLManager()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/background.cpp](../utilities)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/background.cpp](../utilities)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::SSLConnection::~SSLConnection()

- Used By:

    - [src/mongo/util/net/sock.cpp](../network)

### src/mongo/util/net/ssl\_options.cpp

<div></div>

    mongo::addSSLClientOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)

<div></div>

    mongo::storeSSLServerOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::storeSSLClientOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)

-------------

# Group Description
Top level (?) of handling incoming network connections on mongod and mongos. Inherits from  Listener (listen.h).

# Files
- src/mongo/util/net/message\_server.h
- src/mongo/util/net/message\_server\_port.cpp   (mongod, mongos)

# Interface

### src/mongo/util/net/message\_server\_port.cpp

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
