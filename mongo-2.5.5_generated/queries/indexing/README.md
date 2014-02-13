# indexing

# Module Groups

-------------

# Group Description
Indexes and index management code. TODO: go into more details about this. The code is new.  The two parts of the interface that are nice entry points are the "index\_access\_method.h"  (interface for manipulating and accessing the index itself), and "index\_cursor.h" (interface for  getting data from an index) files.   can you say a bit more about the structure in here, wrt. a hypothetical   member of the 'open source community' who wants to add a new type of   index to mongodb?

# Files
- src/mongo/db/index/2d\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/2d\_access\_method.h   (mongod, tools)
- src/mongo/db/index/2d\_common.h   (mongod, tools)
- src/mongo/db/index/btree\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/btree\_access\_method.h   (mongod, tools)
- src/mongo/db/index/btree\_based\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/btree\_based\_access\_method.h   (mongod, tools)
- src/mongo/db/index/btree\_index\_cursor.cpp   (mongod, tools)
- src/mongo/db/index/btree\_index\_cursor.h   (mongod, tools)
- src/mongo/db/index/btree\_interface.cpp   (mongod, tools)
- src/mongo/db/index/btree\_interface.h   (mongod, tools)
- src/mongo/db/index/btree\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/btree\_key\_generator.h   (mongod, tools, mongos)
- src/mongo/db/index/expression\_index.h   (mongod, tools, mongos)
- src/mongo/db/index/fts\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/fts\_access\_method.h   (mongod, tools)
- src/mongo/db/index/hash\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/hash\_access\_method.h   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method.h   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method\_internal.h   (mongod, tools)
- src/mongo/db/index/index\_access\_method.h   (mongod, tools)
- src/mongo/db/index/index\_cursor.h   (mongod, tools)
- src/mongo/db/index/index\_descriptor.h   (mongod, tools, mongos)
- src/mongo/db/index/s2\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/s2\_access\_method.h   (mongod, tools)
- src/mongo/db/index\_builder.cpp   (mongod, tools)
- src/mongo/db/index\_builder.h   (mongod, tools)
- src/mongo/db/index\_legacy.cpp   (mongod, tools)
- src/mongo/db/index\_legacy.h   (mongod, tools)
- src/mongo/db/index\_names.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_names.h   (mongod, tools, mongos)
- src/mongo/db/index\_rebuilder.cpp   (mongod, tools)
- src/mongo/db/index\_rebuilder.h   (mongod, tools)
- src/mongo/db/index\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_set.h   (mongod, tools, mongos)
- src/mongo/db/index\_set\_test.cpp   ()

# Interface

### src/mongo/db/index/2d\_access\_method.cpp

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::TwoDAccessMethod::getKeys(mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)

### src/mongo/db/index/btree\_access\_method.cpp

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index/btree\_based\_access\_method.cpp

<div></div>

    mongo::BtreeBasedAccessMethod::getComparison(int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

### src/mongo/db/index/btree\_index\_cursor.cpp

<div></div>

    mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::seek(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/count.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::pointsAt(mongo::BtreeIndexCursor const&)

- Used By:

    - [src/mongo/db/exec/count.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::aboutToDeleteBucket(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

### src/mongo/db/index/btree\_key\_generator.cpp

<div></div>

    mongo::BtreeKeyGeneratorV1::BtreeKeyGeneratorV1(std::vector<char const*, std::allocator<char const*> >, std::vector<mongo::BSONElement, std::allocator<mongo::BSONElement> >, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeKeyGenerator::getKeys(mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*) const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)

### src/mongo/db/index/fts\_access\_method.cpp

<div></div>

    typeinfo for mongo::FTSAccessMethod

- Used By:

    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)

<div></div>

    mongo::FTSAccessMethod::FTSAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index/hash\_access\_method.cpp

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::HashAccessMethod::makeSingleKey(mongo::BSONElement const&, int, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::HashAccessMethod::getKeysImpl(mongo::BSONObj const&, std::string const&, int, int, bool, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

### src/mongo/db/index/haystack\_access\_method.cpp

<div></div>

    mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::HaystackAccessMethod::searchCommand(mongo::BSONObj const&, double, mongo::BSONObj const&, mongo::BSONObjBuilder*, unsigned int)

- Used By:

    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)

### src/mongo/db/index/s2\_access\_method.cpp

<div></div>

    mongo::S2AccessMethod::S2AccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index\_builder.cpp

<div></div>

    mongo::IndexBuilder::IndexBuilder(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Used By:

    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::IndexBuilder::~IndexBuilder()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::IndexBuilder::build(mongo::Client::Context&) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/db/index\_legacy.cpp

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::getMissingField(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)

### src/mongo/db/index\_names.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)

<div></div>

    mongo::IndexNames::GEO_2D

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/queryutil.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexNames::TEXT

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexNames::HASHED

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index\_rebuilder.cpp

<div></div>

    mongo::indexRebuilder

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/index\_set.cpp

<div></div>

    mongo::IndexPathSet::clear()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::addPath(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::mightBeIndexed(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

# Dependencies

### src/mongo/db/index/2d\_access\_method.cpp

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../geo\_queries)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

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

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::GeoHashConverter::GeoHashConverter(mongo::GeoHashConverter::Parameters const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../geo\_queries)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&, mongo::BSONObj const*) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../geo\_queries)

### src/mongo/db/index/btree\_access\_method.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

### src/mongo/db/index/btree\_based\_access\_method.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::asVersion(mongo::Record*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inDBRepair

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObjExternalSorter::BSONObjExternalSorter(mongo::ExternalSortComparison const*, long)

- Provided By:

    - [src/mongo/db/extsort.cpp](../aggregation\_framework)

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

    mongo::IndexCatalogEntry::setMultikey()

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::IndexCatalogEntry::head() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::IndexCatalogEntry::setHead(mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logContext(char const*)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::IndexCatalogEntry::isReady() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)

- Provided By:

    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::asVersion(mongo::Record*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Provided By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/db/index/btree\_index\_cursor.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

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

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

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

    mongo::IndexCatalogEntry::head() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/index/btree\_interface.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::asVersion(mongo::Record*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::causedBy(std::string const&)

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

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    vtable for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KeyV1::toBson() const

- Provided By:

    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::asVersion(mongo::Record*)

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Provided By:

    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/index/btree\_key\_generator.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/index/fts\_access\_method.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::fts::FTSIndexFormat::getKeys(mongo::fts::FTSSpec const&, mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)

- Provided By:

    - [src/mongo/db/fts/fts\_index\_format.cpp](../full\_text\_search\_module)

<div></div>

    mongo::fts::FTSSpec::FTSSpec(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

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

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/db/index/hash\_access\_method.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Provided By:

    - [src/mongo/db/hasher.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/index/haystack\_access\_method.cpp

<div></div>

    mongo::Point::Point(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

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

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::FetchStage::FetchStage(mongo::WorkingSet*, mongo::PlanStage*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)

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

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Point::Point(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../geo\_queries)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::IndexScan::IndexScan(mongo::IndexScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)

### src/mongo/db/index/s2\_access\_method.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    LogMessageFatal::LogMessageFatal(char const*, int)

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    S2::kAvgEdge

- Provided By:

    - [src/third\_party/s2/s2.cc](../s2)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    LogMessageFatal::~LogMessageFatal()

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2::kMaxCellLevel

- Provided By:

    - [src/third\_party/s2/s2.cc](../s2)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::S2SearchUtil::getKeysForObject(mongo::BSONObj const&, mongo::S2IndexingParams const&, std::vector<std::string, std::allocator<std::string> >*)

- Provided By:

    - [src/mongo/db/geo/s2common.cpp](../geo\_queries)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/db/index\_builder.cpp

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

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

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::CachedBSONObj::_tooBig

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::getOp(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

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

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Database::getOrCreateCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::replLocalAuth()

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index\_legacy.cpp

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::fts::FTSSpec::fixSpec(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/index\_names.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/index\_rebuilder.cpp

<div></div>

    mongo::IndexCatalog::getAndClearUnfinishedIndexes()

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

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

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ReplSetImpl::rss

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/index\_set.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/index\_set\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Class representing an index spec, such as { "a" : 1, "b" : -1 }

# Files
- src/mongo/db/keypattern.cpp   (mongod, tools, mongos)
- src/mongo/db/keypattern.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/keypattern.cpp

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/exec/shard\_filter.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::KeyPattern::keyBounds(mongo::FieldRangeSet const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::KeyPattern::extendRangeBound(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::KeyPattern::isSpecial() const

- Used By:

    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/exec/shard\_filter.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

# Dependencies

### src/mongo/db/keypattern.cpp

<div></div>

    mongo::BSONElementHasher::hash64(mongo::BSONElement const&, int)

- Provided By:

    - [src/mongo/db/hasher.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::FieldRangeSet::universalRange() const

- Provided By:

    - [src/mongo/db/queryutil.cpp](../core\_query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Background job that periodically checks a ttl index.

# Files
- src/mongo/db/ttl.cpp   (mongod, tools)
- src/mongo/db/ttl.h   (mongod, tools)

# Interface

### src/mongo/db/ttl.cpp

<div></div>

    mongo::startTTLBackgroundJob()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/db/ttl.cpp

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::BackgroundJob::go()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::dbHolderUnchecked()

- Provided By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::lockedForWriting()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

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

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)
