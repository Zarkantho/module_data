# concurrency

# Module Groups

-------------

# Group Description
Core locks library. Only in mongod.   can you say a bit more? e.g. database locks are RWlocks, but what *are*   they exactly? any sort of fairness or other performance/"how to use" info?  TODO: There are also a bunch of concurrency related helpers in the UTILITIES section.

## Files
- src/mongo/util/concurrency/rwlock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/rwlockimpl.h   (mongod, tools, mongos)
- src/mongo/db/d\_concurrency.cpp   (mongod, tools)
- src/mongo/db/d\_concurrency.h   (mongod, tools, mongos)
- src/mongo/db/lockstat.cpp   (mongod, tools)
- src/mongo/db/lockstat.h   (mongod, tools, mongos)
- src/mongo/db/lockstate.cpp   (mongod, tools)
- src/mongo/db/lockstate.h   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Spin locks   can you give an example or two of where we tightly spin on locks?

## Files
- src/mongo/util/concurrency/spin\_lock.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/spin\_lock\_test.cpp   ()

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
Condition Variables   why called 'synchronization' then? (what are these, really? can you give   an example?)

## Files
- src/mongo/util/concurrency/synchronization.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/synchronization.h   (mongod, tools, mongos)

## [Interface](interface/2)

## [Dependencies](dependencies/2)
