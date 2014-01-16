# logging\_system

# Module Groups

-------------

jesus, i hope this becomes a library :)   can you say a bit about what kind of logging we do? is there any sort of   ordering or atomicity (maybe per-call-to-log, or per log line?) our   logging guarantees? 'log lines are emitted in-order with respect to each   process thread?' maybe?)  Logging system (NOTE: The first two actually aren't part of the "logger" library, but I see no  reason why they should not be)

- src/mongo/util/log.cpp   (mongod, tools, mongos)
- src/mongo/util/log.h
- src/mongo/logger/appender.h
- src/mongo/logger/console.cpp   (cppclientdriver)
- src/mongo/logger/console.h
- src/mongo/logger/console\_appender.h
- src/mongo/logger/encoder.h
- src/mongo/logger/labeled\_level.h
- src/mongo/logger/log\_domain-impl.h
- src/mongo/logger/log\_domain.h
- src/mongo/logger/log\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_manager.h
- src/mongo/logger/log\_severity-inl.h
- src/mongo/logger/log\_severity.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_severity.h
- src/mongo/logger/log\_test.cpp   ()
- src/mongo/logger/logger.cpp   (cppclientdriver)
- src/mongo/logger/logger.h
- src/mongo/logger/logstream\_builder.cpp   (cppclientdriver)
- src/mongo/logger/logstream\_builder.h
- src/mongo/logger/message\_event.h
- src/mongo/logger/message\_event\_utf8\_encoder.cpp   (mongod, tools, mongos)
- src/mongo/logger/message\_event\_utf8\_encoder.h
- src/mongo/logger/message\_log\_domain.cpp   (cppclientdriver)
- src/mongo/logger/message\_log\_domain.h
- src/mongo/logger/ramlog.cpp   (mongod, tools, mongos)
- src/mongo/logger/ramlog.h
- src/mongo/logger/rotatable\_file\_appender.h
- src/mongo/logger/rotatable\_file\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_manager.h
- src/mongo/logger/rotatable\_file\_writer.cpp   (cppclientdriver)
- src/mongo/logger/rotatable\_file\_writer.h
- src/mongo/logger/rotatable\_file\_writer\_test.cpp   ()
- src/mongo/logger/syslog\_appender.h
- src/mongo/logger/tee.h

## Interface


### src/mongo/util/log.cpp

<pre>mongo::LogIndentLevel::~LogIndentLevel()</pre>

#### Used By:

- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::logContext(char const*)</pre>

#### Used By:

- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::rotateLogs()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<pre>mongo::rawOut(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::setRawOutToStderr()</pre>

#### Used By:

- [src/mongo/tools/tool\_logger.cpp](../tools)

<pre>mongo::warnings</pre>

#### Used By:

- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)

<pre>mongo::tlogLevel</pre>

#### Used By:

- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::getcurns</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/util/net/message\_port.cpp](../network)

<pre>mongo::startupWarningsLog</pre>

#### Used By:

- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::LogIndentLevel::LogIndentLevel()</pre>

#### Used By:

- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::errnoWithDescription(int)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/util/password.cpp](../startup\_initialization)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/util/stacktrace.cpp](../utilities)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/util/logfile.cpp](../journaling)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/util/stacktrace.cpp](../utilities)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/util/password.cpp](../startup\_initialization)
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/util/net/sock.cpp](../network)

### src/mongo/logger/console.cpp

<pre>mongo::Console::Console()</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/tools/tool\_logger.cpp](../tools)

<pre>mongo::Console::out()</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/tools/tool\_logger.cpp](../tools)

### src/mongo/logger/log\_manager.cpp

<pre>mongo::logger::LogManager::LogManager()</pre>

#### Used By:

- [src/mongo/logger/logger.cpp](../logging\_system)

<pre>mongo::logger::LogManager::getNamedDomain(std::string const&)</pre>

#### Used By:

- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

### src/mongo/logger/log\_severity.cpp

<pre>mongo::logger::operator<<(std::ostream&, mongo::logger::LogSeverity)</pre>

#### Used By:

- [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

### src/mongo/logger/logger.cpp

<pre>mongo::logger::globalRotatableFileManager()</pre>

#### Used By:

- [src/mongo/util/log.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::logger::globalLogManager()</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/s/balancer\_policy.cpp](../sharding)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/db/query/plan\_enumerator.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/memconcept.cpp](../utilities)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
- [src/mongo/db/structure/btree/state.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/query/plan\_ranker.cpp](../query\_system)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/tools/import.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/util/progress\_meter.cpp](../utilities)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/util/logfile.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/planner\_analysis.cpp](../query\_system)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/tools/files.cpp](../tools)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/tools/bsondump.cpp](../tools)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/s/version\_manager.cpp](../sharding)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/version\_mongos.cpp](../sharding)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/db/exec/projection.cpp](../query\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/client/examples/clientTest.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
- [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/util/version\_reporting.cpp](../utilities)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/db/projection.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/db/repl/repl\_start.cpp](../replication)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/bson/optime.cpp](../bson)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp
- [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- [src/mongo/db/stats/counters.cpp](../utilities)

### src/mongo/logger/logstream\_builder.cpp

<pre>mongo::logger::LogstreamBuilder::~LogstreamBuilder()</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/s/balancer\_policy.cpp](../sharding)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/db/query/plan\_enumerator.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/memconcept.cpp](../utilities)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
- [src/mongo/db/structure/btree/state.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/query/plan\_ranker.cpp](../query\_system)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/tools/import.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/util/progress\_meter.cpp](../utilities)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/util/logfile.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/planner\_analysis.cpp](../query\_system)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/tools/files.cpp](../tools)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/tools/top.cpp](../tools)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/s/version\_manager.cpp](../sharding)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/version\_mongos.cpp](../sharding)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/db/exec/projection.cpp](../query\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/client/examples/clientTest.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/dbtests/basictests.cpp](../unit\_tests)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
- [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/util/version\_reporting.cpp](../utilities)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/projection.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/db/repl/repl\_start.cpp](../replication)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/bson/optime.cpp](../bson)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/tools/export.cpp](../tools)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp
- [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- [src/mongo/db/stats/counters.cpp](../utilities)

<pre>mongo::logger::LogstreamBuilder::makeStream()</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/s/balancer\_policy.cpp](../sharding)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/db/query/plan\_enumerator.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/memconcept.cpp](../utilities)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
- [src/mongo/db/structure/btree/state.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/query/plan\_ranker.cpp](../query\_system)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/tools/import.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/util/progress\_meter.cpp](../utilities)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/util/logfile.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/planner\_analysis.cpp](../query\_system)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/tools/files.cpp](../tools)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/tools/top.cpp](../tools)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/s/version\_manager.cpp](../sharding)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/version\_mongos.cpp](../sharding)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/db/exec/projection.cpp](../query\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/client/examples/clientTest.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/dbtests/basictests.cpp](../unit\_tests)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
- [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/util/version\_reporting.cpp](../utilities)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/projection.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/db/repl/repl\_start.cpp](../replication)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/bson/optime.cpp](../bson)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/tools/export.cpp](../tools)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp
- [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- [src/mongo/db/stats/counters.cpp](../utilities)

<pre>mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)</pre>

#### Used By:

- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)

<pre>mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
- [src/mongo/s/balancer\_policy.cpp](../sharding)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/db/query/plan\_enumerator.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/memconcept.cpp](../utilities)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
- [src/mongo/db/structure/btree/state.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/query/plan\_ranker.cpp](../query\_system)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/tools/import.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/util/processinfo.cpp](../utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/util/progress\_meter.cpp](../utilities)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/util/logfile.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/planner\_analysis.cpp](../query\_system)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/tools/files.cpp](../tools)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/util/processinfo\_darwin.cpp](../utilities)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/s/version\_manager.cpp](../sharding)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/version\_mongos.cpp](../sharding)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/db/exec/projection.cpp](../query\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/client/examples/clientTest.cpp](../cpp\_client\_driver)
- [src/mongo/util/concurrency/thread\_pool.cpp](../utilities)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
- [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/util/version\_reporting.cpp](../utilities)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/tools/stat.cpp](../tools)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
- [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/db/projection.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/tools/bridge.cpp](../tools)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/db/repl/repl\_start.cpp](../replication)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/util/net/ssl\_manager.cpp](../network)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/bson/optime.cpp](../bson)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/util/file.cpp](../file\_interface)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp
- [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/util/fail\_point.cpp](../utilities)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/auth/security\_key.cpp](../authentication)
- [src/mongo/db/stats/counters.cpp](../utilities)

<pre>mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LabeledLevel)</pre>

#### Used By:

- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<pre>mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/util/mmap\_posix.cpp](../mmap)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/util/net/message\_port.cpp](../network)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/util/net/message\_port.cpp](../network)

### src/mongo/logger/message\_event\_utf8\_encoder.cpp

<pre>mongo::logger::MessageEventDetailsEncoder::~MessageEventDetailsEncoder()</pre>

#### Used By:

- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- [src/mongo/logger/ramlog.cpp](../logging\_system)

<pre>mongo::logger::MessageEventDetailsEncoder::setDateFormatter(std::string (*)(mongo::Date_t))</pre>

#### Used By:

- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)

<pre>vtable for mongo::logger::MessageEventWithContextEncoder</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>vtable for mongo::logger::MessageEventDetailsEncoder</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- [src/mongo/tools/tool\_logger.cpp](../tools)

<pre>vtable for mongo::logger::MessageEventUnadornedEncoder</pre>

#### Used By:

- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::logger::MessageEventDetailsEncoder::encode(mongo::logger::MessageEventEphemeral const&, std::ostream&)</pre>

#### Used By:

- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
- [src/mongo/logger/ramlog.cpp](../logging\_system)

### src/mongo/logger/message\_log\_domain.cpp

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::clearAppenders()</pre>

#### Used By:

- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::~LogDomain()</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::LogDomain()</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)</pre>

#### Used By:

- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/tools/tool\_logger.cpp](../tools)

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::append(mongo::logger::MessageEventEphemeral const&)</pre>

#### Used By:

- [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<pre>mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::detachAppender(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::AppenderHandle)</pre>

#### Used By:

- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

### src/mongo/logger/ramlog.cpp

<pre>mongo::RamLog::getNames(std::vector<std::string, std::allocator<std::string> >&)</pre>

#### Used By:

- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<pre>mongo::RamLog::LineIterator::lastWrite()</pre>

#### Used By:

- [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<pre>mongo::RamLog::toHTML(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/health.cpp](../replication)

<pre>mongo::RamLog::LineIterator::LineIterator(mongo::RamLog*)</pre>

#### Used By:

- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<pre>mongo::RamLog::get(std::string const&)</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::RamLogAppender::RamLogAppender(mongo::RamLog*)</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::RamLog::getLine_inlock(unsigned int) const</pre>

#### Used By:

- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<pre>mongo::RamLog::LineIterator::getTotalLinesWritten()</pre>

#### Used By:

- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<pre>mongo::RamLog::getIfExists(std::string const&)</pre>

#### Used By:

- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

### src/mongo/logger/rotatable\_file\_manager.cpp

<pre>mongo::logger::RotatableFileManager::getFile(std::string const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp

<pre>mongo::logger::RotatableFileManager::RotatableFileManager()</pre>

#### Used By:

- [src/mongo/logger/logger.cpp](../logging\_system)

<pre>mongo::logger::RotatableFileManager::openFile(std::string const&, bool)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::logger::RotatableFileManager::~RotatableFileManager()</pre>

#### Used By:

- [src/mongo/logger/logger.cpp](../logging\_system)

<pre>mongo::logger::RotatableFileManager::rotateAll(std::string const&)</pre>

#### Used By:

- [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/logger/rotatable\_file\_writer.cpp

<pre>mongo::logger::RotatableFileWriter::Use::Use(mongo::logger::RotatableFileWriter*)</pre>

#### Used By:

- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::logger::RotatableFileWriter::RotatableFileWriter()</pre>

#### Used By:

- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)

<pre>mongo::logger::RotatableFileWriter::Use::status()</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::logger::RotatableFileWriter::Use::rotate(std::string const&)</pre>

#### Used By:

- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)

<pre>mongo::logger::RotatableFileWriter::Use::setFileName(std::string const&, bool)</pre>

#### Used By:

- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)

-------------

Helpers to dump a bunch of information about the current process   at crash time only? at any time? can you give an example of when   this is used?

- src/mongo/db/log\_process\_details.cpp   (mongod, tools, mongos)
- src/mongo/db/log\_process\_details.h

## Interface


### src/mongo/db/log\_process\_details.cpp

<pre>mongo::logProcessDetails()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/version\_mongos.cpp](../sharding)

<pre>mongo::logProcessDetailsForLogRotate()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

-------------

MONGO\_INITIALIZERs to add extra information to the server logs.

- src/mongo/db/server\_extra\_log\_context.cpp   (mongod, mongos)

## Interface

(not used outside this module)
