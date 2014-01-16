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

- <pre>mongo::Listener::globalConnectionNumber</pre>
Used By:
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

- <pre>mongo::Listener::setupSockets()</pre>
Used By:
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::Listener::globalTicketHolder</pre>
Used By:
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

- <pre>mongo::Listener::Listener(std::string const&, std::string const&, int, bool)</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::Listener::accepted(boost::shared_ptr<mongo::Socket>, long long)</pre>
Used By:
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::Listener::~Listener()</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::ListeningSockets::get()</pre>
Used By:
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::Listener::_timeTracker</pre>
Used By:
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

- <pre>mongo::Listener::acceptedMP(mongo::MessagingPort*)</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

- <pre>mongo::Listener::initAndListen()</pre>
Used By:
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>typeinfo for mongo::Listener</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/bridge.cpp](../tools)

### src/mongo/util/net/message.cpp

- <pre>mongo::Message::send(mongo::MessagingPort&, char const*)</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::nextMessageId()</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::doesOpGetAResponse(int)</pre>
Used By:
    - [src/mongo/s/d\_logic.cpp](../sharding)

### src/mongo/util/net/message\_port.cpp

- <pre>mongo::MessagingPort::MessagingPort(double, mongo::logger::LogSeverity)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

- <pre>mongo::MessagingPort::say(mongo::Message&, int)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::MessagingPort::recv(mongo::Message&)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::MessagingPort::shutdown()</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::MessagingPort::closeAllSockets(unsigned int)</pre>
Used By:
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::MessagingPort::piggyBack(mongo::Message&, int)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

- <pre>mongo::MessagingPort::MessagingPort(boost::shared_ptr<mongo::Socket>)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::MessagingPort::setSocketTimeout(double)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

- <pre>mongo::MessagingPort::call(mongo::Message&, mongo::Message&)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../tools)

- <pre>mongo::AbstractMessagingPort::setConnectionId(long long)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/util/net/httpclient.cpp

- <pre>mongo::HttpClient::get(std::string const&, mongo::HttpClient::Result*)</pre>
Used By:
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/client/examples/httpClientTest.cpp](../cpp\_client\_driver)

### src/mongo/util/net/sock.cpp

- <pre>mongo::hostbyname(char const*)</pre>
Used By:
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/dbtests/socktests.cpp](../unit\_tests)

- <pre>mongo::Socket::unsafe_recv(char*, int)</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/httpclient.cpp](../network)

- <pre>typeinfo for mongo::SocketException</pre>
Used By:
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

- <pre>mongo::Socket::send(std::vector<std::pair<char*, int>, std::allocator<std::pair<char*, int> > > const&, char const*)</pre>
Used By:
    - [src/mongo/util/net/message.cpp](../network)

- <pre>mongo::portRecvFlags</pre>
Used By:
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

- <pre>mongo::prettyHostName()</pre>
Used By:
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)
    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

- <pre>mongo::Socket::send(char const*, int, char const*)</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/net/message.cpp](../network)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)

- <pre>mongo::Socket::~Socket()</pre>
Used By:
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::Socket::isStillConnected()</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)

- <pre>mongo::Socket::recv(char*, int)</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::unknownAddress</pre>
Used By:
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

- <pre>mongo::portSendFlags</pre>
Used By:
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

- <pre>mongo::SockAddr::getPort() const</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp

- <pre>mongo::Socket::Socket(double, mongo::logger::LogSeverity)</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/util/net/httpclient.cpp](../network)

- <pre>mongo::SockAddr::isLocalHost() const</pre>
Used By:
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

- <pre>mongo::Socket::setTimeout(double)</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::Socket::connect(mongo::SockAddr&)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)

- <pre>mongo::getHostNameCached()</pre>
Used By:
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

- <pre>mongo::enableIPv6(bool)</pre>
Used By:
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Socket::secure(mongo::SSLManagerInterface*, std::string const&)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)

- <pre>mongo::SockAddr::getAddr() const</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::SockAddr::toString(bool) const</pre>
Used By:
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

- <pre>mongo::IPv6Enabled()</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)

- <pre>mongo::Socket::secureAccepted(mongo::SSLManagerInterface*)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::SockAddr::SockAddr(char const*, int)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::disableNagle(int)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>vtable for mongo::SocketException</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::Socket::handleRecvError(int, int)</pre>
Used By:
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

- <pre>mongo::makeUnixSockPath(int)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::Socket::close()</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::getHostName()</pre>
Used By:
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

- <pre>mongo::Socket::doSSLHandshake(char const*, int)</pre>
Used By:
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::Socket::Socket(int, mongo::SockAddr const&)</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/net/message\_port.cpp](../network)

- <pre>mongo::Socket::handleSendError(int, char const*)</pre>
Used By:
    - [src/mongo/util/net/ssl\_manager.cpp](../network)

- <pre>mongo::SockAddr::getType() const</pre>
Used By:
    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/util/net/socket\_poll.cpp

- <pre>mongo::socketPoll(pollfd*, unsigned long, int)</pre>
Used By:
    - [src/mongo/util/net/sock.cpp](../network)

- <pre>mongo::isPollSupported()</pre>
Used By:
    - [src/mongo/util/net/sock.cpp](../network)

### src/mongo/util/net/ssl\_manager.cpp

- <pre>mongo::sslGlobalParams</pre>
Used By:
    - [src/mongo/util/net/message\_port.cpp](../network)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/client/examples/httpClientTest.cpp](../cpp\_client\_driver)

- <pre>mongo::isSSLServer</pre>
Used By:
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::getSSLVersion(std::string const&, std::string const&)</pre>
Used By:
    - [src/mongo/util/version\_reporting.cpp](../utilities)

- <pre>mongo::getSSLManager()</pre>
Used By:
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/util/net/httpclient.cpp](../network)
    - [src/mongo/util/background.cpp](../utilities)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/util/background.cpp](../utilities)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/util/net/listen.cpp](../network)

- <pre>mongo::SSLConnection::~SSLConnection()</pre>
Used By:
    - [src/mongo/util/net/sock.cpp](../network)

### src/mongo/util/net/ssl\_options.cpp

- <pre>mongo::addSSLClientOptions(mongo::optionenvironment::OptionSection*)</pre>
Used By:
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)

- <pre>mongo::storeSSLServerOptions(mongo::optionenvironment::Environment const&)</pre>
Used By:
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

- <pre>mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)</pre>
Used By:
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::storeSSLClientOptions(mongo::optionenvironment::Environment const&)</pre>
Used By:
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

- <pre>mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)</pre>
Used By:
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
