
# Interface

### src/mongo/util/concurrency/thread\_name.cpp

<div></div>

    mongo::setThreadName(mongo::StringData)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../../../network)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authentication)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/s/balancer\_policy.cpp](../../../sharding)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/db/query/plan\_enumerator.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../../../network)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/db/exec/index\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/tests.cpp](../../../dead\_code)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../sharding)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../full\_text\_search\_module)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../aggregation\_framework)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../journaling)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)
    - [src/mongo/db/structure/record\_store.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../../../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authentication)
    - [src/third\_party/s2/base/logging.cc](../../../s2)
    - [src/mongo/db/queryutil.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/log\_process\_details.cpp](../../../logging\_system)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/db/query/plan\_ranker.cpp](../../../core\_query\_system)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/startup\_warnings.cpp](../../../startup\_initialization)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../indexing)
    - [src/mongo/util/log.cpp](../../../logging\_system)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/db/index/fts\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/query/plan\_executor.cpp](../../../core\_query\_system)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/mmap.cpp](../../../mmap)
    - [src/mongo/db/exec/text.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/client/clientAndShell.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/dur\_commitjob.cpp](../../../journaling)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../../../sharding)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/geo/geoquery.cpp](../../../geo\_queries)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../aggregation\_framework)
    - [src/mongo/util/logfile.cpp](../../../journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../unit\_tests)
    - [src/mongo/util/mmap\_posix.cpp](../../../mmap)
    - [src/mongo/db/jsobj.cpp](../../../bson)
    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/third\_party/s2/s2polyline.cc](../../../s2)
    - [src/mongo/util/net/ssl\_manager.cpp](../../../network)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/lockstate.cpp](../../../concurrency)
    - [src/mongo/client/connpool.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../unit\_tests)
    - [src/mongo/db/storage/record.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/db/ops/delete.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/s/shardkey.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/unittest/unittest.cpp](../../../unit\_tests)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/query/stage\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/tools/files.cpp](../../../tools)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/query/query\_planner.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/index/btree\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/s/version\_manager.cpp](../../../sharding)
    - [src/mongo/dbtests/jsontests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authentication)
    - [src/mongo/s/d\_writeback.cpp](../../../sharding)
    - [src/mongo/scripting/bench.cpp](../../../javascript\_libraries)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/version\_mongos.cpp](../../../sharding)
    - [src/mongo/db/structure/btree/key.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/geo/geoparser.cpp](../../../geo\_queries)
    - [src/mongo/db/exec/projection.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/metadata\_loader.cpp](../../../sharding)
    - [src/mongo/client/parallel.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/scripting/v8\_utils.cpp](../../../javascript\_libraries)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../core\_query\_system)
    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/query/planner\_access.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/plan\_cache.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/tools/stat.cpp](../../../tools)
    - [src/mongo/db/storage/extent.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/sync.cpp](../../../replication)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/ssl\_options.cpp](../../../network)
    - [src/mongo/s/d\_merge.cpp](../../../sharding)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/projection.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)
    - [src/mongo/db/ops/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)
    - [src/mongo/util/net/message\_port.cpp](../../../network)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/exec/s2near.cpp](../../../core\_query\_system)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../authentication)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authorization\_session.cpp](../../../authentication)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/repl\_start.cpp](../../../replication)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/bson/optime.cpp](../../../bson)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/sharding.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/tools/import.cpp](../../../tools)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/util/file.cpp](../../../file\_interface)
    - [src/mongo/db/fts/fts\_command.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../../../journaling)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/s/d\_logic.cpp](../../../sharding)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../sharding)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../sharding)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/auth/user\_document\_parser.cpp](../../../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authentication)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/util/fail\_point.cpp](../../../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../../../web\_server)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/s/request.cpp](../../../sharding)
    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)