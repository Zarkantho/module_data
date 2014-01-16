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

- <pre>mongo::validateBSON(char const*, unsigned long long)</pre>
Used By:
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

- <pre>mongo::BSONObjBuilder::numStrs</pre>
Used By:
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

- <pre>mongo::OID::hash_combine(unsigned long&) const</pre>
Used By:
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)

- <pre>mongo::OID::init()</pre>
Used By:
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

- <pre>mongo::OID::regenMachineId()</pre>
Used By:
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

- <pre>mongo::operator<<(std::ostream&, mongo::OID const&)</pre>
Used By:
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

- <pre>mongo::OID::init(mongo::Date_t, bool)</pre>
Used By:
    - [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

- <pre>mongo::OID::init(std::string const&)</pre>
Used By:
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

- <pre>mongo::OID::initSequential()</pre>
Used By:
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONObjBuilder::numStrsReady</pre>
Used By:
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

- <pre>mongo::OID::getMachineId()</pre>
Used By:
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

- <pre>mongo::OID::asTimeT()</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

### src/mongo/bson/optime.cpp

- <pre>mongo::OpTime::last</pre>
Used By:
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)

- <pre>mongo::OpTime::now(mongo::mutex::scoped_lock const&)</pre>
Used By:
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

- <pre>mongo::OpTime::notifier</pre>
Used By:
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)

- <pre>mongo::OpTime::m</pre>
Used By:
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/insert.cpp](../query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

- <pre>mongo::OpTime::_now()</pre>
Used By:
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

- <pre>mongo::OpTime::waitForDifferent(unsigned int)</pre>
Used By:
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)</pre>
Used By:
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/bson/util/bson\_extract.cpp

- <pre>mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)</pre>
Used By:
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

- <pre>mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)</pre>
Used By:
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp

- <pre>mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

- <pre>mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)</pre>
Used By:
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - src/mongo/client/sasl\_client\_authenticate\_impl.cpp
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)

- <pre>mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)</pre>
Used By:
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

### src/mongo/db/jsobj.cpp

- <pre>mongo::BSONObj::_okForStorage(bool, bool) const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSIZE</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

- <pre>mongo::BSONObj::clientReadable() const</pre>
Used By:
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/query/index\_bounds.cpp](../query\_system)
    - [src/mongo/db/queryutil.cpp](../query\_system)

- <pre>mongo::MINKEY</pre>
Used By:
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONObj::couldBeArray() const</pre>
Used By:
    - [src/mongo/db/exec/projection\_exec.cpp](../query\_system)

- <pre>mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::typeName(mongo::BSONType)</pre>
Used By:
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

- <pre>mongo::BSONObj::md5() const</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

- <pre>mongo::GT</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)

- <pre>mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/d\_split.cpp](../sharding)

- <pre>mongo::BSONNULL</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

- <pre>mongo::BSONElement::getGtLtOp(int) const</pre>
Used By:
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

- <pre>mongo::minKey</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)

- <pre>mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONObj::filterFieldsUndotted(mongo::BSONObj const&, bool) const</pre>
Used By:
    - [src/mongo/s/writeback\_listener.cpp](../sharding)

- <pre>mongo::LTE</pre>
Used By:
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

- <pre>mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::staticUndefined</pre>
Used By:
    - [src/mongo/db/queryutil.cpp](../query\_system)

- <pre>mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/shard\_key\_pattern.cpp](../sharding)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::LT</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONObj::valid() const</pre>
Used By:
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

- <pre>mongo::GTE</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

- <pre>mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

- <pre>mongo::getGtLtOp(mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

- <pre>mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)</pre>
Used By:
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)

- <pre>mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const</pre>
Used By:
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

- <pre>mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const</pre>
Used By:
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONElement::Array() const</pre>
Used By:
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

- <pre>mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::MAXKEY</pre>
Used By:
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::NIN</pre>
Used By:
    - [src/mongo/client/distlock.cpp](../sharding)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

- <pre>mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const</pre>
Used By:
    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

- <pre>mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const</pre>
Used By:
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

- <pre>mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const</pre>
Used By:
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

- <pre>mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const</pre>
Used By:
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

- <pre>mongo::BSONUndefined</pre>
Used By:
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

- <pre>mongo::NE</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/tools/files.cpp](../tools)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

- <pre>mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)

- <pre>mongo::BSONObj::getFieldDottedOrArray(char const*&) const</pre>
Used By:
    - [src/mongo/db/fts/fts\_matcher.cpp](../full\_text\_search\_module)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)

- <pre>mongo::staticNull</pre>
Used By:
    - [src/mongo/db/queryutil.cpp](../query\_system)

- <pre>mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const</pre>
Used By:
    - [src/mongo/tools/export.cpp](../tools)

- <pre>mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

- <pre>mongo::maxKey</pre>
Used By:
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/queryutil.cpp](../query\_system)

- <pre>mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const</pre>
Used By:
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/tools/dump.cpp](../tools)

### src/mongo/db/json.cpp

- <pre>mongo::fromjson(std::string const&)</pre>
Used By:
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

- <pre>mongo::fromjson(char const*, int*)</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::setValueSafeNum(mongo::SafeNum)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::isNumeric() const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementSafeNum(mongo::StringData const&, mongo::SafeNum)</pre>
Used By:
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::disableInPlaceUpdates()</pre>
Used By:
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::mutablebson::ConstElement)</pre>
Used By:
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::reset()</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::isIntegral() const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::rightSibling() const</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::compareWithElement(mongo::mutablebson::ConstElement const&, bool) const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementDate(mongo::StringData const&, mongo::Date_t)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementTimestamp(mongo::StringData const&, mongo::OpTime)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::Document()</pre>
Used By:
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)

- <pre>mongo::mutablebson::Element::getValueSafeNum() const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::getValue() const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::remove()</pre>
Used By:
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::rightChild() const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::leftChild() const</pre>
Used By:
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

- <pre>mongo::mutablebson::Document::getInPlaceUpdates(std::vector<mongo::mutablebson::DamageEvent, std::allocator<mongo::mutablebson::DamageEvent> >*, char const**, unsigned long*)</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)

- <pre>mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::getType() const</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::setValueTimestamp(mongo::OpTime)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)</pre>
Used By:
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

- <pre>mongo::mutablebson::Element::setValueString(mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

- <pre>mongo::mutablebson::Document::reset(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

- <pre>mongo::mutablebson::Document::makeElement(mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementBool(mongo::StringData const&, bool)</pre>
Used By:
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::leftSibling() const</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::compareWithBSONElement(mongo::BSONElement const&, bool) const</pre>
Used By:
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::setValueDate(mongo::Date_t)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::hasChildren() const</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::makeElementNewOID(mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)

- <pre>mongo::mutablebson::Element::setValueObject(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::parent() const</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::setValueBSONElement(mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::setValueNull()</pre>
Used By:
    - [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)

- <pre>mongo::mutablebson::Document::~Document()</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::addSiblingRight(mongo::mutablebson::Element)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::getFieldName() const</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::appendElement(mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

- <pre>mongo::mutablebson::Element::operator[](mongo::StringData const&) const</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::appendBool(mongo::StringData const&, bool)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

- <pre>mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

- <pre>mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::toString() const</pre>
Used By:
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

- <pre>mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

- <pre>mongo::mutablebson::Element::appendLong(mongo::StringData const&, long long)</pre>
Used By:
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

- <pre>mongo::mutablebson::Element::appendInt(mongo::StringData const&, int)</pre>
Used By:
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

- <pre>mongo::mutablebson::Element::appendNull(mongo::StringData const&)</pre>
Used By:
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::operator[](unsigned long) const</pre>
Used By:
    - [src/mongo/db/ops/path\_support.cpp](../update\_system)

- <pre>mongo::mutablebson::Element::pushFront(mongo::mutablebson::Element)</pre>
Used By:
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../update\_system)

### src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp

- <pre>mongo::mutablebson::checkEqualNoOrdering(mongo::mutablebson::Document const&, mongo::mutablebson::Document const&)</pre>
Used By:
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)

- <pre>mongo::mutablebson::operator<<(std::ostream&, mongo::mutablebson::UnorderedWrapper_Obj const&)</pre>
Used By:
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
