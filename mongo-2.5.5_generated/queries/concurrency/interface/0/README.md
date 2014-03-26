
# Interface for Core Database Locks
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/concurrency/rwlockimpl.cpp

<div></div>

    mongo::SimpleRWLock::lock_shared()

- Used By:

    - [src/mongo/util/trace.cpp](../../../../dead\_code/dead\_code)

<div></div>

    mongo::SimpleRWLock::unlock_shared()

- Used By:

    - [src/mongo/util/trace.cpp](../../../../dead\_code/dead\_code)

<div></div>

    mongo::SimpleRWLock::SimpleRWLock(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/trace.cpp](../../../../dead\_code/dead\_code)

<div></div>

    mongo::SimpleRWLock::unlock()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/trace.cpp](../../../../dead\_code/dead\_code)

<div></div>

    mongo::SimpleRWLock::lock()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/trace.cpp](../../../../dead\_code/dead\_code)

### src/mongo/db/d\_concurrency.cpp

<div></div>

    mongo::Lock::isR()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::ParallelBatchWriterMode::iAmABatchParticipant()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Used By:

    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)

<div></div>

    mongo::Lock::GlobalWrite::downgrade()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::Lock::isLocked()

- Used By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::readlocktry::~readlocktry()

- Used By:

    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::Lock::GlobalWrite::upgrade()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::dbLevelLockingEnabled()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::atLeastReadLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::writelocktry::~writelocktry()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::writelocktry::writelocktry(int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::nested()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::ParallelBatchWriterMode::_batchLock

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../queries/indexing)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::~UpgradeToExclusive()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::UpgradeToExclusive()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Used By:

    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::isReadLocked()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Lock::isW()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/stats/snapshots\_webplugins.cpp](../../../../utilities/utilities)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/lockstat.cpp

<div></div>

    mongo::LockStat::reset()

- Used By:

    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LockStat::report() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LockStat::report(mongo::StringBuilderImpl<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)

### src/mongo/db/lockstate.cpp

<div></div>

    mongo::LockState::LockState()

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::Acquiring::~Acquiring()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LockState::hasAnyReadLock() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LockState::reportState(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::Acquiring::Acquiring(mongo::Lock::ScopedLock*, mongo::LockState&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LockState::Dump()

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)

<div></div>

    mongo::LockState::hasAnyWriteLock() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LockState::reportState()

- Used By:

    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
