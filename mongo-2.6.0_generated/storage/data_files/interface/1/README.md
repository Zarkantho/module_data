
# Interface for Posix Mmapped File Implementation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/mmap\_posix.cpp

<div></div>

    mongo::MemoryMappedFile::remapPrivateView(void*)

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)

<div></div>

    mongo::MAdvise::~MAdvise()

- Used By:

    - [src/mongo/db/structure/record\_store.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    typeinfo for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MemoryMappedFile::prepareFlush()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MemoryMappedFile::close()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MemoryMappedFile::flush(bool)

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    mongo::MemoryMappedFile::createPrivateMap()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)

<div></div>

    vtable for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MAdvise::MAdvise(void*, unsigned int, mongo::MAdvise::Advice)

- Used By:

    - [src/mongo/db/structure/record\_store.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::g_minOSPageSizeBytes

- Used By:

    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/util/touch\_pages.cpp](../../../../utilities/utilities)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
