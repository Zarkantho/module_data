# database\_commands

# Module Groups

-------------

# Group Description
Base class for mongodb commands. Has a big std::map with the keys of the command name and the  values as the Command itself. These are the commands that you run using  "db.$cmd.findOne({ "serverStatus" : true }).

# Files
- src/mongo/db/commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands.h

# Interface

### src/mongo/db/commands.cpp

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::Command::parseNsFullyQualified(std::string const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Command::findCommand(std::string const&)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::Command::_checkAuthorization(mongo::Command*, mongo::ClientBasic*, std::string const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::parseResourcePattern(std::string const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_split.cpp](../sharding)

<div></div>

    vtable for mongo::Command

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::Command::testCommandsEnabled

- Used By:

    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    typeinfo for mongo::Command

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::Command::_commandsByBestName

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::Command::_webCommands

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, bool, std::string const&)

- Used By:

    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::Command::htmlHelp(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

# Dependencies

### src/mongo/db/commands.cpp

<div></div>

    mongo::DBConnectionPool::appendInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logCommandAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::mutablebson::Document const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::getAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::ActionType::connPoolSync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::DBConnectionPool::flush()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::connPoolStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
A bunch of commands for mongod. However, this ALSO has the definition of Command::execCommand for  mongod (the function that actually runs commands registered using the Command class, which gets  called whenever a query against the "$cmd" collection is made)

# Files
- src/mongo/db/dbcommands.cpp   (mongod, tools)

# Interface

### src/mongo/db/dbcommands.cpp

<div></div>

    mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::_runCommands(char const*, mongo::BSONObj&, mongo::_BufBuilder<mongo::TrivialAllocator>&, mongo::BSONObjBuilder&, bool, int)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

# Dependencies

### src/mongo/db/dbcommands.cpp

<div></div>

    mongo::ActionType::collStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ActionType::dropDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::setMaxTimeMicros(unsigned long long)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::replOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::ShardingState::getVersion(std::string const&) const

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::convertToCapped

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::ReplSetImpl::setMaintenanceMode(bool)

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::Database::_initExtentFreeList()

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::_diaglog

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiagLog::setLevel(int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::setProfilingLevel(int, std::string&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::IndexCatalog::numIndexesReady() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)

- Provided By:

    - [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::DiagLog::flush()

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationSession::setImpersonatedUserNames(std::vector<mongo::UserName, std::allocator<mongo::UserName> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::dbHolderUnchecked()

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::repairDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::GTE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::FetchStage::FetchStage(mongo::WorkingSet*, mongo::PlanStage*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/fetch.cpp](../query\_system)

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isImpersonating() const

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::KeyPattern::extendRangeBound(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::clearUserFlag(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Helpers::inferKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::writelocktry::~writelocktry()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::ActionType::listDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::NamespaceDetails::updateTTLIndex(int, mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::info()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Query::hasReadPreference(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NamespaceDetails::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::_finishInit()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSCommand(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::ActionType::createCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::writelocktry::writelocktry(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::runCount(char const*, mongo::BSONObj const&, std::string&, int&)

- Provided By:

    - [src/mongo/db/ops/count.cpp](../query\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Helpers::toKeyFormat(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::ReplSetImpl::_stepDown(int)

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::ActionType::enableProfiler

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::audit::parseAndRemoveImpersonatedUserField(mongo::BSONObj, mongo::AuthorizationSession*, std::vector<mongo::UserName, std::allocator<mongo::UserName> >*, bool*)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

<div></div>

    mongo::ActionType::collMod

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::OpTime::m

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ExtentManager::getFile(int, int, bool)

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::isCapped() const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::Collection::dataSize() const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ReplSetImpl::lastOtherOpTime() const

- Provided By:

    - [src/mongo/db/repl/health.cpp](../replication)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dropDatabase(std::string const&)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::IndexScan::IndexScan(mongo::IndexScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<div></div>

    mongo::ActionType::diagLogging

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::closeAllDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::fileSize() const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ActionType::dbStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Database::dropCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dbSize(char const*)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::clearImpersonatedUserNames()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::DeregisterEvenIfUnderlyingCodeThrows::~DeregisterEvenIfUnderlyingCodeThrows()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Commands (run using db.$cmd.findOne(...))

# Files
- src/mongo/db/commands/apply\_ops.cpp   (mongod, tools)
- src/mongo/db/commands/authentication\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/authentication\_commands.h
- src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp   (mongod, tools)
- src/mongo/db/commands/collection\_to\_capped.cpp   (mongod, tools)
- src/mongo/db/commands/connection\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/copydb.h
- src/mongo/db/commands/copydb\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/dbhash.cpp   (mongod, tools)
- src/mongo/db/commands/dbhash.h
- src/mongo/db/commands/distinct.cpp   (mongod, tools)
- src/mongo/db/commands/drop\_indexes.cpp   (mongod, tools)
- src/mongo/db/commands/fail\_point\_cmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/find\_and\_modify.cpp   (mongod, tools)
- src/mongo/db/commands/find\_and\_modify.h
- src/mongo/db/commands/find\_and\_modify\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/geonear.cpp   (mongod, tools)
- src/mongo/db/commands/get\_last\_error.cpp   (mongod, tools)
- src/mongo/db/commands/group.cpp   (mongod, tools)
- src/mongo/db/commands/hashcmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/index\_stats.cpp   (mongod, tools)
- src/mongo/db/commands/isself.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/merge\_chunks\_cmd.cpp   (mongod, tools)
- src/mongo/db/commands/mr.cpp   (mongod, tools)
- src/mongo/db/commands/mr.h
- src/mongo/db/commands/mr\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/pipeline\_command.cpp   (mongod, tools)
- src/mongo/db/commands/rename\_collection.cpp   (mongod, tools)
- src/mongo/db/commands/rename\_collection.h
- src/mongo/db/commands/rename\_collection\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.h
- src/mongo/db/commands/shutdown.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/shutdown.h
- src/mongo/db/commands/storage\_details.cpp   (mongod, tools)
- src/mongo/db/commands/test\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/touch.cpp   (mongod)
- src/mongo/db/commands/user\_management\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/validate.cpp   (mongod, tools)
- src/mongo/db/compact.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_admin.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_generic.cpp   (mongod, tools, mongos)
- src/mongo/db/dbeval.cpp   (mongod, tools)
- src/mongo/s/commands\_admin.cpp   (mongos)
- src/mongo/s/commands\_public.cpp   (mongos)
- src/mongo/db/driverHelpers.cpp   (mongod, tools)

# Interface

### src/mongo/db/commands/authentication\_commands.cpp

<div></div>

    mongo::CmdAuthenticate::disableAuthMechanism(std::string)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

### src/mongo/db/commands/copydb\_common.cpp

<div></div>

    mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

### src/mongo/db/commands/dbhash.cpp

<div></div>

    mongo::logOpForDbHash(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/db/commands/get\_last\_error.cpp

<div></div>

    mongo::getLastErrorDefault

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/db/commands/isself.cpp

<div></div>

    mongo::HostAndPort::isSelf() const

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/socktests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/db/commands/server\_status.cpp

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/util/tcmalloc\_server\_status\_section.cpp](../utilities)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)

<div></div>

    mongo::OpCounterServerStatusSection::OpCounterServerStatusSection(std::string const&, mongo::OpCounters*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/dbeval.cpp

<div></div>

    mongo::dbEval(std::string const&, mongo::BSONObj&, mongo::BSONObjBuilder&, std::string&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

### src/mongo/s/commands\_public.cpp

<div></div>

    mongo::Command::runAgainstRegistered(char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, int)

- Used By:

    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)

# Dependencies

### src/mongo/db/commands/apply\_ops.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::applyOperation_inlock(mongo::BSONObj const&, bool, bool)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/authentication\_commands.cpp

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::MongoAuthenticationSession::MongoAuthenticationSession(unsigned long long)

- Provided By:

    - [src/mongo/db/auth/mongo\_authentication\_session.cpp](../authentication)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

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

    mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::mutablebson::Element::leftChild() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::User::getCredentials() const

- Provided By:

    - [src/mongo/db/auth/user.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::logoutDatabase(std::string const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::internalSecurity

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::rightSibling() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Element::getFieldName() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::User::getName() const

- Provided By:

    - [src/mongo/db/auth/user.cpp](../authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::SecureRandom::create()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/auth/user\_name.cpp](../authentication)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::audit::logAuthentication(mongo::ClientBasic*, mongo::StringData const&, mongo::UserName const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp

<div></div>

    mongo::ActionType::cleanupOrphaned

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/collection\_metadata.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::ShardingState::refreshMetadataNow(std::string const&, mongo::ChunkVersion*)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::CollectionMetadata::getMinKey() const

- Provided By:

    - [src/mongo/s/collection\_metadata.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::getDeleter()

- Provided By:

    - [src/mongo/db/range\_deleter\_service.cpp](../sharding)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::RangeDeleter::deleteNow(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, std::string*)

- Provided By:

    - [src/mongo/db/range\_deleter.cpp](../sharding)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const

- Provided By:

    - [src/mongo/s/collection\_metadata.cpp](../sharding)

### src/mongo/db/commands/collection\_to\_capped.cpp

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::convertToCapped

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Collection::dataSize() const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::dropCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/connection\_status.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNames()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/commands/copydb\_common.cpp

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionSet::removeAllActions()

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/commands/dbhash.cpp

<div></div>

    mongo::IndexCatalog::findIdIndex()

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::FetchStage::FetchStage(mongo::WorkingSet*, mongo::PlanStage*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/fetch.cpp](../query\_system)

<div></div>

    mongo::prettyHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::dbHash

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::IndexScan::IndexScan(mongo::IndexScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

### src/mongo/db/commands/distinct.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TypeExplain::getN() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::TypeExplain::isCursorSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::getCursor() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DeregisterEvenIfUnderlyingCodeThrows::~DeregisterEvenIfUnderlyingCodeThrows()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

### src/mongo/db/commands/drop\_indexes.cpp

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::NamespaceDetails::findIndexByName(mongo::StringData const&, bool)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ActionType::reIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::dropIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::IndexCatalog::dropIndex(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/commands/fail\_point\_cmd.cpp

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../utilities)

<div></div>

    mongo::FailPointRegistry::getFailPoint(std::string const&) const

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FailPoint::setMode(mongo::FailPoint::Mode, unsigned int, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FailPoint::toBSON() const

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/commands/find\_and\_modify.cpp

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Query::getFilter() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Projection::init(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/projection.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Query::isComplex(bool*) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Projection::transform(mongo::BSONObj const&, mongo::MatchDetails const*) const

- Provided By:

    - [src/mongo/db/projection.cpp](../query\_system)

<div></div>

    mongo::isSimpleIdQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../query\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/find\_and\_modify\_common.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ResourcePattern::toString() const

- Provided By:

    - [src/mongo/db/auth/resource\_pattern.cpp](../authentication)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/commands/geonear.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearDistance

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

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

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, long long, long long, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexNames::GEO_2D

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::GeoParser::isPoint(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearPoint

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

### src/mongo/db/commands/get\_last\_error.cpp

<div></div>

    mongo::WriteConcernResult::appendTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::appendLastOp(mongo::BSONObjBuilder&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::LastError::noError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::disableForCommand()

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/write\_concern.cpp](../replication)

<div></div>

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/group.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

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

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::DeregisterEvenIfUnderlyingCodeThrows::~DeregisterEvenIfUnderlyingCodeThrows()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

### src/mongo/db/commands/hashcmd.cpp

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Provided By:

    - [src/mongo/db/hasher.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/db/commands/index\_stats.cpp

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ActionType::indexStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

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

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KeyV1::toBson() const

- Provided By:

    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/db/commands/isself.cpp

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::isInternalAuthSet()

- Provided By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::IPv6Enabled()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::authenticateInternalUser(mongo::DBClientWithCommands*)

- Provided By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::DBClientConnection::connect(mongo::HostAndPort const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/db/commands/merge\_chunks\_cmd.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::ActionType::splitChunk

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardingState::gotShardName(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::mergeChunks(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, bool, std::string*)

- Provided By:

    - [src/mongo/s/d\_merge.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::ShardingState::initialize(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OID> const&, mongo::OID*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/commands/mr.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::ShardedConnectionInfo::addHook()

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ShardConnection::forgetNS(std::string const&)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::Context::_finishInit()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/collection\_metadata.cpp](../sharding)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::ShardingState::needCollectionMetadata(std::string const&) const

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::nsGetDB(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::ActionType::mapReduceShardedFinish

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ParallelSortClusteredCursor::more()

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardedConnectionInfo::get(bool)

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::DBClientWithCommands::exists(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientCursor::ClientCursor(std::string const&)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClusteredCursor::init()

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::causedBy(std::exception const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Helpers::upsert(std::string const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::ParallelSortClusteredCursor::next()

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Query::sort(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DeregisterEvenIfUnderlyingCodeThrows::~DeregisterEvenIfUnderlyingCodeThrows()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/mr\_common.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ResourcePattern::toString() const

- Provided By:

    - [src/mongo/db/auth/resource\_pattern.cpp](../authentication)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

### src/mongo/db/commands/parameters.cpp

<div></div>

    mongo::DBException::traceExceptions

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::setJournalCommitInterval(unsigned int)

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_persistence\_stubs.cpp](../sharding)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::getParameter

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::isMongos()

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/db/sorter/sorter\_test.cpp](../aggregation\_framework)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::ReplicaSetMonitor::_maxFailedChecks

- Provided By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::sslGlobalParams

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::setParameter

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::getJournalCommitInterval()

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_persistence\_stubs.cpp](../sharding)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::isJournalingEnabled()

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/s/mongos\_persistence\_stubs.cpp](../sharding)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/commands/pipeline\_command.cpp

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ValueStorage::putVector(mongo::RCVector const*)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::InterruptStatusMongod::status

- Provided By:

    - [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Document::toBson() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Value const&)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::Document::toBsonWithMetaData() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::Pipeline::commandName

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Pipeline::stitch()

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::CurOp::getRemainingMaxTimeMicros() const

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ClientCursorPin::c() const

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Runner*, int, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::PipelineD::prepareCursorSource(boost::intrusive_ptr<mongo::Pipeline> const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/rename\_collection.cpp

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::dropCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/rename\_collection\_common.cpp

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionSet::removeAllActions()

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::renameCollectionSameDB

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::dropCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

### src/mongo/db/commands/server\_status.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Listener::globalConnectionNumber

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::ProcessInfo::getExtraInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::Listener::globalTicketHolder

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::OpCounters::getObj() const

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::RamLog::LineIterator::LineIterator(mongo::RamLog*)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::prettyHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::assertionCount

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::RamLog::getLine_inlock(unsigned int) const

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::RamLog::get(std::string const&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../utilities)

<div></div>

    mongo::ActionType::serverStatus

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::networkCounter

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessId::asLongLong() const

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::RamLog::LineIterator::lastWrite()

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NetworkCounter::append(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/db/commands/shutdown.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::ActionType::shutdown

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

### src/mongo/db/commands/storage\_details.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::drec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Date_t::toTimeT() const

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ProcessInfo::systemInfo

- Provided By:

    - [src/mongo/util/processinfo.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ActionType::storageDetails

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ProcessInfo::pagesInMemory(void const*, unsigned long, std::vector<char, std::allocator<char> >*)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::OID::asTimeT()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

### src/mongo/db/commands/test\_commands.cpp

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::cappedTruncateAfter(char const*, mongo::DiskLoc, bool)

- Provided By:

    - [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::NamespaceDetails::emptyCappedCollection(char const*)

- Provided By:

    - [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/commands/touch.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ActionType::touch

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    typeinfo for mongo::MsgAssertionException

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

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

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

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Provided By:

    - [src/mongo/util/touch\_pages.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/db/commands/user\_management\_commands.cpp

<div></div>

    mongo::ParsedPrivilege::toBSON() const

- Provided By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::invalidateUsersFromDB(std::string const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::ActionType::viewRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::auth::parseCreateOrUpdateUserCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateUserArgs*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::audit::logRevokeRolesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::updateAuthzDocuments(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, int*) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::auth::parseAndValidateDropAllUsersFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logDropAllRolesFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthzDocumentsUpdateGuard::AuthzDocumentsUpdateGuard(mongo::AuthorizationManager*)

- Provided By:

    - [src/mongo/db/auth/authz\_documents\_update\_guard.cpp](../authentication)

<div></div>

    mongo::audit::logCreateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp

<div></div>

    mongo::ActionType::revokeRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::lookupUser(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::rolesCollectionNamespace

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::getBSONForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&, mongo::mutablebson::Element)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::auth::parseDropRoleCommand(mongo::BSONObj const&, std::string const&, mongo::RoleName*, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::auth::parseRoleNamesFromBSONArray(mongo::BSONArray const&, mongo::StringData const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::audit::logDropUser(mongo::ClientBasic*, mongo::UserName const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp

<div></div>

    mongo::Privilege::addPrivilegeToPrivilegeVector(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::Privilege const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::leftChild() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::audit::logRevokePrivilegesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::getUserDescription(mongo::UserName const&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::ROLE_SOURCE_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::invalidateUserCache

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::AuthorizationSession::checkAuthorizedToRevokePrivilege(mongo::Privilege const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::removeRoleDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::ActionType::dropRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::AuthorizationSession::checkAuthorizedToGrantPrivilege(mongo::Privilege const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::auth::parseDropAllRolesFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::invalidateUserCache()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::audit::logRevokeRolesFromUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::AuthorizationManager::invalidateUserByName(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::RoleGraph::isBuiltinRole(mongo::RoleName const&)

- Provided By:

    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::upgradeSchemaStep(mongo::BSONObj const&, bool*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::auth::parseAndValidateDropUserCommand(mongo::BSONObj const&, std::string const&, mongo::UserName*, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthenticatedAsUserWithRole(mongo::RoleName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::createRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::audit::logDropRole(mongo::ClientBasic*, mongo::RoleName const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::authSchemaUpgrade

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::AuthorizationSession::isAuthorizedToChangeOwnCustomDataAsUser(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::auth::parseUsersInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::UsersInfoArgs*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::auth::parseAndValidateRolePrivilegeManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::RoleName*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::ParsedPrivilege::ParsedPrivilege()

- Provided By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)

<div></div>

    mongo::audit::logCreateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::audit::logDropAllUsersFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp

<div></div>

    mongo::ParsedPrivilege::privilegeToParsedPrivilege(mongo::Privilege const&, mongo::ParsedPrivilege*, std::string*)

- Provided By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedToChangeOwnPasswordAsUser(mongo::UserName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::writeAuthSchemaVersionIfNeeded()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::AuthorizationManager::insertPrivilegeDocument(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::User::getRoles() const

- Provided By:

    - [src/mongo/db/auth/user.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::usersCollectionNamespace

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::auth::parseAuthSchemaUpgradeStepCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::ActionType::changeCustomData

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::mutablebson::Element::rightSibling() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::AuthorizationManager::ROLE_NAME_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::audit::logGrantRolesToUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::audit::logUpdateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const*)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Upgrade

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::ActionType::viewUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::auth::parseRolePossessionManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, std::string*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::ActionType::changePassword

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::mutablebson::Element::getFieldName() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::ParsedPrivilege::isValid(std::string*) const

- Provided By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::getRoleDescriptionsForDB(std::string, bool, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedToRevokeRole(mongo::RoleName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ActionType::createUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::AuthorizationSession::isAuthorizedToGrantRole(mongo::RoleName const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::auth::parseCreateOrUpdateRoleCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateRoleArgs*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Privilege::removeActions(mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::removePrivilegeDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::audit::logUpdateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp

<div></div>

    mongo::ActionType::dropUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::audit::logGrantRolesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::queryAuthzDocument(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, boost::function<void (mongo::BSONObj const&)> const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::insertRoleDocument(mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Final

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::auth::parseAndValidatePrivilegeArray(mongo::BSONArray const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::AuthorizationManager::getRoleDescription(mongo::RoleName const&, bool, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthzDocumentsUpdateGuard::tryLock(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/auth/authz\_documents\_update\_guard.cpp](../authentication)

<div></div>

    mongo::audit::logGrantPrivilegesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::RoleName::RoleName(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/auth/role\_name.cpp](../authentication)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::updateRoleDocument(mongo::RoleName const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::updatePrivilegeDocument(mongo::UserName const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/auth/user\_name.cpp](../authentication)

<div></div>

    mongo::AuthzDocumentsUpdateGuard::~AuthzDocumentsUpdateGuard()

- Provided By:

    - [src/mongo/db/auth/authz\_documents\_update\_guard.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::getAuthorizationVersion()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)

<div></div>

    mongo::auth::parseRolesInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::RolesInfoArgs*)

- Provided By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::ParsedPrivilege::~ParsedPrivilege()

- Provided By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)

### src/mongo/db/commands/validate.cpp

<div></div>

    mongo::DiskLoc::drec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

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

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Extent::dump()

- Provided By:

    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ActionType::validate

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::quantizeAllocationSpace(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Collection::isCapped() const

- Provided By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)

- Provided By:

    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

### src/mongo/db/compact.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::NamespaceDetails::incrementStats(long long, long long)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Extent::markEmpty()

- Provided By:

    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Provided By:

    - [src/mongo/util/touch\_pages.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::setLastExtentSize(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::isCurrentlyAReplSetPrimary()

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::NamespaceDetails::orphanDeletedList()

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)

- Provided By:

    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CollectionInfoCache::reset()

- Provided By:

    - [src/mongo/db/structure/collection\_info\_cache.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::freeExtents(mongo::DiskLoc, mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ActionType::compact

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NamespaceDetails::setStats(long long, long long)

- Provided By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Provided By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/dbcommands\_admin.cpp

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::LogFile::~LogFile()

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::AlignedBuilder::kill()

- Provided By:

    - [src/mongo/util/alignedbuilder.cpp](../journaling)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::dur::getJournalDir()

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Provided By:

    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::AlignedBuilder::AlignedBuilder(unsigned int)

- Provided By:

    - [src/mongo/util/alignedbuilder.cpp](../journaling)

### src/mongo/db/dbcommands\_generic.cpp

<div></div>

    mongo::rotateLogs()

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::logRotate

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::RamLog::LineIterator::LineIterator(mongo::RamLog*)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::ActionType::getLog

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getCmdLineOpts

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::prettyHostName()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ProcessInfo::systemInfo

- Provided By:

    - [src/mongo/util/processinfo.cpp](../utilities)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::RamLog::getLine_inlock(unsigned int) const

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::ActionType::hostInfo

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::RamLog::getNames(std::vector<std::string, std::allocator<std::string> >&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::RamLog::LineIterator::getTotalLinesWritten()

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::OID::regenMachineId()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::RamLog::getIfExists(std::string const&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::OID::getMachineId()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logProcessDetailsForLogRotate()

- Provided By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

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

### src/mongo/db/dbeval.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::globalScriptEngine

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/s/commands\_admin.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::ActionType::addShard

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardType::name

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../sharding)

<div></div>

    mongo::ActionType::getShardVersion

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::Shard::runCommand(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ActionType::removeShard

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DatabaseType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::ShardConnection::~ShardConnection()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::ShardConnection::sync()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DBClientWithCommands::getLastError(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::LastErrorHolder::disableForCommand()

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ReplicaSetMonitor::remove(std::string const&, bool)

- Provided By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ShardType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../sharding)

<div></div>

    mongo::ConfigServer::logChange(std::string const&, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ActionType::splitChunk

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ClientInfo::enforceWriteConcern(std::string const&, mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Grid::flushConfig()

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::DBConfig::getAllShardedCollections(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Grid::addShard(std::string*, mongo::ConnectionString const&, long long, std::string&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::Shard::removeShard(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::ShardConnection::done()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ClientInfo::disableForCommand()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DatabaseType::primary

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::listDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Chunk::MaxChunkSize

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONArray> const&, mongo::BSONArray*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::netstat

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::ConfigServer::allUp(std::string&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Shard::reloadShardInfo()

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::ShardType::maxSize

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../sharding)

<div></div>

    mongo::Shard::reset(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::IndexNames::HASHED

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::ActionType::listShards

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSCommand(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::removeHost(std::string const&)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shardkey.cpp](../sharding)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::ChunkManager::_printChunks() const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::Chunk::multiSplit(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::BSONObj&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ActionType::fsync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ActionType::moveChunk

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::DBConfig::reload()

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::Chunk::containsPoint(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ClientInfo::getLastError(std::string const&, mongo::BSONObj const&, mongo::BSONObjBuilder&, std::string&, bool)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DatabaseType::name

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ShardKeyPattern::isUniqueIndexCompatible(mongo::KeyPattern const&) const

- Provided By:

    - [src/mongo/s/shardkey.cpp](../sharding)

<div></div>

    mongo::shardConnectionPool

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::audit::logEnableSharding(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ShardType::draining

- Provided By:

    - [src/mongo/s/type\_shard.cpp](../sharding)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::audit::logShardCollection(mongo::ClientBasic*, mongo::StringData const&, mongo::BSONObj const&, bool)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp

<div></div>

    mongo::getHostNameCached()

- Provided By:

    - [src/mongo/util/net/sock.cpp](../network)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::DBConfig::setPrimary(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ChunkType::shard

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::audit::logRemoveShard(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp

<div></div>

    mongo::audit::logAddShard(mongo::ClientBasic*, mongo::StringData const&, std::string const&, long long)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp

<div></div>

    mongo::Grid::knowAboutShard(std::string const&) const

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::Grid::allowLocalHost() const

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::Chunk::singleSplit(bool, mongo::BSONObj&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ActionType::flushRouterConfig

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ActionType::closeAllDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Chunk::moveAndCommit(mongo::Shard const&, long long, bool, bool, int, mongo::BSONObj&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ChunkManager::getVersion() const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ShardConnection::_finishInit()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBConfig::enableSharding(bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Strategy::useClusterWriteCommands

- Provided By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::ActionType::enableSharding

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ChunkType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../sharding)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/s/commands\_public.cpp

<div></div>

    mongo::ActionType::collStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    typeinfo for mongo::DocumentSource

- Provided By:

    - [src/mongo/db/pipeline/document\_source.cpp](../aggregation\_framework)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::SHARDED

- Provided By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ActionType::dropDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)

- Provided By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::cursorCache

- Provided By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ValueStorage::putDocument(mongo::Document const&)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::reIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Future::CommandResult::join(int)

- Provided By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::ConnectionString::sameLogicalEndpoint(mongo::ConnectionString const&) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../aggregation\_framework)

<div></div>

    mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::versionManager

- Provided By:

    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/s/default\_version.cpp](../sharding)

<div></div>

    mongo::ShardConnection::~ShardConnection()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DocumentStorage::clone() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::Pipeline::canRunInMongos() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::ShardConnection::done()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::Value::Value(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBConfig::getShard(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ActionType::repairDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Command::execCommandClientBasic(mongo::Command*, mongo::ClientBasic&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Provided By:

    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::DBConfig::load()

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::DocumentStorage::findField(mongo::StringData) const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::validate

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Document::toBson() const

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::Chunk::MaxChunkSize

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Grid::removeDBIfExists(mongo::DBConfig const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBConfig::removeSharding(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ActionType::createCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Pipeline::getInitialQuery() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Provided By:

    - [src/mongo/s/shardkey.cpp](../sharding)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Shard::_setAddr(std::string const&)

- Provided By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::enableProfiler

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Pipeline::commandName

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::collMod

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    vtable for mongo::DocumentStorage

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::causedBy(std::exception const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Pipeline::serialize() const

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::splitVector

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Pipeline::splitForSharded()

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ValueStorage::putVector(mongo::RCVector const*)

- Provided By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::convertToCapped

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ChunkManager::drop(boost::shared_ptr<mongo::ChunkManager const>) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::DBConfig::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::DBConfig::dropDatabase(std::string&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ActionType::dropIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::Chunk::splitIfShould(long) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::_finishInit()

- Provided By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)

<div></div>

    mongo::ActionType::dbStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::DBConfig::enableSharding(bool)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::InterruptStatusMongos::status

- Provided By:

    - [src/mongo/s/interrupt\_status\_mongos.cpp](../client\_and\_operation\_tracking)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Provided By:

    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DocumentStorage::appendField(mongo::StringData)

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)

- Provided By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)

<div></div>

    mongo::Chunk::ShouldAutoSplit

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::DocumentSourceOut

- Provided By:

    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)

<div></div>

    mongo::ChunkManager::getShardsForRange(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ActionType::compact

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ChunkManager::hasShardKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::Pipeline::stitch()

- Provided By:

    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

### src/mongo/db/driverHelpers.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Commands + code for fsync of data files

# Files
- src/mongo/db/commands/fsync.cpp   (mongod, tools)
- src/mongo/db/commands/fsync.h

# Interface

### src/mongo/db/commands/fsync.cpp

<div></div>

    mongo::_unlockFsync()

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::lockedForWriting()

- Used By:

    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::filesLockedFsync

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

# Dependencies

### src/mongo/db/commands/fsync.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::ActionType::fsync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::Lock::GlobalWrite::downgrade()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)
