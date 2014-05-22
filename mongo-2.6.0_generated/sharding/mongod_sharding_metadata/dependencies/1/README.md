
# Interface for Collection Metadata
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/s/collection\_metadata.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MAXKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::getRangeMapOverlap(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&, std::vector<std::pair<mongo::BSONObj, mongo::BSONObj>, std::allocator<std::pair<mongo::BSONObj, mongo::BSONObj> > >*)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::rangeMapContains(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::FieldRef::FieldRef()

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::rangeMapOverlaps(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::MINKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::FieldRef::parse(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::overlapToString(std::vector<std::pair<mongo::BSONObj, mongo::BSONObj>, std::allocator<std::pair<mongo::BSONObj, mongo::BSONObj> > >)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::rangeToString(mongo::BSONObj const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

### src/mongo/s/collection\_metadata\_test.cpp

<div></div>

    mongo::ChunkType::clear()

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MockRemoteDBServer::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::max

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::toBSON() const

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::min

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::toBSON() const

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::name

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::CollectionType::epoch

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::keyPattern

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MockConnRegistry::getConnStrHook()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::updatedAt

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::unique

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MINKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::ConnectionString::_connectHook

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MAXKEY

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::MockConnRegistry::get()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::~CollectionType()

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::ns

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ConnectionString::_connectHookMutex

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ChunkType::~ChunkType()

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::MockConnRegistry::addServer(mongo::MockRemoteDBServer*)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::ns

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::ChunkType()

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::MockConnRegistry::clear()

- Provided By:

    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::dropped

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ChunkType::shard

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ChunkType::DEPRECATED_lastmod

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MockRemoteDBServer::MockRemoteDBServer(std::string const&)

- Provided By:

    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::CollectionType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::ChunkType::DEPRECATED_epoch

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::CollectionType::CollectionType()

- Provided By:

    - [src/mongo/s/type\_collection.cpp](../../../../sharding/config\_server\_schema)
