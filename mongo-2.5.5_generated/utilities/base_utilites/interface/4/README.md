
# Interface

### src/mongo/base/parse\_number.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned int>(mongo::StringData const&, int, unsigned int*)

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../bson)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../update\_system)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../sharding)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../../../core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/db/query/explain\_plan.cpp](../../../core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../utilities)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../startup\_initialization)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/commands/distinct.cpp](../../../database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/pipeline/value.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/projection.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
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
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../wire\_protocol\_write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../tools)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
    - [src/mongo/util/version.cpp](../../../build\_information)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/geo/shapes.cpp](../../../geo\_queries)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned long long>(mongo::StringData const&, int, unsigned long long*)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<double>(mongo::StringData const&, int, double*)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../startup\_initialization)
    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)
    - [src/mongo/util/version.cpp](../../../build\_information)
    - [src/mongo/util/time\_support.cpp](../../../utilities)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../startup\_initialization)
    - [src/mongo/db/json.cpp](../../../bson)
