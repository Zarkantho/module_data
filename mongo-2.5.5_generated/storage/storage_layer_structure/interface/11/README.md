
# Interface

### src/mongo/db/storage\_options.cpp

<div></div>

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

<div></div>

    mongo::storageGlobalParams

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authorization)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../aggregation\_framework)
    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../../../replication)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/mmaptests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)
