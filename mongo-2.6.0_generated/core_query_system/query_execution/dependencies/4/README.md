
# Dependencies for Query Plan Stage Implementations
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/exec/2d.cpp

<div></div>

    mongo::Polygon::Polygon()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::inside(mongo::Point, double) const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::GeoHash()

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::Polygon::contains(mongo::Point const&) const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::onBoundary(mongo::Point, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::maxDim() const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::intersects(mongo::Box const&) const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Box::center() const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Polygon::bounds()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeoHashConverter::hash(double, double) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHashConverter::hash(mongo::Point const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::checkEarthBounds(mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Polygon::contains(mongo::Point const&, double) const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::fudge(double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Point::Point(double, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::truncate(double, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::operator=(mongo::GeoHash const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Point::Point()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::Box()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

### src/mongo/db/exec/2dcommon.cpp

<div></div>

    mongo::GeoHashConverter::unhashToBox(mongo::GeoHash const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Point::Point(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::IndexBoundsBuilder::reverseInterval(mongo::Interval*)

- Provided By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBounds::isValidFor(mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GeoHash::GeoHash()

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::up() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::GeoHash::atMinX() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Interval::Interval(mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/db/query/interval.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::GeoHash::GeoHash(mongo::BSONElement const&, unsigned int)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::GeoHash::atMaxY() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::operator+(std::string const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::TwoDAccessMethod::getKeys(mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&) const

- Provided By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

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

    mongo::GeoHash::constrains() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::GeoHash::GeoHash(unsigned int, unsigned int, unsigned int)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::move(int, int)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::IndexBoundsBuilder::allValues()

- Provided By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::GeoHash::canRefine() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::GeoHashConverter::unhashToPoint(mongo::BSONElement const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::GeoHash::operator!=(mongo::GeoHash const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::atMinY() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::hasPrefix(mongo::GeoHash const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHash::operator=(mongo::GeoHash const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeoHash::atMaxX() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::Box::Box()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

### src/mongo/db/exec/2dnear.cpp

<div></div>

    mongo::Point::Point(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../../../../third\_party/s2)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Box::Box(double, double, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Box::intersects(mongo::Box const&) const

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GeoHash::constrains() const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeoHashConverter::hash(double, double) const

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../../../../third\_party/s2)

<div></div>

    mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::checkEarthBounds(mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    vtable for S2Region

- Provided By:

    - [src/third\_party/s2/s2region.cc](../../../../third\_party/s2)

<div></div>

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Provided By:

    - [src/mongo/db/geo/hash.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Point::Point()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Box::Box()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

### src/mongo/db/exec/and\_hash.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/and\_sorted.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/collection\_scan.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Record::likelyInPhysicalMemory() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

### src/mongo/db/exec/count.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::BtreeIndexCursor::pointsAt(mongo::BtreeIndexCursor const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::IndexCatalog::isMultikey(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::BtreeIndexCursor::seek(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/exec/distinct\_scan.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsChecker::IndexBoundsChecker(mongo::IndexBounds const*, mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::IndexBoundsChecker::getStartKey(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsChecker::checkKey(mongo::BSONObj const&, int*, bool*, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/exec/fetch.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../../../../tests/fail\_points)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/index\_scan.cpp

<div></div>

    mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBounds::toBSON() const

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsChecker::IndexBoundsChecker(mongo::IndexBounds const*, mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

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

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::IndexBoundsChecker::getStartKey(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::IndexBounds::toString() const

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::IndexBoundsChecker::checkKey(mongo::BSONObj const&, int*, bool*, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::IndexCatalog::isMultikey(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

### src/mongo/db/exec/keep\_mutations.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

### src/mongo/db/exec/limit.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/merge\_sort.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/oplogstart.cpp

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../../../../utilities/utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Record::_accessing() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::DiskLoc::ext() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/exec/or.cpp

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

### src/mongo/db/exec/projection.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

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

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/projection\_exec.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearDistance

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MatchExpressionParser::_parse(mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::MatchDetails::elemMatchKey() const

- Provided By:

    - [src/mongo/db/matcher/match\_details.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::LiteParsedQuery::metaTextScore

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearPoint

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Provided By:

    - [src/mongo/base/string\_data.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::MatchDetails::MatchDetails()

- Provided By:

    - [src/mongo/db/matcher/match\_details.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::LiteParsedQuery::metaIndexKey

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::LiteParsedQuery::metaDiskLoc

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::MatchDetails::hasElemMatchKey() const

- Provided By:

    - [src/mongo/db/matcher/match\_details.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/projection\_exec\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::MatchExpressionParser::_parse(mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

### src/mongo/db/exec/s2near.cpp

<div></div>

    S2RegionCoverer::S2RegionCoverer()

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../../../../third\_party/s2)

<div></div>

    mongo::FieldRef::FieldRef()

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    S2RegionIntersection::~S2RegionIntersection()

- Provided By:

    - [src/third\_party/s2/s2regionintersection.cc](../../../../third\_party/s2)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsBuilder::makePointInterval(std::string const&)

- Provided By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../../../../third\_party/s2)

<div></div>

    LogMessageFatal::LogMessageFatal(char const*, int)

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../../../../third\_party/s2)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    S2Cell::Init(S2CellId const&)

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../../../../third\_party/s2)

<div></div>

    S2::kAvgEdge

- Provided By:

    - [src/third\_party/s2/s2.cc](../../../../third\_party/s2)

<div></div>

    vtable for S2Cap

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../../../../third\_party/s2)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    S2CellId::kNumFaces

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    LogMessageFatal::~LogMessageFatal()

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../../../../third\_party/s2)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    S2RegionCoverer::set_max_level(int)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../../../../third\_party/s2)

<div></div>

    S2Cap::Complement() const

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../../../../third\_party/s2)

<div></div>

    vtable for mongo::MatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::OrderedIntervalList::toString() const

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    S2RegionCoverer::set_min_level(int)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../../../../third\_party/s2)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    S2::kMaxCellLevel

- Provided By:

    - [src/third\_party/s2/s2.cc](../../../../third\_party/s2)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::OrderedIntervalList::isValidFor(int) const

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsBuilder::makeRangeInterval(std::string const&, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    S2CellId::ToString() const

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    S2CellId::level() const

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::MatchExpression::toString() const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    S2Cap::FromAxisAngle(Vector3<double> const&, S1Angle const&)

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../../../../third\_party/s2)

<div></div>

    S2RegionIntersection::Init(std::vector<S2Region*, std::allocator<S2Region*> >*)

- Provided By:

    - [src/third\_party/s2/s2regionintersection.cc](../../../../third\_party/s2)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../../../../third\_party/s2)

<div></div>

    S2CellId::FromString(std::string const&)

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    vtable for S2Region

- Provided By:

    - [src/third\_party/s2/s2region.cc](../../../../third\_party/s2)

<div></div>

    typeinfo for mongo::MatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ElementPath::init(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    vtable for S2LatLngRect

- Provided By:

    - [src/third\_party/s2/s2latlngrect.cc](../../../../third\_party/s2)

<div></div>

    S2CellId::kMaxLevel

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    mongo::MatchExpression::matchesBSON(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    S2RegionIntersection::S2RegionIntersection()

- Provided By:

    - [src/third\_party/s2/s2regionintersection.cc](../../../../third\_party/s2)

<div></div>

    S2RegionCoverer::~S2RegionCoverer()

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../../../../third\_party/s2)

<div></div>

    S2RegionIntersection::Release(std::vector<S2Region*, std::allocator<S2Region*> >*)

- Provided By:

    - [src/third\_party/s2/s2regionintersection.cc](../../../../third\_party/s2)

<div></div>

    mongo::S2SearchUtil::distanceBetween(Vector3<double> const&, mongo::BSONObj const&, double*)

- Provided By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::Point::Point()

- Provided By:

    - [src/mongo/db/geo/shapes.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    S2CellId::kPosBits

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../../../../third\_party/s2)

<div></div>

    S2LatLngRect::Area() const

- Provided By:

    - [src/third\_party/s2/s2latlngrect.cc](../../../../third\_party/s2)

<div></div>

    mongo::MatchExpression::MatchExpression(mongo::MatchExpression::MatchType)

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    S2RegionCoverer::GetCovering(S2Region const&, std::vector<S2CellId, std::allocator<S2CellId> >*)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../../../../third\_party/s2)

### src/mongo/db/exec/shard\_filter.cpp

<div></div>

    mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)

### src/mongo/db/exec/skip.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/sort.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexNames::nameToType(std::string const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BtreeKeyGeneratorV1::BtreeKeyGeneratorV1(std::vector<char const*, std::allocator<char const*> >, std::vector<mongo::BSONElement, std::allocator<mongo::BSONElement> >, bool)

- Provided By:

    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexBoundsChecker::IndexBoundsChecker(mongo::IndexBounds const*, mongo::BSONObj const&, int)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

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

    mongo::QueryPlanner::plan(mongo::CanonicalQuery const&, mongo::QueryPlannerParams const&, std::vector<mongo::QuerySolution*, std::allocator<mongo::QuerySolution*> >*)

- Provided By:

    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::IndexBoundsChecker::isValidKey(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verboseQueryLogging

- Provided By:

    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::LiteParsedQuery::isTextScoreMeta(mongo::BSONElement)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::BtreeKeyGenerator::ParallelArraysCode

- Provided By:

    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::internalQueryPlannerMaxIndexedSolutions

- Provided By:

    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)

<div></div>

    mongo::IndexNames::BTREE

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/exec/sort\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

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

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

### src/mongo/db/exec/text.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::fts::FTSQuery::toBSON() const

- Provided By:

    - [src/mongo/db/fts/fts\_query.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::fts::FTSIndexFormat::getIndexKey(double, std::string const&, mongo::BSONObj const&, mongo::fts::TextIndexVersion)

- Provided By:

    - [src/mongo/db/fts/fts\_index\_format.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::ElementIterator::Context::reset(mongo::BSONElement, mongo::BSONElement, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ElementIterator::~ElementIterator()

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::fts::FTSMatcher::phrasesMatch(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/fts/fts\_matcher.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::fts::FTSMatcher::FTSMatcher(mongo::fts::FTSQuery const&, mongo::fts::FTSSpec const&)

- Provided By:

    - [src/mongo/db/fts/fts\_matcher.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    typeinfo for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::fts::MAX_WEIGHT

- Provided By:

    - [src/mongo/db/fts/fts\_spec.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::fts::FTSMatcher::hasNegativeTerm(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/fts/fts\_matcher.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DiskLoc::obj() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    vtable for mongo::ElementIterator

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::SimpleArrayElementIterator::SimpleArrayElementIterator(mongo::BSONElement const&, bool)

- Provided By:

    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)
