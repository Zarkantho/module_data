# network

# Module Groups

-------------

# Group Description
Network library   can you say a few words about:   - what this does   - who uses it   - how to use it?

# Files
- src/mongo/util/net/listen.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/listen.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/hostandport.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/message.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/message.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/message\_port.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/message\_port.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/httpclient.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/httpclient.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/sock.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/sock.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/sock\_test.cpp   ()
- src/mongo/util/net/socket\_poll.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/socket\_poll.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/ssl\_manager.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/ssl\_manager.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/net/ssl\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_options.h   (mongod, cppclientdriver, tools, mongos)

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

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
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

<div></div>

    mongo::Socket::handleSendError(int, char const*)

- Used By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

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
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/distlock.cpp](../sharding)
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

# Dependencies

### src/mongo/util/net/listen.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::warnings

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/util/net/message\_port.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

### src/mongo/util/net/httpclient.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/util/net/sock.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::wait(unsigned int)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::SpinLock::SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::SpinLock::~SpinLock()

- Provided By:

    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/util/net/sock\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../utilities)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::FailPointRegistry::getFailPoint(std::string const&) const

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::FailPoint::setMode(mongo::FailPoint::Mode, unsigned int, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

### src/mongo/util/net/ssl\_manager.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/util/net/ssl\_options.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::optionenvironment::OptionDescription::requires(std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
Top level (?) of handling incoming network connections on mongod and mongos. Inherits from  Listener (listen.h).

# Files
- src/mongo/util/net/message\_server.h   (mongod, mongos)
- src/mongo/util/net/message\_server\_port.cpp   (mongod, mongos)

# Interface

### src/mongo/util/net/message\_server\_port.cpp

<div></div>

    mongo::createServer(mongo::MessageServer::Options const&, mongo::MessageHandler*)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/util/net/message\_server\_port.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::networkCounter

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::NetworkCounter::hit(long long, long long)

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)
