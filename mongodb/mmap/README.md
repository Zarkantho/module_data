# mmap

# Module Groups

-------------

# Group Description
mmap library (only depends on file allocation library)

# Files
- src/mongo/util/mmap.cpp   (mongod, tools)
- src/mongo/util/mmap.h
- src/mongo/util/mmap\_posix.cpp   (mongod, tools)

# Interface

### src/mongo/util/mmap.cpp

<div></div>

    mongo::printMemInfo(char const*)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Used By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::MongoFile::getAllFiles()

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::MongoFile::totalMappedLength()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::LockMongoFilesShared::era

- Used By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::MongoFile::notifyPostFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::mapWithOptions(char const*, int)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    mongo::MongoFile::notifyPreFlush

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::MongoFileFinder::findByPath(std::string const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::map(char const*)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

### src/mongo/util/mmap\_posix.cpp

<div></div>

    mongo::MemoryMappedFile::prepareFlush()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::close()

- Used By:

    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::createPrivateMap()

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    vtable for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    typeinfo for mongo::MemoryMappedFile

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::flush(bool)

- Used By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::remapPrivateView(void*)

- Used By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)

- Used By:

    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::g_minOSPageSizeBytes

- Used By:

    - [src/mongo/util/touch\_pages.cpp](../utilities)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/util/logfile.cpp](../journaling)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Used By:

    - [src/mongo/tools/sniffer.cpp](../tools)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

# Dependencies

### src/mongo/util/mmap.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/util/mmap\_posix.cpp

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FileAllocator::allocateAsap(std::string const&, unsigned long long&)

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)
