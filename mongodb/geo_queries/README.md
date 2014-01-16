# geo\_queries

# Module Groups

-------------

# Group Description
GEO query code. TODO: describe the structure of this and how it interacts with the new index  system.

# Files
- src/mongo/db/geo/core.h
- src/mongo/db/geo/geoconstants.h
- src/mongo/db/geo/geoparser.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/geoparser.h
- src/mongo/db/geo/geoparser\_test.cpp   ()
- src/mongo/db/geo/geoquery.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/geoquery.h
- src/mongo/db/geo/hash.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/hash.h
- src/mongo/db/geo/hash\_test.cpp   ()
- src/mongo/db/geo/haystack.cpp   (mongod, tools)
- src/mongo/db/geo/s2common.cpp   (mongod, tools)
- src/mongo/db/geo/s2common.h
- src/mongo/db/geo/shapes.cpp   (mongod, tools, mongos)
- src/mongo/db/geo/shapes.h

# Interface

### src/mongo/db/geo/geoparser.cpp

    mongo::GeoParser::isPoint(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

### src/mongo/db/geo/geoquery.cpp

    mongo::GeometryContainer::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

    mongo::GeoQuery::getRegion() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

    mongo::GeoQuery::satisfiesPredicate(mongo::GeometryContainer const&) const

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

    mongo::NearQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

    mongo::GeometryContainer::hasS2Region() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

    mongo::GeometryContainer::hasFlatRegion() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

    mongo::GeoQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

### src/mongo/db/geo/hash.cpp

    mongo::GeoHash::up() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::GeoHash(mongo::BSONElement const&, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::move(int, int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::constrains() const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::canRefine() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::hash(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::GeoHashConverter::hash(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::hash(mongo::BSONObj const&, mongo::BSONObj const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

    mongo::GeoHash::GeoHash()

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::GeoHash::atMinX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::operator+(std::string const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::unhashToPoint(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::atMinY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::operator=(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::GeoHash::atMaxY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::GeoHash(unsigned int, unsigned int, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::hash(double, double) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::GeoHash::operator!=(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::GeoHashConverter(mongo::GeoHashConverter::Parameters const&)

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

    mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHashConverter::unhashToPoint(mongo::BSONElement const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::hasPrefix(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::GeoHash::atMaxX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

### src/mongo/db/geo/s2common.cpp

    mongo::S2SearchUtil::getKeysForObject(mongo::BSONObj const&, mongo::S2IndexingParams const&, std::vector<std::string, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)

    mongo::S2SearchUtil::distanceBetween(Vector3<double> const&, mongo::BSONObj const&, double*)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)

### src/mongo/db/geo/shapes.cpp

    mongo::Box::Box(mongo::Point, mongo::Point)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::Point::Point(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

    mongo::Polygon::contains(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::inside(mongo::Point, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::onBoundary(mongo::Point, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::Box(double, double, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)

    mongo::Box::fudge(double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Polygon::Polygon()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::intersects(mongo::Box const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::center() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Polygon::bounds()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::maxDim() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::checkEarthBounds(mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::Box()

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Polygon::contains(mongo::Point const&, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Point::Point(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

    mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Point::Point(double, double)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::Box::truncate(double, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../query\_system)

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
