# aggregation\_framework

# Module Groups

-------------

should be a library ;(   who calls/owns this stuff?

- src/mongo/db/pipeline/accumulator.h
- src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_avg.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_first.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_last.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_min\_max.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_push.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_sum.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.h
- src/mongo/db/pipeline/document\_internal.h
- src/mongo/db/pipeline/document\_source.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source.h
- src/mongo/db/pipeline/document\_source\_bson\_array.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_command\_shards.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_cursor.cpp   (mongod, tools)
- src/mongo/db/pipeline/document\_source\_geo\_near.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_group.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_limit.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_match.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_out.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_project.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_redact.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_skip.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_sort.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_unwind.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/expression.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/expression.h
- src/mongo/db/pipeline/expression\_context.h
- src/mongo/db/pipeline/field\_path.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/field\_path.h
- src/mongo/db/pipeline/pipeline.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/pipeline.h
- src/mongo/db/pipeline/pipeline\_d.cpp   (mongod, tools)
- src/mongo/db/pipeline/pipeline\_d.h
- src/mongo/db/pipeline/pipeline\_optimizations.h
- src/mongo/db/pipeline/value.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/value.h
- src/mongo/db/pipeline/value\_internal.h

-------------

Generic interface for getting and merging sorted streams of documents. Only used in aggregation.   +1 "only used in aggregation" :)

- src/mongo/db/sorter/sorter.cpp
- src/mongo/db/sorter/sorter.h
- src/mongo/db/sorter/sorter\_test.cpp   ()

-------------

Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if  external sorting is allowed.   who calls this?

- src/mongo/db/extsort.cpp   (mongod, tools)
- src/mongo/db/extsort.h

-------------

I believe this is just used in External Sort, but it's standing on its own here without a  description.

- src/mongo/db/sort\_phase\_one.h
