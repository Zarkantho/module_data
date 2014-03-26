# Utilities

# Module Groups

-------------

# File Paths
Code to manage paths to files.  Conversion from relative to full path within database directory as  well as code to get the current partition (for readahead checks).

## Files
- src/mongo/util/paths.cpp   (mongod, tools, mongos)
- src/mongo/util/paths.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# Statistics Tracking
Classes to help in tracking statistics

## Files
- src/mongo/db/stats/counters.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/counters.h   (mongod, tools, mongos)
- src/mongo/db/stats/snapshots.cpp   (mongod, tools)
- src/mongo/db/stats/snapshots.h   (mongod, tools, mongos)
- src/mongo/db/stats/snapshots\_webplugins.cpp   (mongod)
- src/mongo/db/stats/timer\_stats.cpp   (mongod, tools, mongos)
- src/mongo/db/stats/timer\_stats.h   (mongod, tools, mongos)
- src/mongo/db/stats/top.cpp   (mongod, tools)
- src/mongo/db/stats/top.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

# BSON Element Hasher
Utilities to hash BSON elements. Used in hashed shard keys and hashed indexes.

## Files
- src/mongo/db/hasher.cpp   (mongod, tools, mongos)
- src/mongo/db/hasher.h   (mongod, tools, mongos)
- src/mongo/db/hasher\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

# Operation Tracker
Helpers to track in progress operations.  This works by inheriting from it when you make a class that represents an operation that should be tracked. The constructor registers itself in an "in progress" map, and the destructor removes it.

## Files
- src/mongo/db/background.cpp   (mongod, tools)
- src/mongo/db/background.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

# Elapsed Time
Utility to check whether a certain time interval has elapsed. Currently only used in  d\_migrate.cpp to check if we should yield.

## Files
- src/mongo/util/elapsed\_tracker.cpp   (mongod, tools)
- src/mongo/util/elapsed\_tracker.h   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

# Progress Meter
Helper classes to accumulate and log progress in a nice format using the logging system (so the logging system is only dependency)

## Files
- src/mongo/util/progress\_meter.cpp   (mongod, tools, mongos)
- src/mongo/util/progress\_meter.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

# Debug Utilities
Debug macros and gdb server helpers

## Files
- src/mongo/util/debug\_util.cpp   (mongod, tools, mongos)
- src/mongo/util/debug\_util.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

# Thread Name
Library to get and set the name of the current thread. Just uses a boost::thread\_specific\_ptr.

## Files
- src/mongo/util/concurrency/thread\_name.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_name.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

# Hex Utils
Utility library to manipulate hex strings

## Files
- src/mongo/util/hex.cpp   (mongod, tools, mongos)
- src/mongo/util/hex.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

# Background Operations
Utilities to run jobs (threads) in the "background".  You can use this to run tasks periodically.  Note that there are two different classes here. One is a Task and one is a BackgroundJob.  They are both used in the code in various places.  Task is just a wrapper around BackgroundJob with a slightly simpler interface.  They both effectively serve the same purpose.

## Files
- src/mongo/util/background.cpp   (mongod, tools, mongos)
- src/mongo/util/background.h   (mongod, tools, mongos)
- src/mongo/util/background\_job\_test.cpp   ()
- src/mongo/util/concurrency/task.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/task.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

# Asynchronous Background Operation Queue
Wrapper around a background task that creates an object with a "server" interface.  What this means is that "messages" (in the form of lambdas) can be registered with this class to be called sometime in the future by the event loop in this task.  Some functions just register the function and return, and others will block until the function is executed.

## Files
- src/mongo/util/concurrency/msg.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

# Map Utilities
mapFindWithDefault - looks something up in a map with a default value.

## Files
- src/mongo/util/map\_util.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

# Pch
I still do not know what this was originally for, but I know we are slowly getting rid of it.

## Files
- src/mongo/pch.cpp   (mongod, tools, mongos)
- src/mongo/pch.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

# Assertions
Assertion library.

## Files
- src/mongo/util/assert\_util.cpp   (mongod, tools, mongos)
- src/mongo/util/assert\_util.h   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

# TODO: Name this group
Helper library that you inherit from to make a class "reference counted"

## Files
- src/mongo/util/intrusive\_counter.cpp   (mongod, tools, mongos)
- src/mongo/util/intrusive\_counter.h   (mongod, tools, mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

# TODO: Name this group
md5 hash library

## Files
- src/mongo/util/md5.cpp   (mongod, tools, mongos)
- src/mongo/util/md5.h   (mongod, tools, mongos)
- src/mongo/util/md5.hpp   (mongod, tools, mongos)
- src/mongo/util/md5\_test.cpp   ()
- src/mongo/util/md5main.cpp   ()

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)

-------------

# TODO: Name this group
Windows service

## Files
- src/mongo/util/ntservice.cpp   (mongod, mongos)
- src/mongo/util/ntservice.h   (mongod, mongos)

#### [Interface](interface/16)

#### [Dependencies](dependencies/16)

-------------

# TODO: Name this group
Utilities to hash a username + password

## Files
- src/mongo/client/auth\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/client/auth\_helpers.h   (mongod, tools, mongos)

#### [Interface](interface/17)

#### [Dependencies](dependencies/17)

-------------

# TODO: Name this group
Giant list of utilities that I haven't gotten to yet. TODO: document what these are for and why  you would use them.

## Files
- src/mongo/util/queue.h   (mongod, tools)
- src/mongo/util/ramlog.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num-inl.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num.cpp   (mongod, tools, mongos)
- src/mongo/util/safe\_num.h   (mongod, tools, mongos)
- src/mongo/util/safe\_num\_test.cpp   ()
- src/mongo/util/scopeguard.h   (mongod, tools, mongos)
- src/mongo/util/sequence\_util.h   (mongod, tools, mongos)
- src/mongo/util/signal\_handlers.cpp   (mongod, tools, mongos)
- src/mongo/util/signal\_handlers.h   (mongod, tools, mongos)
- src/mongo/util/signal\_win32.cpp   (mongod, tools, mongos)
- src/mongo/util/signal\_win32.h   (mongod, mongos)
- src/mongo/util/stack\_introspect.cpp   (mongod, tools, mongos)
- src/mongo/util/stack\_introspect.h   (mongod, tools, mongos)
- src/mongo/util/stacktrace.cpp   (mongod, tools, mongos)
- src/mongo/util/stacktrace.h   (mongod, tools, mongos)
- src/mongo/util/startup\_test.cpp   (mongod, tools, mongos)
- src/mongo/util/startup\_test.h   (mongod, tools, mongos)
- src/mongo/util/string\_map.h   (mongod, tools, mongos)
- src/mongo/util/string\_map\_test.cpp   ()
- src/mongo/util/stringutils.cpp   (mongod, tools, mongos)
- src/mongo/util/stringutils.h   (mongod, tools, mongos)
- src/mongo/util/stringutils\_test.cpp   ()
- src/mongo/util/tcmalloc\_server\_status\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/text.cpp   (mongod, tools, mongos)
- src/mongo/util/text.h   (mongod, tools, mongos)
- src/mongo/util/text\_startuptest.cpp   (mongod, tools, mongos)
- src/mongo/util/text\_test.cpp   ()
- src/mongo/util/time\_support.cpp   (mongod, tools, mongos)
- src/mongo/util/time\_support.h   (mongod, tools, mongos)
- src/mongo/util/time\_support\_test.cpp   ()
- src/mongo/util/timer-generic-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-posixclock-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer-win32-inl.h   (mongod, tools, mongos)
- src/mongo/util/timer.cpp   (mongod, tools, mongos)
- src/mongo/util/timer.h   (mongod, tools, mongos)
- src/mongo/util/touch\_pages.cpp   (mongod, tools)
- src/mongo/util/touch\_pages.h   (mongod, tools)
- src/mongo/util/trace.h   (mongod, tools, mongos)
- src/mongo/util/unordered\_fast\_key\_table.h   (mongod, tools, mongos)
- src/mongo/util/unordered\_fast\_key\_table\_internal.h   (mongod, tools, mongos)
- src/mongo/util/util.cpp   (mongod, tools, mongos)
- src/mongo/util/version\_reporting.cpp   (mongod, tools, mongos)
- src/mongo/util/version\_reporting.h   (mongod, tools, mongos)
- src/mongo/util/version\_test.cpp   ()
- src/mongo/util/winutil.h   (mongod, mongos)
- src/mongo/util/admin\_access.h   (mongod, tools, mongos)
- src/mongo/util/allocator.h   (mongod, tools, mongos)
- src/mongo/util/array.h   ()
- src/mongo/util/base64.cpp   (mongod, tools, mongos)
- src/mongo/util/base64.h   (mongod, tools, mongos)
- src/mongo/util/bson\_util.h   (mongod, tools)
- src/mongo/util/bufreader.h   (mongod, tools, mongos)
- src/mongo/util/checksum.h   (mongod, tools)
- src/mongo/util/compress.cpp   (mongod, tools)
- src/mongo/util/compress.h   (mongod, tools)
- src/mongo/util/concurrency/list.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mapsf.h   (mongod, tools)
- src/mongo/util/concurrency/mutex.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mutexdebugger.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/mutexdebugger.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/mvar.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/qlock.h   (mongod, tools)
- src/mongo/util/concurrency/race.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/shared\_mutex\_win.hpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/simplerwlock.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_pool.cpp   (mongod, tools, mongos)
- src/mongo/util/concurrency/thread\_pool.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/threadlocal.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/ticketholder.h   (mongod, tools, mongos)
- src/mongo/util/concurrency/value.h   (mongod, tools, mongos)
- src/mongo/util/descriptive\_stats-inl.h   (mongod, tools)
- src/mongo/util/descriptive\_stats.h   (mongod, tools)
- src/mongo/util/descriptive\_stats\_test.cpp   ()
- src/mongo/util/embedded\_builder.h   (mongod, tools, mongos)
- src/mongo/util/exception\_filter\_win32.cpp   (mongod, tools, mongos)
- src/mongo/util/exception\_filter\_win32.h   (mongod, tools, mongos)
- src/mongo/util/exit\_code.h   (mongod, tools, mongos)
- src/mongo/util/gcov.h   (mongod, tools, mongos)
- src/mongo/util/goodies.h   (mongod, tools, mongos)
- src/mongo/util/heapcheck.h   (mongod, tools, mongos)

#### [Interface](interface/18)

#### [Dependencies](dependencies/18)

-------------

# TODO: Name this group
Platform specific code? TODO: Verify this and document what they are for.

## Files
- src/mongo/platform/atomic\_intrinsics.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_gcc\_generic.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_gcc\_intel.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_intrinsics\_win32.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_word.h   (mongod, tools, mongos)
- src/mongo/platform/atomic\_word\_test.cpp   ()
- src/mongo/platform/backtrace.cpp   (mongod, tools, mongos)
- src/mongo/platform/backtrace.h   (mongod, tools, mongos)
- src/mongo/platform/basic.h   (mongod, tools, mongos)
- src/mongo/platform/bits.h   (mongod, tools)
- src/mongo/platform/bits\_test.cpp   ()
- src/mongo/platform/compiler.h   (mongod, tools, mongos)
- src/mongo/platform/compiler\_gcc.h   (mongod, tools, mongos)
- src/mongo/platform/compiler\_msvc.h   (mongod, tools, mongos)
- src/mongo/platform/cstdint.h   (mongod, tools, mongos)
- src/mongo/platform/float\_utils.h   (mongod, tools, mongos)
- src/mongo/platform/hash\_namespace.h   (mongod, tools, mongos)
- src/mongo/platform/posix\_fadvise.cpp   (mongod, tools, mongos)
- src/mongo/platform/posix\_fadvise.h   (mongod, tools, mongos)
- src/mongo/platform/process\_id.cpp   (mongod, tools, mongos)
- src/mongo/platform/process\_id.h   (mongod, tools, mongos)
- src/mongo/platform/process\_id\_test.cpp   ()
- src/mongo/platform/random.cpp   (mongod, tools, mongos)
- src/mongo/platform/random.h   (mongod, tools, mongos)
- src/mongo/platform/random\_test.cpp   ()
- src/mongo/platform/strcasestr.cpp   (mongod, tools, mongos)
- src/mongo/platform/strcasestr.h   (mongod, tools, mongos)
- src/mongo/platform/strtoll.h   (mongod, tools, mongos)
- src/mongo/platform/unordered\_map.h   (mongod, tools, mongos)
- src/mongo/platform/unordered\_set.h   (mongod, tools, mongos)
- src/mongo/platform/windows\_basic.h   (mongod, tools, mongos)
- src/mongo/util/platform\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo.h   (mongod, tools, mongos)
- src/mongo/util/processinfo\_darwin.cpp   (mongod, tools, mongos)
- src/mongo/util/processinfo\_test.cpp   ()
- src/mongo/util/mongoutils/checksum.h   (mongod, tools)
- src/mongo/util/mongoutils/hash.h   (mongod, tools)
- src/mongo/util/mongoutils/html.h   (mongod, tools, mongos)
- src/mongo/util/mongoutils/str.h   (mongod, tools, mongos)

#### [Interface](interface/19)

#### [Dependencies](dependencies/19)
