# file\_allocation

# Module Groups

-------------

# Group Description
File allocation library

# Files
- src/mongo/util/file\_allocator.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/file\_allocator.h   (mongod, cppclientdriver, tools, mongos)

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

# Dependencies

### src/mongo/util/file\_allocator.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    mongo::msgassertedNoTrace(int, char const*)

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

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

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

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::filesystem3::path::parent_path() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithPrefix(char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::setThreadName(mongo::StringData)

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    mongo::msgassertedNoTrace(int, char const*)

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

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

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

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::filesystem3::path::parent_path() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithPrefix(char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)
