# file\_allocation

# Module Groups

-------------

File allocation library

- src/mongo/util/file\_allocator.cpp   (cppclientdriver)
- src/mongo/util/file\_allocator.h

## Interface


### src/mongo/util/file\_allocator.cpp

<pre>mongo::FileAllocator::requestAllocation(std::string const&, long&)</pre>

#### Used By:

- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<pre>mongo::ensureParentDirCreated(boost::filesystem3::path const&)</pre>

#### Used By:

- [src/mongo/db/durop.cpp](../journaling)

<pre>mongo::FileAllocator::waitUntilFinished() const</pre>

#### Used By:

- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::FileAllocator::allocateAsap(std::string const&, unsigned long long&)</pre>

#### Used By:

- [src/mongo/util/mmap\_posix.cpp](../mmap)

<pre>mongo::FileAllocator::get()</pre>

#### Used By:

- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
- [src/mongo/util/mmap\_posix.cpp](../mmap)

<pre>mongo::FileAllocator::hasFailed() const</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<pre>mongo::FileAllocator::start()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
