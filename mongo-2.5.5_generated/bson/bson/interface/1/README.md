
# Interface for Uncategorized BSON code
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/bson/bson\_validate.cpp

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/dbmessage.cpp](../../../../network/network\_core)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

### src/mongo/bson/oid.cpp

<div></div>

    mongo::BSONObjBuilder::numStrs

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../queries/update\_system)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/explain\_plan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/util/options\_parser/environment.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/projection.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/geo/hash.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/isself.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OID::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::OID::init()

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/client/gridfs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::OID::regenMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../queries/update\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../queries/update\_system)

<div></div>

    mongo::OID::init(std::string const&)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OID::initSequential()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../queries/update\_system)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/explain\_plan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../../utilities/utilities)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/util/options\_parser/environment.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/projection.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/geo/hash.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/isself.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OID::getMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::OID::asTimeT()

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)

### src/mongo/bson/optime.cpp

<div></div>

    mongo::OpTime::last

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../queries/update\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../../queries/update\_system)

<div></div>

    mongo::OpTime::notifier

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::OpTime::m

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../queries/update\_system)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../../queries/update\_system)

<div></div>

    mongo::OpTime::_now()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OpTime::max()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/bson/util/bson\_extract.cpp

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/client/auth\_helpers.cpp](../../../../utilities/utilities)

<div></div>

    mongo::bsonExtractIntegerField(mongo::BSONObj const&, mongo::StringData const&, long long*)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractIntegerFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, long long, long long*)

- Used By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::_okForStorage(bool, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::clientReadable() const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::MINKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::typeName(mongo::BSONType)

- Used By:

    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../queries/update\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../../queries/update\_system)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)

<div></div>

    mongo::BSONObj::md5() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)

<div></div>

    mongo::BSONNULL

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::GT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/geo/geoquery.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../../queries/update\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::minKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSIZE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LTE

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::staticUndefined

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BSONObj::valid() const

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::GTE

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)
    - [src/mongo/db/keypattern.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Used By:

    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONElement::Array() const

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/geo/geoparser.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../queries/update\_system)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MAXKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NIN

- Used By:

    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/query\_solution.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/db/query/plan\_enumerator.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/keypattern.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/query/interval.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/query\_planner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/type\_tags.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/query/planner\_access.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/merge\_sort.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Used By:

    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/client/syncclusterconnection.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BSONUndefined

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NE

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Used By:

    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::staticNull

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Used By:

    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::maxKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
