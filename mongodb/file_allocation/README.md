# file\_allocation

# Module Groups

-------------

# Group Description
File allocation library

# Files
- src/mongo/util/file\_allocator.cpp   (cppclientdriver)
- src/mongo/util/file\_allocator.h

# Interface

### src/mongo/util/file\_allocator.cpp

<div></div>

    mongo::FileAllocator::requestAllocation(std::string const&, long&)

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::ensureParentDirCreated(boost::filesystem3::path const&)

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Used By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::FileAllocator::allocateAsap(std::string const&, unsigned long long&)

- Used By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::FileAllocator::get()

- Used By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::FileAllocator::hasFailed() const

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::FileAllocator::start()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
