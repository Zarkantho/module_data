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

-------------

Spin locks   can you give an example or two of where we tightly spin on locks?

- src/mongo/util/concurrency/spin\_lock.cpp   (cppclientdriver)
- src/mongo/util/concurrency/spin\_lock.h
- src/mongo/util/concurrency/spin\_lock\_test.cpp   ()

-------------

Condition Variables   why called 'synchronization' then? (what are these, really? can you give   an example?)

- src/mongo/util/concurrency/synchronization.cpp   (cppclientdriver)
- src/mongo/util/concurrency/synchronization.h
