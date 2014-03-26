
# Interface

### src/mongo/bson/bson\_validate.cpp

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/dbmessage.cpp](../../../network\_core)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/bsondump.cpp](../../../tools)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/tools/bridge.cpp](../../../tools)

### src/mongo/bson/oid.cpp

<div></div>

    mongo::BSONObjBuilder::numStrs

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/expressiontests.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../../../core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/query/explain\_plan.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../utilities)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/util/version.cpp](../../../build\_information)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/util/options\_parser/environment.cpp](../../../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../../../javascript\_libraries)
    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/projection.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)
    - [src/mongo/db/geo/hash.cpp](../../../geo\_queries)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../sharding)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../tools)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../geo\_queries)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)

<div></div>

    mongo::OID::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)

<div></div>

    mongo::OID::init()

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/db/structure/btree/key.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/client/gridfs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../sharding)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::OID::regenMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/type\_chunk.cpp](../../../sharding)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)

<div></div>

    mongo::OID::init(std::string const&)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::OID::initSequential()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/expressiontests.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../../../core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/query/explain\_plan.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../utilities)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/util/version.cpp](../../../build\_information)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/util/options\_parser/environment.cpp](../../../startup\_initialization)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../../../javascript\_libraries)
    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/projection.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)
    - [src/mongo/db/geo/hash.cpp](../../../geo\_queries)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../sharding)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../tools)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../geo\_queries)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)

<div></div>

    mongo::OID::getMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)

<div></div>

    mongo::OID::asTimeT()

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)

### src/mongo/bson/optime.cpp

<div></div>

    mongo::OpTime::last

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)

<div></div>

    mongo::OpTime::notifier

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)

<div></div>

    mongo::OpTime::m

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)

<div></div>

    mongo::OpTime::_now()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::OpTime::max()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

### src/mongo/bson/util/bson\_extract.cpp

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../authorization)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/client/auth\_helpers.cpp](../../../utilities)

<div></div>

    mongo::bsonExtractIntegerField(mongo::BSONObj const&, mongo::StringData const&, long long*)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../authorization)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../database\_commands)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../authorization)

<div></div>

    mongo::bsonExtractIntegerFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, long long, long long*)

- Used By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../authorization)

<div></div>

    mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../cpp\_client\_driver)

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObj::_okForStorage(bool, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/s/shardkey.cpp](../../../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObj::clientReadable() const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../../../core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)

<div></div>

    mongo::MINKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../core\_query\_system)

<div></div>

    mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::typeName(mongo::BSONType)

- Used By:

    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/pipeline/expression.cpp](../../../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::BSONObj::md5() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::BSONNULL

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../unit\_tests)

<div></div>

    mongo::GT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../sharding)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../aggregation\_framework)
    - [src/mongo/db/geo/geoquery.cpp](../../../geo\_queries)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../full\_text\_search\_module)

<div></div>

    mongo::minKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)

<div></div>

    mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSIZE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::LTE

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)

<div></div>

    mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::staticUndefined

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)

<div></div>

    mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../../../sharding)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::LT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../sharding)

<div></div>

    mongo::BSONObj::valid() const

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    mongo::GTE

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)

<div></div>

    mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)
    - [src/mongo/db/keypattern.cpp](../../../indexing)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Used By:

    - [src/mongo/db/structure/btree/key.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::BSONElement::Array() const

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/geo/geoparser.cpp](../../../geo\_queries)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::MAXKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::NIN

- Used By:

    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../sharding)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/exec/2dcommon.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/query\_solution.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/s/balancer\_policy.cpp](../../../sharding)
    - [src/mongo/db/query/plan\_enumerator.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/keypattern.cpp](../../../indexing)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../core\_query\_system)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/index\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/range\_arithmetic.cpp](../../../sharding)
    - [src/mongo/db/query/interval.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/expressiontests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../../../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../core\_query\_system)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../core\_query\_system)
    - [src/mongo/s/shardkey.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/db/query/query\_planner.cpp](../../../core\_query\_system)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/db/structure/btree/key.cpp](../../../storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../mutable\_bson)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/type\_tags.cpp](../../../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../../../core\_query\_system)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../indexing)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)
    - [src/mongo/db/exec/and\_hash.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../indexing)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../sharding)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/merge\_sort.cpp](../../../core\_query\_system)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Used By:

    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/tools/bsondump.cpp](../../../tools)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/tools/export.cpp](../../../tools)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/db/index/btree\_interface.cpp](../../../indexing)
    - [src/mongo/client/syncclusterconnection.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::BSONUndefined

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)

<div></div>

    mongo::NE

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/tools/files.cpp](../../../tools)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/tools/import.cpp](../../../tools)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Used By:

    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../../../full\_text\_search\_module)

<div></div>

    mongo::staticNull

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Used By:

    - [src/mongo/tools/export.cpp](../../../tools)

<div></div>

    mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../core\_query\_system)

<div></div>

    mongo::maxKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../sharding)
    - [src/mongo/tools/dump.cpp](../../../tools)
