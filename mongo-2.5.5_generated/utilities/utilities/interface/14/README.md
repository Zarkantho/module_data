
# Interface for Reference Count Helper
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/intrusive\_counter.cpp

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../../../../queries/aggregation\_framework)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::RCString::create(mongo::StringData)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_skip.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_project.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_limit.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_redact.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](../../../../queries/aggregation\_framework)
