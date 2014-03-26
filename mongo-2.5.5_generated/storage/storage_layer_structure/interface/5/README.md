
# Interface for Database Class
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/catalog/database.cpp

<div></div>

    mongo::Database::clearTmpCollections()

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)

<div></div>

    mongo::Database::setProfilingLevel(int, std::string&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Database::getOrCreateCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication/replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../sharding/sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../../../queries/geo\_queries)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/compact.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../queries/database\_commands)
    - [src/mongo/db/exec/2dnear.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/prefetch.cpp](../../../storage/page\_fault\_utilities)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/commands/storage\_details.cpp](../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/ops/count.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
    - [src/mongo/db/exec/2d.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::Database::duplicateUncasedName(bool, std::string const&, std::string const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)

<div></div>

    mongo::Database::dropCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::Database::_initExtentFreeList()

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Database::Database(char const*, bool&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../tests/unit\_tests)
