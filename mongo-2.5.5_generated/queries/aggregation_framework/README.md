# Aggregation Framework

# Module Groups

-------------

# Mongod Aggregation Commands
Entry point into aggregation for mongod.  These are all database Commands run using db.$cmd.findOne(...)

## Files
- src/mongo/db/commands/pipeline\_command.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# Accumulators
An accumulator represents a stateful operation.  For example, in an operation such as $sum, you can feed in values until there is no more data, then extract the final result

## Files
- src/mongo/db/pipeline/accumulator.h   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_avg.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_first.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_last.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_min\_max.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_push.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_sum.cpp   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

# BSON Representation
In memory representation of BSON for aggregation.  Similar to a the BSONElement/BSONObj interface except the Value class does not contain its key like a BSONElement, and the Document class is just a map of keys to values

## Files
- src/mongo/db/pipeline/value.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/value.h   (mongod, tools, mongos)
- src/mongo/db/pipeline/value\_internal.h   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.h   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_internal.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

# Pipeline Stages
Files containing the pipeline stages.  Document Source is the name for a pipeline stage in our code

## Files
- src/mongo/db/pipeline/document\_source.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source.h   (mongod, tools, mongos)
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

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

# Expressions
An expression represents a stateless operation.  For example, in an operation such as $add, you provide a set of values, and immediately recieve a result

## Files
- src/mongo/db/pipeline/expression.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/expression.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

# Pipeline Stage Context
This file is currently misnamed.  The context for a pipeline stage, such as whether its being run on a Source (source shard) or a Merger (primary shard responsible for merging results), whether there has been an interrupt, and other global information.

## Files
- src/mongo/db/pipeline/expression\_context.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

# Dotted Field Utilities
Wrapper classes for parsed and validated dotted field names

## Files
- src/mongo/db/pipeline/field\_path.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/field\_path.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

# Aggregation Common Entry Point
These files contain the central entry point for aggregation.  While the initial entry points for mongos and mongod differ, most of the aggregation code is shared between them.  This holds the two paths together, and also contains the optimization code

## Files
- src/mongo/db/pipeline/pipeline.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/pipeline.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

# Mongod Specific Aggregation Extensions
Mongod specific extensions to aggregation

## Files
- src/mongo/db/pipeline/pipeline\_d.cpp   (mongod, tools)
- src/mongo/db/pipeline/pipeline\_d.h   (mongod, tools)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

# Pipeline Optimizations
Optimizations that are done as part of the aggregation process.  There are two optimization types, local and sharded.  In a sharded cluster, first the local optimizations are done which rewrites the pipeline stages, then the sharded optimizations are done, which controls exactly what gets farmed out to the source shards, then each source shard runs the local optimization again

## Files
- src/mongo/db/pipeline/pipeline\_optimizations.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

# Data Dependency Tracking
Code to track what information is needed in the aggregation pipeline.  For example, for some queries only certain fields of the document are actually needed

## Files
- src/mongo/db/pipeline/dependencies.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/dependencies.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

# Sorter
Generic interface for getting and merging sorted streams of documents. Only used in aggregation

## Files
- src/mongo/db/sorter/sorter.cpp   (mongod, tools, mongos)
- src/mongo/db/sorter/sorter.h   (mongod, tools, mongos)
- src/mongo/db/sorter/sorter\_test.cpp   ()

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

# External Sorter
Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if external sorting is allowed

## Files
- src/mongo/db/extsort.cpp   (mongod, tools)
- src/mongo/db/extsort.h   (mongod, tools)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

# Index Key Sorter
Wrapper around the External Sorter specialized for index keys.  Used in bottom up fast index builds where keys are pre sorted.

## Files
- src/mongo/db/sort\_phase\_one.h   (mongod, tools)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)
