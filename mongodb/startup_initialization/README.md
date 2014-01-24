# startup\_initialization

# Module Groups

-------------

# Group Description
Check various expected startup conditions and log warnings to the user if necessary   what uses these? everything? mongod/mongos only? what sort of checks?

# Files
- src/mongo/db/startup\_warnings.cpp   (mongod, tools)
- src/mongo/db/startup\_warnings.h   (mongod, tools)

# Interface

### src/mongo/db/startup\_warnings.cpp

<div></div>

    mongo::logStartupWarnings()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/db/startup\_warnings.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::versionString

- Provided By:

    - [src/mongo/util/version.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

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

    mongo::startupWarningsLog

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

-------------

# Group Description
MONGO\_INITIALIZER startup initialization framework.   what should use these? any tool? mongod/mongos only?

# Files
- src/mongo/base/global\_initializer.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/global\_initializer.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/init.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/init.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_context.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_context.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph\_test.cpp   ()
- src/mongo/base/initializer\_function.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/initializer\_test.cpp   ()
- src/mongo/base/make\_string\_vector.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/base/make\_string\_vector.h   (mongod, cppclientdriver, tools, mongos)

# Interface

### src/mongo/base/global\_initializer.cpp

<div></div>

    mongo::getGlobalInitializer()

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)
    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/base/global\_initializer\_registerer.cpp

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/commands/cluster\_hint\_cmd.cpp](../sharding)
    - [src/mongo/logger/ramlog.cpp](../logging\_system)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
    - [src/mongo/logger/ramlog.cpp](../logging\_system)
    - [src/mongo/tools/tool\_logger.cpp](../tools)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/util/processinfo.cpp](../utilities)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
    - [src/mongo/util/processinfo.cpp](../utilities)
    - [src/mongo/base/init.cpp](../startup\_initialization)
    - [src/mongo/db/range\_deleter\_service.cpp](../sharding)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
    - [src/mongo/logger/logger.cpp](../logging\_system)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/third\_party/s2/s2regioncoverer.cc](../s2)
    - [src/mongo/db/commands/hint\_commands.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)
    - [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
    - [src/mongo/util/fail\_point\_service.cpp](../utilities)
    - [src/mongo/db/ops/modifier\_table.cpp](../update\_system)
    - [src/mongo/util/fail\_point\_service.cpp](../utilities)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/third\_party/s2/s2cellid.cc](../s2)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/fts/stop\_words.cpp](../full\_text\_search\_module)
    - [src/mongo/logger/logger.cpp](../logging\_system)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

### src/mongo/base/initializer.cpp

<div></div>

    mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)

- Used By:

    - [src/mongo/unittest/unittest\_main.cpp](../unit\_tests)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

<div></div>

    mongo::runGlobalInitializers(int, char const* const*, char const* const*)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/init.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Initializer::~Initializer()

- Used By:

    - [src/mongo/base/global\_initializer.cpp](../startup\_initialization)

<div></div>

    mongo::Initializer::Initializer()

- Used By:

    - [src/mongo/base/global\_initializer.cpp](../startup\_initialization)

### src/mongo/base/initializer\_context.cpp

<div></div>

    mongo::InitializerContext::InitializerContext(std::vector<std::string, std::allocator<std::string> > const&, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&)

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

### src/mongo/base/initializer\_dependency\_graph.cpp

<div></div>

    mongo::InitializerDependencyGraph::~InitializerDependencyGraph()

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::InitializerDependencyGraph::addInitializer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::InitializerDependencyGraph::topSort(std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::InitializerDependencyGraph::InitializerDependencyGraph()

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

<div></div>

    mongo::InitializerDependencyGraph::getInitializerFunction(std::string const&) const

- Used By:

    - [src/mongo/base/initializer.cpp](../startup\_initialization)

### src/mongo/base/make\_string\_vector.cpp

<div></div>

    mongo::_makeStringVector(int, ...)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
    - [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/commands/cluster\_hint\_cmd.cpp](../sharding)
    - [src/mongo/logger/ramlog.cpp](../logging\_system)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
    - [src/mongo/logger/ramlog.cpp](../logging\_system)
    - [src/mongo/tools/tool\_logger.cpp](../tools)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/util/processinfo.cpp](../utilities)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
    - [src/mongo/util/processinfo.cpp](../utilities)
    - [src/mongo/base/init.cpp](../startup\_initialization)
    - [src/mongo/db/range\_deleter\_service.cpp](../sharding)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
    - [src/mongo/logger/logger.cpp](../logging\_system)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/third\_party/s2/s2regioncoverer.cc](../s2)
    - [src/mongo/db/commands/hint\_commands.cpp](../database\_commands)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)
    - [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
    - [src/mongo/util/fail\_point\_service.cpp](../utilities)
    - [src/mongo/db/ops/modifier\_table.cpp](../update\_system)
    - [src/mongo/util/fail\_point\_service.cpp](../utilities)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/third\_party/s2/s2cellid.cc](../s2)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/fts/stop\_words.cpp](../full\_text\_search\_module)
    - [src/mongo/logger/logger.cpp](../logging\_system)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

# Dependencies

### src/mongo/base/global\_initializer\_registerer.cpp

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/base/initializer.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/base/initializer\_dependency\_graph.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/base/initializer\_dependency\_graph\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/base/initializer\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Initialize the global state common to mongod and mongos, such as logging.

# Files
- src/mongo/db/initialize\_server\_global\_state.cpp   (mongod, mongos)
- src/mongo/db/initialize\_server\_global\_state.h   (mongod, mongos)

# Interface

### src/mongo/db/initialize\_server\_global\_state.cpp

<div></div>

    mongo::signalForkSuccess()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::initializeServerGlobalState()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::forkServerOrDie()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::setupCoreSignals()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/db/initialize\_server\_global\_state.cpp

<div></div>

    mongo::Console::Console()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

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

    mongo::logger::RotatableFileWriter::Use::Use(mongo::logger::RotatableFileWriter*)

- Provided By:

    - [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Listener::globalTicketHolder

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../logging\_system)

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

    mongo::writePidFile(std::string const&)

- Provided By:

    - [src/mongo/util/processinfo.cpp](../utilities)

<div></div>

    mongo::RamLogAppender::RamLogAppender(mongo::RamLog*)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Console::out()

- Provided By:

    - [src/mongo/logger/console.cpp](../logging\_system)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::RamLog::get(std::string const&)

- Provided By:

    - [src/mongo/logger/ramlog.cpp](../logging\_system)

<div></div>

    mongo::logger::RotatableFileManager::openFile(std::string const&, bool)

- Provided By:

    - [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../network)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::globalRotatableFileManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogManager::getNamedDomain(std::string const&)

- Provided By:

    - [src/mongo/logger/log\_manager.cpp](../logging\_system)

<div></div>

    mongo::setInternalUserAuthParams(mongo::BSONObj)

- Provided By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::logger::RotatableFileWriter::Use::status()

- Provided By:

    - [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::terseCurrentTime(bool)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    vtable for mongo::logger::MessageEventWithContextEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::clearAppenders()

- Provided By:

    - [src/mongo/logger/message\_log\_domain.cpp](../logging\_system)

<div></div>

    mongo::setUpSecurityKey(std::string const&)

- Provided By:

    - [src/mongo/db/auth/security\_key.cpp](../authentication)

<div></div>

    mongo::saslCommandUserDBFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)

<div></div>

    vtable for mongo::logger::MessageEventDetailsEncoder

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::saslCommandMechanismFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
Options parser library (command line and config files)   where do the options get stored / how can people grab options later?   are they set once and immutable or can they be updated?

# Files
- src/mongo/util/options\_parser/constraints.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/constraints.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment\_test.cpp   ()
- src/mongo/util/options\_parser/option\_description.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_description.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_test.cpp   ()
- src/mongo/util/options\_parser/startup\_option\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_option\_init.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/options\_parser/environment.cpp

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Used By:

    - [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
    - [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
    - [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)

### src/mongo/util/options\_parser/option\_description.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongooplog\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::optionenvironment::OptionDescription::requires(std::string const&)

- Used By:

    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Used By:

    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Used By:

    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

### src/mongo/util/options\_parser/option\_section.cpp

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)

### src/mongo/util/options\_parser/startup\_options.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Used By:

    - [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
    - [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
    - [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)

<div></div>

    mongo::optionenvironment::startupOptions

- Used By:

    - [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongodump\_options.cpp](../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options.cpp](../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)
    - [src/mongo/tools/mongofiles\_options.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongooplog\_options.cpp](../tools)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)

### src/mongo/util/options\_parser/value.cpp

<div></div>

    mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(double*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)

<div></div>

    mongo::optionenvironment::Value::get(unsigned int*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(long*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Used By:

    - [src/mongo/tools/mongoexport\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(unsigned long long*) const

- Used By:

    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../tools)

# Dependencies

### src/mongo/util/options\_parser/constraints.cpp

<div></div>

    pcrecpp::RE::FullMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    pcrecpp::RE::no_arg

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    pcrecpp::RE::~RE()

- Provided By:

    - [src/third\_party/pcre-8.30/pcrecpp.cc](../pcrecpp)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/options\_parser/environment.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

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

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::demangleName(std::type_info const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/util/options\_parser/environment\_test.cpp

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/options\_parser/option\_description.cpp

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

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

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/options\_parser/option\_section.cpp

<div></div>

    vtable for boost::program_options::validation_error

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::validation_error::validation_error(boost::program_options::validation_error::kind_t, std::string const&, std::string const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description::add_options()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    typeinfo for boost::program_options::validation_error

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::program_options::validate(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool*, int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::validators::check_first_occurrence(boost::any const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    vtable for boost::program_options::value_semantic_codecvt_helper<char>

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::operator<<(std::ostream&, boost::program_options::options_description const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::program_options::positional_options_description::positional_options_description()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/positional\_options.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::positional_options_description::name_for_position(unsigned int) const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/positional\_options.cpp](../boost\_program\_options)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::program_options::validation_error::what() const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::positional_options_description::max_total_count() const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/positional\_options.cpp](../boost\_program\_options)

<div></div>

    typeinfo for boost::program_options::value_semantic_codecvt_helper<char>

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description::add(boost::program_options::options_description const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description_easy_init::operator()(char const*, boost::program_options::value_semantic const*, char const*)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::invalid_option_value::invalid_option_value(std::string const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::validate(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, std::string*, int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::arg

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::bool_switch()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::positional_options_description::add(char const*, int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/positional\_options.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description::options_description(unsigned int, unsigned int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::options_description::m_default_line_length

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/options\_parser/options\_parser.cpp

<div></div>

    boost::program_options::to_internal(std::string const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/convert.cpp](../boost\_program\_options)

<div></div>

    YAML::detail::node_data::end()

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/node\_data.cpp](../yaml)

<div></div>

    boost::program_options::variables_map::variables_map()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/variables\_map.cpp](../boost\_program\_options)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned int>(mongo::StringData const&, int, unsigned int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    boost::program_options::basic_parsed_options<char> boost::program_options::parse_config_file<char>(std::basic_istream<char, std::char_traits<char> >&, boost::program_options::options_description const&, bool)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/parsers.cpp](../boost\_program\_options)

<div></div>

    mongo::Status::operator!=(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::program_options::detail::cmdline::style(int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/cmdline.cpp](../boost\_program\_options)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    YAML::detail::memory_holder::merge(YAML::detail::memory_holder&)

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/memory.cpp](../yaml)

<div></div>

    YAML::detail::node_data::begin()

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/node\_data.cpp](../yaml)

<div></div>

    boost::program_options::positional_options_description::positional_options_description()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/positional\_options.cpp](../boost\_program\_options)

<div></div>

    YAML::detail::node_data::mark_defined()

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/node\_data.cpp](../yaml)

<div></div>

    boost::program_options::detail::cmdline::set_options_description(boost::program_options::options_description const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/cmdline.cpp](../boost\_program\_options)

<div></div>

    YAML::detail::node_data::empty_scalar

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/node\_data.cpp](../yaml)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::program_options::multiple_occurrences::get_option_name() const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::store(boost::program_options::basic_parsed_options<char> const&, boost::program_options::variables_map&, bool)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/variables\_map.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::detail::cmdline::cmdline(std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/cmdline.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::abstract_variables_map::operator[](std::string const&) const

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/variables\_map.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::detail::cmdline::run()

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/cmdline.cpp](../boost\_program\_options)

<div></div>

    boost::program_options::detail::cmdline::set_positional_options(boost::program_options::positional_options_description const&)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/cmdline.cpp](../boost\_program\_options)

<div></div>

    YAML::detail::memory::create_node()

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/memory.cpp](../yaml)

<div></div>

    YAML::Load(std::string const&)

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/parse.cpp](../yaml)

<div></div>

    boost::program_options::options_description::options_description(unsigned int, unsigned int)

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned long long>(mongo::StringData const&, int, unsigned long long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<double>(mongo::StringData const&, int, double*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    boost::program_options::options_description::m_default_line_length

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/options\_description.cpp](../boost\_program\_options)

<div></div>

    vtable for boost::program_options::variables_map

- Provided By:

    - [src/third\_party/boost/libs/program\_options/src/variables\_map.cpp](../boost\_program\_options)

<div></div>

    YAML::detail::node_data::set_null()

- Provided By:

    - [src/third\_party/yaml-cpp-0.5.1/src/node\_data.cpp](../yaml)

### src/mongo/util/options\_parser/options\_parser\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

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

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/util/options\_parser/value.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
Command line utilities   can you say a bit more? (give an example?)

# Files
- src/mongo/util/cmdline\_utils/censor\_cmdline.cpp   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline.h   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp   ()

# Interface

### src/mongo/util/cmdline\_utils/censor\_cmdline.cpp

<div></div>

    mongo::cmdline_utils::censorArgvArray(int, char**)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/util/cmdline\_utils/censor\_cmdline.cpp

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

# Files
- src/mongo/util/password.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/password.h   (mongod, cppclientdriver, tools, mongos)

# Interface

### src/mongo/util/password.cpp

<div></div>

    mongo::askPassword()

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

# Dependencies

### src/mongo/util/password.cpp

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

-------------

# Group Description
Command line options shared between mongod and mongos   give an example (--hostname?)

# Files
- src/mongo/db/server\_options.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/db/server\_options.h   (mongod, cppclientdriver, tools, mongos)
- src/mongo/db/server\_options\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options\_helpers.h   (mongod, tools, mongos)
- src/mongo/db/server\_options\_test.cpp   ()

# Interface

### src/mongo/db/server\_options.cpp

<div></div>

    mongo::serverGlobalParams

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/stats/snapshots.cpp](../utilities)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/util/net/ssl\_options.cpp](../network)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/auth/security\_key.cpp](../authentication)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/db/server\_options\_helpers.cpp

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::printCommandLineOpts()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::isMongos()

- Used By:

    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

# Dependencies

### src/mongo/db/server\_options\_helpers.cpp

<div></div>

    mongo::DBException::traceExceptions

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::MessageEventDetailsEncoder::setDateFormatter(std::string (*)(mongo::Date_t))

- Provided By:

    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

    typeinfo for mongo::MsgAssertionException

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

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

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

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

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

    mongo::storeSSLServerOptions(mongo::optionenvironment::Environment const&)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../network)

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/server\_options\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::logger::operator<<(std::ostream&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/log\_severity.cpp](../logging\_system)

<div></div>

    mongo::unittest::Test::~Test()

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

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

# Files
- src/mongo/db/server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_parameters.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_inline.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_test.cpp   ()

# Interface

### src/mongo/db/server\_parameters.cpp

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    typeinfo for mongo::ServerParameter

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)

<div></div>

    mongo::ExportedServerParameter<double>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
    - [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../sharding)

# Dependencies

### src/mongo/db/server\_parameters.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<double>(mongo::StringData const&, int, double*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

### src/mongo/db/server\_parameters\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)
