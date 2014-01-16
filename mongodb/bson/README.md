# bson

# Module Groups

-------------

# Group Description
BSON library   is this library standalone? (lots of third party stuff might want to make   use of BSON) - what does it depend on?   why is some of this stuff in db/ ?

# Files
- src/mongo/bson/bson-inl.h
- src/mongo/bson/bson\_builder\_base.h
- src/mongo/bson/bson\_db.h
- src/mongo/bson/bson\_field.h
- src/mongo/bson/bson\_field\_test.cpp   ()
- src/mongo/bson/bson\_obj\_test.cpp   ()
- src/mongo/bson/bson\_validate.cpp   (cppclientdriver)
- src/mongo/bson/bson\_validate.h
- src/mongo/bson/bson\_validate\_test.cpp   ()
- src/mongo/bson/bsondemo/bsondemo.cpp   ()
- src/mongo/bson/bsonelement.h
- src/mongo/bson/bsonmisc.h
- src/mongo/bson/bsonobj.h
- src/mongo/bson/bsonobjbuilder.h
- src/mongo/bson/bsonobjbuilder\_test.cpp   ()
- src/mongo/bson/bsonobjiterator.h
- src/mongo/bson/bsontypes.h
- src/mongo/bson/inline\_decls.h
- src/mongo/bson/oid.cpp   (mongod, tools, mongos)
- src/mongo/bson/oid.h
- src/mongo/bson/optime.cpp   (mongod, tools, mongos)
- src/mongo/bson/optime.h
- src/mongo/bson/ordering.h
- src/mongo/bson/util/atomic\_int.h
- src/mongo/bson/util/bson\_extract.cpp   (cppclientdriver)
- src/mongo/bson/util/bson\_extract.h
- src/mongo/bson/util/bson\_extract\_test.cpp   ()
- src/mongo/bson/util/builder.h
- src/mongo/bson/util/builder\_test.cpp   ()
- src/mongo/bson/util/misc.h
- src/mongo/db/jsobj.cpp   (cppclientdriver)
- src/mongo/db/jsobj.h
- src/mongo/db/jsobjmanipulator.h
- src/mongo/db/json.cpp   (mongod, tools, mongos)
- src/mongo/db/json.h

# Interface

### src/mongo/bson/bson\_validate.cpp

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)

### src/mongo/bson/oid.cpp

<div></div>

    mongo::BSONObjBuilder::numStrs

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../query\_system)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/version.cpp](../utilities)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/projection.cpp](../query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/db/exec/projection\_exec.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/client/examples/authTest.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/util/version.cpp](../utilities)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::OID::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

<div></div>

    mongo::OID::init()

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/ops/insert.cpp](../query\_system)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::OID::regenMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::OID::init(mongo::Date_t, bool)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::OID::init(std::string const&)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<div></div>

    mongo::OID::initSequential()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/db/geo/hash.cpp](../geo\_queries)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../query\_system)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/util/version.cpp](../utilities)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../sharding)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/scripting/v8\_utils.cpp](../javascript\_libraries)
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/projection.cpp](../query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/db/exec/projection\_exec.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/oplog.cpp](../tools)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/client/examples/authTest.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/d\_logic.cpp](../sharding)
    - [src/mongo/util/version.cpp](../utilities)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<div></div>

    mongo::OID::getMachineId()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<div></div>

    mongo::OID::asTimeT()

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

### src/mongo/bson/optime.cpp

<div></div>

    mongo::OpTime::last

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

<div></div>

    mongo::OpTime::notifier

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::OpTime::m

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

<div></div>

    mongo::OpTime::_now()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/bson/util/bson\_extract.cpp

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

<div></div>

    mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::BSONObj::_okForStorage(bool, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSIZE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::clientReadable() const

- Used By:

    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../query\_system)
    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::MINKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../query\_system)

<div></div>

    mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::typeName(mongo::BSONType)

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/pipeline/expression.cpp](../aggregation\_framework)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/bson/util/bson\_extract.cpp](../bson)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::BSONObj::md5() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::GT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../sharding)

<div></div>

    mongo::BSONNULL

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

<div></div>

    mongo::minKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::filterFieldsUndotted(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../sharding)

<div></div>

    mongo::LTE

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::staticUndefined

- Used By:

    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../sharding)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::LT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::valid() const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::GTE

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<div></div>

    mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)

- Used By:

    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONElement::Array() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MAXKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::NIN

- Used By:

    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/query/query\_solution.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/s/balancer\_policy.cpp](../sharding)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/exec/and\_sorted.cpp](../query\_system)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/range\_arithmetic.cpp](../sharding)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/query/interval.cpp](../query\_system)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/db/exec/sort.cpp](../query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../query\_system)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/query/planner\_analysis.cpp](../query\_system)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/query/query\_planner.cpp](../query\_system)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../sharding)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/s/type\_tags.cpp](../sharding)
    - [src/mongo/db/query/planner\_access.cpp](../query\_system)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/index\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/db/exec/and\_hash.cpp](../query\_system)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../sharding)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/db/exec/merge\_sort.cpp](../query\_system)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/client/examples/second.cpp](../cpp\_client\_driver)
    - src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/client/examples/first.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/export.cpp](../tools)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/client/examples/whereExample.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONUndefined

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::NE

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Used By:

    - [src/mongo/db/fts/fts\_matcher.cpp](../full\_text\_search\_module)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)

<div></div>

    mongo::staticNull

- Used By:

    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Used By:

    - [src/mongo/tools/export.cpp](../tools)

<div></div>

    mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<div></div>

    mongo::maxKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/tools/dump.cpp](../tools)

### src/mongo/db/json.cpp

<div></div>

    mongo::fromjson(std::string const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
    - [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::fromjson(char const*, int*)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/examples/tutorial.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

# Dependencies

### src/mongo/bson/bson\_field\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/bson\_obj\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/bson\_validate.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/bson/bson\_validate\_test.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::PseudoRandom::PseudoRandom(int)

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/bson/bsondemo/bsondemo.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/bsonobjbuilder\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/oid.cpp

<div></div>

    mongo::SecureRandom::create()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/bson/optime.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/bson/util/bson\_extract.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/bson/util/bson\_extract\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/util/builder\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<unsigned int>(mongo::StringData const&, int, unsigned int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    _md5_finish

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    _md5_init

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LexNumCmp::LexNumCmp(bool)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LexNumCmp::cmp(mongo::StringData const&, mongo::StringData const&) const

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::base64::encode(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&, char const*, int)

- Provided By:

    - [src/mongo/util/base64.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::LexNumCmp::operator()(mongo::StringData const&, mongo::StringData const&) const

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    _md5_append

- Provided By:

    - [src/mongo/util/md5.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/json.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::base64::chars

- Provided By:

    - [src/mongo/util/base64.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ErrorCodes::errorString(mongo::ErrorCodes::Error)

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/client\_build/mongo/base/error\_codes.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::base64::decode(std::string const&)

- Provided By:

    - [src/mongo/util/base64.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Mutable BSON is built on top of the BSON library. It has a mutable, consistently sized vector of  the changes that have been made to an object.   is this part of libbson? does this depend on bson/* ?

# Files
- src/mongo/bson/mutable/algorithm.h
- src/mongo/bson/mutable/const\_element-inl.h
- src/mongo/bson/mutable/const\_element.h
- src/mongo/bson/mutable/damage\_vector.h
- src/mongo/bson/mutable/document-inl.h
- src/mongo/bson/mutable/document.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.h
- src/mongo/bson/mutable/element-inl.h
- src/mongo/bson/mutable/element.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.h
- src/mongo/bson/mutable/mutable\_bson\_algo\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.h

# Interface

### src/mongo/bson/mutable/document.cpp

<div></div>

    mongo::mutablebson::Element::setValueSafeNum(mongo::SafeNum)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::isNumeric() const

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementSafeNum(mongo::StringData const&, mongo::SafeNum)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::disableInPlaceUpdates()

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::mutablebson::ConstElement)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::reset()

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::isIntegral() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::rightSibling() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::compareWithElement(mongo::mutablebson::ConstElement const&, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementDate(mongo::StringData const&, mongo::Date_t)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementTimestamp(mongo::StringData const&, mongo::OpTime)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::Document()

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::getValueSafeNum() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::getValue() const

- Used By:

    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::remove()

- Used By:

    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::rightChild() const

- Used By:

    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::leftChild() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::getInPlaceUpdates(std::vector<mongo::mutablebson::DamageEvent, std::allocator<mongo::mutablebson::DamageEvent> >*, char const**, unsigned long*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::getType() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueTimestamp(mongo::OpTime)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::mutablebson::Document::reset(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::mutablebson::Document::makeElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementBool(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::leftSibling() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::compareWithBSONElement(mongo::BSONElement const&, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueDate(mongo::Date_t)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::hasChildren() const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementNewOID(mongo::StringData const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::mutablebson::Element::setValueObject(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::parent() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueBSONElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueNull()

- Used By:

    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::Element::addSiblingRight(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::getFieldName() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)

### src/mongo/bson/mutable/element.cpp

<div></div>

    mongo::mutablebson::Element::appendElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::mutablebson::Element::operator[](mongo::StringData const&) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::appendBool(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::toString() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::mutablebson::Element::appendLong(mongo::StringData const&, long long)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::mutablebson::Element::appendInt(mongo::StringData const&, int)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::mutablebson::Element::appendNull(mongo::StringData const&)

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::operator[](unsigned long) const

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::pushFront(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

### src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp

<div></div>

    mongo::mutablebson::checkEqualNoOrdering(mongo::mutablebson::Document const&, mongo::mutablebson::Document const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::operator<<(std::ostream&, mongo::mutablebson::UnorderedWrapper_Obj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

# Dependencies

### src/mongo/bson/mutable/document.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/mutable/element.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/bson/mutable/mutable\_bson\_algo\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/bson/mutable/mutable\_bson\_test.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::SafeNum::isEquivalent(mongo::SafeNum const&) const

- Provided By:

    - [src/mongo/util/safe\_num.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::SafeNum const&)

- Provided By:

    - [src/mongo/util/safe\_num.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::jsTime()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)
