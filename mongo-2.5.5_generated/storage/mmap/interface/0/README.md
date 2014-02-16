
# Interface

### src/mongo/util/mmap.cpp

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Used By:

    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)
    - [src/mongo/dbtests/mmaptests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::MongoFile::getAllFiles()

- Used By:

    - [src/mongo/db/dur.cpp](../../../journaling)

<div></div>

    mongo::MongoFile::totalMappedLength()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::LockMongoFilesShared::era

- Used By:

    - [src/mongo/db/pagefault.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Used By:

    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/write\_concern.cpp](../../../replication)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)

<div></div>

    mongo::MongoFile::notifyPostFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::mapWithOptions(char const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MongoFile::notifyPreFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../journaling)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::MongoFileFinder::findByPath(std::string const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::map(char const*)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

### src/mongo/util/mmap\_posix.cpp

<div></div>

    mongo::MemoryMappedFile::prepareFlush()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::close()

- Used By:

    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::createPrivateMap()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    vtable for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MAdvise::MAdvise(void*, unsigned int, mongo::MAdvise::Advice)

- Used By:

    - [src/mongo/db/structure/record\_store.cpp](../../../storage\_layer\_structure)

<div></div>

    typeinfo for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MAdvise::~MAdvise()

- Used By:

    - [src/mongo/db/structure/record\_store.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)

- Used By:

    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::flush(bool)

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::remapPrivateView(void*)

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)

<div></div>

    mongo::g_minOSPageSizeBytes

- Used By:

    - [src/mongo/util/touch\_pages.cpp](../../../utilities)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/util/logfile.cpp](../../../journaling)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Used By:

    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
