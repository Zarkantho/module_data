
# Interface for Mongos Specific Client State
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/s\_only.cpp

<div></div>

    mongo::Client::clientAddress(bool) const

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/util/signal\_handlers.cpp](../../../../utilities/utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Client::shutdown()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Command::execCommandClientBasic(mongo::Command*, mongo::ClientBasic&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::usingAShardConnection(std::string const&)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::currentClient

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/structure/catalog/cap.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/lockstate.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/exec/2d.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/exec/2dnear.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/geo/haystack.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
