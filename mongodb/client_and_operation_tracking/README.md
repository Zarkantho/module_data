# client\_and\_operation\_tracking

# Module Groups

-------------

mongos's version of a "Client". This is the big bucket of global state. This ALSO has the  definition of Command::execCommand for mongos (the function that actually runs commands registered  using the Command class, which gets called whenever a query against the "$cmd" collection is made)

- src/mongo/s/s\_only.cpp   (mongos)

## Interface
### src/mongo/s/s\_only.cpp
<pre>mongo::Client::clientAddress(bool) const</pre>
#### Used By:
- [src/mongo/s/config.cpp](../sharding)

<pre>mongo::Client::shutdown()</pre>
#### Used By:
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::Command::execCommandClientBasic(mongo::Command*, mongo::ClientBasic&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)</pre>
#### Used By:
- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::usingAShardConnection(std::string const&)</pre>
#### Used By:
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::currentClient</pre>
#### Used By:
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/exec/2dnear.cpp](../query\_system)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/repl\_reads\_ok.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/exec/2d.cpp](../query\_system)
- [src/mongo/db/commands/distinct.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/exec/oplogstart.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<pre>mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)</pre>
#### Used By:
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<pre>mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)</pre>
#### Used By:
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/tools/tool.cpp](../tools)

-------------

mongod's version of a "Client". This is the big bucket of global state.  There is also the concept of a "Context" that one can take at the beginning of an operation that  holds a subset of the global state. There is also a "ReadContext" and a "WriteContext which  take locks. These are all nested classes in "Client". It's a bizarre situation because  "client.h" contains the declaration of the class, but there are two different definitions. One in  "s\_only.cpp" for mongos, and one in "client.cpp" for mongod. This means that mongos files may  contain "client.h" and pass compile fine when using something in it, but then may fail link  because it happens to be something that's only defined in "client.cpp". I don't see any  definitions so far for "Context" in mongos, and a grep for "Client::WriteContext::WriteContext"  (the definition of the WriteContext constructor) only shows up in client.cpp, which is mongod  only.

- src/mongo/db/client.cpp   (mongod, tools)
- src/mongo/db/client.h

## Interface
### src/mongo/db/client.cpp
<pre>mongo::Client::Context::inDB(std::string const&, std::string const&) const</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Client::appendLastOp(mongo::BSONObjBuilder&) const</pre>
#### Used By:
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<pre>mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)</pre>
#### Used By:
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::Client::clientAddress(bool) const</pre>
#### Used By:
- [src/mongo/s/config.cpp](../sharding)

<pre>mongo::Client::Context::_finishInit()</pre>
#### Used By:
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Client::allowedToThrowPageFaultException() const</pre>
#### Used By:
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<pre>mongo::CachedBSONObj::_tooBig</pre>
#### Used By:
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<pre>mongo::OpDebug::reset()</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/master\_slave.cpp](../replication)

<pre>mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)</pre>
#### Used By:
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::Client::Context::~Context()</pre>
#### Used By:
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<pre>mongo::Client::recommendedYieldMicros(int*, int*, bool)</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/d\_concurrency.cpp](../concurrency)

<pre>mongo::Client::Context::Context(std::string const&, mongo::Database*)</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::Client::clientsMutex</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<pre>mongo::Client::clients</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<pre>mongo::Client::shutdown()</pre>
#### Used By:
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/tools/tool.cpp](../tools)

<pre>mongo::currentClient</pre>
#### Used By:
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/exec/2dnear.cpp](../query\_system)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/repl\_reads\_ok.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/dur\_commitjob.cpp](../journaling)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/db/lockstate.cpp](../concurrency)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/exec/2d.cpp](../query\_system)
- [src/mongo/db/commands/distinct.cpp](../database\_commands)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/exec/oplogstart.cpp](../query\_system)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<pre>mongo::Client::getActiveClientCount(int&, int&)</pre>
#### Used By:
- [src/mongo/db/d\_concurrency.cpp](../concurrency)

<pre>mongo::Client::gotHandshake(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/repl/replset\_commands.cpp](../replication)

<pre>mongo::ClientBasic::getCurrent()</pre>
#### Used By:
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/s/cursors.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/repl/rs.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

<pre>mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)</pre>
#### Used By:
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::OpDebug::report(mongo::CurOp const&) const</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Client::Context::Context(std::string const&, std::string const&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

-------------

The current "operation" within the current "Client"

- src/mongo/db/curop-inl.h
- src/mongo/db/curop.cpp   (mongod, tools)
- src/mongo/db/curop.h
- src/mongo/db/curop\_test.cpp   ()

## Interface
### src/mongo/db/curop.cpp
<pre>mongo::CurOp::ensureStarted()</pre>
#### Used By:
- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)

<pre>mongo::CurOp::enter(mongo::Client::Context*)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::CurOp::reset()</pre>
#### Used By:
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)

<pre>mongo::CurOp::info()</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::CurOp::getRemainingMaxTimeMicros() const</pre>
#### Used By:
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

<pre>mongo::OpDebug::recordStats()</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::CurOp::kill(bool*)</pre>
#### Used By:
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::CurOp::reset(mongo::HostAndPort const&, int)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::CurOp::getOp(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/index\_builder.cpp](../indexing)

<pre>mongo::CurOp::~CurOp()</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::CurOp::setMaxTimeMicros(unsigned long long)</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

<pre>mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::CurOp::setNS(mongo::StringData const&)</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

Functions to kill the current "operation"

- src/mongo/db/kill\_current\_op.cpp   (mongod, tools)
- src/mongo/db/kill\_current\_op.h

## Interface
### src/mongo/db/kill\_current\_op.cpp
<pre>mongo::KillCurrentOp::reset()</pre>
#### Used By:
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::KillCurrentOp::checkForInterruptNoAssert()</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)

<pre>mongo::KillCurrentOp::checkForInterrupt(bool)</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/db/write\_concern.cpp](../replication)

<pre>mongo::KillCurrentOp::notifyAllWaiters()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::KillCurrentOp::killAll()</pre>
#### Used By:
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::KillCurrentOp::kill(mongo::AtomicUInt)</pre>
#### Used By:
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

Helpers to check whether the current operation in the current client has been interrupted.

- src/mongo/db/interrupt\_status.h
- src/mongo/db/interrupt\_status\_mongod.cpp   (mongod, tools)
- src/mongo/db/interrupt\_status\_mongod.h
- src/mongo/s/interrupt\_status\_mongos.cpp   (mongos)
- src/mongo/s/interrupt\_status\_mongos.h

## Interface

-------------

Base class for a Client on mongod and mongos: ClientBasic

- src/mongo/db/client\_basic.cpp   (mongod, tools, mongos)
- src/mongo/db/client\_basic.h

## Interface
### src/mongo/db/client\_basic.cpp
<pre>mongo::ClientBasic::hasAuthorizationSession() const</pre>
#### Used By:
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)

<pre>mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)</pre>
#### Used By:
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<pre>mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)</pre>
#### Used By:
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<pre>mongo::ClientBasic::getAuthorizationSession() const</pre>
#### Used By:
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
- [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/s/d\_state.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_private.cpp
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

-------------

Seems to be the "mongos only" version of the "Client" class: ClientInfo Also inherits from ClientBasic

- src/mongo/s/client\_info.cpp   (mongos)
- src/mongo/s/client\_info.h

## Interface
### src/mongo/s/client\_info.cpp
<pre>mongo::ClientInfo::getLastError(std::string const&, mongo::BSONObj const&, mongo::BSONObjBuilder&, std::string&, bool)</pre>
#### Used By:
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::ClientInfo::newRequest()</pre>
#### Used By:
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/s/writeback\_listener.cpp](../sharding)

<pre>mongo::ClientInfo::enforceWriteConcern(std::string const&, mongo::BSONObj const&, std::string*)</pre>
#### Used By:
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::ClientInfo::disableForCommand()</pre>
#### Used By:
- [src/mongo/s/commands\_admin.cpp](../database\_commands)

<pre>mongo::ClientInfo::addHostOpTimes(std::map<mongo::ConnectionString, mongo::OpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::OpTime> > > const&)</pre>
#### Used By:
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::ClientInfo::get(mongo::AbstractMessagingPort*)</pre>
#### Used By:
- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::ClientInfo::create(mongo::AbstractMessagingPort*)</pre>
#### Used By:
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::ClientInfo::newPeerRequest(mongo::HostAndPort const&)</pre>
#### Used By:
- [src/mongo/s/request.cpp](../sharding)

<pre>mongo::ClientInfo::exists()</pre>
#### Used By:
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::ClientBasic::getCurrent()</pre>
#### Used By:
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../authentication)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/s/cursors.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- [src/mongo/db/repl/rs.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

-------------

The database's internal concept of a cursor from a client

- src/mongo/db/clientcursor.cpp   (mongod, tools)
- src/mongo/db/clientcursor.h

## Interface
### src/mongo/db/clientcursor.cpp
<pre>mongo::ClientCursorPin::ClientCursorPin(long long)</pre>
#### Used By:
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::ClientCursor::find(std::string const&, std::set<long long, std::less<long long>, std::allocator<long long> >&)</pre>
#### Used By:
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)

<pre>mongo::ClientCursorPin::deleteUnderlying()</pre>
#### Used By:
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

<pre>mongo::ClientCursor::~ClientCursor()</pre>
#### Used By:
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

<pre>mongo::ClientCursor::suggestYieldMicros()</pre>
#### Used By:
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<pre>mongo::ClientCursorPin::c() const</pre>
#### Used By:
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

<pre>mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<pre>mongo::ClientCursor::updateSlaveLocation(mongo::CurOp&)</pre>
#### Used By:
- [src/mongo/db/query/new\_find.cpp](../query\_system)

<pre>mongo::ClientCursor::idleTimeReport(unsigned int)</pre>
#### Used By:
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::ClientCursor::ClientCursor(std::string const&)</pre>
#### Used By:
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::ClientCursor::registerRunner(mongo::Runner*)</pre>
#### Used By:
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/commands/distinct.cpp](../database\_commands)
- [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/ops/count.cpp](../query\_system)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/query/internal\_runner.cpp](../query\_system)
- [src/mongo/db/commands/group.cpp](../database\_commands)

<pre>vtable for mongo::ClientCursorMonitor</pre>
#### Used By:
- [src/mongo/db/d\_globals.cpp](../legacy\_code)

<pre>mongo::ClientCursor::erase(long long)</pre>
#### Used By:
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::ClientCursorPin::~ClientCursorPin()</pre>
#### Used By:
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::ClientCursor::shouldTimeout(unsigned int)</pre>
#### Used By:
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<pre>mongo::ClientCursor::aboutToDelete(mongo::StringData const&, mongo::NamespaceDetails const*, mongo::DiskLoc const&)</pre>
#### Used By:
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<pre>mongo::ClientCursor::eraseIfAuthorized(int, long long*)</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::ClientCursor::invalidate(mongo::StringData const&)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<pre>mongo::ClientCursor::deregisterRunner(mongo::Runner*)</pre>
#### Used By:
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/query/internal\_runner.cpp](../query\_system)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::ClientCursor::clientCursorsById</pre>
#### Used By:
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<pre>mongo::ClientCursor::ClientCursor(mongo::Runner*, int, mongo::BSONObj)</pre>
#### Used By:
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

-------------

Contains helper functions for running common operations against the local server. For example,  has findOne, ensureIndex, upsert, etc. which all just run the respective options on the server the  code is running on.

- src/mongo/db/dbhelpers.cpp   (mongod, tools)
- src/mongo/db/dbhelpers.h

## Interface
### src/mongo/db/dbhelpers.cpp
<pre>mongo::Helpers::findById(mongo::Client&, char const*, mongo::BSONObj, mongo::BSONObj&, bool*, bool*)</pre>
#### Used By:
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::ensureIndex(char const*, mongo::BSONObj, bool, char const*)</pre>
#### Used By:
- [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::Helpers::findById(mongo::Collection*, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::Helpers::RemoveSaver::~RemoveSaver()</pre>
#### Used By:
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::toKeyFormat(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::RemoveSaver::RemoveSaver(std::string const&, std::string const&, std::string const&)</pre>
#### Used By:
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::removeRange(mongo::KeyRange const&, bool, bool, mongo::Helpers::RemoveSaver*, bool, bool)</pre>
#### Used By:
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::reverseNaturalObj</pre>
#### Used By:
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::Helpers::RemoveSaver::goingToDelete(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)

<pre>mongo::Helpers::findAll(std::string const&, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<pre>mongo::Helpers::inferKeyPattern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::getLast(char const*, mongo::BSONObj&)</pre>
#### Used By:
- [src/mongo/db/repl/rs.cpp](../replication)

<pre>mongo::Helpers::putSingleton(char const*, mongo::BSONObj)</pre>
#### Used By:
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<pre>mongo::Helpers::upsert(std::string const&, mongo::BSONObj const&, bool)</pre>
#### Used By:
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Helpers::putSingletonGod(char const*, mongo::BSONObj, bool)</pre>
#### Used By:
- [src/mongo/db/repl/rs\_config.cpp](../replication)

<pre>mongo::Helpers::emptyCollection(char const*)</pre>
#### Used By:
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<pre>mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, bool)</pre>
#### Used By:
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<pre>mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)</pre>
#### Used By:
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<pre>mongo::Helpers::getLocsInRange(mongo::KeyRange const&, long long, std::set<mongo::DiskLoc, std::less<mongo::DiskLoc>, std::allocator<mongo::DiskLoc> >*, long long*, long long*)</pre>
#### Used By:
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)

-------------

Code to get a handle to the "system.profile" collection for a given Database

- src/mongo/db/introspect.cpp   (mongod, tools)
- src/mongo/db/introspect.h

## Interface
### src/mongo/db/introspect.cpp
<pre>mongo::getOrCreateProfileCollection(mongo::Database*, bool, std::string*)</pre>
#### Used By:
- [src/mongo/db/database.cpp](../storage\_layer\_structure)

<pre>mongo::profile(mongo::Client const&, int, mongo::CurOp&)</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

Just an enum for different cursor time limit states.

- src/mongo/db/max\_time.h

## Interface
