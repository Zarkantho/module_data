
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/geo/geoparser.cpp

<div></div>

    mongo::GeoParser::isPoint(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)

### src/mongo/db/geo/geoquery.cpp

<div></div>

    mongo::GeometryContainer::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoQuery::getRegion() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoQuery::satisfiesPredicate(mongo::GeometryContainer const&) const

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::NearQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeometryContainer::hasS2Region() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeometryContainer::hasFlatRegion() const

- Used By:

    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoQuery::parseFrom(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/geo/hash.cpp

<div></div>

    mongo::GeoHash::up() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::GeoHash(mongo::BSONElement const&, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::move(int, int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::constrains() const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::canRefine() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::GeoHash(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::hash(mongo::BSONObj const&, mongo::BSONObj const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::GeoHash::GeoHash()

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::atMinX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::operator+(std::string const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::sizeEdge(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::unhashToPoint(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::atMinY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::operator=(mongo::GeoHash const&)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::atMaxY() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::GeoHash(unsigned int, unsigned int, unsigned int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::hash(double, double) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::operator!=(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::GeoHashConverter(mongo::GeoHashConverter::Parameters const&)

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::appendToBuilder(mongo::BSONObjBuilder*, char const*) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHashConverter::unhashToPoint(mongo::BSONElement const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::hasPrefix(mongo::GeoHash const&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::GeoHash::atMaxX() const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/geo/s2common.cpp

<div></div>

    mongo::S2SearchUtil::getKeysForObject(mongo::BSONObj const&, mongo::S2IndexingParams const&, std::vector<std::string, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::S2SearchUtil::distanceBetween(Vector3<double> const&, mongo::BSONObj const&, double*)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/geo/shapes.cpp

<div></div>

    mongo::Box::Box(mongo::Point, mongo::Point)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Point::Point(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::inside(mongo::Point, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Polygon::contains(mongo::Point const&) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::onBoundary(mongo::Point, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::Box(double, double, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::fudge(double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Polygon::Polygon()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::intersects(mongo::Box const&) const

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::center() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Polygon::bounds()

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::maxDim() const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::checkEarthBounds(mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::distanceWithin(mongo::Point const&, mongo::Point const&, double)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::distance(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::Box()

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Polygon::contains(mongo::Point const&, double) const

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Point::Point(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::spheredist_deg(mongo::Point const&, mongo::Point const&)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Point::Point(double, double)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Box::truncate(double, double)

- Used By:

    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Point::Point()

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/planner\_access.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/query\_planner.cpp](../../../../queries/core\_query\_system)
