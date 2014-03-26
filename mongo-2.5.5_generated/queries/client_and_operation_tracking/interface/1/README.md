
# Interface

### src/mongo/db/client.cpp

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Client::appendLastOp(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/storage/record.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::Client::clientAddress(bool) const

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)

<div></div>

    mongo::Client::Context::_finishInit()

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)

<div></div>

    mongo::OpDebug::reset()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authorization)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/tools/oplog.cpp](../../../tools)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/tools/tool.cpp](../../../tools)

<div></div>

    mongo::Client::clients

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../../../web\_server)

<div></div>

    mongo::saveGLEStats(mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/s/shard.cpp](../../../sharding)

<div></div>

    mongo::Client::Context::~Context()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/repl/sync.cpp](../../../replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/db/storage/record.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)

<div></div>

    mongo::Client::recommendedYieldMicros(int*, int*, bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Client::clientsMutex

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../../../web\_server)

<div></div>

    mongo::Client::shutdown()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/dbtests/threadedtests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/tools/tool.cpp](../../../tools)

<div></div>

    mongo::currentClient

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/exec/2dnear.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/exec/2d.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../../../replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/dur\_commitjob.cpp](../../../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/dbtests/threadedtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../../../concurrency)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/storage/record.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/structure/catalog/cap.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/exec/oplogstart.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/sync.cpp](../../../replication)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/s2near.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::CachedBSONObj::_tooBig

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/clientlistplugin.cpp](../../../web\_server)

<div></div>

    mongo::Client::getActiveClientCount(int&, int&)

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)

<div></div>

    mongo::Client::gotHandshake(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../authorization)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../aggregation\_framework)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/repl/sync.cpp](../../../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)
