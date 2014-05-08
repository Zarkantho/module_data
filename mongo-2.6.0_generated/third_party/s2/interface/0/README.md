
# Interface for S2 Library
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/third\_party/s2/base/logging.cc

<div></div>

    LogMessageFatal::~LogMessageFatal()

- Used By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/external\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    LogMessageFatal::LogMessageFatal(char const*, int)

- Used By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/external\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

### src/third\_party/s2/s1angle.cc

<div></div>

    S1Angle::S1Angle(Vector3<double> const&, Vector3<double> const&)

- Used By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2.cc

<div></div>

    S2::kAvgEdge

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/external\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2::kMaxCellLevel

- Used By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/index/external\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

### src/third\_party/s2/s2cap.cc

<div></div>

    vtable for S2Cap

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Cap::Complement() const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2Cap::FromAxisAngle(Vector3<double> const&, S1Angle const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Cap::MayIntersect(S2Cell const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2cell.cc

<div></div>

    S2Cell::Init(S2CellId const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    vtable for S2Cell

- Used By:

    - [src/mongo/db/query/planner\_access.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/2dnear.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/query/query\_solution.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Cell::MayIntersect(S2Cell const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2cellid.cc

<div></div>

    S2CellId::level() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::kNumFaces

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::ToString() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::FromString(std::string const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::kMaxLevel

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::kPosBits

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2CellId::FromPoint(Vector3<double> const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2latlng.cc

<div></div>

    S2LatLng::Normalized() const

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2LatLng::ToPoint() const

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2latlngrect.cc

<div></div>

    S2LatLngRect::Area() const

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    vtable for S2LatLngRect

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

### src/third\_party/s2/s2loop.cc

<div></div>

    S2Loop::IsValid() const

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Loop::Contains(S2Loop const*) const

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Loop::~S2Loop()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Loop::Normalize()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Loop::Invert()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Loop::S2Loop(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2polygon.cc

<div></div>

    S2Polygon::S2Polygon()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::Contains(S2Polygon const*) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::IntersectWithPolyline(S2Polyline const*, std::vector<S2Polyline*, std::allocator<S2Polyline*> >*) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::MayIntersect(S2Cell const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::~S2Polygon()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::Intersects(S2Polygon const*) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::Contains(Vector3<double> const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polygon::Project(Vector3<double> const&) const

- Used By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2polygonbuilder.cc

<div></div>

    S2PolygonBuilder::S2PolygonBuilder(S2PolygonBuilderOptions const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2PolygonBuilder::~S2PolygonBuilder()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2PolygonBuilder::AddLoop(S2Loop const*)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2PolygonBuilderOptions::set_xor_edges(bool)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2PolygonBuilder::AssemblePolygon(S2Polygon*, std::vector<std::pair<Vector3<double>, Vector3<double> >, std::allocator<std::pair<Vector3<double>, Vector3<double> > > >*)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2PolygonBuilderOptions::set_validate(bool)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2polyline.cc

<div></div>

    S2Polyline::MayIntersect(S2Cell const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::S2Polyline()

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::IsValid(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::~S2Polyline()

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::Init(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)

- Used By:

    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::Intersects(S2Polyline const*) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::NearlyCoversPolyline(S2Polyline const&, S1Angle const&) const

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2Polyline::Project(Vector3<double> const&, int*) const

- Used By:

    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)

### src/third\_party/s2/s2region.cc

<div></div>

    S2Region::~S2Region()

- Used By:

    - [src/mongo/db/query/stage\_builder.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/query/planner\_access.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/2dnear.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/query\_solution.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)

### src/third\_party/s2/s2regioncoverer.cc

<div></div>

    S2RegionCoverer::S2RegionCoverer()

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionCoverer::set_max_cells(int)

- Used By:

    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    S2RegionCoverer::set_max_level(int)

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionCoverer::set_min_level(int)

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/geo/s2common.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionCoverer::~S2RegionCoverer()

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionCoverer::GetCovering(S2Region const&, std::vector<S2CellId, std::allocator<S2CellId> >*)

- Used By:

    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

### src/third\_party/s2/s2regionintersection.cc

<div></div>

    S2RegionIntersection::S2RegionIntersection()

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionIntersection::Release(std::vector<S2Region*, std::allocator<S2Region*> >*)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionIntersection::Init(std::vector<S2Region*, std::allocator<S2Region*> >*)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    S2RegionIntersection::~S2RegionIntersection()

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

### src/third\_party/s2/s2regionunion.cc

<div></div>

    S2RegionUnion::Add(S2Region*)

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    S2RegionUnion::S2RegionUnion()

- Used By:

    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)
