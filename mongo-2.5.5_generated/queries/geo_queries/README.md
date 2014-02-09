# geo\_queries

# Module Groups

-------------

# Group Description
GEO query code. TODO: describe the structure of this and how it interacts with the new index  system.

# Files
- src/mongo/db/geo/core.h   (mongod, tools, mongos)
- src/mongo/db/geo/geoconstants.h   (mongod, tools, mongos)
- src/mongo/db/geo/geoparser.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/geoparser.h   (mongod, tools, mongos)
- src/mongo/db/geo/geoparser\_test.cpp   ()
- src/mongo/db/geo/geoquery.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/geoquery.h   (mongod, tools, mongos)
- src/mongo/db/geo/hash.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/hash.h   (mongod, tools, mongos)
- src/mongo/db/geo/hash\_test.cpp   ()
- src/mongo/db/geo/haystack.cpp   (mongod, tools)
- src/mongo/db/geo/s2.h   (mongod, tools, mongos)
- src/mongo/db/geo/s2common.cpp   (mongod, tools)
- src/mongo/db/geo/s2common.h   (mongod, tools, mongos)
- src/mongo/db/geo/shapes.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/shapes.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/geo/geoparser.cpp

<div></div>

    mongo::GeoParser::isPoint(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

### src/mongo/db/geo/geoquery.cpp

<div></div>

    mongo::GeometryContainer::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

<div></div>

    mongo::GeoQuery::getRegion() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<div></div>

    mongo::GeoQuery::satisfiesPredicate(mongo::GeometryContainer const&) const

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

<div></div>

    mongo::NearQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

<div></div>

    mongo::GeometryContainer::hasS2Region() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

<div></div>

    mongo::GeometryContainer::hasFlatRegion() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

<div></div>

    mongo::GeoQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

### src/mongo/db/geo/hash.cpp

<div></div>

    mongo::GeoHash::up() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::GeoHash(mongo::BSONElement const&, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::move(int, int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::constrains() const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::canRefine() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&, mongo::BSONObj const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

<div></div>

    mongo::GeoHash::GeoHash()

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::GeoHash::atMinX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::operator+(std::string const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::unhashToPoint(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::atMinY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::operator=(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::GeoHash::atMaxY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::GeoHash(unsigned int, unsigned int, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::hash(double, double) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::GeoHash::operator!=(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::GeoHashConverter(mongo::GeoHashConverter::Parameters const&)

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

<div></div>

    mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHashConverter::unhashToPoint(mongo::BSONElement const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::hasPrefix(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::GeoHash::atMaxX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

### src/mongo/db/geo/s2common.cpp

<div></div>

    mongo::S2SearchUtil::getKeysForObject(mongo::BSONObj const&, mongo::S2IndexingParams const&, std::vector<std::string, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)

<div></div>

    mongo::S2SearchUtil::distanceBetween(Vector3<double> const&, mongo::BSONObj const&, double*)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)

### src/mongo/db/geo/shapes.cpp

<div></div>

    mongo::Box::Box(mongo::Point, mongo::Point)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::Point::Point(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

<div></div>

    mongo::Box::inside(mongo::Point, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Polygon::contains(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::onBoundary(mongo::Point, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::Box(double, double, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)

<div></div>

    mongo::Box::fudge(double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Polygon::Polygon()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::intersects(mongo::Box const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::center() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Polygon::bounds()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::maxDim() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::checkEarthBounds(mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::Box()

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Polygon::contains(mongo::Point const&, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Point::Point(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

<div></div>

    mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Point::Point(double, double)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Box::truncate(double, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Point::Point()

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/query/planner\_access.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../query\_system)

# Dependencies

### src/mongo/db/geo/geoparser.cpp

<div></div>

    S2Loop::IsValid() const

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    S2LatLng::ToPoint() const

- Provided By:

    - [src/third\_party/s2/s2latlng.cc](../s2)

<div></div>

    S2PolygonBuilder::S2PolygonBuilder(S2PolygonBuilderOptions const&)

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    S2Loop::~S2Loop()

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    LogMessageFatal::LogMessageFatal(char const*, int)

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    S2Cell::Init(S2CellId const&)

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    S2Polyline::S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    vtable for S2Cap

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../s2)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Loop::Contains(S2Loop const*) const

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    S2Loop::Normalize()

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    S2PolygonBuilder::~S2PolygonBuilder()

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    LogMessageFatal::~LogMessageFatal()

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Polyline::IsValid(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Polygon::S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2LatLng::Normalized() const

- Provided By:

    - [src/third\_party/s2/s2latlng.cc](../s2)

<div></div>

    S2PolygonBuilder::AddLoop(S2Loop const*)

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    S2Polyline::Init(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2Loop::S2Loop(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    S2Cap::FromAxisAngle(Vector3<double> const&, S1Angle const&)

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../s2)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../s2)

<div></div>

    S2Loop::Invert()

- Provided By:

    - [src/third\_party/s2/s2loop.cc](../s2)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    S2PolygonBuilderOptions::set_xor_edges(bool)

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    S2PolygonBuilder::AssemblePolygon(S2Polygon*, std::vector<std::pair<Vector3<double>, Vector3<double> >, std::allocator<std::pair<Vector3<double>, Vector3<double> > > >*)

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    S2PolygonBuilderOptions::set_validate(bool)

- Provided By:

    - [src/third\_party/s2/s2polygonbuilder.cc](../s2)

<div></div>

    S2Polygon::~S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2CellId::FromPoint(Vector3<double> const&)

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

### src/mongo/db/geo/geoparser\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    mongo::fromjson(std::string const&)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    S2Polyline::S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

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

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Polyline::~S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2Polygon::S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../s2)

<div></div>

    S2Polygon::Contains(Vector3<double> const&) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    S2Polygon::~S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/db/geo/geoquery.cpp

<div></div>

    S2Polyline::MayIntersect(S2Cell const&) const

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2RegionUnion::Add(S2Region*)

- Provided By:

    - [src/third\_party/s2/s2regionunion.cc](../s2)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    S2Polyline::S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    vtable for S2Cap

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../s2)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Cell::MayIntersect(S2Cell const&) const

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    S2Polygon::Intersects(S2Polygon const*) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

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

    S2Polyline::~S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2Polygon::S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../s2)

<div></div>

    S2Polygon::Contains(S2Polygon const*) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    S2Polygon::Contains(Vector3<double> const&) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2Polygon::IntersectWithPolyline(S2Polyline const*, std::vector<S2Polyline*, std::allocator<S2Polyline*> >*) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2Polyline::NearlyCoversPolyline(S2Polyline const&, S1Angle const&) const

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2RegionUnion::S2RegionUnion()

- Provided By:

    - [src/third\_party/s2/s2regionunion.cc](../s2)

<div></div>

    S2Polygon::MayIntersect(S2Cell const&) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    S2Polygon::~S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2Polyline::Intersects(S2Polyline const*) const

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2Cap::MayIntersect(S2Cell const&) const

- Provided By:

    - [src/third\_party/s2/s2cap.cc](../s2)

### src/mongo/db/geo/hash.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

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

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/geo/hash\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::PseudoRandom::PseudoRandom(int)

- Provided By:

    - [src/mongo/platform/random.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

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

### src/mongo/db/geo/haystack.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../authentication)

<div></div>

    mongo::IndexCatalog::findIndexByType(std::string const&, std::vector<mongo::IndexDescriptor*, std::allocator<mongo::IndexDescriptor*> >&) const

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Command::parseResourcePattern(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::HaystackAccessMethod::searchCommand(mongo::BSONObj const&, double, mongo::BSONObj const&, mongo::BSONObjBuilder*, unsigned int)

- Provided By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

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

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

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

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Provided By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

### src/mongo/db/geo/s2common.cpp

<div></div>

    S2RegionCoverer::S2RegionCoverer()

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2RegionCoverer::set_max_cells(int)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for S2Cell

- Provided By:

    - [src/third\_party/s2/s2cell.cc](../s2)

<div></div>

    LogMessageFatal::LogMessageFatal(char const*, int)

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    S2::kAvgEdge

- Provided By:

    - [src/third\_party/s2/s2.cc](../s2)

<div></div>

    S2Polyline::S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2CellId::kNumFaces

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

<div></div>

    LogMessageFatal::~LogMessageFatal()

- Provided By:

    - [src/third\_party/s2/base/logging.cc](../s2)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    S2RegionCoverer::set_max_level(int)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2::kMaxCellLevel

- Provided By:

    - [src/third\_party/s2/s2.cc](../s2)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    S2Polyline::~S2Polyline()

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2Polygon::S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2CellId::ToString() const

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

<div></div>

    S2CellId::level() const

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

<div></div>

    S2Region::~S2Region()

- Provided By:

    - [src/third\_party/s2/s2region.cc](../s2)

<div></div>

    S2RegionCoverer::set_min_level(int)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    S2RegionCoverer::~S2RegionCoverer()

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

<div></div>

    S1Angle::S1Angle(Vector3<double> const&, Vector3<double> const&)

- Provided By:

    - [src/third\_party/s2/s1angle.cc](../s2)

<div></div>

    S2CellId::kMaxLevel

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

<div></div>

    S2Polygon::~S2Polygon()

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2Polyline::Project(Vector3<double> const&, int*) const

- Provided By:

    - [src/third\_party/s2/s2polyline.cc](../s2)

<div></div>

    S2CellId::kPosBits

- Provided By:

    - [src/third\_party/s2/s2cellid.cc](../s2)

<div></div>

    S2Polygon::Project(Vector3<double> const&) const

- Provided By:

    - [src/third\_party/s2/s2polygon.cc](../s2)

<div></div>

    S2RegionCoverer::GetCovering(S2Region const&, std::vector<S2CellId, std::allocator<S2CellId> >*)

- Provided By:

    - [src/third\_party/s2/s2regioncoverer.cc](../s2)

### src/mongo/db/geo/shapes.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

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
