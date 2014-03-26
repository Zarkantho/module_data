
# Interface for Mongod Client State Implementation
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/client.cpp

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Client::appendLastOp(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication/replication)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../security/authorization)
    - [src/mongo/db/prefetch.cpp](../../../storage/page\_fault\_utilities)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/s/d\_split.cpp](../../../sharding/sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/storage/record.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::Client::clientAddress(bool) const

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding/sharding)
    - [src/mongo/s/config.cpp](../../../sharding/sharding)

<div></div>

    mongo::Client::Context::_finishInit()

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pagefault.cpp](../../../storage/page\_fault\_utilities)

<div></div>

    mongo::OpDebug::reset()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication/replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../security/authorization)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities/utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/perftests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding/sharding)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/tools/oplog.cpp](../../../tools/tools)
    - [src/mongo/db/dur.cpp](../../../storage/journaling)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)

<div></div>

    mongo::Client::clients

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../../../network/web\_server)

<div></div>

    mongo::saveGLEStats(mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/s/shard.cpp](../../../sharding/sharding)

<div></div>

    mongo::Client::Context::~Context()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication/replication)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../sharding/sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../security/authorization)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/catalog/database.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../../../queries/database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../storage/page\_fault\_utilities)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/storage/record.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Client::recommendedYieldMicros(int*, int*, bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../../../queries/concurrency)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Client::clientsMutex

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../../../network/web\_server)

<div></div>

    mongo::Client::shutdown()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication/replication)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../queries/database\_commands)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities/utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/perftests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)
    - [src/mongo/dbtests/threadedtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/dur.cpp](../../../storage/journaling)
    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)

<div></div>

    mongo::currentClient

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities/utilities)
    - [src/mongo/db/commands/group.cpp](../../../queries/database\_commands)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/exec/2dnear.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/framework.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/exec/2d.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication/replication)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../../../replication/replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/db/pagefault.cpp](../../../storage/page\_fault\_utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dur\_commitjob.cpp](../../../storage/journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../../../queries/geo\_queries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/threadedtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/dur.cpp](../../../storage/journaling)
    - [src/mongo/db/catalog/database.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/lockstate.cpp](../../../queries/concurrency)
    - [src/mongo/db/prefetch.cpp](../../../storage/page\_fault\_utilities)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/storage/record.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../queries/indexing)
    - [src/mongo/db/structure/catalog/cap.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication/replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication/replication)
    - [src/mongo/db/exec/oplogstart.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/dbhash.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/config.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../queries/database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/geonear.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/d\_concurrency.cpp](../../../queries/concurrency)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/exec/s2near.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/validate.cpp](../../../queries/database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/s/d\_logic.cpp](../../../sharding/writeback\_listener)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::CachedBSONObj::_tooBig

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/clientlistplugin.cpp](../../../network/web\_server)

<div></div>

    mongo::Client::getActiveClientCount(int&, int&)

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../queries/concurrency)

<div></div>

    mongo::Client::gotHandshake(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication/replication)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/cursors.cpp](../../../sharding/sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../security/authorization)
    - [src/mongo/db/commands/server\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/connection\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../process\_management/logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/commands/group.cpp](../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding/sharding)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/catalog/database.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pdfile.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../queries/database\_commands)
