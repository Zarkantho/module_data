# Concurrency
Concurrency management for operations on mongod as well as synchronization primitives.


-------------

## Mongod Concurrency System Interface
Top level entry point into the mongod concurrency system.

#### Files
- src/mongo/db/d\_concurrency.cpp   (mongod, tools)
- src/mongo/db/d\_concurrency.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Lock State
State of all the locks that this client/thread/operation has aquired.  There is one LockState per thread stored in thread local storage.

The three lock types are:

1. Global 2. DB Level - called "other" in the code 3. Special DB Level - called "nestable" in the code

The "Special DB Level" locks are for the "admin" and "local" databases.  The idea is that sometimes we want to do something to one of those databases (like inserting into the oplog), but we want still want to keep the lock on our original database (for example, to preserve our ordering guarantees in relation to the oplog).  This is why the lock is called "nestable".

All the DB level locks are "Reader Writer Locks", and the global lock is a "Quad Lock".

#### Files
- src/mongo/db/lockstate.cpp   (mongod, tools)
- src/mongo/db/lockstate.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Reader Writer Locks
Implementation of a reader writer lock primitive.

#### Files
- src/mongo/util/concurrency/rwlock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Quad Locks
Implmentation of a lock with intents and an upgradeable lock state.

See http://technet.microsoft.com/en-us/library/aa213039(v=SQL.80).aspx for a general discussion of locking.

The mapping between the names of the states are as follows:

<state in MongoDB Quad Lock> = <state in SQL Server Lock> r = IS w = IX R = S W = X X = U

#### Files
- src/mongo/util/concurrency/qlock.h   (mongod, tools)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Spin Locks
Spin locks

#### Files
- src/mongo/util/concurrency/spin\_lock.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Condition Variables
Condition Variables

#### Files
- src/mongo/util/concurrency/synchronization.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/synchronization.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Lock Stats
Statistics about locking behavior.

#### Files
- src/mongo/db/lockstat.cpp   (mongod, tools)
- src/mongo/db/lockstat.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)
