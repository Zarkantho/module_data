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

- <pre>mongo::GeoParser::isPoint(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

### src/mongo/db/geo/geoquery.cpp

- <pre>mongo::GeometryContainer::parseFrom(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

- <pre>mongo::GeoQuery::getRegion() const</pre>
Used By:
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

- <pre>mongo::GeoQuery::satisfiesPredicate(mongo::GeometryContainer const&) const</pre>
Used By:
    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)

- <pre>mongo::NearQuery::parseFrom(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

- <pre>mongo::GeometryContainer::hasS2Region() const</pre>
Used By:
    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

- <pre>mongo::GeometryContainer::hasFlatRegion() const</pre>
Used By:
    - [src/mongo/db/query/planner\_ixselect.cpp](../query\_system)

- <pre>mongo::GeoQuery::parseFrom(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)

### src/mongo/db/geo/hash.cpp

- <pre>mongo::GeoHash::up() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::GeoHash(mongo::BSONElement const&, unsigned int)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::move(int, int)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::constrains() const</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::canRefine() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::hash(mongo::Point const&) const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::GeoHash::GeoHash(mongo::GeoHash const&)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::hash(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::hash(mongo::BSONObj const&, mongo::BSONObj const*) const</pre>
Used By:
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

- <pre>mongo::GeoHash::GeoHash()</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::GeoHash::atMinX() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::operator+(std::string const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::unhashToPoint(mongo::GeoHash const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::atMinY() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::operator=(mongo::GeoHash const&)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::GeoHash::atMaxY() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::GeoHash(unsigned int, unsigned int, unsigned int)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::hash(double, double) const</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::GeoHash::operator!=(mongo::GeoHash const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::GeoHashConverter(mongo::GeoHashConverter::Parameters const&)</pre>
Used By:
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

- <pre>mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const</pre>
Used By:
    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHashConverter::unhashToPoint(mongo::BSONElement const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::hasPrefix(mongo::GeoHash const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::GeoHash::atMaxX() const</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

### src/mongo/db/geo/s2common.cpp

- <pre>mongo::S2SearchUtil::getKeysForObject(mongo::BSONObj const&, mongo::S2IndexingParams const&, std::vector<std::string, std::allocator<std::string> >*)</pre>
Used By:
    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)

- <pre>mongo::S2SearchUtil::distanceBetween(Vector3<double> const&, mongo::BSONObj const&, double*)</pre>
Used By:
    - [src/mongo/db/exec/s2near.cpp](../query\_system)

### src/mongo/db/geo/shapes.cpp

- <pre>mongo::Box::Box(mongo::Point, mongo::Point)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::Point::Point(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)

- <pre>mongo::Polygon::contains(mongo::Point const&) const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::inside(mongo::Point, double) const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::onBoundary(mongo::Point, double)</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::Box(double, double, double)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)

- <pre>mongo::Box::fudge(double)</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Polygon::Polygon()</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::intersects(mongo::Box const&) const</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::center() const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Polygon::bounds()</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::maxDim() const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::checkEarthBounds(mongo::Point const&)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::distance(mongo::Point const&, mongo::Point const&)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::Box()</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Polygon::contains(mongo::Point const&, double) const</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Point::Point(mongo::BSONElement const&)</pre>
Used By:
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

- <pre>mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)</pre>
Used By:
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Point::Point(double, double)</pre>
Used By:
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Box::truncate(double, double)</pre>
Used By:
    - [src/mongo/db/exec/2d.cpp](../query\_system)

- <pre>mongo::Point::Point()</pre>
Used By:
    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/query/planner\_access.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)
    - [src/mongo/db/exec/2d.cpp](../query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../query\_system)
