# startup\_initialization

# Module Groups

-------------

Check various expected startup conditions and log warnings to the user if necessary   what uses these? everything? mongod/mongos only? what sort of checks?

- src/mongo/db/startup\_warnings.cpp   (mongod, tools)
- src/mongo/db/startup\_warnings.h

## Interface


### src/mongo/db/startup\_warnings.cpp

<pre>mongo::logStartupWarnings()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

-------------

MONGO\_INITIALIZER startup initialization framework.   what should use these? any tool? mongod/mongos only?

- src/mongo/base/global\_initializer.cpp   (cppclientdriver)
- src/mongo/base/global\_initializer.h
- src/mongo/base/global\_initializer\_registerer.cpp   (mongod, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.h
- src/mongo/base/init.cpp   (cppclientdriver)
- src/mongo/base/init.h
- src/mongo/base/initializer.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer.h
- src/mongo/base/initializer\_context.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer\_context.h
- src/mongo/base/initializer\_dependency\_graph.cpp   (cppclientdriver)
- src/mongo/base/initializer\_dependency\_graph.h
- src/mongo/base/initializer\_dependency\_graph\_test.cpp   ()
- src/mongo/base/initializer\_function.h
- src/mongo/base/initializer\_test.cpp   ()
- src/mongo/base/make\_string\_vector.cpp   (mongod, tools, mongos)
- src/mongo/base/make\_string\_vector.h

## Interface


### src/mongo/base/global\_initializer.cpp

<pre>mongo::getGlobalInitializer()</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/base/global\_initializer\_registerer.cpp

<pre>mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_options\_init.cpp
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_manager\_global.cpp
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
- [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
- [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/base/init.cpp](../startup\_initialization)
- [src/mongo/db/range\_deleter\_service.cpp](../sharding)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/canon\_mongodb\_internal.cpp
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
- [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
- [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
- [src/mongo/logger/logger.cpp](../logging\_system)
- [src/third\_party/s2/s2regioncoverer.cc](../s2)
- [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)
- [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/util/fail\_point\_service.cpp](../utilities)
- [src/mongo/db/ops/modifier\_table.cpp](../update\_system)
- [src/mongo/util/fail\_point\_service.cpp](../utilities)
- [src/third\_party/s2/s2cellid.cc](../s2)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/tools/tool\_logger.cpp](../tools)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
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
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

### src/mongo/base/initializer.cpp

<pre>mongo::runGlobalInitializersOrDie(int, char const* const*, char const* const*)</pre>

#### Used By:

- [src/mongo/unittest/unittest\_main.cpp](../unit\_tests)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/bridge.cpp](../tools)

<pre>mongo::runGlobalInitializers(int, char const* const*, char const* const*)</pre>

#### Used By:

- [src/mongo/client/init.cpp](../cpp\_client\_driver)

<pre>mongo::Initializer::~Initializer()</pre>

#### Used By:

- [src/mongo/base/global\_initializer.cpp](../startup\_initialization)

<pre>mongo::Initializer::Initializer()</pre>

#### Used By:

- [src/mongo/base/global\_initializer.cpp](../startup\_initialization)

### src/mongo/base/initializer\_context.cpp

<pre>mongo::InitializerContext::InitializerContext(std::vector<std::string, std::allocator<std::string> > const&, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&)</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)

### src/mongo/base/initializer\_dependency\_graph.cpp

<pre>mongo::InitializerDependencyGraph::~InitializerDependencyGraph()</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)

<pre>mongo::InitializerDependencyGraph::addInitializer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)</pre>

#### Used By:

- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<pre>mongo::InitializerDependencyGraph::topSort(std::vector<std::string, std::allocator<std::string> >*) const</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)

<pre>mongo::InitializerDependencyGraph::InitializerDependencyGraph()</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)

<pre>mongo::InitializerDependencyGraph::getInitializerFunction(std::string const&) const</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)

### src/mongo/base/make\_string\_vector.cpp

<pre>mongo::_makeStringVector(int, ...)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_options\_init.cpp
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/db/commands/fail\_point\_cmd.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
- [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_manager\_global.cpp
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
- [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
- [src/mongo/db/auth/role\_graph\_builtin\_roles.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/base/init.cpp](../startup\_initialization)
- [src/mongo/db/range\_deleter\_service.cpp](../sharding)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/canon\_mongodb\_internal.cpp
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
- [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
- [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
- [src/mongo/logger/logger.cpp](../logging\_system)
- [src/third\_party/s2/s2regioncoverer.cc](../s2)
- [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)
- [src/mongo/db/commands/hashcmd.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/util/fail\_point\_service.cpp](../utilities)
- [src/mongo/db/ops/modifier\_table.cpp](../update\_system)
- [src/mongo/util/fail\_point\_service.cpp](../utilities)
- [src/third\_party/s2/s2cellid.cc](../s2)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/tools/tool\_logger.cpp](../tools)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
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
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)

-------------

Initialize the global state common to mongod and mongos, such as logging.

- src/mongo/db/initialize\_server\_global\_state.cpp   (mongod, mongos)
- src/mongo/db/initialize\_server\_global\_state.h

## Interface


### src/mongo/db/initialize\_server\_global\_state.cpp

<pre>mongo::signalForkSuccess()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::initializeServerGlobalState()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::forkServerOrDie()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::setupCoreSignals()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

-------------

Options parser library (command line and config files)   where do the options get stored / how can people grab options later?   are they set once and immutable or can they be updated?

- src/mongo/util/options\_parser/constraints.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/constraints.h
- src/mongo/util/options\_parser/environment.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.h
- src/mongo/util/options\_parser/environment\_test.cpp   ()
- src/mongo/util/options\_parser/option\_description.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_description.h
- src/mongo/util/options\_parser/option\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.h
- src/mongo/util/options\_parser/options\_parser.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.h
- src/mongo/util/options\_parser/options\_parser\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_test.cpp   ()
- src/mongo/util/options\_parser/startup\_option\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_option\_init.h
- src/mongo/util/options\_parser/startup\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.h
- src/mongo/util/options\_parser/value.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.h

## Interface


### src/mongo/util/options\_parser/environment.cpp

<pre>mongo::optionenvironment::Environment::operator[](std::string const&) const</pre>

#### Used By:

- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/tools/mongobridge\_options.cpp](../tools)

<pre>mongo::optionenvironment::Environment::count(std::string const&) const</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/tools/bsondump\_options.cpp](../tools)
- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/tools/mongodump\_options.cpp](../tools)
- [src/mongo/tools/mongorestore\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongostat\_options.cpp](../tools)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/tools/mongoimport\_options.cpp](../tools)
- [src/mongo/tools/mongotop\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/tools/mongobridge\_options.cpp](../tools)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/tools/mongofiles\_options.cpp](../tools)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/tools/mongooplog\_options.cpp](../tools)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>mongo::optionenvironment::Environment::validate()</pre>

#### Used By:

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

<pre>mongo::optionenvironment::OptionDescription::hidden()</pre>

#### Used By:

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

<pre>mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)</pre>

#### Used By:

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

<pre>mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)</pre>

#### Used By:

- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/util/net/ssl\_options.cpp](../network)

<pre>mongo::optionenvironment::OptionDescription::requires(std::string const&)</pre>

#### Used By:

- [src/mongo/tools/mongodump\_options.cpp](../tools)
- [src/mongo/util/net/ssl\_options.cpp](../network)

<pre>mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/tools/mongodump\_options.cpp](../tools)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp

<pre>mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)</pre>

#### Used By:

- [src/mongo/tools/bsondump\_options.cpp](../tools)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongofiles\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/tools/mongotop\_options.cpp](../tools)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongostat\_options.cpp](../tools)

<pre>mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::optionenvironment::OptionDescription::positional(int, int)</pre>

#### Used By:

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

<pre>mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/tools/bsondump\_options.cpp](../tools)
- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/tools/mongodump\_options.cpp](../tools)
- [src/mongo/tools/mongorestore\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongostat\_options.cpp](../tools)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/tools/mongoimport\_options.cpp](../tools)
- [src/mongo/tools/mongotop\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/tools/mongobridge\_options.cpp](../tools)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/tools/mongofiles\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/tools/mongooplog\_options.cpp](../tools)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp

<pre>mongo::optionenvironment::OptionSection::helpString() const</pre>

#### Used By:

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

<pre>mongo::optionenvironment::startupOptionsParsed</pre>

#### Used By:

- [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
- [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
- [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
- [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options\_init.cpp
- [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
- [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
- [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
- [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
- [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)

<pre>mongo::optionenvironment::startupOptions</pre>

#### Used By:

- [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
- [src/mongo/tools/bsondump\_options.cpp](../tools)
- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options\_init.cpp
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
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
- src/mongo/db/modules/subscription/src/snmp/snmp\_options.cpp
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
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/tools/mongooplog\_options.cpp](../tools)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
- [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)

### src/mongo/util/options\_parser/value.cpp

<pre>mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>mongo::optionenvironment::Value::get(double*) const</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::optionenvironment::Value::get(std::string*) const</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/tool\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/tools/mongobridge\_options.cpp](../tools)

<pre>mongo::optionenvironment::Value::get(unsigned int*) const</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>mongo::optionenvironment::Value::get(long*) const</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::optionenvironment::Value::get(std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > >*) const</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp

<pre>mongo::optionenvironment::Value::get(bool*) const</pre>

#### Used By:

- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::optionenvironment::Value::get(unsigned long long*) const</pre>

#### Used By:

- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>mongo::optionenvironment::Value::get(int*) const</pre>

#### Used By:

- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/mongobridge\_options.cpp](../tools)

-------------

Command line utilities   can you say a bit more? (give an example?)

- src/mongo/util/cmdline\_utils/censor\_cmdline.cpp   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline.h
- src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp   ()

## Interface


### src/mongo/util/cmdline\_utils/censor\_cmdline.cpp

<pre>mongo::cmdline_utils::censorArgvArray(int, char**)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

-------------

Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

- src/mongo/util/password.cpp   (mongod, tools, mongos)
- src/mongo/util/password.h

## Interface


### src/mongo/util/password.cpp

<pre>mongo::askPassword()</pre>

#### Used By:

- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

-------------

Command line options shared between mongod and mongos   give an example (--hostname?)

- src/mongo/db/server\_options.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options.h
- src/mongo/db/server\_options\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options\_helpers.h
- src/mongo/db/server\_options\_test.cpp   ()

## Interface


### src/mongo/db/server\_options.cpp

<pre>mongo::serverGlobalParams</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
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
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/version\_mongos.cpp](../sharding)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/snmp/snmp\_oid.cpp
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/log\_process\_details.cpp](../logging\_system)
- [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
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

<pre>mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)</pre>

#### Used By:

- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)</pre>

#### Used By:

- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::printCommandLineOpts()</pre>

#### Used By:

- [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<pre>mongo::isMongos()</pre>

#### Used By:

- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)

-------------

ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

- src/mongo/db/server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_parameters.h
- src/mongo/db/server\_parameters\_inline.h
- src/mongo/db/server\_parameters\_test.cpp   ()

## Interface


### src/mongo/db/server\_parameters.cpp

<pre>mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)

<pre>mongo::ServerParameter::~ServerParameter()</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/qlog.cpp](../query\_system)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::ExportedServerParameter<std::string>::setFromString(std::string const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp

<pre>mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/qlog.cpp](../query\_system)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>typeinfo for mongo::ServerParameter</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/qlog.cpp](../query\_system)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::ExportedServerParameter<bool>::setFromString(std::string const&)</pre>

#### Used By:

- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/qlog.cpp](../query\_system)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::ExportedServerParameter<int>::setFromString(std::string const&)</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)

<pre>mongo::ExportedServerParameter<double>::setFromString(std::string const&)</pre>

#### Used By:

- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<pre>mongo::ExportedServerParameter<std::vector<std::string, std::allocator<std::string> > >::setFromString(std::string const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp

<pre>mongo::ServerParameterSet::getGlobal()</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/db/auth/auth\_server\_parameters.cpp](../authentication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/qlog.cpp](../query\_system)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/s/shardconnection.cpp](../sharding)
