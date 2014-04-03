
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

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../queries/update\_system)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../../network/write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/query/explain\_plan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/bson/mutable/element.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/client/auth\_helpers.cpp](../../../../utilities/utilities)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../../network/write\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/projection.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
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
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/geo/shapes.cpp](../../../../queries/geo\_queries)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

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

    - [src/mongo/util/options\_parser/options\_parser.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)
    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
