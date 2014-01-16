# s2

# Module Groups

-------------

Third Party - Google spherical geometry math library

- src/third\_party/s2/base/basictypes.h
- src/third\_party/s2/base/casts.h
- src/third\_party/s2/base/definer.h
- src/third\_party/s2/base/int128.cc   (mongod, tools, mongos)
- src/third\_party/s2/base/int128.h
- src/third\_party/s2/base/integral\_types.h
- src/third\_party/s2/base/logging.cc   (mongod, tools, mongos)
- src/third\_party/s2/base/logging.h
- src/third\_party/s2/base/macros.h
- src/third\_party/s2/base/port.h
- src/third\_party/s2/base/scoped\_ptr.h
- src/third\_party/s2/base/stringprintf.cc   (mongod, tools, mongos)
- src/third\_party/s2/base/stringprintf.h
- src/third\_party/s2/base/strtoint.cc   (mongod, tools, mongos)
- src/third\_party/s2/base/strtoint.h
- src/third\_party/s2/base/template\_util.h
- src/third\_party/s2/base/type\_traits.h
- src/third\_party/s2/hash.h
- src/third\_party/s2/r1interval.h
- src/third\_party/s2/s1angle.cc   (mongod, tools, mongos)
- src/third\_party/s2/s1angle.h
- src/third\_party/s2/s1interval.cc   (mongod, tools, mongos)
- src/third\_party/s2/s1interval.h
- src/third\_party/s2/s2.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2.h
- src/third\_party/s2/s2cap.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2cap.h
- src/third\_party/s2/s2cell.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2cell.h
- src/third\_party/s2/s2cellid.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2cellid.h
- src/third\_party/s2/s2cellunion.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2cellunion.h
- src/third\_party/s2/s2edgeindex.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2edgeindex.h
- src/third\_party/s2/s2edgeutil.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2edgeutil.h
- src/third\_party/s2/s2latlng.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2latlng.h
- src/third\_party/s2/s2latlngrect.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2latlngrect.h
- src/third\_party/s2/s2loop.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2loop.h
- src/third\_party/s2/s2pointregion.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2pointregion.h
- src/third\_party/s2/s2polygon.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2polygon.h
- src/third\_party/s2/s2polygonbuilder.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2polygonbuilder.h
- src/third\_party/s2/s2polyline.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2polyline.h
- src/third\_party/s2/s2r2rect.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2r2rect.h
- src/third\_party/s2/s2region.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2region.h
- src/third\_party/s2/s2regioncoverer.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2regioncoverer.h
- src/third\_party/s2/s2regionintersection.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2regionintersection.h
- src/third\_party/s2/s2regionunion.cc   (mongod, tools, mongos)
- src/third\_party/s2/s2regionunion.h
- src/third\_party/s2/strings/ascii\_ctype.h
- src/third\_party/s2/strings/split.cc   (mongod, tools, mongos)
- src/third\_party/s2/strings/split.h
- src/third\_party/s2/strings/stringprintf.cc   (mongod, tools, mongos)
- src/third\_party/s2/strings/stringprintf.h
- src/third\_party/s2/strings/strutil.cc   (mongod, tools, mongos)
- src/third\_party/s2/strings/strutil.h
- src/third\_party/s2/util/coding/coder.cc   (mongod, tools, mongos)
- src/third\_party/s2/util/coding/coder.h
- src/third\_party/s2/util/coding/varint.cc   (mongod, tools, mongos)
- src/third\_party/s2/util/coding/varint.h
- src/third\_party/s2/util/endian/endian.h
- src/third\_party/s2/util/hash/hash\_jenkins\_lookup2.h
- src/third\_party/s2/util/math/exactfloat/exactfloat.h
- src/third\_party/s2/util/math/mathlimits.cc
- src/third\_party/s2/util/math/mathlimits.h
- src/third\_party/s2/util/math/mathutil.cc   (mongod, tools, mongos)
- src/third\_party/s2/util/math/mathutil.h
- src/third\_party/s2/util/math/matrix3x3-inl.h
- src/third\_party/s2/util/math/matrix3x3.h
- src/third\_party/s2/util/math/vector2-inl.h
- src/third\_party/s2/util/math/vector2.h
- src/third\_party/s2/util/math/vector3-inl.h
- src/third\_party/s2/util/math/vector3.h
- src/third\_party/s2/util/math/vector4.h

## Interface
### src/third\_party/s2/base/logging.cc
<pre>google_base::DateLogger::HumanDate()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>google_base::DateLogger::DateLogger()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
### src/third\_party/s2/s1angle.cc
<pre>S1Angle::S1Angle(Vector3<double> const&, Vector3<double> const&)</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
### src/third\_party/s2/s2.cc
<pre>S2::kAvgEdge</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2::kMaxCellLevel</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
### src/third\_party/s2/s2cap.cc
<pre>vtable for S2Cap</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Cap::Complement() const</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)

<pre>S2Cap::FromAxisAngle(Vector3<double> const&, S1Angle const&)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Cap::MayIntersect(S2Cell const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
### src/third\_party/s2/s2cell.cc
<pre>vtable for S2Cell</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/query\_solution.cpp](../query\_system)
- [src/mongo/db/exec/2dnear.cpp](../query\_system)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)

<pre>S2Cell::MayIntersect(S2Cell const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Cell::Init(S2CellId const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
### src/third\_party/s2/s2cellid.cc
<pre>S2CellId::level() const</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2CellId::kNumFaces</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2CellId::ToString() const</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2CellId::kMaxLevel</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2CellId::kPosBits</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2CellId::FromPoint(Vector3<double> const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
### src/third\_party/s2/s2latlng.cc
<pre>S2LatLng::Normalized() const</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2LatLng::ToPoint() const</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
### src/third\_party/s2/s2latlngrect.cc
<pre>S2LatLngRect::Area() const</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>vtable for S2LatLngRect</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
### src/third\_party/s2/s2loop.cc
<pre>S2Loop::IsValid() const</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Loop::~S2Loop()</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Loop::Contains(S2Loop const*) const</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Loop::Normalize()</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Loop::Invert()</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Loop::S2Loop(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
### src/third\_party/s2/s2polygon.cc
<pre>S2Polygon::S2Polygon()</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::Contains(S2Polygon const*) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::IntersectWithPolyline(S2Polyline const*, std::vector<S2Polyline*, std::allocator<S2Polyline*> >*) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::MayIntersect(S2Cell const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::~S2Polygon()</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::Intersects(S2Polygon const*) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::Contains(Vector3<double> const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polygon::Project(Vector3<double> const&) const</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
### src/third\_party/s2/s2polygonbuilder.cc
<pre>S2PolygonBuilder::S2PolygonBuilder(S2PolygonBuilderOptions const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2PolygonBuilder::~S2PolygonBuilder()</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2PolygonBuilder::AddLoop(S2Loop const*)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2PolygonBuilderOptions::set_xor_edges(bool)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2PolygonBuilder::AssemblePolygon(S2Polygon*, std::vector<std::pair<Vector3<double>, Vector3<double> >, std::allocator<std::pair<Vector3<double>, Vector3<double> > > >*)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2PolygonBuilderOptions::set_validate(bool)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
### src/third\_party/s2/s2polyline.cc
<pre>S2Polyline::MayIntersect(S2Cell const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polyline::S2Polyline()</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polyline::IsValid(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Polyline::~S2Polyline()</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polyline::Init(std::vector<Vector3<double>, std::allocator<Vector3<double> > > const&)</pre>
#### Used By:
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)

<pre>S2Polyline::Intersects(S2Polyline const*) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polyline::NearlyCoversPolyline(S2Polyline const&, S1Angle const&) const</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2Polyline::Project(Vector3<double> const&, int*) const</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
### src/third\_party/s2/s2region.cc
<pre>S2Region::~S2Region()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/query/query\_solution.cpp](../query\_system)
- [src/mongo/db/matcher/expression\_geo.cpp](../query\_system)
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
- [src/mongo/db/geo/geoparser.cpp](../geo\_queries)
- [src/mongo/db/exec/2dnear.cpp](../query\_system)
- [src/mongo/db/query/planner\_access.cpp](../query\_system)
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
### src/third\_party/s2/s2regioncoverer.cc
<pre>S2RegionCoverer::S2RegionCoverer()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2RegionCoverer::set_max_cells(int)</pre>
#### Used By:
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)

<pre>S2RegionCoverer::set_max_level(int)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2RegionCoverer::set_min_level(int)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2RegionCoverer::~S2RegionCoverer()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)

<pre>S2RegionCoverer::GetCovering(S2Region const&, std::vector<S2CellId, std::allocator<S2CellId> >*)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/geo/s2common.cpp](../geo\_queries)
- [src/mongo/db/query/index\_bounds\_builder.cpp](../query\_system)
### src/third\_party/s2/s2regionintersection.cc
<pre>S2RegionIntersection::Release(std::vector<S2Region*, std::allocator<S2Region*> >*)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)

<pre>S2RegionIntersection::Init(std::vector<S2Region*, std::allocator<S2Region*> >*)</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)

<pre>S2RegionIntersection::~S2RegionIntersection()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)

<pre>S2RegionIntersection::S2RegionIntersection()</pre>
#### Used By:
- [src/mongo/db/exec/s2near.cpp](../query\_system)
### src/third\_party/s2/s2regionunion.cc
<pre>S2RegionUnion::Add(S2Region*)</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)

<pre>S2RegionUnion::S2RegionUnion()</pre>
#### Used By:
- [src/mongo/db/geo/geoquery.cpp](../geo\_queries)
