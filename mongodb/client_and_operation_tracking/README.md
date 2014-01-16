# client\_and\_operation\_tracking

# Module Groups

-------------

# Group Description
mongos's version of a "Client". This is the big bucket of global state. This ALSO has the  definition of Command::execCommand for mongos (the function that actually runs commands registered  using the Command class, which gets called whenever a query against the "$cmd" collection is made)

# Files
- src/mongo/s/s\_only.cpp   (mongos)

# Interface

### src/mongo/s/s\_only.cpp

<div></div>

    mongo::Client::clientAddress(bool) const

- Used By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::Client::shutdown()

- Used By:

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

<div></div>

    mongo::Command::execCommandClientBasic(mongo::Command*, mongo::ClientBasic&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::usingAShardConnection(std::string const&)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../sharding)

<div></div>

    mongo::currentClient

- Used By:

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

<div></div>

    mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Used By:

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

# Group Description
mongod's version of a "Client". This is the big bucket of global state.  There is also the concept of a "Context" that one can take at the beginning of an operation that  holds a subset of the global state. There is also a "ReadContext" and a "WriteContext which  take locks. These are all nested classes in "Client". It's a bizarre situation because  "client.h" contains the declaration of the class, but there are two different definitions. One in  "s\_only.cpp" for mongos, and one in "client.cpp" for mongod. This means that mongos files may  contain "client.h" and pass compile fine when using something in it, but then may fail link  because it happens to be something that's only defined in "client.cpp". I don't see any  definitions so far for "Context" in mongos, and a grep for "Client::WriteContext::WriteContext"  (the definition of the WriteContext constructor) only shows up in client.cpp, which is mongod  only.

# Files
- src/mongo/db/client.cpp   (mongod, tools)
- src/mongo/db/client.h

# Interface

### src/mongo/db/client.cpp

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::appendLastOp(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Used By:

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

<div></div>

    mongo::Client::clientAddress(bool) const

- Used By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::Client::Context::_finishInit()

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::CachedBSONObj::_tooBig

- Used By:

    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<div></div>

    mongo::OpDebug::reset()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Used By:

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

<div></div>

    mongo::Client::Context::~Context()

- Used By:

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

<div></div>

    mongo::Client::recommendedYieldMicros(int*, int*, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::Client::clientsMutex

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<div></div>

    mongo::Client::clients

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

<div></div>

    mongo::Client::shutdown()

- Used By:

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

<div></div>

    mongo::currentClient

- Used By:

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

<div></div>

    mongo::Client::getActiveClientCount(int&, int&)

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::gotHandshake(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../replication)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

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

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Used By:

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

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Used By:

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

# Group Description
The current "operation" within the current "Client"

# Files
- src/mongo/db/curop-inl.h
- src/mongo/db/curop.cpp   (mongod, tools)
- src/mongo/db/curop.h
- src/mongo/db/curop\_test.cpp   ()

# Interface

### src/mongo/db/curop.cpp

<div></div>

    mongo::CurOp::ensureStarted()

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

<div></div>

    mongo::CurOp::enter(mongo::Client::Context*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::CurOp::reset()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::CurOp::info()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::getRemainingMaxTimeMicros() const

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::OpDebug::recordStats()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::kill(bool*)

- Used By:

    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::getOp(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

<div></div>

    mongo::CurOp::~CurOp()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::CurOp::setMaxTimeMicros(unsigned long long)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::CurOp::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

# Group Description
Functions to kill the current "operation"

# Files
- src/mongo/db/kill\_current\_op.cpp   (mongod, tools)
- src/mongo/db/kill\_current\_op.h

# Interface

### src/mongo/db/kill\_current\_op.cpp

<div></div>

    mongo::KillCurrentOp::reset()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Used By:

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

<div></div>

    mongo::KillCurrentOp::notifyAllWaiters()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::KillCurrentOp::killAll()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

# Group Description
Helpers to check whether the current operation in the current client has been interrupted.

# Files
- src/mongo/db/interrupt\_status.h
- src/mongo/db/interrupt\_status\_mongod.cpp   (mongod, tools)
- src/mongo/db/interrupt\_status\_mongod.h
- src/mongo/s/interrupt\_status\_mongos.cpp   (mongos)
- src/mongo/s/interrupt\_status\_mongos.h

# Interface
(not used outside this module)

-------------

# Group Description
Base class for a Client on mongod and mongos: ClientBasic

# Files
- src/mongo/db/client\_basic.cpp   (mongod, tools, mongos)
- src/mongo/db/client\_basic.h

# Interface

### src/mongo/db/client\_basic.cpp

<div></div>

    mongo::ClientBasic::hasAuthorizationSession() const

- Used By:

    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)

<div></div>

    mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<div></div>

    mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Used By:

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

# Group Description
Seems to be the "mongos only" version of the "Client" class: ClientInfo Also inherits from ClientBasic

# Files
- src/mongo/s/client\_info.cpp   (mongos)
- src/mongo/s/client\_info.h

# Interface

### src/mongo/s/client\_info.cpp

<div></div>

    mongo::ClientInfo::getLastError(std::string const&, mongo::BSONObj const&, mongo::BSONObjBuilder&, std::string&, bool)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

<div></div>

    mongo::ClientInfo::newRequest()

- Used By:

    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)

<div></div>

    mongo::ClientInfo::enforceWriteConcern(std::string const&, mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

<div></div>

    mongo::ClientInfo::disableForCommand()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

<div></div>

    mongo::ClientInfo::addHostOpTimes(std::map<mongo::ConnectionString, mongo::OpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::OpTime> > > const&)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClientInfo::create(mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ClientInfo::newPeerRequest(mongo::HostAndPort const&)

- Used By:

    - [src/mongo/s/request.cpp](../sharding)

<div></div>

    mongo::ClientInfo::exists()

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

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

# Group Description
The database's internal concept of a cursor from a client

# Files
- src/mongo/db/clientcursor.cpp   (mongod, tools)
- src/mongo/db/clientcursor.h

# Interface

### src/mongo/db/clientcursor.cpp

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(long long)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::find(std::string const&, std::set<long long, std::less<long long>, std::allocator<long long> >&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::ClientCursor::~ClientCursor()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<div></div>

    mongo::ClientCursorPin::c() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<div></div>

    mongo::ClientCursor::updateSlaveLocation(mongo::CurOp&)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::ClientCursor::idleTimeReport(unsigned int)

- Used By:

    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::ClientCursor(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Used By:

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

<div></div>

    vtable for mongo::ClientCursorMonitor

- Used By:

    - [src/mongo/db/d\_globals.cpp](../legacy\_code)

<div></div>

    mongo::ClientCursor::erase(long long)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::shouldTimeout(unsigned int)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::aboutToDelete(mongo::StringData const&, mongo::NamespaceDetails const*, mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursor::eraseIfAuthorized(int, long long*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursor::invalidate(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursor::deregisterRunner(mongo::Runner*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::clientCursorsById

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Runner*, int, mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

-------------

# Group Description
Contains helper functions for running common operations against the local server. For example,  has findOne, ensureIndex, upsert, etc. which all just run the respective options on the server the  code is running on.

# Files
- src/mongo/db/dbhelpers.cpp   (mongod, tools)
- src/mongo/db/dbhelpers.h

# Interface

### src/mongo/db/dbhelpers.cpp

<div></div>

    mongo::Helpers::findById(mongo::Client&, char const*, mongo::BSONObj, mongo::BSONObj&, bool*, bool*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::ensureIndex(char const*, mongo::BSONObj, bool, char const*)

- Used By:

    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::Helpers::findById(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::Helpers::RemoveSaver::~RemoveSaver()

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::toKeyFormat(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::RemoveSaver::RemoveSaver(std::string const&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::removeRange(mongo::KeyRange const&, bool, bool, mongo::Helpers::RemoveSaver*, bool, bool)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::reverseNaturalObj

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::Helpers::RemoveSaver::goingToDelete(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)

<div></div>

    mongo::Helpers::findAll(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Helpers::inferKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::getLast(char const*, mongo::BSONObj&)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::Helpers::putSingleton(char const*, mongo::BSONObj)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<div></div>

    mongo::Helpers::upsert(std::string const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::Helpers::putSingletonGod(char const*, mongo::BSONObj, bool)

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::Helpers::emptyCollection(char const*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<div></div>

    mongo::Helpers::getLocsInRange(mongo::KeyRange const&, long long, std::set<mongo::DiskLoc, std::less<mongo::DiskLoc>, std::allocator<mongo::DiskLoc> >*, long long*, long long*)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)

-------------

# Group Description
Code to get a handle to the "system.profile" collection for a given Database

# Files
- src/mongo/db/introspect.cpp   (mongod, tools)
- src/mongo/db/introspect.h

# Interface

### src/mongo/db/introspect.cpp

<div></div>

    mongo::getOrCreateProfileCollection(mongo::Database*, bool, std::string*)

- Used By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

-------------

# Group Description
Just an enum for different cursor time limit states.

# Files
- src/mongo/db/max\_time.h

# Interface
(not used outside this module)
