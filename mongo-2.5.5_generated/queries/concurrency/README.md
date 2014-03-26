# Concurrency
TODO: concurrency description


-------------

## Core Database Locks
Core locks library. Only in mongod.
TODO: Split up this section and go into more detail about the types of locks used here.
TODO: There are also a bunch of concurrency related helpers in the UTILITIES section.

#### Files
- src/mongo/util/concurrency/rwlock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.h   (mongod, tools, mongos)
- src/mongo/db/d\_concurrency.cpp   (mongod, tools)
- src/mongo/db/d\_concurrency.h   (mongod, tools, mongos)
- src/mongo/db/lockstat.cpp   (mongod, tools)
- src/mongo/db/lockstat.h   (mongod, tools, mongos)
- src/mongo/db/lockstate.cpp   (mongod, tools)
- src/mongo/db/lockstate.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Spin Locks
Spin locks

#### Files
- src/mongo/util/concurrency/spin\_lock.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Condition Variables
Condition Variables

#### Files
- src/mongo/util/concurrency/synchronization.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/synchronization.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
