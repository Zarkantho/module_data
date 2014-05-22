
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/file\_allocator.cpp

<div></div>

    mongo::FileAllocator::requestAllocation(std::string const&, long&)

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FileAllocator::allocateAsap(std::string const&, unsigned long long&)

- Used By:

    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)

<div></div>

    mongo::ensureParentDirCreated(boost::filesystem3::path const&)

- Used By:

    - [src/mongo/db/durop.cpp](../../../../storage/journaling)

<div></div>

    mongo::FileAllocator::get()

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FileAllocator::hasFailed() const

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::FileAllocator::start()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
