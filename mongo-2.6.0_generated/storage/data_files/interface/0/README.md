
# Interface for Mmapped File Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/mmap.cpp

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MongoFile::getAllFiles()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::MongoFile::totalMappedLength()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LockMongoFilesShared::era

- Used By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::MongoFile::notifyPostFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::MemoryMappedFile::mapWithOptions(char const*, int)

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MongoFile::notifyPreFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::MongoFileFinder::findByPath(std::string const&) const

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MemoryMappedFile::map(char const*)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
