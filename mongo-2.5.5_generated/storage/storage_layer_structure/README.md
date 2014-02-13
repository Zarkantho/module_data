# storage\_layer\_structure

# Module Groups

-------------

# Group Description
Helper to manage strings that look like "<db>.<collection>"

# Files
- src/mongo/db/namespace\_string-inl.h   (mongod, tools, mongos)
- src/mongo/db/namespace\_string.h   (mongod, tools, mongos)
- src/mongo/db/namespace\_string\_test.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/namespace\_string\_test.cpp

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

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

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

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Class to hold namespace strings that look like "<db>.<collection>" in a fixed width form

# Files
- src/mongo/db/structure/catalog/namespace.cpp   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace-inl.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace\_test.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/structure/catalog/namespace\_test.cpp

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

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Files containing the btree datastructure code.  Currently this is the only index datastructure we use.  While this is intended to be a low level datastructure, it currently has a few fingers into replication and other parts of the server, including calling isMaster

# Files
- src/mongo/db/structure/btree/btree.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree.h   (mongod, tools)
- src/mongo/db/structure/btree/btree\_stats.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree\_stats.h   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.h   (mongod, tools)
- src/mongo/db/structure/btree/key.cpp   (mongod, tools)
- src/mongo/db/structure/btree/key.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/structure/btree/btree.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::asVersion(mongo::Record*)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::asVersion(mongo::Record*)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::IndexCatalogEntry*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::IndexCatalogEntry const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::IndexCatalogEntry const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

### src/mongo/db/structure/btree/btreebuilder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

### src/mongo/db/structure/btree/key.cpp

<div></div>

    mongo::KeyV1::dataSize() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::woEqual(mongo::KeyV1 const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::toBson() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

# Dependencies

### src/mongo/db/structure/btree/btree.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

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

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::MsgAssertionException

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::BtreeIndexCursor::aboutToDeleteBucket(mongo::DiskLoc const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/structure/btree/btree\_stats.cpp

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

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

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/structure/btree/btreebuilder.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

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

### src/mongo/db/structure/btree/key.cpp

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

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

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

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

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

-------------

# Group Description
Classes to manage and iterate indexes.  There should only be one index catalog per collection.  Contains some subset of the metadata about an index as well as an index descriptor containing the rest of the data

# Files
- src/mongo/db/catalog/index\_catalog.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.h   (mongod, tools, mongos)
- src/mongo/db/catalog/index\_catalog\_entry.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog\_entry.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexCatalog::findIndexByType(std::string const&, std::vector<mongo::IndexDescriptor*, std::allocator<mongo::IndexDescriptor*> >&) const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)

<div></div>

    mongo::IndexCatalog::getAndClearUnfinishedIndexes()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::haveIdIndex() const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/tools/admin.cpp](../tools)

<div></div>

    mongo::IndexCatalog::findIdIndex() const

- Used By:

    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool) const

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::updateTTLSetting(mongo::IndexDescriptor const*, long long)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::IndexCatalog::ensureHaveIdIndex()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::numIndexesReady() const

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::okToAddIndex(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/exec/distinct\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropIndex(mongo::IndexDescriptor*)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::next()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::more()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::IndexIterator(mongo::IndexCatalog const*, bool)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/exec/2d.cpp](../core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::ok() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*) const

- Used By:

    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::IndexCatalog::isMultikey(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../core\_query\_system)

### src/mongo/db/catalog/index\_catalog\_entry.cpp

<div></div>

    mongo::IndexCatalogEntry::setMultikey()

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::IndexCatalogEntry::head() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)

<div></div>

    mongo::IndexCatalogEntry::setHead(mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::IndexCatalogEntry::isReady() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

# Dependencies

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::FieldRef::FieldRef()

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../update\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::LeafMatchExpression::matches(mongo::MatchableDocument const*, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ComparisonMatchExpression::equivalent(mongo::MatchExpression const*) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::ComparisonMatchExpression::init(mongo::StringData const&, mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)

<div></div>

    typeinfo for mongo::ComparisonMatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

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

    vtable for mongo::MatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../core\_query\_system)

<div></div>

    vtable for mongo::LeafMatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::IndexNames::HASHED

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ComparisonMatchExpression::debugString(mongo::StringBuilderImpl<mongo::TrivialAllocator>&, int) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::MatchExpression::toString() const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../core\_query\_system)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::IndexNames::TEXT

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ComparisonMatchExpression::matchesSingleElement(mongo::BSONElement const&) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../core\_query\_system)

<div></div>

    mongo::FieldRef::FieldRef(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../update\_system)

<div></div>

    mongo::audit::logDropIndex(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)

<div></div>

    mongo::S2AccessMethod::S2AccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)

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

    mongo::MatchExpression::matchesBSON(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../core\_query\_system)

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::FTSAccessMethod::FTSAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::ErrorCodes::fromInt(int)

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/base/error\_codes.cpp](../base\_utilites)

<div></div>

    mongo::IndexNames::GEO_2D

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::FieldRef::getPart(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../update\_system)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::MatchExpression::MatchExpression(mongo::MatchExpression::MatchType)

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../core\_query\_system)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/db/catalog/index\_catalog\_entry.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Top level class to keep track of databases.  Essentially a map of path + dbname to a Database object with extra logic to optionally create the database if it does not exist.

# Files
- src/mongo/db/catalog/database\_holder.cpp   (mongod, tools)
- src/mongo/db/catalog/database\_holder.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/database\_holder.cpp

<div></div>

    mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

# Dependencies

### src/mongo/db/catalog/database\_holder.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Class to manage a single database.  This currently contains the code to manage data files and collections and provides mechanisms to access other database information, such as indexes.

# Files
- src/mongo/db/catalog/database.cpp   (mongod, tools)
- src/mongo/db/catalog/database.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/database.cpp

<div></div>

    mongo::Database::clearTmpCollections()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::Database::setProfilingLevel(int, std::string&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)

<div></div>

    mongo::Database::getOrCreateCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../core\_query\_system)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/tools/admin.cpp](../tools)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/exec/2d.cpp](../core\_query\_system)

<div></div>

    mongo::Database::duplicateUncasedName(bool, std::string const&, std::string const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Database::dropCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<div></div>

    mongo::Database::_initExtentFreeList()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::Database::Database(char const*, bool&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/catalog/database.cpp

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Top::global

- Provided By:

    - [src/mongo/db/stats/top.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::audit::logCreateCollection(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::nsGetDB(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logDropCollection(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)

<div></div>

    mongo::Top::collectionDropped(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/stats/top.cpp](../utilities)

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

    mongo::nsGetCollection(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::audit::logRenameCollection(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::audit::logCreateDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)

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

    mongo::getOrCreateProfileCollection(mongo::Database*, bool, std::string*)

- Provided By:

    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::authindex::createSystemIndexes(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/auth/auth\_index\_d.cpp](../authentication)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Class to manage the disk format of the ".ns" files

# Files
- src/mongo/db/structure/catalog/namespace\_details-inl.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace\_details.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/namespace\_details.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/structure/catalog/namespace\_details.cpp

<div></div>

    mongo::bucketSizes

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::quantizeAllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::getRecordAllocationSize(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::setUserFlag(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::idx(int, bool)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::writingWithExtra()

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::alloc(mongo::Collection*, mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::setPaddingFactor(double)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceDetails::clearUserFlag(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::setIndexIsMultikey(int, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

# Dependencies

### src/mongo/db/structure/catalog/namespace\_details.cpp

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

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

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::applyUpdateOperators(mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    vtable for mongo::MsgAssertionException

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

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Scope::storedFuncMod()

- Provided By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

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

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

-------------

# Group Description
Class to manage a single collection, including collection data and collection metadata.

# Files
- src/mongo/db/catalog/collection.cpp   (mongod, tools)
- src/mongo/db/catalog/collection.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/collection.cpp

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::Collection::docFor(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)

<div></div>

    mongo::Collection::dataSize() const

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)

<div></div>

    mongo::CompactOptions::toString() const

- Used By:

    - [src/mongo/db/commands/compact.cpp](../database\_commands)

<div></div>

    mongo::Collection::requiresIdIndex() const

- Used By:

    - [src/mongo/tools/admin.cpp](../tools)

<div></div>

    mongo::Collection::isCapped() const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Collection::insertDocument(mongo::DocWriter const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::Collection::numRecords() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::Collection::updateDocument(mongo::DiskLoc const&, mongo::BSONObj const&, bool, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

# Dependencies

### src/mongo/db/catalog/collection.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::PlanCache::~PlanCache()

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::QuerySettings::~QuerySettings()

- Provided By:

    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)

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

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::causedBy(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

-------------

# Group Description
Contains methods to update and access non persistent collection state, such as the current query plan cache

# Files
- src/mongo/db/catalog/collection\_info\_cache.cpp   (mongod, tools)
- src/mongo/db/catalog/collection\_info\_cache.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/collection\_info\_cache.cpp

<div></div>

    mongo::CollectionInfoCache::computeIndexKeys()

- Used By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::CollectionInfoCache::getQuerySettings() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)

<div></div>

    mongo::CollectionInfoCache::getPlanCache() const

- Used By:

    - [src/mongo/db/query/cached\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)

# Dependencies

### src/mongo/db/catalog/collection\_info\_cache.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

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

    mongo::IndexPathSet::clear()

- Provided By:

    - [src/mongo/db/index\_set.cpp](../indexing)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::QuerySettings::QuerySettings()

- Provided By:

    - [src/mongo/db/query/query\_settings.cpp](../core\_query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::PlanCache::notifyOfWriteOp()

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)

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

    mongo::IndexPathSet::addPath(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/index\_set.cpp](../indexing)

<div></div>

    mongo::PlanCache::PlanCache(std::string const&)

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::PlanCache::~PlanCache()

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::PlanCache::clear()

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../core\_query\_system)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

-------------

# Group Description
Keeps track of cursors and query runners for timeout and invalidation purposes.  The pattern is that the relevant objects must be registered here so that this code can essentially call back to do the invalidation when necessary

# Files
- src/mongo/db/catalog/collection\_cursor\_cache.cpp   (mongod, tools)
- src/mongo/db/catalog/collection\_cursor\_cache.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/catalog/collection\_cursor\_cache.cpp

<div></div>

    mongo::CollectionCursorCache::registerRunner(mongo::Runner*)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::invalidateDocument(mongo::DiskLoc const&, mongo::InvalidationType)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::CollectionCursorCache::deregisterCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::find(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::getCursorIds(std::set<long long, std::less<long long>, std::allocator<long long> >*)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::numCursors()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::deregisterRunner(mongo::Runner*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::registerCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionCursorCache::eraseCursorGlobal(long long)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::invalidateAll(bool)

- Used By:

    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::timeoutCursorsGlobal(unsigned int)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/catalog/collection\_cursor\_cache.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::ClientCursor::kill()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logKillCursorsAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::ActionType::killCursors

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ClientCursor::~ClientCursor()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

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

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::SecureRandom::create()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursor::shouldTimeout(unsigned int)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::assertAtLeastReadLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

-------------

# Group Description
Free function to create an index in the foreground.  TODO: Find all the ways an index can be created and put them in the same section

# Files
- src/mongo/db/catalog/index\_create.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_create.h   (mongod, tools)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/catalog/index\_create.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BackgroundOperation::BackgroundOperation(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../core\_query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

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

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::audit::logCreateIndex(mongo::ClientBasic*, mongo::BSONObj const*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)

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

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

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

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)

<div></div>

    mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

-------------

# Group Description
Command line options for the storage system.  This should only be in binaries that have a storaage layer.

# Files
- src/mongo/db/storage\_options.cpp   (mongod, tools)
- src/mongo/db/storage\_options.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/storage\_options.cpp

<div></div>

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::storageGlobalParams

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/commands/create\_indexes.cpp](../database\_commands)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/tools/admin.cpp](../tools)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../aggregation\_framework)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../database\_commands)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/ops/count.cpp](../core\_query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<div></div>

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

# Dependencies

### src/mongo/db/storage\_options.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<double>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

-------------

# Group Description
Contains code to do low level storage management of a capped collection, such as allocation of new records

# Files
- src/mongo/db/structure/catalog/cap.cpp   (mongod, tools)

# Interface

### src/mongo/db/structure/catalog/cap.cpp

<div></div>

    mongo::NamespaceDetails::cappedTruncateAfter(char const*, mongo::DiskLoc, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::emptyCappedCollection(char const*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

# Dependencies

### src/mongo/db/structure/catalog/cap.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Helpers::findAll(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Fixed size hash table that is appropriate for managing memory that is persisted to disk

# Files
- src/mongo/db/structure/catalog/hashtab.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
On disk format of index metadata

# Files
- src/mongo/db/structure/catalog/index\_details.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/index\_details.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/structure/catalog/index\_details.cpp

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

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Manages the ".ns" files, including adding the metadata for a new namespace or removing metadata for a deleted namespace

# Files
- src/mongo/db/structure/catalog/namespace\_index.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/namespace\_index.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/structure/catalog/namespace\_index.cpp

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/admin.cpp](../tools)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::NamespaceIndex::_init()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/db/structure/catalog/namespace\_index.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DurableMappedFile::create(std::string const&, unsigned long long&, bool)

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

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

    mongo::dbexit(mongo::ExitCode, char const*)

- Provided By:

    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DurableMappedFile::open(std::string const&, bool)

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

-------------

# Group Description
Contains the code that actually does the work of compacting a collection.  TODO: put this near the actual compact command

# Files
- src/mongo/db/structure/collection\_compact.cpp   (mongod, tools)

# Interface

### src/mongo/db/structure/collection\_compact.cpp

<div></div>

    mongo::Collection::compact(mongo::CompactOptions const*)

- Used By:

    - [src/mongo/db/commands/compact.cpp](../database\_commands)

# Dependencies

### src/mongo/db/structure/collection\_compact.cpp

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

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Provided By:

    - [src/mongo/util/touch\_pages.cpp](../utilities)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

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

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
Contains code that essentially does a table scan of a collection. Has iterators for both capped and non capped collections.

# Files
- src/mongo/db/structure/collection\_iterator.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_iterator.h   (mongod, tools)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/structure/collection\_iterator.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

-------------

# Group Description
A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database storage space.

# Files
- src/mongo/db/diskloc.h   (mongod, tools, mongos)
- src/mongo/db/diskloc\_test.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/diskloc\_test.cpp

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
Type of a DiskLoc invalidation.

# Files
- src/mongo/db/invalidation\_type.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

# Files
- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::DiskLoc::obj() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/exec/working\_set\_common.cpp](../core\_query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../core\_query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/exec/2d.cpp](../core\_query\_system)

<div></div>

    mongo::Record::touch(bool) const

- Used By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Record::likelyInPhysicalMemory() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::DiskLoc::rec() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/exec/2dcommon.cpp](../core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::Record::_accessing() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DiskLoc::drec() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)

<div></div>

    mongo::DiskLoc::ext() const

- Used By:

    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

# Dependencies

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::blockInMemory(void const*)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

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

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

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

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

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

    mongo::PageFaultException::PageFaultException(mongo::Record const*)

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

-------------

# Group Description
Manages Records.  Contains code to delete and insert records, as well as helpers to construct a Record object from a DiscLoc.  Also handles allocating new extents if the current extent does not have room for another record.

# Files
- src/mongo/db/structure/record\_store.cpp   (mongod, tools)
- src/mongo/db/structure/record\_store.h   (mongod, tools, mongos)

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/structure/record\_store.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::MAdvise::MAdvise(void*, unsigned int, mongo::MAdvise::Advice)

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

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

    mongo::MAdvise::~MAdvise()

- Provided By:

    - [src/mongo/util/mmap\_posix.cpp](../mmap)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

# Files
- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/storage/extent.cpp

<div></div>

    mongo::Extent::dump()

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Extent::initialSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<div></div>

    mongo::Extent::followupSize(int, int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<div></div>

    mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Extent::maxSize()

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/storage/extent.cpp

<div></div>

    mongo::DataFile::maxSize()

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

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

    std::string mongo::integerToHex<unsigned int>(unsigned int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

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

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

# Files
- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/storage/extent\_manager.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::flushFiles(bool)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::ExtentManager::quantizeExtentSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<div></div>

    mongo::ExtentManager::getFile(int, int, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::fileSize() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

# Dependencies

### src/mongo/db/storage/extent\_manager.cpp

<div></div>

    mongo::DataFile::openExisting(char const*)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DataFile::open(char const*, int, bool)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DataFile::flush(bool)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DataFile::allocExtentArea(int)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::DataFile::maxSize()

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DataFile::badOfs(int) const

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

-------------

# Group Description
Utilities to clone entire collections and databases

# Files
- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h   (mongod, tools)

# Interface

### src/mongo/db/cloner.cpp

<div></div>

    mongo::Cloner::Cloner()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::Cloner::cloneFrom(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::string&, int*, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Cloner::copyCollectionFromRemote(std::string const&, std::string const&, std::string&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)

<div></div>

    mongo::Cloner::go(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*, std::string&, int*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

# Dependencies

### src/mongo/db/cloner.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::Context::_finishInit()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Command::parseNsFullyQualified(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replAuthenticate(mongo::DBClientBase*)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Query::toString() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

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

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)

<div></div>

    mongo::NE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Query::snapshot()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::NIN

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::getErrField(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::HostAndPort::isSelf() const

- Provided By:

    - [src/mongo/db/commands/isself.cpp](../database\_commands)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
One of the very hairy, very old parts of the server. Contains code for the DBDirectClient, which  is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the  same interface as the client driver, except that instead of connecting over the network it is just  doing operations on the local server behind the scenes.   This also has code for the "BSONElementManipulator which is what allows us to do in place  updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds"  field for a document in a TTL index.   Also have random things like "getDatabaseNames" which just iteratest the db directory getting all  the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.   clarify relationship between instance.cpp and the various ops/* (insert/update etc)

# Files
- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/instance.cpp

<div></div>

    typeinfo for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::exitCleanly(mongo::ExitCode)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::DBDirectClient::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::lockFile

- Used By:

    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::_diaglog

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::mongoAbort(char const*)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    vtable for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../core\_query\_system)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DiagLog::flush()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/stats/snapshots.cpp](../utilities)
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::DiagLog::setLevel(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBDirectClient::killCursor(long long)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::dbExecCommand

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::acquirePathLock(bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::replHasDatabases()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

<div></div>

    mongo::killCurrentOp

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/tools/admin.cpp](../tools)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/repl/rs.cpp](../replication)

# Dependencies

### src/mongo/db/instance.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::_unlockFsync()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::causedBy(mongo::Status const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Client::clients

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*, mongo::UpdateDriver*, mongo::CanonicalQuery*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::audit::logInsertAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

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

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ReplSet::shutdown()

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../fail\_points)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../fail\_points)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::AuthorizationSession::startRequest()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::nsGetDB(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::ExceptionInfo::append(mongo::BSONObjBuilder&, char const*, char const*) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)

<div></div>

    mongo::oplogCheckCloseDatabase(mongo::Database*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::audit::logKillOpAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::lockedForWriting()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../fail\_points)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::inprog

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::dur::haveJournalFiles(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::ActionType::unlock

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::info()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::audit::logUpdateAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::nsGetCollection(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::setPostRunCommandHook(boost::function<void (mongo::BSONObj const&, std::string const&)>)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ActionType::killop

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::MessagingPort::closeAllSockets(unsigned int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ListeningSockets::get()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../core\_query\_system)

<div></div>

    mongo::KillCurrentOp::killAll()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::dur::journalCleanup(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::dur::commitJob

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../fail\_points)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logQueryAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::OpTime::m

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

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

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::audit::logInProgAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::runCount(std::string const&, mongo::BSONObj const&, std::string&, int&)

- Provided By:

    - [src/mongo/db/ops/count.cpp](../core\_query\_system)

<div></div>

    mongo::OpDebug::reset()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../fail\_points)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../core\_query\_system)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::audit::logDeleteAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::readlocktry::~readlocktry()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::audit::logFsyncUnlockAuthzCheck(mongo::ClientBasic*, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::isReadLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    typeinfo for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)

- Provided By:

    - [src/mongo/s/d\_logic.cpp](../sharding)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::CanonicalQuery::isSimpleIdQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logGetMoreAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../core\_query\_system)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::clientsMutex

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../core\_query\_system)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
This is another really hairy, really old legacy file. At this point it's easier to just write out  all the functions in the interface than describe what it does. I believe "pdfile" is short for  "persistent data file". It contains a bunch of old legacy things to manipulate data files and  data file metadata.   Here are all the functions in pdfile.cpp that are currently used in the project.   mongo::inDBRepair  mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)  mongo::dbSize(char const*)  mongo::dropDatabase(std::string const&)  mongo::dbHolderUnchecked()  mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)  mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)  mongo::\_deleteDataFiles(char const*)  mongo::dropAllDatabasesExceptLocal()  mongo::isValidNS(mongo::StringData const&)  mongo::repairDatabase(std::string, std::string&, bool, bool)

# Files
- src/mongo/db/pdfile.cpp   (mongod, tools)
- src/mongo/db/pdfile.h   (mongod, tools, mongos)
- src/mongo/db/pdfile\_private.h   (mongod, tools)
- src/mongo/db/pdfile\_version.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::inDBRepair

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)

<div></div>

    mongo::dbSize(char const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::dropDatabase(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::dbHolderUnchecked()

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../web\_server)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::_deleteDataFiles(char const*)

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)

<div></div>

    mongo::dropAllDatabasesExceptLocal()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

# Dependencies

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

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

    mongo::BackgroundOperation::assertNoBgOpInProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

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

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logDropDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../auditing)

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

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::freeSpace(std::string const&)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
