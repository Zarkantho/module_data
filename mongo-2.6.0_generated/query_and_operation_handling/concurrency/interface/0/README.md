
# Interface for Mongod Concurrency System Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/d\_concurrency.cpp

<div></div>

    mongo::Lock::isR()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isLocked()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Lock::atLeastReadLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Lock::dbLevelLockingEnabled()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::GlobalWrite::downgrade()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::writelocktry::~writelocktry()

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/auth\_index\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::~UpgradeToExclusive()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::ScopedLock::recordTime()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::Lock::isReadLocked()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)

<div></div>

    mongo::Lock::isW()

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/stats/snapshots\_webplugins.cpp](../../../../utilities/utilities)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::readlocktry::~readlocktry()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::ParallelBatchWriterMode::iAmABatchParticipant()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::Lock::nested()

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Lock::GlobalWrite::upgrade()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::writelocktry::writelocktry(int)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Lock::ParallelBatchWriterMode::_batchLock

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::UpgradeToExclusive()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Lock::ScopedLock::resetTime()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
