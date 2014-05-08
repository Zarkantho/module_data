
# Interface for Number To String Conversion
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/base/parse\_number.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned int>(mongo::StringData const&, int, unsigned int*)

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/projection.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/index/2d\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/bson/mutable/element.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/query/type\_explain.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned long long>(mongo::StringData const&, int, unsigned long long*)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<double>(mongo::StringData const&, int, double*)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Used By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)
    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
