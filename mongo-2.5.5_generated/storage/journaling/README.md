# journaling

# Module Groups

-------------

# Group Description
Page aligned buffer builder   what sort of buffer? i don't understand ;(

# Files
- src/mongo/util/alignedbuilder.cpp   (mongod, tools)
- src/mongo/util/alignedbuilder.h   (mongod, tools)

# Interface

### src/mongo/util/alignedbuilder.cpp

<div></div>

    mongo::AlignedBuilder::kill()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

<div></div>

    mongo::AlignedBuilder::AlignedBuilder(unsigned int)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

# Dependencies

### src/mongo/util/alignedbuilder.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Journaling module   who calls/owns stuff in here? only used by mongod, correct?

# Files
- src/mongo/db/dur.cpp   (mongod, tools)
- src/mongo/db/dur.h   (mongod, tools, mongos)
- src/mongo/db/dur\_commitjob.cpp   (mongod, tools)
- src/mongo/db/dur\_commitjob.h   (mongod, tools)
- src/mongo/db/dur\_journal.cpp   (mongod, tools)
- src/mongo/db/dur\_journal.h   (mongod, tools)
- src/mongo/db/dur\_journalformat.h   (mongod, tools)
- src/mongo/db/dur\_journalimpl.h   (mongod, tools)
- src/mongo/db/dur\_preplogbuffer.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.h   (mongod, tools)
- src/mongo/db/dur\_stats.h   (mongod, tools)
- src/mongo/db/dur\_writetodatafiles.cpp   (mongod, tools)
- src/mongo/db/durop.cpp   (mongod, tools)
- src/mongo/db/durop.h   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.cpp   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/dur.cpp

<div></div>

    mongo::dur::Stats::S::_asCSV()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::dur::Stats::S::_asObj()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::dur::commitJob

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dur::stats

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::dur::Stats::S::_CSVHeader()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::dur::Stats::S::reset()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::dur::DurableInterface::_impl

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/catalog/database\_holder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/cap.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dur::startup()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::dur::releasingWriteLock()

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

### src/mongo/db/dur\_journal.cpp

<div></div>

    mongo::dur::getJournalDir()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

<div></div>

    mongo::dur::haveJournalFiles(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::dur::journalCleanup(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/db/storage/durable\_mapped\_file.cpp

<div></div>

    mongo::DurableMappedFile::create(std::string const&, unsigned long long&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::DurableMappedFile::open(std::string const&, bool)

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Used By:

    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

# Dependencies

### src/mongo/db/dur.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mongoAbort(char const*)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::UpgradeToExclusive()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::DBWrite::UpgradeToExclusive::~UpgradeToExclusive()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::atLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::GlobalWrite::upgrade()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::filesLockedFsync

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::Lock::GlobalWrite::downgrade()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NotifyAll::awaitBeyondNow()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::MongoFile::getAllFiles()

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::NotifyAll::notifyAll(unsigned long long)

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

### src/mongo/db/dur\_commitjob.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NotifyAll::NotifyAll()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::NotifyAll::now()

- Provided By:

    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)

### src/mongo/db/dur\_journal.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::MongoFile::notifyPostFlush

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::rawCompress(char const*, unsigned long, char*, unsigned long*)

- Provided By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    mongo::File::truncate(unsigned long long)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

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

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::is_open() const

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::File::freeSpace(std::string const&)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::File::fsync() const

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::File::len()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::maxCompressedLength(unsigned long)

- Provided By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    mongo::SecureRandom::create()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::MongoFile::notifyPreFlush

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::read(unsigned long long, char*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

### src/mongo/db/dur\_preplogbuffer.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::printStackTrace(std::ostream&)

- Provided By:

    - [src/mongo/util/stacktrace.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/db/dur\_recover.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MemoryMappedFile::close()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::MemoryMappedFile::mapWithOptions(char const*, int)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::uncompress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::hexdump(char const*, unsigned int)

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LockMongoFilesShared::era

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::MongoFileFinder::findByPath(std::string const&) const

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    vtable for mongo::MemoryMappedFile

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/db/dur\_writetodatafiles.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/db/durop.cpp

<div></div>

    mongo::ensureParentDirCreated(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::File::File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

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

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::File::~File()

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::_deleteDataFiles(char const*)

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::File::is_open() const

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::File::fsync() const

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

### src/mongo/db/storage/durable\_mapped\_file.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::MemoryMappedFile::prepareFlush()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MemoryMappedFile::close()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::MemoryMappedFile::createPrivateMap()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::MemoryMappedFile::mapWithOptions(char const*, int)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    vtable for mongo::MemoryMappedFile

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::MemoryMappedFile::MemoryMappedFile()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LockMongoFilesShared::era

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::MemoryMappedFile

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::MemoryMappedFile::flush(bool)

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::LockMongoFilesShared::mmmutex

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::MemoryMappedFile::remapPrivateView(void*)

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

-------------

# Group Description
This is not actually used in our logging system. Just utilities to create files that you can  append to. One notable example of a system that uses this is our preallocation of journal files.  In fact, it isn't used in anything not journaling related right now.

# Files
- src/mongo/util/logfile.cpp   (mongod, tools)
- src/mongo/util/logfile.h   (mongod, tools)

# Interface

### src/mongo/util/logfile.cpp

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LogFile::~LogFile()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LogFile::readAt(unsigned long long, void*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

# Dependencies

### src/mongo/util/logfile.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::g_minOSPageSizeBytes

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)
