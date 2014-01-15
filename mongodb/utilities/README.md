# utilities

# Module Groups

-------------

Code to manage paths to files. Conversion from relative to full path within database directory as  well as code to get the current partition (for readahead checks).

- src/mongo/util/paths.cpp   (mongod, tools, mongos)
- src/mongo/util/paths.h

-------------

Classes to help in tracking statistics

- src/mongo/db/stats/counters.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/counters.h
- src/mongo/db/stats/snapshots.cpp   (mongod, tools)
- src/mongo/db/stats/snapshots.h
- src/mongo/db/stats/snapshots\_webplugins.cpp   (mongod)
- src/mongo/db/stats/timer\_stats.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/timer\_stats.h
- src/mongo/db/stats/top.cpp   (mongod, tools)
- src/mongo/db/stats/top.h

-------------

Utilities to hash BSON elements. Used in hashed shard keys and hashed indexes.

- src/mongo/db/hasher.cpp   (mongod, tools, mongos)
- src/mongo/db/hasher.h
- src/mongo/db/hasher\_test.cpp   ()

-------------

Helpers to track in progress operations. The constructor registers itself in an "in progress"  map, and the destructor removes it.

- src/mongo/db/background.cpp   (mongod, tools)
- src/mongo/db/background.h

-------------

Utility to check whether a certain time interval has elapsed. Currently only used in  d\_migrate.cpp to check if we should yield.

- src/mongo/util/elapsed\_tracker.cpp   (mongod, tools)
- src/mongo/util/elapsed\_tracker.h

-------------

Helper classes to accumulate and log progress in a nice format using the  logging system (so the logging system is only dependency)

- src/mongo/util/progress\_meter.cpp   (mongod, tools, mongos)
- src/mongo/util/progress\_meter.h

-------------

Debug macros and gdb server helpers

- src/mongo/util/debug\_util.cpp   (cppclientdriver)
- src/mongo/util/debug\_util.h

-------------

Library to get and set the name of the current thread. Just uses a boost::thread\_specific\_ptr.

- src/mongo/util/concurrency/thread\_name.cpp   (cppclientdriver)
- src/mongo/util/concurrency/thread\_name.h

-------------

Utility library to manipulate hex strings

- src/mongo/util/hex.cpp   (cppclientdriver)
- src/mongo/util/hex.h

-------------

Utilities to run jobs (threads) in the "background". You can use this to run tasks periodically.

- src/mongo/util/background.cpp   (mongod, tools, mongos)
- src/mongo/util/background.h
- src/mongo/util/background\_job\_test.cpp   ()

-------------

mapFindWithDefault - looks something up in a map with a default value.

- src/mongo/util/map\_util.h

-------------

These appear to be for debugging. Not used on OSX so it's hard for met to tell. Notably used in  mmap\_win.cpp (windows mmap)

- src/mongo/db/memconcept.cpp   (mongod, tools)
- src/mongo/db/memconcept.h

-------------

I still don't know what this was originally for, but I know we are slowly getting rid of it.

- src/mongo/pch.cpp   (cppclientdriver)
- src/mongo/pch.h

-------------

Assertion library.

- src/mongo/util/assert\_util.cpp   (cppclientdriver)
- src/mongo/util/assert\_util.h

-------------

Library for adding fail points into the code for testing purposes

- src/mongo/util/fail\_point.cpp   (mongod, tools, mongos)
- src/mongo/util/fail\_point.h
- src/mongo/util/fail\_point\_registry.cpp   (cppclientdriver)
- src/mongo/util/fail\_point\_registry.h
- src/mongo/util/fail\_point\_service.cpp   (mongod, tools, mongos)
- src/mongo/util/fail\_point\_service.h
- src/mongo/util/fail\_point\_test.cpp   ()

-------------

Helper library that you inherit from to make a class "reference counted"

- src/mongo/util/intrusive\_counter.cpp   (mongod, tools, mongos)
- src/mongo/util/intrusive\_counter.h

-------------

md5 hash library

- src/mongo/util/md5.cpp   (cppclientdriver)
- src/mongo/util/md5.h
- src/mongo/util/md5.hpp
- src/mongo/util/md5\_test.cpp   ()
- src/mongo/util/md5main.cpp   (cppclientdriver)

-------------

Windows service

- src/mongo/util/ntservice.cpp   (mongod, mongos)
- src/mongo/util/ntservice.h

-------------

Utilities to hash a username + password

- src/mongo/client/auth\_helpers.cpp   (cppclientdriver)
- src/mongo/client/auth\_helpers.h

-------------

Giant list of utilities that I haven't gotten to yet. TODO: document what these are for and why  you would use them.

- src/mongo/util/queue.h
- src/mongo/util/ramlog.h
- src/mongo/util/safe\_num-inl.h
- src/mongo/util/safe\_num.cpp   (mongod, tools, mongos)
- src/mongo/util/safe\_num.h
- src/mongo/util/safe\_num\_test.cpp   ()
- src/mongo/util/scopeguard.h
- src/mongo/util/sequence\_util.h
- src/mongo/util/signal\_handlers.cpp   (cppclientdriver)
- src/mongo/util/signal\_handlers.h
- src/mongo/util/stack\_introspect.cpp   (mongod, tools, mongos)
- src/mongo/util/stack\_introspect.h
- src/mongo/util/stacktrace.cpp   (mongod, tools, mongos)
- src/mongo/util/stacktrace.h
- src/mongo/util/startup\_test.cpp   (mongod, tools, mongos)
- src/mongo/util/startup\_test.h
- src/mongo/util/string\_map.h
- src/mongo/util/string\_map\_internal.h
- src/mongo/util/string\_map\_test.cpp   ()
- src/mongo/util/stringutils.cpp   (mongod, tools, mongos)
- src/mongo/util/stringutils.h
- src/mongo/util/stringutils\_test.cpp   ()
- src/mongo/util/tcmalloc\_server\_status\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/text.cpp   (cppclientdriver)
- src/mongo/util/text.h
- src/mongo/util/text\_startuptest.cpp   (mongod, tools, mongos)
- src/mongo/util/text\_test.cpp   ()
- src/mongo/util/time\_support.cpp   (mongod, tools, mongos)
- src/mongo/util/time\_support.h
- src/mongo/util/time\_support\_test.cpp   ()
- src/mongo/util/timer-generic-inl.h
- src/mongo/util/timer-inl.h
- src/mongo/util/timer-posixclock-inl.h
- src/mongo/util/timer-win32-inl.h
- src/mongo/util/timer.cpp   (mongod, tools, mongos)
- src/mongo/util/timer.h
- src/mongo/util/touch\_pages.cpp   (mongod, tools)
- src/mongo/util/touch\_pages.h
- src/mongo/util/trace.h
- src/mongo/util/unordered\_fast\_key\_table.h
- src/mongo/util/unordered\_fast\_key\_table\_internal.h
- src/mongo/util/util.cpp   (mongod, tools, mongos)
- src/mongo/util/version.cpp   (mongod, tools, mongos)
- src/mongo/util/version.h
- src/mongo/util/version\_reporting.cpp   (mongod, tools, mongos)
- src/mongo/util/version\_reporting.h
- src/mongo/util/version\_test.cpp   ()
- src/mongo/util/winutil.h
- src/mongo/util/admin\_access.h
- src/mongo/util/allocator.h
- src/mongo/util/array.h
- src/mongo/util/base64.cpp   (cppclientdriver)
- src/mongo/util/base64.h
- src/mongo/util/bson\_util.h
- src/mongo/util/bufreader.h
- src/mongo/util/checksum.h
- src/mongo/util/compress.cpp   (mongod, tools)
- src/mongo/util/compress.h
- src/mongo/util/concurrency/list.h
- src/mongo/util/concurrency/mapsf.h
- src/mongo/util/concurrency/msg.h
- src/mongo/util/concurrency/mutex.h
- src/mongo/util/concurrency/mutexdebugger.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/mutexdebugger.h
- src/mongo/util/concurrency/mvar.h
- src/mongo/util/concurrency/qlock.h
- src/mongo/util/concurrency/race.h
- src/mongo/util/concurrency/shared\_mutex\_win.hpp
- src/mongo/util/concurrency/simplerwlock.h
- src/mongo/util/concurrency/task.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/task.h
- src/mongo/util/concurrency/thread\_pool.cpp   (cppclientdriver)
- src/mongo/util/concurrency/thread\_pool.h
- src/mongo/util/concurrency/threadlocal.h
- src/mongo/util/concurrency/ticketholder.h
- src/mongo/util/concurrency/value.h
- src/mongo/util/descriptive\_stats-inl.h
- src/mongo/util/descriptive\_stats.h
- src/mongo/util/descriptive\_stats\_test.cpp   ()
- src/mongo/util/embedded\_builder.h
- src/mongo/util/exception\_filter\_win32.cpp   (mongod, tools, mongos)
- src/mongo/util/exception\_filter\_win32.h
- src/mongo/util/exit\_code.h
- src/mongo/util/gcov.h
- src/mongo/util/goodies.h
- src/mongo/util/hashtab.h
- src/mongo/util/heapcheck.h

-------------

Platform specific code? TODO: Verify this and document what they are for.

- src/mongo/platform/atomic\_intrinsics.h
- src/mongo/platform/atomic\_intrinsics\_gcc.h
- src/mongo/platform/atomic\_intrinsics\_win32.h
- src/mongo/platform/atomic\_word.h
- src/mongo/platform/atomic\_word\_test.cpp   ()
- src/mongo/platform/backtrace.cpp   (mongod, tools, mongos)
- src/mongo/platform/backtrace.h
- src/mongo/platform/basic.h
- src/mongo/platform/bits.h
- src/mongo/platform/bits\_test.cpp   ()
- src/mongo/platform/compiler.h
- src/mongo/platform/compiler\_gcc.h
- src/mongo/platform/compiler\_msvc.h
- src/mongo/platform/cstdint.h
- src/mongo/platform/float\_utils.h
- src/mongo/platform/hash\_namespace.h
- src/mongo/platform/posix\_fadvise.cpp   (mongod, tools, mongos)
- src/mongo/platform/posix\_fadvise.h
- src/mongo/platform/process\_id.cpp   (mongod, tools, mongos)
- src/mongo/platform/process\_id.h
- src/mongo/platform/process\_id\_test.cpp   ()
- src/mongo/platform/random.cpp   (cppclientdriver)
- src/mongo/platform/random.h
- src/mongo/platform/random\_test.cpp   ()
- src/mongo/platform/strcasestr.cpp   (mongod, tools, mongos)
- src/mongo/platform/strcasestr.h
- src/mongo/platform/strtoll.h
- src/mongo/platform/unordered\_map.h
- src/mongo/platform/unordered\_set.h
- src/mongo/platform/windows\_basic.h
- src/mongo/util/platform\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo.cpp   (cppclientdriver)
- src/mongo/util/processinfo.h
- src/mongo/util/processinfo\_darwin.cpp   (cppclientdriver)
- src/mongo/util/processinfo\_test.cpp   ()
- src/mongo/util/mongoutils/checksum.h
- src/mongo/util/mongoutils/hash.h
- src/mongo/util/mongoutils/html.h
- src/mongo/util/mongoutils/str.h
