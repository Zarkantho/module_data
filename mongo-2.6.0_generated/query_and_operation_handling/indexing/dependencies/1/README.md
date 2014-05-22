
# Interface for Btree Backed Index Interface
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/index/btree\_based\_access\_method.cpp

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ErrorCodes::isInterruption(mongo::ErrorCodes::Error)

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/base/error\_codes.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::inDBRepair

- Provided By:

    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::BSONObjExternalSorter::BSONObjExternalSorter(mongo::ExternalSortComparison const*, long)

- Provided By:

    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexCatalogEntry::setMultikey()

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::IndexCatalogEntry::head() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::IndexCatalogEntry::setHead(mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../../network/network\_core)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logContext(char const*)

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::IndexCatalogEntry::isReady() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)
