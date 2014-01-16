# concurrency

# Module Groups

-------------

Core locks library. Only in mongod.   can you say a bit more? e.g. database locks are RWlocks, but what *are*   they exactly? any sort of fairness or other performance/"how to use" info?  TODO: There are also a bunch of concurrency related helpers in the UTILITIES section.

- src/mongo/util/concurrency/rwlock.h
- src/mongo/util/concurrency/rwlockimpl.cpp   (cppclientdriver)
- src/mongo/util/concurrency/rwlockimpl.h
- src/mongo/db/d\_concurrency.cpp   (mongod, tools)
- src/mongo/db/d\_concurrency.h
- src/mongo/db/lockstat.cpp   (mongod, tools)
- src/mongo/db/lockstat.h
- src/mongo/db/lockstate.cpp   (mongod, tools)
- src/mongo/db/lockstate.h

## Interface


### src/mongo/util/concurrency/rwlockimpl.cpp

<pre>mongo::SimpleRWLock::SimpleRWLock(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::SimpleRWLock::unlock()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::SimpleRWLock::lock()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

### src/mongo/db/d\_concurrency.cpp

<pre>mongo::Lock::isR()</pre>

#### Used By:

- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Lock::ParallelBatchWriterMode::iAmABatchParticipant()</pre>

#### Used By:

- [src/mongo/db/repl/rs\_sync.cpp](../replication)

<pre>mongo::Lock::somethingWriteLocked()</pre>

#### Used By:

- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/index\_builder.cpp](../indexing)

<pre>mongo::Lock::GlobalWrite::downgrade()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)

<pre>mongo::writelocktry::~writelocktry()</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::DBRead::DBRead(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/repl/rs.cpp](../replication)

<pre>mongo::readlocktry::~readlocktry()</pre>

#### Used By:

- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Lock::GlobalRead::GlobalRead(int)</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Lock::GlobalWrite::upgrade()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::dbLevelLockingEnabled()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::atLeastReadLocked(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::isWriteLocked(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)

<pre>mongo::writelocktry::writelocktry(int)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::nested()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::ParallelBatchWriterMode::_batchLock</pre>

#### Used By:

- [src/mongo/db/repl/rs\_sync.cpp](../replication)

<pre>mongo::Lock::assertWriteLocked(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/structure/collection\_info\_cache.cpp](../storage\_layer\_structure)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Lock::DBWrite::~DBWrite()</pre>

#### Used By:

- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::Lock::GlobalRead::~GlobalRead()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Lock::DBWrite::UpgradeToExclusive::~UpgradeToExclusive()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::TempRelease::~TempRelease()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Lock::DBWrite::UpgradeToExclusive::UpgradeToExclusive()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::GlobalWrite::~GlobalWrite()</pre>

#### Used By:

- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/dbtests/basictests.cpp](../unit\_tests)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::TempRelease::TempRelease()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::GlobalWrite::GlobalWrite(bool, int)</pre>

#### Used By:

- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/dbtests/basictests.cpp](../unit\_tests)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/querytests.cpp](../unit\_tests)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::Lock::DBRead::~DBRead()</pre>

#### Used By:

- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/repl/rs.cpp](../replication)

<pre>mongo::readlocktry::readlocktry(int)</pre>

#### Used By:

- [src/mongo/db/repl/health.cpp](../replication)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Lock::isReadLocked()</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::Lock::isW()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/db/stats/snapshots\_webplugins.cpp](../utilities)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Lock::isLocked()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/auth/authz\_session\_external\_state\_d.cpp](../authentication)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/db/lockstat.cpp

<pre>mongo::LockStat::reset()</pre>

#### Used By:

- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LockStat::report() const</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LockStat::report(mongo::StringBuilderImpl<mongo::TrivialAllocator>&) const</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/lockstate.cpp

<pre>mongo::LockState::LockState()</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Acquiring::~Acquiring()</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)

<pre>mongo::LockState::hasAnyReadLock() const</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LockState::reportState(mongo::BSONObjBuilder&)</pre>

#### Used By:

- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Acquiring::Acquiring(mongo::Lock::ScopedLock*, mongo::LockState&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/counttests.cpp](../unit\_tests)

<pre>mongo::LockState::Dump()</pre>

#### Used By:

- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<pre>mongo::LockState::hasAnyWriteLock() const</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<pre>mongo::LockState::reportState()</pre>

#### Used By:

- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)

-------------

Spin locks   can you give an example or two of where we tightly spin on locks?

- src/mongo/util/concurrency/spin\_lock.cpp   (cppclientdriver)
- src/mongo/util/concurrency/spin\_lock.h
- src/mongo/util/concurrency/spin\_lock\_test.cpp   ()

## Interface


### src/mongo/util/concurrency/spin\_lock.cpp

<pre>mongo::SpinLock::SpinLock()</pre>

#### Used By:

- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/db/stats/counters.cpp](../utilities)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/s/shardconnection.cpp](../sharding)

<pre>mongo::SpinLock::~SpinLock()</pre>

#### Used By:

- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/util/net/sock.cpp](../network)
- [src/mongo/db/stats/counters.cpp](../utilities)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/s/shardconnection.cpp](../sharding)

-------------

Condition Variables   why called 'synchronization' then? (what are these, really? can you give   an example?)

- src/mongo/util/concurrency/synchronization.cpp   (cppclientdriver)
- src/mongo/util/concurrency/synchronization.h

## Interface


### src/mongo/util/concurrency/synchronization.cpp

<pre>mongo::NotifyAll::now()</pre>

#### Used By:

- [src/mongo/db/dur\_commitjob.cpp](../journaling)

<pre>mongo::Notification::notifyOne()</pre>

#### Used By:

- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::NotifyAll::awaitBeyondNow()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)

<pre>mongo::Notification::waitToBeNotified()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::Notification::Notification()</pre>

#### Used By:

- [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)

<pre>mongo::NotifyAll::NotifyAll()</pre>

#### Used By:

- [src/mongo/db/dur\_commitjob.cpp](../journaling)

<pre>mongo::NotifyAll::notifyAll(unsigned long long)</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
