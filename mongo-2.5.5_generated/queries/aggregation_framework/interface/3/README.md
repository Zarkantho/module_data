
# Interface

### src/mongo/db/pipeline/document\_source.cpp

<div></div>

    typeinfo for mongo::DocumentSource

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)

### src/mongo/db/pipeline/document\_source\_bson\_array.cpp

<div></div>

    mongo::DocumentSourceBsonArray::create(mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_command\_shards.cpp

<div></div>

    mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)

### src/mongo/db/pipeline/document\_source\_cursor.cpp

<div></div>

    mongo::DocumentSourceCursor::create(std::string const&, long long, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DocumentSourceCursor::getLimit() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_geo\_near.cpp

<div></div>

    mongo::DocumentSourceGeoNear::create(boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_group.cpp

<div></div>

    mongo::DocumentSourceGroup::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_limit.cpp

<div></div>

    mongo::DocumentSourceLimit::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DocumentSourceLimit::create(boost::intrusive_ptr<mongo::ExpressionContext> const&, long long)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_match.cpp

<div></div>

    mongo::DocumentSourceMatch::redactSafePortion() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DocumentSourceMatch::getQuery() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DocumentSourceMatch::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    typeinfo for mongo::DocumentSourceMatch

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp

<div></div>

    mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)

### src/mongo/db/pipeline/document\_source\_out.cpp

<div></div>

    typeinfo for mongo::DocumentSourceOut

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding)

### src/mongo/db/pipeline/document\_source\_project.cpp

<div></div>

    mongo::DocumentSourceProject::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_sort.cpp

<div></div>

    typeinfo for mongo::DocumentSourceSort

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

<div></div>

    mongo::DocumentSourceSort::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)

### src/mongo/db/pipeline/document\_source\_unwind.cpp

<div></div>

    mongo::DocumentSourceUnwind::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../unit\_tests)
